# day 08: Dictionaries and Maps

n = int(input())
name_and_number = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_and_number}

while True:
    try:
        name = input()
        if name in phone_book:
            print(f"{name}={phone_book[name]}")
        else:
            print('Not found')
    except:
        break