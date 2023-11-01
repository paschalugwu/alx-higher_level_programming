#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
print(f"The last digit of {number:d} is {digit:d} and the number is ", end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("zero")
else:
    print("less than 6 and not equal to 0")
