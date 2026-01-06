#!/usr/bin/env python3


def main():
    students = []

    with open("grades.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()[1:]  # Skip header

        for line in lines:
            parts = line.strip().split(";")
            name = parts[0]
            grades = [int(parts[1]), int(parts[2]), int(parts[3])]
            avg = sum(grades) / len(grades)
            students.append((name, avg))

    students.sort(key=lambda x: x[1])

    worst = students[0]
    best = students[-1]

    class_avg = sum(s[1] for s in students) / len(students)

    print(f"Legjobb átlag: {best[0]} ({best[1]:.2f})")
    print(f"Legrosszabb átlag: {worst[0]} ({worst[1]:.2f})")
    print(f"Osztályátlag: {class_avg:.2f}")

    with open("results.txt", "w", encoding="utf-8") as outF:
        for name, avg in students:
            outF.write(f"{name}: átlag ({avg:.2f})\n")

    print("-- results.txt was created")


if __name__ == "__main__":
    main()
