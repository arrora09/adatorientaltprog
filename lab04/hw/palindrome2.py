def isPalindromeIterative(s):
    s = s.lower()
    s = s.replace(" ", "")
    i = 0
    while i < len(s):
        if s[i] != s[len(s) - i - 1]:
            return False
        i += 1

    return True


def isPalindromeRec(s):
    s = s.lower()
    s = s.replace(" ", "")
    if len(s) < 2:
        return True

    if s[0] != s[-1]:
        return False
    else:
        return isPalindromeRec(s[1:-1])


def main():
    print("iterative")

    print("görög")
    print(isPalindromeIterative("görög"))
    print("kocsi")
    print(isPalindromeIterative("kocsi"))
    print("házifeladat")
    print(isPalindromeIterative("házifeladat"))

    print()

    print("recursive")

    print("görög")
    print(isPalindromeRec("görög"))
    print("kocsi")
    print(isPalindromeRec("kocsi"))
    print("házifeladat")
    print(isPalindromeRec("házifeladat"))


if __name__ == "__main__":
    main()
