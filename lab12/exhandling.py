def main():
    while True:
        try:
            szam1 = float(input("1. szam: "))
            szam2 = float(input("2. szam: "))
            result = szam1 / szam2
            print("Az osztas eredmenye: {0:.2f}".format(result))
            print("-" * 10)
        except ZeroDivisionError:
            print("0-val való osztás nem megengedett")
        except ValueError:
            print("Adjon meg számot!")
        except (EOFError, KeyboardInterrupt):
            print()
            return
        else:
            print("Lefut, ha a try blokkban nem lett eldobva 1 kivetel sem")
        finally:
            print("Mindig lefut")


if __name__ == "__main__":
    main()
