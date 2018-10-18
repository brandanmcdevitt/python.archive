def calculation(n):
    sum = 0
    for numerator in range(1, n):
        sum += numerator / (n - numerator)
    print(sum)

calculation(31)