rateOne = 1.10
rateTwo = 2.20
rateThree = 3.70
rateFour = 3.80

weight = int(input('Enter weight of parcel: '))
if (weight <= 2):
    print('Shipping: $', round(weight * rateOne, 2))
elif (weight > 2 and weight < 6):
    print('Shipping: $', round(weight * rateTwo, 2))
elif (weight > 6 and weight < 10):
    print('Shipping: $', round(weight * rateThree, 2))
else:
    print('Shipping: $', round(weight * rateFour, 2))
