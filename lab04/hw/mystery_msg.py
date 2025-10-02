TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


def main():
    global TEXT

    abc = "aábcdeéfgghiíjklmnoóöőpqrstuúüűvwyxz"
    ABC = abc.upper()

    nt = ""
    for x in TEXT:
        if x in abc:
            a = ((ord(x) + 2 - ord("a")) % 26) + ord("a")
            nt = nt + chr(a)
        elif x in ABC:
            a = ((ord(x) + 2 - ord("A")) % 26) + ord("A")
            nt = nt + chr(a)
        else:
            nt = nt + x

    print(nt)


if __name__ == "__main__":
    main()
