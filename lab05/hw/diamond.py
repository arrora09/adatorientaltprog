def diamond(h):
    if h % 2 == 0:
        print("hiba: a magassag nem paratlan")
        return
    for i in range(1, h, 2):
        print(str("*" * i).center(h))
    for i in range(h, 0, -2):
        print(str("*" * i).center(h))


diamond(3)
print()
diamond(4)
print()
diamond(5)
print()
diamond(7)
