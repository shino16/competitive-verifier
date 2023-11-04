import datetime
import filecmp
import inspect
import logging
import os
import pathlib
from typing import Any

import pytest
import yaml
from pytest_mock import MockerFixture
from pytest_subtests import SubTests

from competitive_verifier.documents.main import main

from .data import (
    DESTINATION_ROOT,
    RESULT_FILE_PATH,
    TARGETS,
    TARGETS_PATH,
    VERIFY_FILE_PATH,
)

DEFAULT_ARGS = [
    "--verify-json",
    VERIFY_FILE_PATH,
    RESULT_FILE_PATH,
]


@pytest.fixture(scope="session")
def clean():
    import shutil

    if DESTINATION_ROOT.is_dir():
        shutil.rmtree(DESTINATION_ROOT)


@pytest.fixture
def setup_docs(clean: Any, mocker: MockerFixture):
    tzinfo = datetime.timezone(datetime.timedelta(hours=9), name="Asia/Tokyo")
    MOCK_TIME = datetime.datetime(2023, 12, 4, 5, 6, 7, 8910, tzinfo=tzinfo)

    mocker.patch(
        "competitive_verifier.git.get_commit_time",
        return_value=MOCK_TIME,
    )
    mocker.patch.dict(
        os.environ,
        {
            "GITHUB_REF_NAME": "TESTING_GIT_REF",
            "GITHUB_WORKFLOW": "TESTING_WORKFLOW",
        },
    )


def check_common(
    destination: pathlib.Path,
    *,
    subtests: SubTests,
):
    assert destination.is_dir()

    targets = {t.path: t for t in TARGETS}

    for target_file in filter(
        lambda p: p.is_file(),
        (destination / TARGETS_PATH).glob("**/*"),
    ):
        path_str = target_file.relative_to(destination).as_posix()
        with subtests.test(  # pyright: ignore[reportUnknownMemberType]
            msg="Check testdata", path=path_str
        ):
            target_value = target_file.read_bytes().strip()
            assert target_value.startswith(b"---\n")

            front_matter_end = target_value.index(b"---", 4)
            front_matter = yaml.safe_load(target_value[4:front_matter_end])
            content = target_value[front_matter_end + 3 :].strip()

            assert content == targets[path_str].content
            assert front_matter == targets[path_str].front_matter
        del targets[path_str]

    assert not list(targets.keys())


@pytest.mark.usefixtures("setup_docs")
def test_with_config(subtests: SubTests):
    destination = DESTINATION_ROOT / inspect.stack()[0].function
    docs_settings_dir = pathlib.Path("testdata/docs_settings")

    main(
        [
            "--docs",
            docs_settings_dir.as_posix(),
            "--destination",
            destination.as_posix(),
        ]
        + DEFAULT_ARGS
    )

    check_common(destination, subtests=subtests)

    config_yml = yaml.safe_load((destination / "_config.yml").read_bytes())
    assert config_yml == {
        "action_name": "TESTING_WORKFLOW",
        "basedir": "",
        "branch_name": "TESTING_GIT_REF",
        "description": "My description",
        "filename-index": True,
        "highlightjs-style": "vs2015",
        "plugins": [
            "jemoji",
            "jekyll-redirect-from",
            "jekyll-remote-theme",
        ],
        "mathjax": 2,
        "sass": {"style": "compressed"},
        "theme": "jekyll-theme-modernist",
        "icons": {
            "LIBRARY_ALL_AC": ":heavy_check_mark:",
            "LIBRARY_ALL_WA": ":x:",
            "LIBRARY_NO_TESTS": ":warning:",
            "LIBRARY_PARTIAL_AC": ":heavy_check_mark:",
            "LIBRARY_SOME_WA": ":question:",
            "TEST_ACCEPTED": ":100:",
            "TEST_WAITING_JUDGE": ":warning:",
            "TEST_WRONG_ANSWER": ":x:",
        },
    }

    assert (destination / "static.md").exists()
    assert (destination / "static.md").read_text(
        encoding="utf-8"
    ) == "# Static page\n\nI'm Static!"

    static_dir = docs_settings_dir / "static"
    for static_file in filter(lambda p: p.is_file(), static_dir.glob("**/*")):
        assert filecmp.cmp(
            static_file, destination / static_file.relative_to(static_dir)
        )


