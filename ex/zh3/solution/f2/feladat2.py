def main():
    with open("mass_effect.txt", "r", encoding="utf-8") as f:
        lines = []
        for line in f:
            stripped = line.strip()
            parts = stripped.split(",")
            lines.append((int(parts[1]), parts[2]))
        sorted_lines = sorted(lines, key=lambda t: t[0])

        print("".join([s[1] for s in sorted_lines]).replace("_", " "))


if __name__ == "__main__":
    main()
