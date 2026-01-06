#!/usr/bin/env python3


def isPalindrome(word):
    return word == word[::-1]


def main():
    with open("words_palindrome.txt", encoding="utf-8") as f:
        palindromes = []
        for line in f:
            word = line.strip()
            if len(word) >= 4 and isPalindrome(word.lower()):
                palindromes.append(word)

        print(f"Palindrómok száma: {len(palindromes)}")

        sorted_by_length = sorted(palindromes, key=len, reverse=True)
        print("Leghosszabbak:")
        for i in range(min(3, len(sorted_by_length))):
            word = sorted_by_length[i]
            print(f"- {word} (hossz: {len(word)})")


if __name__ == "__main__":
    main()
