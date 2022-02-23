TEST_INPUT = "2x3x4"


def main():

    with open("inputs/day2.txt") as f:
        data = f.read().splitlines()

    part_1 = sum(calculate_wrapping_for_present(row) for row in data)
    print(f"Part 1 solution: {part_1}")

    part_2 = sum(calculate_ribbon_length(row) for row in data)
    print(f"Part 2 solution: {part_2}")


def calculate_ribbon_length(measures: str) -> int:

    """We need to find the 2 smallest side, calculate the volume from them
    and then also add the bow length"""

    l, w, h = (int(m) for m in measures.split("x"))
    sorted_distances = list(sorted([l, w, h]))

    volume = sorted_distances[0] * 2 + sorted_distances[1] * 2
    bow_length = l * w * h

    return volume + bow_length


def calculate_wrapping_for_present(measures: str) -> int:

    """We need to calculate the areas, find the smallest one
    then add together all (x2 for areas because there are two of each"""

    l, w, h = (int(m) for m in measures.split("x"))
    areas = (l * w, w * h, h * l)
    smallest_area = min(areas)

    return sum(areas) * 2 + smallest_area


if __name__ == "__main__":
    main()
