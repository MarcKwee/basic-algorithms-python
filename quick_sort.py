def quick_sort(array):
    if (len(array) < 2):
        return array
    pivot = array[0]

    less = []
    for i in array[1:]:
        if (i <= pivot):
            less.append(i)
    more = []
    for i in array[1:]:
        if (i > pivot):
            more.append(i)

    return quick_sort(less) + [pivot] + quick_sort(more)


print(quick_sort([1, 6, 7, 23, 1, 2, 4, 6, 8, 5, 90, 60, 401, 12, 5, 6, 7]))
