# using Euclid's algorithm to find the greatest common factor between two numbers

def euclids_algorithm(num1, num2):
    if num1 == num2:
        return num1
    num3 = max(num1, num2) - min(num1, num2)
    if num1 > num2:
        num1 = num3
    elif num1 < num2:
        num2 = num3
    
    return euclids_algorithm(num1, num2)
    

print(euclids_algorithm(50, 35))