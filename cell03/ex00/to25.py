#!/usr/bin/env python

num = int(input())
if num <= 25:
    while num <= 25:
        print(f"Inside the loop, my variable is {num}")
        num += 1
else:
    print("Error")