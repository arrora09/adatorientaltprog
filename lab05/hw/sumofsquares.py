s1 = sum([n**2 for n in range(101)])

s2 = sum([n for n in range(101)]) ** 2

print(s1)
print(s2)


print(s2 - s1)
