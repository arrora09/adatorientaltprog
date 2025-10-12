print(sum(range(101)))


print()

li = [list(str(n)) for n in range(101)]

res = 0
for e in li:
    for s in e:
        res += int(s)

print(res)
