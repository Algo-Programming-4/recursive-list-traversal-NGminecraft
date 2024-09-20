def list_traverse(lst, depth=1, totalItems = 0):
    """ Recursively sum all the items in a list as well as it's nested lists
    Args:
        lst (list): A list to sum the items of

    Returns:
        tuple: sum of the list
    """
    sum = 0
    totalItems = 0
    calls = 0
    deepest= 0
    for i in lst:
        if type(i) is int:
            totalItems += 1
            sum += i
        elif type(i) is list:
            recieved = list_traverse(i, depth+1, totalItems)
            sum += recieved[0]
            totalItems += recieved[2]+1
            calls += recieved[1] + 1
            print(recieved, i, deepest)
        else:
            print(f"Expected int, got {type(i)}: {i}")
    return (sum, calls, totalItems, deepest)


lst = [1, [2, 3], [[4], [5, [6, 7]]], 8]
print(list_traverse(lst))