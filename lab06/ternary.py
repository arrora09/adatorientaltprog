def loop(num, debug=False, twice=False):
    if debug:
        print("# start loop")

    multiplier = 2 if twice else 1

    for i in range(num):
        print((i + 1) * multiplier)

    if debug:
        print("# end loop")


loop(5, debug=True)
print()
loop(5, debug=True, twice=True)
