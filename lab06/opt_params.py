def greet(name, greeting="Hello"):
    print(f"{greeting} {name}")


greet("Aron")
print()
greet("Aron", greeting="Hola")
print()
greet("Aron", greeting="Bonjour")


print()


def hello(name, repeat=1, postfix=""):
    for i in range(repeat):
        print(name + postfix)


hello("Aron")
print()
hello("Aron", repeat=3)
print()
hello("Aron", repeat=2, postfix="!")

# a kotelezo csak a name, a tobbi opcionalis
# a valtozonevek feltuntetesevel lehet a sorrendet modositani, kul sorban

print()


def loop(num, debug=False, twice=False):
    if debug:
        print("# start loop")

    def linePrint(multiply=1):
        for i in range(num):
            print((i + 1) * multiply)

    if twice:
        linePrint(2)
    else:
        linePrint()

    if debug:
        print("# end loop")


loop(5)
print()
loop(5, debug=True)
print()
loop(5, debug=True, twice=True)
