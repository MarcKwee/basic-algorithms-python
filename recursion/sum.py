def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


print(sum([1, 2, 4, 5, 6, 4, 2, 1]))
