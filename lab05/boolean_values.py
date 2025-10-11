# hamisnak szamit
print(False)
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool({}))

# barmi mas mar
print(bool("asd"))
print(bool(1))
print(bool([1]))

li = []
# if .... :
#   print("nem ures")
if li:
    print("nem ures")

# if .... :
#   print("ures")
if not li:
    print("nem ures")
