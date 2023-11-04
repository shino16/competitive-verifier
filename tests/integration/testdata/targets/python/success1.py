# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/aplusb
import sys

import targets.python.lib_some_skip
from targets.python.lib_some_failure import KB

input = sys.stdin.buffer.readline


def main() -> None:
    a, b = map(int, input().split())
    if KB < 1000:
        print("No")
    print(targets.python.lib_some_skip.aplusb(a, b))


if __name__ == "__main__":
    main()
