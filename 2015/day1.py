def main():

    with open("inputs/day1.txt") as f:
        data = f.read()

    converted_data = convert_parentheses(data)
    part_1 = sum(converted_data)
    print(f"Part 1 solution: {part_1}")

    part_2 = find_first_basement_pos(converted_data)
    print(f"Part 2 solution: {part_2}")


def find_first_basement_pos(nums: list[int]) -> int:
    """Go through the converted numbers and
    when current_level will be -1, return the position
    we are on (+1 because solution shouldn't be zero indexed)
    """

    current_level = 0

    for i, num in enumerate(nums):
        current_level += num
        if current_level == -1:
            return i + 1


def convert_parentheses(parents: str) -> list[int]:
    """Convert the parentheses to a list of integers
    where ( equals 1 and ) equals -1"""

    return [1 if x == "(" else -1 for x in parents]


if __name__ == "__main__":
    main()
