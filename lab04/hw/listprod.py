from math import prod

def listprod(li):
    return 1 if len(li)==0 else prod(li)

def main():
    print(listprod([1,2,3]))
    print(listprod([1,2,4]))
    print(listprod([1,2,5]))
    print(listprod([]))


if __name__ == "__main__":
    main()
