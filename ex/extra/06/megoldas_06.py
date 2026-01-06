#!/usr/bin/env python3


def cleanPhone(phone):
    return "".join(c for c in phone if c.isdigit())


def formatPhone(phone):
    if len(phone) == 11:
        return f"+{phone[:2]}-{phone[2:4]}-{phone[4:7]}-{phone[7:]}"
    return None


def main():
    valid = []
    invalid_count = 0
    total = 0

    with open("contacts.txt", "r", encoding="utf-8") as f:
        for line in f:
            total += 1
            stripped = line.strip()
            if ":" in stripped:
                parts = stripped.split(":", 1)
                name = parts[0].strip()
                phone = parts[1].strip()

                cleaned = cleanPhone(phone)
                formatted = formatPhone(cleaned)

                if formatted:
                    valid.append((name, formatted))
                else:
                    invalid_count += 1

    print(f"Összesen: {total} névjegy")
    print(f"Érvényes: {len(valid)} névjegy")
    print(f"Érvénytelen: {invalid_count} névjegy")

    with open("formatted_contacts.txt", "w", encoding="utf-8") as outF:
        for name, phone in valid:
            outF.write(f"{name}: {phone}\n")

    print("-- formatted_contacts.txt was created")


if __name__ == "__main__":
    main()
