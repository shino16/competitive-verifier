import json
import pathlib
from typing import Any, Optional, Protocol

import pytest
from pytest_mock import MockerFixture

from competitive_verifier.oj_resolve.main import main
from competitive_verifier_oj_clone.languages import special_comments

from .types import FilePaths


@pytest.fixture
def setenv_resolve(mocker: MockerFixture):
    special_comments.list_special_comments.cache_clear()
    special_comments.list_embedded_urls.cache_clear()

    def python_get_execute_command(
        path: pathlib.Path, *, basedir: pathlib.Path, tempdir: pathlib.Path
    ) -> str:
        return f"env PYTHONPATH={basedir.resolve().as_posix()} python {path.as_posix()}"

    mocker.patch(
        "competitive_verifier_oj_clone.languages.python.PythonLanguageEnvironment.get_execute_command",
        side_effect=python_get_execute_command,
    )


class _ArgsFunc(Protocol):
    def __call__(
        self,
        *,
        bundle: bool = True,
        include: Optional[list[str]] = None,
        exclude: Optional[list[str]] = None,
        config: Optional[str] = None,
    ) -> list[str]:
        ...


@pytest.fixture
def expected(file_paths: FilePaths) -> dict[str, Any]:
    return dict(
        {
            "files": {
                "targets/encoding/EUC-KR.txt": {
                    "dependencies": ["targets/encoding/EUC-KR.txt"],
                    "verification": [],
                    "document_attributes": {},
                    "additonal_sources": [
                        {
                            "name": "bundled",
                            "path": ".competitive-verifier/bundled/targets/encoding/EUC-KR.txt",
                        }
                    ],
                },
                "targets/encoding/cp932.txt": {
                    "dependencies": ["targets/encoding/cp932.txt"],
                    "verification": [],
                    "document_attributes": {},
                    "additonal_sources": [
                        {
                            "name": "bundled",
                            "path": ".competitive-verifier/bundled/targets/encoding/cp932.txt",
                        }
                    ],
                },
                "targets/python/lib_all_failure.py": {
                    "dependencies": ["targets/python/lib_all_failure.py"],
                    "verification": [],
                    "document_attributes": {"links": []},
                    "additonal_sources": [],
                },
                "targets/python/lib_some_failure.py": {
                    "dependencies": ["targets/python/lib_some_failure.py"],
                    "verification": [],
                    "document_attributes": {"links": []},
                    "additonal_sources": [],
                },
                "targets/python/lib_skip.py": {
                    "dependencies": ["targets/python/lib_skip.py"],
                    "verification": [],
                    "document_attributes": {"links": []},
                    "additonal_sources": [],
                },
                "targets/python/lib_some_skip_some_wa.py": {
                    "dependencies": ["targets/python/lib_some_skip_some_wa.py"],
                    "verification": [],
                    "document_attributes": {"links": []},
                    "additonal_sources": [],
                },
                "targets/python/success1.py": {
                    "dependencies": [
                        "targets/python/lib_some_failure.py",
                        "targets/python/lib_some_skip.py",
                        "targets/python/success1.py",
                    ],
                    "verification": [
                        {
                            "name": "Python",
                            "type": "problem",
                            "command": f"env PYTHONPATH={file_paths.root.as_posix()} python targets/python/success1.py",
                            "problem": "https://judge.yosupo.jp/problem/aplusb",
                        }
                    ],
                    "document_attributes": {
                        "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                        "links": ["https://judge.yosupo.jp/problem/aplusb"],
                    },
                    "additonal_sources": [],
                },
                "targets/python/failure.wa.py": {
                    "dependencies": [
                        "targets/python/failure.wa.py",
                        "targets/python/lib_all_failure.py",
                        "targets/python/lib_some_skip_some_wa.py",
                    ],
                    "verification": [
                        {
                            "name": "Python",
                            "type": "problem",
                            "command": f"env PYTHONPATH={file_paths.root.as_posix()} python targets/python/failure.wa.py",
                            "problem": "https://judge.yosupo.jp/problem/aplusb",
                        }
                    ],
                    "document_attributes": {
                        "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                        "links": ["https://judge.yosupo.jp/problem/aplusb"],
                    },
                    "additonal_sources": [],
                },
                "targets/python/failure.mle.py": {
                    "dependencies": [
                        "targets/python/failure.mle.py",
                        "targets/python/lib_all_failure.py",
                        "targets/python/lib_some_failure.py",
                    ],
                    "verification": [
                        {
                            "name": "Python",
                            "type": "problem",
                            "command": f"env PYTHONPATH={file_paths.root.as_posix()} python targets/python/failure.mle.py",
                            "problem": "https://judge.yosupo.jp/problem/aplusb",
                            "mle": 100.0,
                        }
                    ],
                    "document_attributes": {
                        "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                        "MLE": "100",
                        "links": ["https://judge.yosupo.jp/problem/aplusb"],
                    },
                    "additonal_sources": [],
                },
                "targets/python/skip.py": {
                    "dependencies": [
                        "targets/python/lib_skip.py",
                        "targets/python/lib_some_skip_some_wa.py",
                        "targets/python/skip.py",
                    ],
                    "verification": [{"type": "const", "status": "skipped"}],
                    "document_attributes": {
                        "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                        "IGNORE": "",
                        "links": ["https://judge.yosupo.jp/problem/aplusb"],
                    },
                    "additonal_sources": [],
                },
                "targets/python/success2.py": {
                    "dependencies": [
                        "targets/python/lib_all_success.py",
                        "targets/python/lib_some_skip_some_wa.py",
                        "targets/python/success2.py",
                    ],
                    "verification": [
                        {
                            "name": "Python",
                            "type": "problem",
                            "command": f"env PYTHONPATH={file_paths.root.as_posix()} python targets/python/success2.py",
                            "problem": "https://judge.yosupo.jp/problem/aplusb",
                        }
                    ],
                    "document_attributes": {
                        "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                        "links": ["https://judge.yosupo.jp/problem/aplusb"],
                    },
                    "additonal_sources": [],
                },
                "targets/python/lib_all_success.py": {
                    "dependencies": ["targets/python/lib_all_success.py"],
                    "verification": [],
                    "document_attributes": {"links": []},
                    "additonal_sources": [],
                },
                "targets/python/failure.re.py": {
                    "dependencies": [
                        "targets/python/failure.re.py",
                        "targets/python/lib_all_failure.py",
                    ],
                    "verification": [
                        {
                            "name": "Python",
                            "type": "problem",
                            "command": f"env PYTHONPATH={file_paths.root.as_posix()} python targets/python/failure.re.py",
                            "problem": "https://judge.yosupo.jp/problem/aplusb",
                        }
                    ],
                    "document_attributes": {
                        "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                        "links": ["https://judge.yosupo.jp/problem/aplusb"],
                    },
                    "additonal_sources": [],
                },
                "targets/python/lib_some_skip.py": {
                    "dependencies": ["targets/python/lib_some_skip.py"],
                    "verification": [],
                    "document_attributes": {"links": []},
                    "additonal_sources": [],
                },
                "targets/python/failure.tle.py": {
                    "dependencies": [
                        "targets/python/failure.tle.py",
                        "targets/python/lib_all_failure.py",
                    ],
                    "verification": [
                        {
                            "name": "Python",
                            "type": "problem",
                            "command": f"env PYTHONPATH={file_paths.root.as_posix()} python targets/python/failure.tle.py",
                            "problem": "https://judge.yosupo.jp/problem/aplusb",
                            "tle": 0.09,
                        }
                    ],
                    "document_attributes": {
                        "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                        "TLE": "0.09",
                        "links": ["https://judge.yosupo.jp/problem/aplusb"],
                    },
                    "additonal_sources": [],
                },
            }
        }
    )


