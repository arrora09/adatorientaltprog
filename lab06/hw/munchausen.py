def f1():
    li = []
    li.append(0)
    print(0)
    for i in range(10000):
        s = str(i)
        summa = 0
        for x in s:
            summa += int(x) ** int(x)

        if summa == i:
            li.append(i)

        i += 1

    print(li)


def f2():
    print(0)
    for i in range(440000000):
        nums = (int(j) for j in str(i))

        if sum(j**j for j in nums) == i:
            print(i)


f1()
f2()
