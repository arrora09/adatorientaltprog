#!/usr/bin/env python3


def main():
    with open("text_data.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

        line_count = len(lines)

        longest = max(lines, key=len)
        longest_stripped = longest.strip()

        all_words = []
        for line in lines:
            words = line.strip().split()
            all_words.extend(words)

        total_length = sum(len(word) for word in all_words)
        avg_length = total_length / len(all_words) if all_words else 0

        long_words = [word for word in all_words if len(word) > 5]

        print(f"Sorok száma: {line_count}")
        print(
            f'Leghosszabb sor ({len(longest_stripped)} karakter): "{longest_stripped}"'
        )
        print(f"Átlagos szóhossz: {avg_length:.2f} karakter")
        print(f"5+ karakteres szavak: {len(long_words)} db")


if __name__ == "__main__":
    main()
