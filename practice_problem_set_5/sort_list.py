def find_next(names, start_index):
    """
    Finds the index of the smallest string alphabetically in the unsorted portion of the list.
    :param names: List of names
    :param start_index: Index where the unsorted portion begins
    :return: Index of the smallest string in the unsorted portion
    """
    min_index = start_index
    for i in range(start_index + 1, len(names)):
        if names[i] < names[min_index]:
            min_index = i
    return min_index


def put_in_order(names, start_index, min_index):
    """
    Swaps the element at start_index with the element at min_index.
    :param names: List of names
    :param start_index: Index of the first element in the unsorted portion
    :param min_index: Index of the smallest element in the unsorted portion
    """
    names[start_index], names[min_index] = names[min_index], names[start_index]


def main():
    """
    Main function to sort a list of names alphabetically.
    """
    names = ["Zita", "Henny", "Benny", "Harold", "Danny", "Penny"]
    print("Unsorted list:")
    print(names)

    for i in range(len(names)):
        min_index = find_next(names, i)
        put_in_order(names, i, min_index)

    print("Sorted list:")
    print(names)


if __name__ == "__main__":
    main()
