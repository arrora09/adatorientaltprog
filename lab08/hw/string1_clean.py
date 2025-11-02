



def donuts(count):

    res = "Number of donuts: "

    if count >= 10:
        res = res + "many"
    else:
        res = res + str(count)

    return res


def both_ends(s):
    if len(s) < 2:
        res = ""
    else:
        res = s[:2] + s[-2:]
    return res


def fix_start(s):
    res = ""
    for i in range(0, len(s)):
        if s[0] == s[i] and i != 0:
            res = res + "*"
        else:
            res = res + s[i]
    return res


def mix_up(a, b):
    res1 = b[:2] + a[2:]
    res2 = a[:2] + b[2:]

    return f"{res1} {res2}"


def test(got, expected):
    if got == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print("{p} got: {g}; expected: {e}".format(p=prefix, g=got, e=expected))


def main():
    print("donuts")
    test(donuts(4), "Number of donuts: 4")
    test(donuts(9), "Number of donuts: 9")
    test(donuts(10), "Number of donuts: many")
    test(donuts(99), "Number of donuts: many")

    print()
    print("both_ends")
    test(both_ends("spring"), "spng")
    test(both_ends("Hello"), "Helo")
    test(both_ends("a"), "")
    test(both_ends("xyz"), "xyyz")

    print()
    print("fix_start")
    test(fix_start("babble"), "ba**le")
    test(fix_start("aardvark"), "a*rdv*rk")
    test(fix_start("google"), "goo*le")
    test(fix_start("donut"), "donut")

    print()
    print("mix_up")
    test(mix_up("mix", "pod"), "pox mid")
    test(mix_up("dog", "dinner"), "dig donner")
    test(mix_up("gnash", "sport"), "spash gnort")
    test(mix_up("pezzy", "firm"), "fizzy perm")



if __name__ == "__main__":
    main()
