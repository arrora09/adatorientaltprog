num = 1000
l = [[j * i for j in range(1, num + 1)] for i in range(1, num + 1)]

maxlen = max([max([len(str(n)) for n in sl]) for sl in l])


for sl in l:
    print("".join([f"{n:<{maxlen+1}}" for n in sl]))
