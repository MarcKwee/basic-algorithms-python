def max(list):
    if (len(list) == 0):
        return None
    if (len(list) == 1):
        return list[0]
    else:
        newMax = max(list[1:])
        return list[0] if list[0] > newMax else newMax


print(max([1, 5, 6, 1, 2, 3, 10, 12, 23, 40, 2, 54, 3, 67, 10, 7]))
