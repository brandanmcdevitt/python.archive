#task 1
def show_all(txt_file):
    file = open(txt_file, 'r')
    print(file.read() + "\n")
    file.close()

#task 2
def lowest_value(txt_file):

    file = open(txt_file, 'r')
    read = file.readline()
    prices = {}
    lowest = 10000000.00

    for line in file.read().splitlines():
        split = line.split('\t')
        if len(split[2]) > 0:
            split[2] = split[2].replace('"', '')
            split[2] = split[2].replace(',', '')
            prices[split[1]] = float(split[2])

    for key, value in prices.items():

        if value < float(lowest):
            lowest = value
            ans = key + " - $" + str(value)

    print("Lowest last price: {}\n".format(ans))

    file.close()

#task 3
def min_max_avg(txt_file):
    min = 0
    max = 0
    company_min = {}
    company_max = {}
    avg = 0
    avg_count = []
    file = open(txt_file, 'r')
    read = file.readline()

    for line in file.read().splitlines():
        split = line.split('\t')
        avg_count.append(split[3])
        if len(split[2]) > 0:
            avg += float(split[3])

        if len(split[2]) > 0 and float(split[3]) < 0:
            company_min[split[1]] = float(split[3])
        elif len(split[2]) > 0 and float(split[3]) > 0:
            company_max[split[1]] = float(split[3])

    for key, value in company_min.items():
        if value < float(min):
            min = value

    for key, value in company_max.items():
        if value > float(max):
            max = value

    print("Minimum change: {}".format(min))
    print("Maximum change: {}".format(max))
    print("Average change: {}\n".format(avg / len(avg_count)))

#task 4
def symbol(txt_file):
    file = open(txt_file, 'r')
    read = file.readline()
    symbols = []

    for line in file.read().splitlines():
        split = line.split('\t')
        if len(split[2]) > 0:
            symbols.append(split[0])

    print(symbols[3:5])
    print("")

#task 5
def symbol_volume(txt_file):
    file = open(txt_file, 'r')
    read = file.readline()
    symbol_and_volume = {}

    for line in file.read().splitlines():
        split = line.split('\t')
        if len(split[2]) > 0:
            symbol_and_volume[split[0]] = split[5]

    print(symbol_and_volume)


show_all('FTSE_100.txt')

lowest_value('FTSE_100.txt')

min_max_avg('FTSE_100.txt')

symbol('FTSE_100.txt')

symbol_volume('FTSE_100.txt')