@pytest.mark.usefixtures("setup_docs")
def test_without_config(subtests: SubTests):
    destination = DESTINATION_ROOT / inspect.stack()[0].function

    main(
        [
            "--docs",
            "testdata/nothing",
            "--destination",
            destination.as_posix(),
        ]
        + DEFAULT_ARGS
    )

    check_common(destination, subtests=subtests)

    config_yml = yaml.safe_load((destination / "_config.yml").read_bytes())
    assert config_yml == {
        "action_name": "TESTING_WORKFLOW",
        "basedir": "",
        "branch_name": "TESTING_GIT_REF",
        "description": '<small>This documentation is automatically generated by <a href="https://github.com/competitive-verifier/competitive-verifier">competitive-verifier/competitive-verifier</a></small>',
        "filename-index": False,
        "highlightjs-style": "default",
        "plugins": [
            "jemoji",
            "jekyll-redirect-from",
            "jekyll-remote-theme",
        ],
        "mathjax": 3,
        "sass": {"style": "compressed"},
        "theme": "jekyll-theme-minimal",
        "icons": {
            "LIBRARY_ALL_AC": ":heavy_check_mark:",
            "LIBRARY_ALL_WA": ":x:",
            "LIBRARY_NO_TESTS": ":warning:",
            "LIBRARY_PARTIAL_AC": ":heavy_check_mark:",
            "LIBRARY_SOME_WA": ":question:",
            "TEST_ACCEPTED": ":heavy_check_mark:",
            "TEST_WAITING_JUDGE": ":warning:",
            "TEST_WRONG_ANSWER": ":x:",
        },
    }

    assert not (destination / "static.md").exists()

    resource_dir = pathlib.Path("src/competitive_verifier_resources/jekyll")
    for resource_file in filter(lambda p: p.is_file(), resource_dir.glob("**/*")):
        assert filecmp.cmp(
            resource_file, destination / resource_file.relative_to(resource_dir)
        )


@pytest.mark.usefixtures("setup_docs")
def test_logging_default(subtests: SubTests, caplog: pytest.LogCaptureFixture):
    caplog.set_level(logging.WARNING)
    destination = DESTINATION_ROOT / inspect.stack()[0].function

    main(
        [
            "--docs",
            "testdata/nothing",
            "--destination",
            destination.as_posix(),
        ]
        + DEFAULT_ARGS
    )

    check_common(destination, subtests=subtests)

    def doc_path(record: logging.LogRecord):
        assert isinstance(record.args, tuple)
        p = record.args[0]
        assert isinstance(p, str)
        return p

    assert sorted(
        (
            doc_path(r)
            for r in caplog.records
            if r.name == "competitive_verifier.documents.job"
            and r.levelno == logging.WARNING
            and r.msg == "the `documentation_of` path of %s is not target: %s"
        ),
        key=str.casefold,
    ) == [
        "examples/awk/aplusb2.md",
        "examples/cpp/segment_tree.md",
        "examples/external/sub/dummy.md",
        "examples/tests/encoding/cp932.md",
        "examples/tests/encoding/EUC-KR.md",
    ]


@pytest.mark.usefixtures("setup_docs")
def test_logging_include(subtests: SubTests, caplog: pytest.LogCaptureFixture):
    caplog.set_level(logging.WARNING)
    destination = DESTINATION_ROOT / inspect.stack()[0].function

    main(
        [
            "--include",
            TARGETS_PATH,
            "--docs",
            "testdata/nothing",
            "--destination",
            destination.as_posix(),
        ]
        + DEFAULT_ARGS
    )

    check_common(destination, subtests=subtests)

    def doc_path(record: logging.LogRecord):
        assert isinstance(record.args, tuple)
        p = record.args[0]
        assert isinstance(p, str)
        return p

    assert not [
        doc_path(r)
        for r in caplog.records
        if r.name == "competitive_verifier.documents.job"
        and r.levelno == logging.WARNING
        and r.msg == "the `documentation_of` path of %s is not target: %s"
    ]


@pytest.mark.usefixtures("setup_docs")
def test_logging_exclude(subtests: SubTests, caplog: pytest.LogCaptureFixture):
    caplog.set_level(logging.WARNING)
    destination = DESTINATION_ROOT / inspect.stack()[0].function

    main(
        [
            "--exclude",
            "examples/",
            "--docs",
            "testdata/nothing",
            "--destination",
            destination.as_posix(),
        ]
        + DEFAULT_ARGS
    )

    check_common(destination, subtests=subtests)

    def doc_path(record: logging.LogRecord):
        assert isinstance(record.args, tuple)
        p = record.args[0]
        assert isinstance(p, str)
        return p

    assert not [
        doc_path(r)
        for r in caplog.records
        if r.name == "competitive_verifier.documents.job"
        and r.levelno == logging.WARNING
        and r.msg == "the `documentation_of` path of %s is not target: %s"
    ]