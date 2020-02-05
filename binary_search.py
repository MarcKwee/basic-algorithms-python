def binary_search(needle, haystack):
    index = None

    low = 0
    high = len(haystack) - 1

    while (low <= high):
        mid = (low + high) // 2
        quess = haystack[mid]
        # Found it!
        if (quess == needle):
            index = mid
            break

        # Update
        if (quess < needle):
            low = mid + 1
        else:
            high = mid - 1

    return index


haystack = [0, 2, 4, 5, 6, 7, 10, 123, 423, 565, 600, 711, 712, 713, 6098]
needle = 10
result = binary_search(needle, haystack)
print(result)
