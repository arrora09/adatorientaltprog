#!/usr/bin/env python3


def main():
    counters = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    errors = []

    with open("serverlog", "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if "]" in stripped:
                parts = stripped.split("]", 1)
                rest = parts[1].strip()

                if ":" in rest:
                    level_msg = rest.split(":", 1)
                    level = level_msg[0].strip()
                    message = level_msg[1].strip()

                    if level in counters:
                        counters[level] += 1

                    if level == "ERROR":
                        errors.append(message)

    print(f"INFO: {counters['INFO']} db")
    print(f"WARNING: {counters['WARNING']} db")
    print(f"ERROR: {counters['ERROR']} db")

    with open("errors.txt", "w", encoding="utf-8") as outF:
        for error in errors:
            outF.write(error + "\n")

    print("-- errors.txt was created")


if __name__ == "__main__":
    main()
