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
    numbers and group must > 0
    """

    nums = []
    base = start

    # Handling in case the numbers arent perfectibly divisible
    iterations = numbers // group
    leftover = numbers % group

    # In each iteration "group" numbers will be added to the list,
    # So to get "numbers" numbers we need to divide them.
    # The base at first is the start number, the actual num starts
    # counting up from it.
    # After each group is added, the skip amount is added to the base
    # to create the difference between each group.
    for actual_num in range(iterations):
        for group_num in range(group):
            nums.append(base + actual_num + group_num)
        base += skip_amount

    # Check if it has been assigned
    # This is a safety measure because in rare cases (e.g. start = 0,
    # numbers = 1) the previous loop will be skipped, leaving
    # actual_num unnassigned
    if 'actual_num' not in locals():
        actual_num = start

    # This is basically the same loop that is nested in the previous
    # one except with leftover < group
    for leftover_num in range(leftover):
        nums.append(base + actual_num + leftover)

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

def make_sections(ls, size, spaces=None):
    """
    splits list with sections of determined size
    fills in with spaces if keyword is given
    """
    new_list = []

    # Remove from list
    while len(ls) >= size:
        new_list.append(ls[:size])
        del ls[:size]

    # Check if there are any leftovers
    if len(ls):
        if spaces != None:
            # Add amount of spaces needed to fulfill size
            for i in range(size - len(ls)):
                ls.append(spaces)
        # Add leftovers
        new_list.append(ls)

    return new_list

# TODO: Add function to make all items inside list the same length
#       "1" -> " 1"

# TODO: Add function to apply functions recursively inside 2d lists
#       "if type(l) == list:
#           inner_l = []
#            for i in list:
#                inner_l.append(this_function(i))
#           new_list.append(inner_l)

# Add function

if __name__ == "__main__":
    print(generate_numbers(int(input("Start: ")),
                           int(input("End: ")),
                           int(input("Step: "))))

