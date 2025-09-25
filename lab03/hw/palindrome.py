
def isPalindrome(s):
    return s == s[::-1]


def main():
    print(isPalindrome("görög"))
    print(isPalindrome("kocsi"))
    print(isPalindrome("házifeladat"))


if __name__ == "__main__":
    main()

