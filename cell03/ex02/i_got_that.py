#!/usr/bin/env python

print("What you gotta say? :", end=" ")
text = input()
while True:
    if text == "STOP":
        break
    print("I got that! Anything else? :", end=" ")
    text = input()