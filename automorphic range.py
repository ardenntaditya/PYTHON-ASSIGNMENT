for i in range(1, 10001):
    temp = i
    digits = 0

    # count digits
    while temp > 0:
        digits += 1
        temp //= 10

    # check automorphic
    if (i * i) % (10 ** digits) == i:
        print(i, end=" ")
