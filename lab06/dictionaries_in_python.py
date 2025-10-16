# kulcs ertek parok

d = {}
print(d)
d["a"] = "alfa"
d["b"] = "beta"
d["g"] = "gamma"
print(d)
print(d["g"])
print(d.get("g"))
print(d.get("c"))
print(d.get("c", "not found"))
print(d.get("g", "not found"))
d["a"] = "ALFA"
print(d)

d2 = {1: "egy", 2: "ketto"}
print(d2)

print(d.keys())
print(list(d.keys()))
print(d.values())

print()

for e in sorted(d.keys()):
    print(f"{e}: {d[e]}")

print()

for key, value in d.items():
    print(f"{key}: {value}")

print()
del d["a"]
print(d)
