import collections

a = [3, 6, 2]

print(len(a))

print(a[:2])
print(a[-2:])

print([1, 2] == [1, 2])
print([1, 2] == [1, 3])

b = [True, 3.14, 42, "asd"]
# heterogen, de inakbb homogenkent kene kezelni

print(type(a))

print([1, 2] + [5, 8])

a = [1, 2, 3]
b = a
b[0] = 100
print(a)

print()


for e in a:
    print(e)


for e in a:
    e *= a

print(a)


print(list("asd"))
# karakterekre szedi


# nem ajanlott beepitett fv nevekre nevezni valtozokat


res = []

for e in a:
    if e % 2 == 0:
        res.append(e)

print(res)

print()
a = [6, 2, 9]

print(a)

print(8 in a)
print(9 in a)

print()


s = "c, c++, d, java"

print("--" in s)
print("++" in s)

print()


li = [6, 2, 9]


print("verem")
print(li)
li.append(10)

print(li)

li.pop(2)
print(li)

li.pop()
print(li)


print()

print("sor")
li.append(123)
print(li)
li.pop(0)
print(li)


q = collections.deque([3, 4, 5])
print(q)

q.append(6)
q.append(7)

print(q)

q.popleft()
print(q)


print()
print("torles")
del q

a = [3, 7, 4, 9]

del a[1]

print(a)

print()
print()
a = [3, 4, 9]
print(a)
a.insert(2, 5)
print(a)
a.insert(-2, 100)
print(a)

print()


b = [1, 2, 3]
# a.append(b)
print(a)


print(a.extend(b))
print(a)


print(a.index(100))
# exception ha nincs benne

a.remove(100)
print(a)

a.remove(3)
print(a)
# csak az elso elemet torli
# ugyan ugy exception, ha nincs


print()


sorted(a)
print(a)
print(sorted(a))
# a sorted beepitett fv, kap egy listat, de azt nem modositja, uj masoaltot keszit rola. helyben rendezi es adja vissza azt

b = sorted(a)
print(b)

c = sorted(a, reverse=True)
print(c)

sl = ["dd", "cc", "aa", "bb"]
print(sorted(sl))

print()
print(a)
a.sort()
print(a)
# a .sort() nem beepitett fv, hanem eljarasa a list osztalynak
# nem ad vissza erteket, hanem helyben rendezi a listat

# vagy a=sorted(a) vagy a.sort() es done

print()
print(max(a))
print(min(a))
print(sum(a))

print()
s = "aa:bb:cc:dd"
print(s)
print(s.split(":"))

s2 = "            dfas             sdf               sdf            sdfsdf"
print(s2.split())


li = ["aa", "bb", "cc", "dd"]
print(":".join(li))
print(":::".join(li))


print()
print(list(range(20)))
print(range(20))
print((range(5, 20)))
print(list(range(5, 20)))
print((range(5, 20, 2)))
print(list(range(5, 20, 2)))
print((range(20, 10, -1)))
print(list(range(20, 10, -1)))

print()
print(list(range(23, 46)))
print(list(range(42, 22, -1)))
