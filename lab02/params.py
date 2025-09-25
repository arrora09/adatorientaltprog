import sys

def main():
    try:
        print("Hello "+sys.argv[1]+"!")
    except IndexError:
        print("nincs megadva nev")


def main2():
    try:
        if  sys.argv[1] == "Batman" or sys.argv[1] == "Robin":
            print("Denevérveszély!")
        else:
            print("Hello " + sys.argv[1] + "!")
    except IndexError:
        print("nincs megadva nev")

if __name__=="__main__":
    main2()