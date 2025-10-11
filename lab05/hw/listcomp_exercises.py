# 1
print([s.upper() + "!" for s in ["auto", "villamos", "metro"]])
# 2
print([s.capitalize() for s in ["aladar", "bela", "cecil"]])
# 3
print([0 for n in range(10)])
# lehetne [0]*10 is, de nvm
# 4
print([2 * n for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
# 5
print([int(n) for n in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]])
# 6
print([int(s) for s in "1234567"])
# 7
print([len(s) for s in "The quick brown fox jumps over the lazy dog".split()])
# 8
print([s[0] for s in "python is an awesome language".split()])
# 9
print([(s, len(s)) for s in "The quick brown fox jumps over the lazy dog".split()])
# 10
print([n for n in range(10) if n % 2 == 0])
# 11
print([n**2 for n in range(20) if n ** 2 % 2 == 0])
# 12
print([n**2 for n in range(20) if str(n**2)[-1] == "4"])
# 13
print("".join([chr(s) for s in range(ord("A"), ord("Z") + 1)]))
# 14
print([s.strip() for s in [" apple ", " banana ", " kiwi"]])
# 15
print("".join([str(n) for n in [1, 0, 1, 1, 0, 1, 0, 0]]))
