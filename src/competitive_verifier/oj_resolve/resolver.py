import os
import pathlib
import traceback
from itertools import chain
from logging import getLogger
from typing import Generator

import competitive_verifier.config as config
import competitive_verifier.git as git
import competitive_verifier.oj as oj
import oj_verify_clone.list
from competitive_verifier.models import (
    AddtionalSource,
    ConstVerification,
    ProblemVerification,
    ResultStatus,
    Verification,
    VerificationFile,
    VerificationInput,
)
from oj_verify_clone.languages.models import LanguageEnvironment

logger = getLogger(__name__)


def get_bundled_dir() -> pathlib.Path:
    return config.config_dir / "bundled"


class OjResolver:
    include: list[pathlib.Path]
    exclude: list[pathlib.Path]

    def __init__(
        self,
        *,
        include: list[pathlib.Path],
        exclude: list[pathlib.Path],
    ) -> None:
        self.include = include
        self.exclude = exclude

    def resolve(self, *, bundle: bool) -> VerificationInput:
        files: dict[pathlib.Path, VerificationFile] = {}
        basedir = pathlib.Path.cwd()

        def to_relative(path: pathlib.Path) -> pathlib.Path:
            if path.is_absolute():
                return path.relative_to(basedir)
            return path

        exclude_paths = set(
            chain.from_iterable(p.glob("**/*") for p in map(to_relative, self.exclude))
        )

        for path in git.ls_files(*self.include):
            if path in exclude_paths:
                continue

            language = oj_verify_clone.list.get(path)
            if language is None:
                continue

            deps = set(git.ls_files(*language.list_dependencies(path, basedir=basedir)))
            attr = language.list_attributes(path, basedir=basedir)

            def env_to_verifications(
                env: LanguageEnvironment,
            ) -> Generator[Verification, None, None]:
                error_str = attr.get("ERROR")
                error = float(error_str) if error_str else None
                url = attr.get("PROBLEM")

                if url:
                    tempdir = oj.get_directory(url)
                    yield ProblemVerification(
                        command=env.get_execute_command(
                            path, basedir=basedir, tempdir=tempdir
                        ),
                        compile=env.get_compile_command(
                            path, basedir=basedir, tempdir=tempdir
                        ),
                        problem=url,
                        error=error,
                    )

                unit_test_envvar = attr.get("UNITTEST")
                if unit_test_envvar:
                    var = os.getenv(unit_test_envvar)
                    if var is None:
                        logger.warning(
                            "UNITTEST envvar %s is not defined.",
                            unit_test_envvar,
                        )
                        yield ConstVerification(status=ResultStatus.FAILURE)
                    elif var.lower() == "false" or var == "0":
                        logger.info(
                            "UNITTEST envvar %s=%s is falsy.",
                            unit_test_envvar,
                            var,
                        )
                        yield ConstVerification(status=ResultStatus.FAILURE)
                    else:
                        logger.info(
                            "UNITTEST envvar %s=%s is truthy.",
                            unit_test_envvar,
                            var,
                        )
                        yield ConstVerification(status=ResultStatus.SUCCESS)

            additonal_sources: list[AddtionalSource] = []
            if bundle:
                try:
                    bundled_code = language.bundle(path, basedir=basedir)
                    if bundled_code:
                        dest_dir = get_bundled_dir()
                        dest_path = dest_dir / path
                        dest_path.parent.mkdir(parents=True, exist_ok=True)
                        logger.info("bundle_path=%s", dest_path.as_posix())
                        dest_path.write_bytes(bundled_code)
                        additonal_sources.append(
                            AddtionalSource(name="bundled", path=dest_path)
                        )
                except Exception:
                    bundled_code = traceback.format_exc()
                    dest_dir = get_bundled_dir()
                    dest_path = dest_dir / path
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    logger.info("bundle_path=%s", dest_path.as_posix())
                    dest_path.write_text(bundled_code)
                    additonal_sources.append(
                        AddtionalSource(name="bundle error", path=dest_path)
                    )

            verifications = list(
                chain.from_iterable(
                    env_to_verifications(vs)
                    for vs in language.list_environments(path, basedir=basedir)
                )
            )
            files[path] = VerificationFile(
                dependencies=deps,
                verification=verifications,
                document_attributes=attr,
                additonal_sources=additonal_sources,
            )
        return VerificationInput(files=files)
