import pathlib
from typing import Any

from pydantic import BaseModel

TARGETS_PATH = "testdata/targets"
VERIFY_FILE_PATH = "testdata/test-verify.json"
RESULT_FILE_PATH = "testdata/test-result.json"
DESTINATION_ROOT = pathlib.Path("testdata/dst_dir")


class MarkdownData(BaseModel):
    path: str
    front_matter: dict[str, Any]
    content: bytes = b""


TARGETS: list[MarkdownData] = [
    MarkdownData(
        path=f"{TARGETS_PATH}/encoding/EUC-KR.txt.md",
        front_matter={
            "data": {
                "attributes": {},
                "dependencies": [
                    {"files": [], "type": "Depends on"},
                    {"files": [], "type": "Required by"},
                    {"files": [], "type": "Verified with"},
                ],
                "dependsOn": [],
                "embedded": [
                    {
                        "code": "컴퓨터 프로그램(영국 영어: computer programme, 미국 영어: computer program)은 컴퓨터에서 실행될 때 특정 작업(specific task)을 수행하는 일련의 명령어들의 모음(집합)이다.[1][2] 특정 문제를 해결하기 위해 처리 방법과 순서를 기술하여 컴퓨터에 입력되는 일련의 명령문 집합체이며 대부분의 프로그램은 실행 중(즉, 명령어를 '불러들일' 때)에 사용자의 입력에 반응하도록 구현된 일련의 명령어들로 구성되어 있다. 대부분의 프로그램들은 하드디스크 등의 매체에 바이너리 형식의 파일로 저장되어 있다가 사용자가 실행시키면 메모리로 적재되어 실행된다. 컴퓨터 소프트웨어와 비슷한 뜻을 가지고 있다. \"컴퓨터프로그램저작물\"은 저작권법상 저작물로서 보호된다. 동법에서 컴퓨터프로그램저작물이라 함은 특정한 결과를 얻기 위하여 컴퓨터 등 정보처리능력을 가진 장치 내에서 직접 또는 간접으로 사용되는 일련의 지시?· 명령으로 표현된 창작물을 말한다. (대한민국 저작권법 제2조 16호 및 제4조 제1항 9호)",
                        "name": "default",
                    }
                ],
                "isFailed": False,
                "isVerificationFile": False,
                "path": "testdata/targets/encoding/EUC-KR.txt",
                "pathExtension": "txt",
                "requiredBy": [],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "LIBRARY_NO_TESTS",
                "verifiedWith": [],
            },
            "documentation_of": "testdata/targets/encoding/EUC-KR.txt",
            "layout": "document",
            "title": "testdata/targets/encoding/EUC-KR.txt",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/encoding/cp932.txt.md",
        front_matter={
            "data": {
                "attributes": {},
                "dependencies": [
                    {"files": [], "type": "Depends on"},
                    {"files": [], "type": "Required by"},
                    {"files": [], "type": "Verified with"},
                ],
                "dependsOn": [],
                "embedded": [
                    {
                        "code": "雨ニモマケズ\n風ニモマケズ\n雪ニモ夏ノ暑サニモマケヌ\n丈夫ナカラダヲモチ\n慾ハナク\n決シテ瞋ラズ\nイツモシヅカニワラッテヰル\n一日ニ玄米四合ト\n味噌ト少シノ野菜ヲタベ\nアラユルコトヲ\nジブンヲカンジョウニ入レズニ\nヨクミキキシワカリ\nソシテワスレズ\n野原ﾉ松ﾉ林ﾉ陰ﾉ\n小ｻﾅ萱ﾌﾞｷﾉ小屋ﾆヰﾃ\n東ﾆ病気ﾉｺﾄﾞﾓｱﾚﾊﾞ\n行ｯﾃ看病ｼﾃﾔﾘ\n西ﾆﾂｶﾚﾀ母ｱﾚﾊﾞ\n行ｯﾃｿﾉ稲ﾉ束ｦ負ﾋ\n南ﾆ死ﾆｻｳﾅ人ｱﾚﾊﾞ\n行ｯﾃｺﾊｶﾞﾗﾅｸﾃﾓｲヽﾄｲﾋ\n北ﾆｹﾝｸヮﾔｿｼｮｳｶﾞｱﾚﾊﾞ\nﾂﾏﾗﾅｲｶﾗﾔﾒﾛﾄｲﾋ\nﾋﾃﾞﾘﾉﾄｷﾊﾅﾐﾀﾞｦﾅｶﾞｼ\nｻﾑｻﾉﾅﾂﾊｵﾛｵﾛｱﾙｷ\nﾐﾝﾅﾆﾃﾞｸﾉﾎﾞーﾄﾖﾊﾞﾚ\nﾎﾒﾗﾚﾓｾｽﾞ\nｸﾆﾓｻﾚｽﾞ\nｻｳｲﾌﾓﾉﾆ\nﾜﾀｼﾊﾅﾘﾀｲ",
                        "name": "default",
                    }
                ],
                "isFailed": False,
                "isVerificationFile": False,
                "path": "testdata/targets/encoding/cp932.txt",
                "pathExtension": "txt",
                "requiredBy": [],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "LIBRARY_NO_TESTS",
                "verifiedWith": [],
            },
            "documentation_of": "testdata/targets/encoding/cp932.txt",
            "layout": "document",
            "title": "testdata/targets/encoding/cp932.txt",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/python/failure.mle.py.md",
        front_matter={
            "data": {
                "attributes": {
                    "MLE": "10",
                    "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                    "links": ["https://judge.yosupo.jp/problem/aplusb"],
                },
                "dependencies": [
                    {
                        "files": [
                            {
                                "filename": "lib_all_failure.py",
                                "icon": "LIBRARY_ALL_WA",
                                "path": "testdata/targets/python/lib_all_failure.py",
                                "title": "Lib All failure",
                            },
                            {
                                "filename": "lib_some_failure.py",
                                "icon": "LIBRARY_SOME_WA",
                                "path": "testdata/targets/python/lib_some_failure.py",
                            },
                        ],
                        "type": "Depends on",
                    },
                    {"files": [], "type": "Required by"},
                    {"files": [], "type": "Verified with"},
                ],
                "dependsOn": [
                    "testdata/targets/python/lib_all_failure.py",
                    "testdata/targets/python/lib_some_failure.py",
                ],
                "documentPath": "testdata/targets/python/sub/failure.mle.md",
                "embedded": [
                    {
                        "code": '# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/aplusb\n# competitive-verifier: MLE 10\nimport sys\n\n\nimport testdata.targets.python.lib_all_failure\nfrom testdata.targets.python.lib_some_failure import MB\n\ninput = sys.stdin.buffer.readline\n\n\ndef main() -> None:\n    a, b = map(int, input().split())\n    if a % 2 == 0:\n        sum([1] * 10 * MB)\n    print(testdata.targets.python.lib_all_failure.aplusb(a, b))\n\n\nif __name__ == "__main__":\n    main()\n',
                        "name": "default",
                    }
                ],
                "isFailed": True,
                "isVerificationFile": True,
                "path": "testdata/targets/python/failure.mle.py",
                "pathExtension": "py",
                "requiredBy": [],
                "testcases": [
                    {
                        "elapsed": 3.86,
                        "environment": "Python",
                        "memory": 32.18,
                        "name": "example_00",
                        "status": "MLE",
                    },
                    {
                        "elapsed": 5.52,
                        "environment": "Python",
                        "memory": 32.08,
                        "name": "example_01",
                        "status": "MLE",
                    },
                    {
                        "elapsed": 8.76,
                        "environment": "Python",
                        "memory": 36.62,
                        "name": "random_00",
                        "status": "MLE",
                    },
                    {
                        "elapsed": 9.5,
                        "environment": "Python",
                        "memory": 33.4,
                        "name": "random_01",
                        "status": "AC",
                    },
                    {
                        "elapsed": 4.59,
                        "environment": "Python",
                        "memory": 4.92,
                        "name": "random_02",
                        "status": "AC",
                    },
                    {
                        "elapsed": 6.24,
                        "environment": "Python",
                        "memory": 19.01,
                        "name": "random_03",
                        "status": "MLE",
                    },
                    {
                        "elapsed": 6.24,
                        "environment": "Python",
                        "memory": 60.96,
                        "name": "random_04",
                        "status": "AC",
                    },
                    {
                        "elapsed": 2.25,
                        "environment": "Python",
                        "memory": 49.52,
                        "name": "random_05",
                        "status": "AC",
                    },
                    {
                        "elapsed": 4.7,
                        "environment": "Python",
                        "memory": 69.86,
                        "name": "random_06",
                        "status": "AC",
                    },
                    {
                        "elapsed": 4.75,
                        "environment": "Python",
                        "memory": 92.7,
                        "name": "random_07",
                        "status": "MLE",
                    },
                    {
                        "elapsed": 0.89,
                        "environment": "Python",
                        "memory": 65.51,
                        "name": "random_08",
                        "status": "AC",
                    },
                    {
                        "elapsed": 8.24,
                        "environment": "Python",
                        "memory": 64.35,
                        "name": "random_09",
                        "status": "MLE",
                    },
                ],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "TEST_WRONG_ANSWER",
                "verifiedWith": [],
            },
            "documentation_of": "testdata/targets/python/failure.mle.py",
            "layout": "document",
            "title": "Failure-MLE",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/python/failure.re.py.md",
        front_matter={
            "data": {
                "attributes": {
                    "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                    "links": ["https://judge.yosupo.jp/problem/aplusb"],
                },
                "dependencies": [
                    {
                        "files": [
                            {
                                "filename": "lib_all_failure.py",
                                "icon": "LIBRARY_ALL_WA",
                                "path": "testdata/targets/python/lib_all_failure.py",
                                "title": "Lib All failure",
                            }
                        ],
                        "type": "Depends on",
                    },
                    {"files": [], "type": "Required by"},
                    {"files": [], "type": "Verified with"},
                ],
                "dependsOn": ["testdata/targets/python/lib_all_failure.py"],
                "documentPath": "testdata/targets/failure.re.md",
                "embedded": [
                    {
                        "code": '# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/aplusb\nimport sys\n\n\nimport testdata.targets.python.lib_all_failure\n\ninput = sys.stdin.buffer.readline\n\n\ndef main() -> None:\n    a, b = map(int, input().split())\n    print(testdata.targets.python.lib_all_failure.aplusb(a // 0, b))\n\n\nif __name__ == "__main__":\n    main()\n',
                        "name": "default",
                    }
                ],
                "isFailed": True,
                "isVerificationFile": True,
                "path": "testdata/targets/python/failure.re.py",
                "pathExtension": "py",
                "requiredBy": [],
                "testcases": [
                    {
                        "elapsed": 8.39,
                        "environment": "Python",
                        "memory": 49.02,
                        "name": "example_00",
                        "status": "RE",
                    },
                    {
                        "elapsed": 1.54,
                        "environment": "Python",
                        "memory": 11.86,
                        "name": "example_01",
                        "status": "RE",
                    },
                    {
                        "elapsed": 2.47,
                        "environment": "Python",
                        "memory": 21.78,
                        "name": "random_00",
                        "status": "RE",
                    },
                    {
                        "elapsed": 2.22,
                        "environment": "Python",
                        "memory": 18.88,
                        "name": "random_01",
                        "status": "RE",
                    },
                    {
                        "elapsed": 0.66,
                        "environment": "Python",
                        "memory": 99.45,
                        "name": "random_02",
                        "status": "RE",
                    },
                    {
                        "elapsed": 6.75,
                        "environment": "Python",
                        "memory": 68.16,
                        "name": "random_03",
                        "status": "RE",
                    },
                    {
                        "elapsed": 2.42,
                        "environment": "Python",
                        "memory": 10.48,
                        "name": "random_04",
                        "status": "RE",
                    },
                    {
                        "elapsed": 8.17,
                        "environment": "Python",
                        "memory": 58.68,
                        "name": "random_05",
                        "status": "RE",
                    },
                    {
                        "elapsed": 0.08,
                        "environment": "Python",
                        "memory": 19.08,
                        "name": "random_06",
                        "status": "RE",
                    },
                    {
                        "elapsed": 5.99,
                        "environment": "Python",
                        "memory": 30.79,
                        "name": "random_07",
                        "status": "RE",
                    },
                    {
                        "elapsed": 8.97,
                        "environment": "Python",
                        "memory": 8.48,
                        "name": "random_08",
                        "status": "RE",
                    },
                    {
                        "elapsed": 9.17,
                        "environment": "Python",
                        "memory": 27.24,
                        "name": "random_09",
                        "status": "RE",
                    },
                ],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "TEST_WRONG_ANSWER",
                "verifiedWith": [],
            },
            "documentation_of": "testdata/targets/python/failure.re.py",
            "layout": "document",
            "title": "Failure-RE",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/python/failure.tle.py.md",
        front_matter={
            "data": {
                "attributes": {
                    "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                    "TLE": "0.09",
                    "links": ["https://judge.yosupo.jp/problem/aplusb"],
                },
                "dependencies": [
                    {
                        "files": [
                            {
                                "filename": "lib_all_failure.py",
                                "icon": "LIBRARY_ALL_WA",
                                "path": "testdata/targets/python/lib_all_failure.py",
                                "title": "Lib All failure",
                            }
                        ],
                        "type": "Depends on",
                    },
                    {"files": [], "type": "Required by"},
                    {"files": [], "type": "Verified with"},
                ],
                "dependsOn": ["testdata/targets/python/lib_all_failure.py"],
                "documentPath": "testdata/targets/python/sub/failure.tle.md",
                "embedded": [
                    {
                        "code": '# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/aplusb\n# competitive-verifier: TLE 0.09\nimport sys\nimport time\n\n\nimport testdata.targets.python.lib_all_failure\n\ninput = sys.stdin.buffer.readline\n\n\ndef main() -> None:\n    a, b = map(int, input().split())\n    if a % 2 == 0:\n        time.sleep(0.1)\n    print(testdata.targets.python.lib_all_failure.aplusb(a, b))\n\n\nif __name__ == "__main__":\n    main()\n',
                        "name": "default",
                    }
                ],
                "isFailed": True,
                "isVerificationFile": True,
                "path": "testdata/targets/python/failure.tle.py",
                "pathExtension": "py",
                "requiredBy": [],
                "testcases": [
                    {
                        "elapsed": 0.08,
                        "environment": "Python",
                        "memory": 57.82,
                        "name": "example_00",
                        "status": "TLE",
                    },
                    {
                        "elapsed": 3.09,
                        "environment": "Python",
                        "memory": 98.62,
                        "name": "example_01",
                        "status": "TLE",
                    },
                    {
                        "elapsed": 0,
                        "environment": "Python",
                        "memory": 72.57,
                        "name": "random_00",
                        "status": "TLE",
                    },
                    {
                        "elapsed": 2.39,
                        "environment": "Python",
                        "memory": 65.36,
                        "name": "random_01",
                        "status": "AC",
                    },
                    {
                        "elapsed": 7.38,
                        "environment": "Python",
                        "memory": 16.75,
                        "name": "random_02",
                        "status": "AC",
                    },
                    {
                        "elapsed": 7.04,
                        "environment": "Python",
                        "memory": 19.56,
                        "name": "random_03",
                        "status": "TLE",
                    },
                    {
                        "elapsed": 0.18,
                        "environment": "Python",
                        "memory": 96.25,
                        "name": "random_04",
                        "status": "AC",
                    },
                    {
                        "elapsed": 2.85,
                        "environment": "Python",
                        "memory": 7.67,
                        "name": "random_05",
                        "status": "AC",
                    },
                    {
                        "elapsed": 1.37,
                        "environment": "Python",
                        "memory": 54.44,
                        "name": "random_06",
                        "status": "AC",
                    },
                    {
                        "elapsed": 0.45,
                        "environment": "Python",
                        "memory": 52.03,
                        "name": "random_07",
                        "status": "TLE",
                    },
                    {
                        "elapsed": 5.1,
                        "environment": "Python",
                        "memory": 5.15,
                        "name": "random_08",
                        "status": "AC",
                    },
                    {
                        "elapsed": 6.94,
                        "environment": "Python",
                        "memory": 73.75,
                        "name": "random_09",
                        "status": "TLE",
                    },
                ],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "TEST_WRONG_ANSWER",
                "verifiedWith": [],
            },
            "documentation_of": "testdata/targets/python/failure.tle.py",
            "layout": "document",
            "title": "Failure-TLE",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/python/failure.wa.py.md",
        front_matter={
            "data": {
                "attributes": {
                    "MLE": "10",
                    "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                    "links": ["https://judge.yosupo.jp/problem/aplusb"],
                },
                "dependencies": [
                    {
                        "files": [
                            {
                                "filename": "lib_all_failure.py",
                                "icon": "LIBRARY_ALL_WA",
                                "path": "testdata/targets/python/lib_all_failure.py",
                                "title": "Lib All failure",
                            },
                            {
                                "filename": "lib_some_skip_some_wa.py",
                                "icon": "LIBRARY_SOME_WA",
                                "path": "testdata/targets/python/lib_some_skip_some_wa.py",
                            },
                        ],
                        "type": "Depends on",
                    },
                    {"files": [], "type": "Required by"},
                    {"files": [], "type": "Verified with"},
                ],
                "dependsOn": [
                    "testdata/targets/python/lib_all_failure.py",
                    "testdata/targets/python/lib_some_skip_some_wa.py",
                ],
                "documentPath": "testdata/targets/failure.wa.md",
                "embedded": [
                    {
                        "code": '# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/aplusb\nimport sys\n\n\nimport testdata.targets.python.lib_all_failure\nfrom testdata.targets.python.lib_some_skip_some_wa import stderr\n\ninput = sys.stdin.buffer.readline\n\n\ndef main() -> None:\n    a, b = map(int, input().split())\n    stderr()\n    print(testdata.targets.python.lib_all_failure.aplusb(a, b) // 2 * 2)\n\n\nif __name__ == "__main__":\n    main()\n',
                        "name": "default",
                    }
                ],
                "isFailed": True,
                "isVerificationFile": True,
                "path": "testdata/targets/python/failure.wa.py",
                "pathExtension": "py",
                "requiredBy": [],
                "testcases": [
                    {
                        "elapsed": 1.66,
                        "environment": "Python",
                        "memory": 67.55,
                        "name": "example_00",
                        "status": "AC",
                    },
                    {
                        "elapsed": 8.36,
                        "environment": "Python",
                        "memory": 54.78,
                        "name": "example_01",
                        "status": "AC",
                    },
                    {
                        "elapsed": 6.5,
                        "environment": "Python",
                        "memory": 96.77,
                        "name": "random_00",
                        "status": "AC",
                    },
                    {
                        "elapsed": 5.49,
                        "environment": "Python",
                        "memory": 28.57,
                        "name": "random_01",
                        "status": "WA",
                    },
                    {
                        "elapsed": 8.59,
                        "environment": "Python",
                        "memory": 2.27,
                        "name": "random_02",
                        "status": "WA",
                    },
                    {
                        "elapsed": 7.96,
                        "environment": "Python",
                        "memory": 3.72,
                        "name": "random_03",
                        "status": "AC",
                    },
                    {
                        "elapsed": 7.5,
                        "environment": "Python",
                        "memory": 91.85,
                        "name": "random_04",
                        "status": "WA",
                    },
                    {
                        "elapsed": 7.42,
                        "environment": "Python",
                        "memory": 69.59,
                        "name": "random_05",
                        "status": "WA",
                    },
                    {
                        "elapsed": 4.52,
                        "environment": "Python",
                        "memory": 2.56,
                        "name": "random_06",
                        "status": "AC",
                    },
                    {
                        "elapsed": 4.53,
                        "environment": "Python",
                        "memory": 54.8,
                        "name": "random_07",
                        "status": "AC",
                    },
                    {
                        "elapsed": 6.39,
                        "environment": "Python",
                        "memory": 41.19,
                        "name": "random_08",
                        "status": "WA",
                    },
                    {
                        "elapsed": 5.67,
                        "environment": "Python",
                        "memory": 24.36,
                        "name": "random_09",
                        "status": "WA",
                    },
                ],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "TEST_WRONG_ANSWER",
                "verifiedWith": [],
            },
            "documentation_of": "testdata/targets/python/failure.wa.py",
            "layout": "document",
            "title": "Failure-WA",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/python/lib_all_failure.py.md",
        content=b"# Lib All failure",
        front_matter={
            "data": {
                "attributes": {"links": []},
                "dependencies": [
                    {"files": [], "type": "Depends on"},
                    {"files": [], "type": "Required by"},
                    {
                        "files": [
                            {
                                "filename": "failure.mle.py",
                                "icon": "TEST_WRONG_ANSWER",
                                "path": "testdata/targets/python/failure.mle.py",
                                "title": "Failure-MLE",
                            },
                            {
                                "filename": "failure.re.py",
                                "icon": "TEST_WRONG_ANSWER",
                                "path": "testdata/targets/python/failure.re.py",
                                "title": "Failure-RE",
                            },
                            {
                                "filename": "failure.tle.py",
                                "icon": "TEST_WRONG_ANSWER",
                                "path": "testdata/targets/python/failure.tle.py",
                                "title": "Failure-TLE",
                            },
                            {
                                "filename": "failure.wa.py",
                                "icon": "TEST_WRONG_ANSWER",
                                "path": "testdata/targets/python/failure.wa.py",
                                "title": "Failure-WA",
                            },
                        ],
                        "type": "Verified with",
                    },
                ],
                "dependsOn": [],
                "documentPath": "testdata/targets/python/docs_lib_all_failure.md",
                "embedded": [
                    {
                        "code": "def aplusb(a: int, b: int):\n    return a + b\n",
                        "name": "default",
                    }
                ],
                "isFailed": True,
                "isVerificationFile": False,
                "path": "testdata/targets/python/lib_all_failure.py",
                "pathExtension": "py",
                "requiredBy": [],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "LIBRARY_ALL_WA",
                "verifiedWith": [
                    "testdata/targets/python/failure.mle.py",
                    "testdata/targets/python/failure.re.py",
                    "testdata/targets/python/failure.tle.py",
                    "testdata/targets/python/failure.wa.py",
                ],
            },
            "documentation_of": "testdata/targets/python/lib_all_failure.py",
            "layout": "document",
            "title": "Lib All failure",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/python/lib_all_success.py.md",
        content=b"# Lib All Success",
        front_matter={
            "data": {
                "attributes": {"links": []},
                "dependencies": [
                    {"files": [], "type": "Depends on"},
                    {"files": [], "type": "Required by"},
                    {
                        "files": [
                            {
                                "filename": "success2.py",
                                "icon": "TEST_ACCEPTED",
                                "path": "testdata/targets/python/success2.py",
                                "title": "Success2",
                            }
                        ],
                        "type": "Verified with",
                    },
                ],
                "dependsOn": [],
                "documentPath": "testdata/targets/python/docs_lib_all_success.md",
                "embedded": [
                    {
                        "code": "def aplusb(a: int, b: int):\n    return a + b\n",
                        "name": "default",
                    }
                ],
                "isFailed": False,
                "isVerificationFile": False,
                "path": "testdata/targets/python/lib_all_success.py",
                "pathExtension": "py",
                "requiredBy": [],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "LIBRARY_ALL_AC",
                "verifiedWith": ["testdata/targets/python/success2.py"],
            },
            "documentation_of": "testdata/targets/python/lib_all_success.py",
            "layout": "document",
            "title": "Lib All Success",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/python/lib_skip.py.md",
        content=b"# Skip",
        front_matter={
            "data": {
                "attributes": {"links": []},
                "dependencies": [
                    {"files": [], "type": "Depends on"},
                    {"files": [], "type": "Required by"},
                    {
                        "files": [
                            {
                                "filename": "skip.py",
                                "icon": "TEST_WAITING_JUDGE",
                                "path": "testdata/targets/python/skip.py",
                            }
                        ],
                        "type": "Verified with",
                    },
                ],
                "dependsOn": [],
                "documentPath": "testdata/targets/python/docs_skip.md",
                "embedded": [
                    {
                        "code": "def aplusb(a: int, b: int):\n    return a + b\n",
                        "name": "default",
                    }
                ],
                "isFailed": False,
                "isVerificationFile": False,
                "path": "testdata/targets/python/lib_skip.py",
                "pathExtension": "py",
                "requiredBy": [],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "LIBRARY_NO_TESTS",
                "verifiedWith": ["testdata/targets/python/skip.py"],
            },
            "documentation_of": "testdata/targets/python/lib_skip.py",
            "layout": "document",
            "title": "Skip Library",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/python/lib_some_failure.py.md",
        front_matter={
            "data": {
                "attributes": {"links": []},
                "dependencies": [
                    {"files": [], "type": "Depends on"},
                    {"files": [], "type": "Required by"},
                    {
                        "files": [
                            {
                                "filename": "failure.mle.py",
                                "icon": "TEST_WRONG_ANSWER",
                                "path": "testdata/targets/python/failure.mle.py",
                                "title": "Failure-MLE",
                            },
                            {
                                "filename": "success1.py",
                                "icon": "TEST_ACCEPTED",
                                "path": "testdata/targets/python/success1.py",
                                "title": "Success1",
                            },
                        ],
                        "type": "Verified with",
                    },
                ],
                "dependsOn": [],
                "embedded": [
                    {"code": "KB = 1024\nMB = 1024 * 1024\n", "name": "default"}
                ],
                "isFailed": True,
                "isVerificationFile": False,
                "path": "testdata/targets/python/lib_some_failure.py",
                "pathExtension": "py",
                "requiredBy": [],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "LIBRARY_SOME_WA",
                "verifiedWith": [
                    "testdata/targets/python/failure.mle.py",
                    "testdata/targets/python/success1.py",
                ],
            },
            "documentation_of": "testdata/targets/python/lib_some_failure.py",
            "layout": "document",
            "title": "testdata/targets/python/lib_some_failure.py",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/python/lib_some_skip.py.md",
        front_matter={
            "data": {
                "attributes": {"links": []},
                "dependencies": [
                    {"files": [], "type": "Depends on"},
                    {"files": [], "type": "Required by"},
                    {
                        "files": [
                            {
                                "filename": "success1.py",
                                "icon": "TEST_ACCEPTED",
                                "path": "testdata/targets/python/success1.py",
                                "title": "Success1",
                            }
                        ],
                        "type": "Verified with",
                    },
                ],
                "dependsOn": [],
                "embedded": [
                    {
                        "code": "def aplusb(a: int, b: int):\n    return a + b\n",
                        "name": "default",
                    }
                ],
                "isFailed": False,
                "isVerificationFile": False,
                "path": "testdata/targets/python/lib_some_skip.py",
                "pathExtension": "py",
                "requiredBy": [],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "LIBRARY_ALL_AC",
                "verifiedWith": ["testdata/targets/python/success1.py"],
            },
            "documentation_of": "testdata/targets/python/lib_some_skip.py",
            "layout": "document",
            "title": "testdata/targets/python/lib_some_skip.py",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/python/lib_some_skip_some_wa.py.md",
        front_matter={
            "data": {
                "attributes": {"links": []},
                "dependencies": [
                    {"files": [], "type": "Depends on"},
                    {"files": [], "type": "Required by"},
                    {
                        "files": [
                            {
                                "filename": "failure.wa.py",
                                "icon": "TEST_WRONG_ANSWER",
                                "path": "testdata/targets/python/failure.wa.py",
                                "title": "Failure-WA",
                            },
                            {
                                "filename": "skip.py",
                                "icon": "TEST_WAITING_JUDGE",
                                "path": "testdata/targets/python/skip.py",
                            },
                            {
                                "filename": "success2.py",
                                "icon": "TEST_ACCEPTED",
                                "path": "testdata/targets/python/success2.py",
                                "title": "Success2",
                            },
                        ],
                        "type": "Verified with",
                    },
                ],
                "dependsOn": [],
                "embedded": [
                    {
                        "code": 'import sys\n\n\ndef stderr():\n    print("Debug", file=sys.stderr)\n',
                        "name": "default",
                    }
                ],
                "isFailed": True,
                "isVerificationFile": False,
                "path": "testdata/targets/python/lib_some_skip_some_wa.py",
                "pathExtension": "py",
                "requiredBy": [],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "LIBRARY_SOME_WA",
                "verifiedWith": [
                    "testdata/targets/python/failure.wa.py",
                    "testdata/targets/python/skip.py",
                    "testdata/targets/python/success2.py",
                ],
            },
            "documentation_of": "testdata/targets/python/lib_some_skip_some_wa.py",
            "layout": "document",
            "title": "testdata/targets/python/lib_some_skip_some_wa.py",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/python/skip.py.md",
        front_matter={
            "data": {
                "attributes": {
                    "IGNORE": "",
                    "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                    "links": ["https://judge.yosupo.jp/problem/aplusb"],
                },
                "dependencies": [
                    {
                        "files": [
                            {
                                "filename": "lib_skip.py",
                                "icon": "LIBRARY_NO_TESTS",
                                "path": "testdata/targets/python/lib_skip.py",
                                "title": "Skip Library",
                            },
                            {
                                "filename": "lib_some_skip_some_wa.py",
                                "icon": "LIBRARY_SOME_WA",
                                "path": "testdata/targets/python/lib_some_skip_some_wa.py",
                            },
                        ],
                        "type": "Depends on",
                    },
                    {"files": [], "type": "Required by"},
                    {"files": [], "type": "Verified with"},
                ],
                "dependsOn": [
                    "testdata/targets/python/lib_skip.py",
                    "testdata/targets/python/lib_some_skip_some_wa.py",
                ],
                "embedded": [
                    {
                        "code": '# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/aplusb\n# competitive-verifier: IGNORE\nimport sys\n\n\nimport testdata.targets.python.lib_skip\nfrom testdata.targets.python.lib_some_skip_some_wa import stderr\n\ninput = sys.stdin.buffer.readline\n\n\ndef main() -> None:\n    stderr()\n    a, b = map(int, input().split())\n    print(testdata.targets.python.lib_skip.aplusb(a, b))\n\n\nif __name__ == "__main__":\n    main()\n',
                        "name": "default",
                    }
                ],
                "isFailed": False,
                "isVerificationFile": True,
                "path": "testdata/targets/python/skip.py",
                "pathExtension": "py",
                "requiredBy": [],
                "testcases": [],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "TEST_WAITING_JUDGE",
                "verifiedWith": [],
            },
            "documentation_of": "testdata/targets/python/skip.py",
            "layout": "document",
            "title": "testdata/targets/python/skip.py",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/python/success1.py.md",
        front_matter={
            "data": {
                "attributes": {
                    "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                    "links": ["https://judge.yosupo.jp/problem/aplusb"],
                },
                "dependencies": [
                    {
                        "files": [
                            {
                                "filename": "lib_some_failure.py",
                                "icon": "LIBRARY_SOME_WA",
                                "path": "testdata/targets/python/lib_some_failure.py",
                            },
                            {
                                "filename": "lib_some_skip.py",
                                "icon": "LIBRARY_ALL_AC",
                                "path": "testdata/targets/python/lib_some_skip.py",
                            },
                        ],
                        "type": "Depends on",
                    },
                    {"files": [], "type": "Required by"},
                    {"files": [], "type": "Verified with"},
                ],
                "dependsOn": [
                    "testdata/targets/python/lib_some_failure.py",
                    "testdata/targets/python/lib_some_skip.py",
                ],
                "documentPath": "testdata/targets/python/docs_success1.md",
                "embedded": [
                    {
                        "code": '# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/aplusb\nimport sys\n\n\nimport testdata.targets.python.lib_some_skip\nfrom testdata.targets.python.lib_some_failure import KB\n\ninput = sys.stdin.buffer.readline\n\n\ndef main() -> None:\n    a, b = map(int, input().split())\n    if KB < 1000:\n        print("No")\n    print(testdata.targets.python.lib_some_skip.aplusb(a, b))\n\n\nif __name__ == "__main__":\n    main()\n',
                        "name": "default",
                    }
                ],
                "isFailed": False,
                "isVerificationFile": True,
                "path": "testdata/targets/python/success1.py",
                "pathExtension": "py",
                "requiredBy": [],
                "testcases": [
                    {
                        "elapsed": 5.46,
                        "environment": "Python",
                        "memory": 12.28,
                        "name": "example_00",
                        "status": "AC",
                    },
                    {
                        "elapsed": 2.61,
                        "environment": "Python",
                        "memory": 42.9,
                        "name": "example_01",
                        "status": "AC",
                    },
                    {
                        "elapsed": 4.92,
                        "environment": "Python",
                        "memory": 86.99,
                        "name": "random_00",
                        "status": "AC",
                    },
                    {
                        "elapsed": 8.15,
                        "environment": "Python",
                        "memory": 48.74,
                        "name": "random_01",
                        "status": "AC",
                    },
                    {
                        "elapsed": 9.65,
                        "environment": "Python",
                        "memory": 83.95,
                        "name": "random_02",
                        "status": "AC",
                    },
                    {
                        "elapsed": 0.11,
                        "environment": "Python",
                        "memory": 71.94,
                        "name": "random_03",
                        "status": "AC",
                    },
                    {
                        "elapsed": 9.8,
                        "environment": "Python",
                        "memory": 56.89,
                        "name": "random_04",
                        "status": "AC",
                    },
                    {
                        "elapsed": 1.62,
                        "environment": "Python",
                        "memory": 51.09,
                        "name": "random_05",
                        "status": "AC",
                    },
                    {
                        "elapsed": 6.3,
                        "environment": "Python",
                        "memory": 84.93,
                        "name": "random_06",
                        "status": "AC",
                    },
                    {
                        "elapsed": 8.89,
                        "environment": "Python",
                        "memory": 70.98,
                        "name": "random_07",
                        "status": "AC",
                    },
                    {
                        "elapsed": 9.83,
                        "environment": "Python",
                        "memory": 27.53,
                        "name": "random_08",
                        "status": "AC",
                    },
                    {
                        "elapsed": 9.22,
                        "environment": "Python",
                        "memory": 7.34,
                        "name": "random_09",
                        "status": "AC",
                    },
                ],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "TEST_ACCEPTED",
                "verifiedWith": [],
            },
            "documentation_of": "testdata/targets/python/success1.py",
            "layout": "document",
            "title": "Success1",
        },
    ),
    MarkdownData(
        path=f"{TARGETS_PATH}/python/success2.py.md",
        front_matter={
            "data": {
                "attributes": {
                    "PROBLEM": "https://judge.yosupo.jp/problem/aplusb",
                    "links": ["https://judge.yosupo.jp/problem/aplusb"],
                },
                "dependencies": [
                    {
                        "files": [
                            {
                                "filename": "lib_all_success.py",
                                "icon": "LIBRARY_ALL_AC",
                                "path": "testdata/targets/python/lib_all_success.py",
                                "title": "Lib All Success",
                            },
                            {
                                "filename": "lib_some_skip_some_wa.py",
                                "icon": "LIBRARY_SOME_WA",
                                "path": "testdata/targets/python/lib_some_skip_some_wa.py",
                            },
                        ],
                        "type": "Depends on",
                    },
                    {"files": [], "type": "Required by"},
                    {"files": [], "type": "Verified with"},
                ],
                "dependsOn": [
                    "testdata/targets/python/lib_all_success.py",
                    "testdata/targets/python/lib_some_skip_some_wa.py",
                ],
                "documentPath": "testdata/targets/python/docs_success2.md",
                "embedded": [
                    {
                        "code": '# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/aplusb\nimport sys\n\n\nimport testdata.targets.python.lib_all_success\nfrom testdata.targets.python.lib_some_skip_some_wa import stderr\n\ninput = sys.stdin.buffer.readline\n\n\ndef main() -> None:\n    a, b = map(int, input().split())\n    stderr()\n    print(testdata.targets.python.lib_all_success.aplusb(a, b))\n\n\nif __name__ == "__main__":\n    main()\n',
                        "name": "default",
                    }
                ],
                "isFailed": False,
                "isVerificationFile": True,
                "path": "testdata/targets/python/success2.py",
                "pathExtension": "py",
                "requiredBy": [],
                "testcases": [
                    {
                        "elapsed": 6.49,
                        "environment": "Python",
                        "memory": 47.75,
                        "name": "example_00",
                        "status": "AC",
                    },
                    {
                        "elapsed": 5.34,
                        "environment": "Python",
                        "memory": 33.01,
                        "name": "example_01",
                        "status": "AC",
                    },
                    {
                        "elapsed": 5.7,
                        "environment": "Python",
                        "memory": 94.96,
                        "name": "random_00",
                        "status": "AC",
                    },
                    {
                        "elapsed": 2.85,
                        "environment": "Python",
                        "memory": 64.89,
                        "name": "random_01",
                        "status": "AC",
                    },
                    {
                        "elapsed": 8.46,
                        "environment": "Python",
                        "memory": 25.92,
                        "name": "random_02",
                        "status": "AC",
                    },
                    {
                        "elapsed": 9.48,
                        "environment": "Python",
                        "memory": 48.09,
                        "name": "random_03",
                        "status": "AC",
                    },
                    {
                        "elapsed": 4.52,
                        "environment": "Python",
                        "memory": 60.27,
                        "name": "random_04",
                        "status": "AC",
                    },
                    {
                        "elapsed": 0.1,
                        "environment": "Python",
                        "memory": 48.76,
                        "name": "random_05",
                        "status": "AC",
                    },
                    {
                        "elapsed": 0.73,
                        "environment": "Python",
                        "memory": 2.49,
                        "name": "random_06",
                        "status": "AC",
                    },
                    {
                        "elapsed": 5.55,
                        "environment": "Python",
                        "memory": 54.47,
                        "name": "random_07",
                        "status": "AC",
                    },
                    {
                        "elapsed": 6.69,
                        "environment": "Python",
                        "memory": 11.32,
                        "name": "random_08",
                        "status": "AC",
                    },
                    {
                        "elapsed": 4.81,
                        "environment": "Python",
                        "memory": 42.05,
                        "name": "random_09",
                        "status": "AC",
                    },
                ],
                "timestamp": "2023-12-04 05:06:07.008910+09:00",
                "verificationStatus": "TEST_ACCEPTED",
                "verifiedWith": [],
            },
            "documentation_of": "testdata/targets/python/success2.py",
            "layout": "document",
            "title": "Success2",
        },
    ),
]