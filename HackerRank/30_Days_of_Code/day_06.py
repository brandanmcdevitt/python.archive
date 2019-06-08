# day06: Let's Review

# Enter your code here. Read input from STDIN. Print output to STDOUT
words = []
cases = int(input())
for i in range(0, cases):
    words.append(input())

def evens_odds(*args):
    for arg in args:
        print(arg[::2] + " " + arg[1::2])

evens_odds(*words)