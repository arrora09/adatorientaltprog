def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip().split()
            s = stripped[0][1:-1]

            for i in range(3, len(s)):
                if (
                    s[i] != s[i - 1]
                    and s[i] != s[i - 2]
                    and s[i] != s[i - 3]
                    and s[i - 1] != s[i - 2]
                    and s[i - 1] != s[i - 3]
                    and s[i - 2] != s[i - 3]
                ):
                    print(s[i - 3] + s[i - 2] + s[i - 1] + s[i])
                    break


if __name__ == "__main__":
    main()
