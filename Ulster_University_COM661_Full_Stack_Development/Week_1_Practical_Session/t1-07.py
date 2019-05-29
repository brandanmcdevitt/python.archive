price = 99.00

amount = int(input('Enter amount of packages you would like to purchase: '))
if amount >= 10 and amount < 20:
    print('Discount of 20% applied. Grand total = $', round(amount * price * 0.8,2))
elif amount >= 20 and amount < 50:
    print('Discount of 30% applied. Grand total = $', round(amount * price * 0.7,2))
elif amount >= 50 and amount < 100:
    print('Discount of 40% applied. Grand total = $', round(amount * price * 0.6,2))
elif amount >= 100:
    print('Discount of 50% applied. Grand total = $', round(amount * price - amount * price * 0.5,2))
