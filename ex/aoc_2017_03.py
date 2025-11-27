def find_manhattan_distance(target):
    if target == 1:
        return 0

    ring = 0
    while (2 * ring + 1) ** 2 < target:
        ring += 1

    side_length = 2 * ring + 1

    max_value = side_length**2

    side_size = side_length - 1

    position_from_end = max_value - target

    position_on_side = position_from_end % side_size

    offset_from_midpoint = abs(position_on_side - (side_size // 2))

    return ring + offset_from_midpoint


def main():
    puzzle_input = 277678
    result = find_manhattan_distance(puzzle_input)
    print(result)


if __name__ == "__main__":
    main()
