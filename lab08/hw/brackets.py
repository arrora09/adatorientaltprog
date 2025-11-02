def test(p):
    l = []
    for c in p:
        if c == "(":
            l.append("(")

        elif c == ")":
            if l[-1] != "(":
                return False
            else:
                l.remove("(")

        if c == "[":
            l.append("[")

        elif c == "]":
            if l[-1] != "[":
                return False
            else:
                l.remove("[")

        if c == "{":
            l.append("{")

        elif c == "}":
            if l[-1] != "{":
                return False

            else:
                l.remove("{")

    return len(l) == 0


print(test("((5+3)*2+1)") == True)
print(test("{[(3+1)+2]+}") == True)
print(test("(3+{1-1)}") == False)
print(test("[1+1]+(2*2)-{3/3}") == True)
print(test("(({[(((1)-2)+3)-3]/3}-3)") == False)
