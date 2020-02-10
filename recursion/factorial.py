def fact(i):
    if i == 1:
        return i
    else:
        return i * fact(i-1)


print(fact(3))
