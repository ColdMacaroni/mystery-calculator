##
# mystery_calculator.py
# Dago
# 2021-04-15


def generate_numbers(start, numbers, group=1, skip_amount=0):
    """
    Generates numbers according to the parameters.
    Starting number tells what the starting number of the sequence
    will be
    Numbers determines how many numbers it will have
    Group is how many consecutive nums before there is a skip
    skip amount is the numbers to skip between each group
    """

    nums = []
    base = start

    # In each iteration "group" numbers will be added to the list,
    # So to get "numbers" numbers we need to divide them.
    # The base at first is the start number, the actual num starts
    # counting up from it.
    # After each group is added, the skip amount is added to the base
    # to create the difference between each group.
    for actual_num in range(numbers // group):
        for group_num in range(group):
            nums.append(base + actual_num + group_num)
        base += skip_amount

    return nums


def mystery_numbers():
    """
    Returns the numbers necessary to get the mystery calculator to work
    """
    # The patterns necessary to generate the numbers
    # Format:
    #   - start
    #   - numbers needed
    #   - step
    #   - skip after this many numbers (default = 1)
    #   - amount to skip (default = 0))
    patterns = [[1, 32, 1, 1],
                [1, 32, 8, 9],
                [2, 32, 2, 3],
                [16, 32, 16, 9],
                [4, 32, 4, 5],
                [32, 32, 1, 0]]

    numbers = []
    for pattern in patterns:
        numbers.append(generate_numbers(pattern[0],
                                        pattern[1],
                                        pattern[2],
                                        pattern[3]))
    return numbers

if __name__ == "__main__":
    print(generate_numbers(int(input("Start: ")),
                           int(input("End: ")),
                           int(input("Step: "))))
