#!/usr/bin/env python3


def isValidEmail(email):
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    if not parts[0] or not parts[1]:
        return False
    domain = parts[1]
    if "." not in domain:
        return False
    return True


def main():
    fileName = "users.csv"

    print(f"-- reading {fileName}")

    valid = []
    invalid_count = 0

    with open(fileName, "r", encoding="utf-8") as f:
        lines = f.readlines()[1:]

        for line in lines:
            stripped = line.strip()
            parts = stripped.split(";")
            name = parts[0]
            email = parts[2]

            if isValidEmail(email):
                valid.append((name, email))
            else:
                invalid_count += 1

    print(f"Érvényes emailek: {len(valid)}")
    print(f"Érvénytelen emailek: {invalid_count}")

    with open("valid_emails.txt", "w", encoding="utf-8") as outF:
        for name, email in valid:
            outF.write(f"{name} - {email}\n")

    print("-- valid_emails.txt was created")
    print("-- done")


if __name__ == "__main__":
    main()
