
if __name__ == "__main__":
    print("példából: ")
    lang_info = [
        ("Fortran", 1954, 0.435),
        ("Cobol", 1959, 0.391),
        ("C", 1972, 16.076),
        ("C++", 1980, 9.014),
        ("Python", 1991, 6.482),
        ("Java", 1995, 17.99),
        ("C#", 2001, 6.687),
    ]
    print("legyen egy listánk, amik tuple elemeket tartalmaz")
    print()
    print(f"Minden formázás nélkül így néz ki: {lang_info}")
    print()
    print("Soronként kirakva, elemekre bontva: ")
    for x in lang_info:
        print(x[0] + " " + str(x[1]) + " " + str(x[2]))

    print()
    print("Meg lehet adni minimum szélességet is az egyes elemeknek a formázás során.")
    print("Szintaktika: {elemnév vagy sorszám:minimum szélesség karakterszámban}")
    print("Ekkor így néz ki:")
    for x in lang_info:
        print("{lang:12} {year:8} {rating:8}".format(lang=x[0], year=x[1], rating=x[2]))