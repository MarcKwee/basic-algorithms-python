def countdown(i):
    if (i == 0):
        return i
    print(i)
    i = i-1
    countdown(i)


countdown(87)
