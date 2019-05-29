input = raw_input("Enter a series of positive numbers: ")

numbers = []
sum = 0

n_split = input.split()

for n in n_split:
    numbers.append(n)

for i in numbers:
    if int(i) > 0:
        sum += int(i)
    elif int(i) < 0:
        print(sum)
        exit(0)