def findSmallest(arr):
    smallest = arr[0]

    index = 0

    for i in range(len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            index = i

    return index


def sort(arr):
    sortedArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        sortedArr.append(arr[smallest])
        arr.pop(smallest)
    return sortedArr


arr = [20, 30, 4, 1, 34, 5, 6, 7, 8, 10]

sortedArr = sort(arr)
print(sortedArr)
