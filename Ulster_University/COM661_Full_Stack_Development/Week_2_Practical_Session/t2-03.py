def print_pattern(n):

    if n < 1:
        exit(0)
    else:
        print(n* "* ")
        print_pattern(n - 1)

print_pattern(5)