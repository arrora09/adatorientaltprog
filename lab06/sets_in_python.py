from mimetypes import guess_type
from traceback import print_tb

kosar = ["alma", "ananasz", "banan", "alma", "narancs", "banan"]
print(kosar)
gyumolcs = set(kosar)
print(gyumolcs)
print(type(kosar))
print(type(gyumolcs))

vissza = list(gyumolcs)
print(vissza)
print(type(vissza))

print()
print(sorted(gyumolcs))
# a sorted mindig egy litat ad vissza, akarmi a bemenet

print(sorted("aladar"))

print()


print("alma" in gyumolcs)
print("kiwi" in gyumolcs)

print()
# ures halmaz
emptyset = set()
print(emptyset)
print(type(emptyset))

emptyset.add(8)
print(emptyset)

a = ["alma", "banan", "citrom"]
a = set(a)
print(a)

b = set()

b.add("banan")
b.add("narancs")
print(b)
print("unio")
print(a.union(b))
print("intersection")
print(a.intersection(b))
print("diff")
print(a.difference(b))

print()
print()
a.remove("citrom")
print(a)
