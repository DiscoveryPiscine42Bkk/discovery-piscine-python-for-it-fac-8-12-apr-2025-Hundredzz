#!/usr/bin/env python

print("Enter the first number:")
first_num = float(input())
print("Enter the second number:")
second_num = float(input())
result = first_num * second_num
print(f"{first_num} x {second_num} = {result}")
if result == 0:
    print("The result is positive and negative.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive.")