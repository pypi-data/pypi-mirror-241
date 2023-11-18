import sys

sys.setrecursionlimit(500000)


def readInt() -> any:
    return int(sys.stdin.readline().rstrip())


def readIntLine() -> any:
    return list(map(int, sys.stdin.readline().rstrip().split()))


def readString() -> any:
    return sys.stdin.readline().rstrip()


def readStringLine() -> any:
    return list(sys.stdin.readline().rstrip().split())
