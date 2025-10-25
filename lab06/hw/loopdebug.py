def loop(num, debug=False):
    if debug:
        print("# ciklus kezdete")

    for i in range(num):
        print(i + 1, end=" ")

    if debug:
        print("")
        print("# ciklus vege")


loop(5)
print()
loop(5, debug=True)
