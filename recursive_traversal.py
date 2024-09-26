def list_traverse(lst, depth=-1, totalItems = 0):
    """ Recursively sum all the items in a list as well as it's nested lists
    Args:
        lst (list): A list to sum the items of

    Returns:
        tuple: sum of the list, number of calls, number of items, deepest item
    """
    sum = 0
    totalItems = len(lst)
    calls = 0
    deepest= depth+1
    for i in lst:
        if type(i) is int:
            sum += i
        elif type(i) is list:
            received = list_traverse(i, depth+1, totalItems)
            sum += received[0]
            totalItems += received[2]
            calls += received[1] + 1
            if deepest < received[-1]:
                deepest = received[-1]
        else:
            print(f"Expected int, got {type(i)}: {i}")
    print(deepest)
    return (sum, calls, totalItems, deepest)


lst = [1, [2, 3], [[4], [5, [6, 7, [8, 9, 10, [11, [12]]]]]], 12]
print(list_traverse(lst))