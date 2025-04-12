#!/usr/bin/env python

print("Give me a number:", end = " ")
num = float(input())
if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")