#!/usr/bin/env python

print("Please tell me your age:", end = " ")
age = int(input())
print(f"You are currently {age} years old.")
for i in range(10, 31, 10):
    print(f"In {i} years, you'll be {age + i} years old.")
