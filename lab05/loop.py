li = ["alfa", "beta", "gamma"]

# manualisan
i = 0

for e in li:
    print(f"{i}: {e}")
    i += 1

# vagy

for i in range(len(li)):
    print(f"{i}: {li[i]}")

# enumerate
for i, e in enumerate(li):
    print(f"{i}: {e}")

print(enumerate(li))
print(list(enumerate(li)))
print(list(enumerate(li, start=1)))
# meg lehet adni a start erteket
