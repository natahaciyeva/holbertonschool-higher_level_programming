#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x integers of a list.
    Args:
        my_list (list): The list to print integers from.
        x (int): The number of integers to print.
    Returns:
        int: The number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
