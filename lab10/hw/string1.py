#!/usr/bin/env python3


def donuts(count) -> str:
    # +++your code here+++

    res: str = "Number of donuts: "

    if count >= 10:
        res = res + "many"
    else:
        res = res + str(count)

    return res


def both_ends(s) -> str:
    if len(s) < 2:
        res: str = ""
    else:
        res = s[:2] + s[-2:]
    return res


def fix_start(s) -> str:
    # +++your code here+++
    res: str = ""
    for i in range(0, len(s)):
        if s[0] == s[i] and i != 0:
            res = res + "*"
        else:
            res = res + s[i]
    return res


def mix_up(a, b) -> str:
    res1: str = b[:2] + a[2:]
    res2: str = a[:2] + b[2:]

    return f"{res1} {res2}"
