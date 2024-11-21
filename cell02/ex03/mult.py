#!/usr/bin/env python3
number = int(input("Enter the first number :"))
number1 = int(input("Enter the second number :"))

sum = number * number1

print(f"{number} x {number1} = {sum}")

if sum > 0:
    print("The result is positive.")
elif sum < 0:
    print("The result is negative.")
else:
    print("The result is zero.")