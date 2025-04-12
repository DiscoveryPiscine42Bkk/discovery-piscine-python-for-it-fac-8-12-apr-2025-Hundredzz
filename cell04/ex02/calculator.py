#!/usr/bin/env python

print("Give me the first number:", end=" ")
first_num = int(input())
print("Give me the second number:", end=" ")
second_num = int(input())
print("Thank you!")
print(f"{first_num} + {second_num} = {first_num + second_num}")
print(f"{first_num} - {second_num} = {first_num - second_num}")
if (first_num / second_num).is_integer():
    print(f"{first_num} / {second_num} = {int(first_num / second_num)}")
else:
    print(f"{first_num} / {second_num} = {first_num / second_num}")
print(f"{first_num} * {second_num} = {first_num * second_num}")
