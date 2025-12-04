import re


def regex_ex():
    with open("pelda.txt", encoding="utf-8") as f:
        print(f.read())

        f.seek(0)
        m = re.search(r"s.r", f.read())
        print(m.group())

        f.seek(0)
        m = re.search(r"\d", f.read())
        print(m.group())

        f.seek(0)
        m = re.search(r"\d{2}", f.read())
        print(m.group())

        f.seek(0)

        m = re.search(r" \d{4}", f.read())
        print(m.group())


if __name__ == "__main__":
    regex_ex()
