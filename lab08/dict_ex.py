d = {1: [2, 5, 8], 8: [2, 6, 9, 9], 10: [8, 8]}

print(d[1])

print(d.get(3, "error"))

n = 2

for e in d.get(n, []):
    print(e)
