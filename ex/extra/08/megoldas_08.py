#!/usr/bin/env python3


def caesarEncode(text, shift):
    result = []
    for c in text:
        if "a" <= c <= "z":
            new_char = chr((ord(c) - ord("a") + shift) % 26 + ord("a"))
            result.append(new_char)
        elif "A" <= c <= "Z":
            new_char = chr((ord(c) - ord("A") + shift) % 26 + ord("A"))
            result.append(new_char)
        else:
            result.append(c)
    return "".join(result)


def main():
    with open("message.txt", "r", encoding="utf-8") as f:
        original = f.read()

    shift = 3
    encoded = caesarEncode(original, shift)

    print(f'Eredeti: "{original[:50]}..."')
    print(f'Kódolt: "{encoded[:50]}..."')

    with open("encoded.txt", "w", encoding="utf-8") as outF:
        outF.write(encoded)

    print("-- encoded.txt was created")


if __name__ == "__main__":
    main()