@pytest.fixture
def make_args() -> _ArgsFunc:
    def _make_args(
        *,
        bundle: bool = True,
        include: Optional[list[str]] = None,
        exclude: Optional[list[str]] = None,
        config: Optional[str] = None,
    ) -> list[str]:
        args: list[str] = []
        if not bundle:
            args.append("--no-bundle")
        if include is not None:
            args.append("--include")
            args.extend(include)
        if exclude is not None:
            args.append("--exclude")
            args.extend(exclude)
        if config is not None:
            args.append("--config")
            args.append(config)
        return args

    return _make_args


@pytest.mark.integration
@pytest.mark.dependency(name="resolve_default", scope="package")
@pytest.mark.usefixtures("setenv_resolve")
def test_with_config_include(
    make_args: _ArgsFunc,
    expected: dict[str, Any],
    capfd: pytest.CaptureFixture[str],
    file_paths: FilePaths,
):
    args = make_args(
        include=[file_paths.targets],
        config="config.toml",
        bundle=True,
    )
    main(args)

    stdout = capfd.readouterr().out
    resolved = json.loads(stdout)
    assert (
        pathlib.Path(".competitive-verifier/bundled/targets/encoding/EUC-KR.txt")
        .read_bytes()
        .strip()
        == b"cp949"
    )
    assert (
        pathlib.Path(".competitive-verifier/bundled/targets/encoding/cp932.txt")
        .read_bytes()
        .strip()
        == b"cp932"
    )
    assert resolved == expected

    pathlib.Path(file_paths.verify).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(file_paths.verify).write_text(stdout)


@pytest.mark.usefixtures("setenv_resolve")
def test_with_config_include_nobundle(
    make_args: _ArgsFunc,
    expected: dict[str, Any],
    capfd: pytest.CaptureFixture[str],
    file_paths: FilePaths,
):
    expected["files"]["targets/encoding/EUC-KR.txt"]["additonal_sources"] = []
    expected["files"]["targets/encoding/cp932.txt"]["additonal_sources"] = []

    args = make_args(
        include=[file_paths.targets],
        config="config.toml",
        bundle=False,
    )
    main(args)
    stdout = capfd.readouterr().out
    resolved = json.loads(stdout)
    assert resolved == expected


@pytest.mark.parametrize(
    "exclude",
    [
        ["dummy/"],
        ["dummy/dummy.py"],
    ],
)
@pytest.mark.usefixtures("setenv_resolve")
def test_without_with_exclude_dir(
    exclude: list[str],
    make_args: _ArgsFunc,
    expected: dict[str, Any],
    capfd: pytest.CaptureFixture[str],
):
    del expected["files"]["targets/encoding/EUC-KR.txt"]
    del expected["files"]["targets/encoding/cp932.txt"]

    args = make_args(exclude=exclude)
    main(args)
    stdout = capfd.readouterr().out
    resolved = json.loads(stdout)
    assert resolved == expected


@pytest.mark.usefixtures("setenv_resolve")
def test_without_args(
    make_args: _ArgsFunc,
    expected: dict[str, Any],
    capfd: pytest.CaptureFixture[str],
):
    del expected["files"]["targets/encoding/EUC-KR.txt"]
    del expected["files"]["targets/encoding/cp932.txt"]

    expected["files"]["dummy/dummy.py"] = {
        "additonal_sources": [],
        "dependencies": ["dummy/dummy.py"],
        "document_attributes": {"links": []},
        "verification": [],
    }

    args = make_args()
    main(args)
    stdout = capfd.readouterr().out
    resolved = json.loads(stdout)
    assert resolved == expected