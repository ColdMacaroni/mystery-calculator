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
    if size < 0:
        raise ValueError('Cannot be negative')
    
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


def make_size(string, size, char=" "):
    """
    Adds chars to the start of a string to make it the specific length
    """
    length = len(string)

    # Add starting chars
    new_string = char * (size - length)

    # Rest of string
    new_string += string

    return new_string

    
def recursive_func(ls, func, argument=None):
    """
    Applies a function recursively to the list provided, has support for
    multidimensional lists
    has support for a single argument
    """
    # In case the given argument isnt a list
    if type(ls) != list:
        if argument == None:
                    return func(ls)
        else:
                    return func(ls, argument)

    new_list = []
    for item in ls:
        # If the item is also a list run this same function on it
        if type(item) == list:
            nested_list = []
            
            for i in item:
                if argument == None:
                    nested_list.append(recursive_func(i, func))
                else:
                    nested_list.append(recursive_func(i, func, argument))
            
            new_list.append(nested_list)

        else:
            if argument == None:
                    new_list.append(func(item))
            else:
                    new_list.append(func(item, argument))

    return new_list


def make_table(ls, columns):
    """
    Displays a table with given columns
    No support for 2d lists
    """
    sectioned = make_sections(ls, columns, spaces = " ")

    rows = []
    # Turn into strings
    for row in sectioned:
        rows.append(' '.join(row))

    table = "\n".join(rows)
    
    return table
    

def main():
    print("Mystery calculator :0")
    
    for numbers in mystery_numbers():
        # Blank Line
        print()
        
        # Make them all into strings
        string_numbers = recursive_func(numbers, str)

        # Make them all same size
        same_size = recursive_func(string_numbers, make_size, 2)

        # Displlay table
        print(make_table(same_size, 8))
        
    
    
if __name__ == "__main__":
    main()
