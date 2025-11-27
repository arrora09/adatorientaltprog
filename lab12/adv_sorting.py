from typing import Tuple, List

help(sorted)

words = ["aaa", "a", "aaaa", "bb"]

print(sorted(words))
print(sorted(words, key=len))

words = ["BB", "aa", "Cc", "zz"]

print(sorted(words))
print(sorted(words, key=str.lower))

words = ["xc", "zb", "yd", "wa"]
print(sorted(words))


def my_func(s):
    return s[-1]


print(sorted(words, key=my_func))

print()
print()
# 1
data = [
    (1, "Albany", "NY", 162692),
    (121, "Wyoming", "NY", 8722),
    (3, "Allegany", "NY", 11986),
    (123, "Yates", "NY", 5094),
]


def f1(t: Tuple[int, str, str, int]) -> int:
    return t[-1]


print(sorted(data, key=f1))
print(sorted(data, key=lambda x: x[-1]))

# 2
users = ["10:User1", "80:User2", "100:User3", "00:User4", "75:User4", "45:User5"]


def f2(user: str) -> int:
    return int(user.split(":")[0])


print(sorted(users, key=f2, reverse=True))
print(sorted(users, key=lambda user: int(user.split(":")[0]), reverse=True))

# 3
matrix = [[2, 6], [1, 3], [5, 4]]


def f3(l: List[int]) -> int:
    return l[1]


print(sorted(matrix, key=f3))
print(sorted(matrix, key=lambda l: l[1]))
