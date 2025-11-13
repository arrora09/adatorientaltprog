#!/usr/bin/env python3
import sys


def main():
    if len(sys.argv) != 2:
        print("Hibás paraméterezés! Csak egy számjegyet kell megadni!")
        return
    arg_num_str = sys.argv[1]

    with open("data.csv", "r") as f:
        for l in f:
            line = l.strip()
            parts = line.split(";")
            name = parts[5]
            ssn = parts[8]
            if ssn.startswith(arg_num_str):
                print(f"{name};{ssn}")


if __name__ == "__main__":
    main()
