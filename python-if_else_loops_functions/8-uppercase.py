#!/usr/bin/python3
def uppercase(str):
    for char in str:
        offset = 32 if 'a' <= char <= 'z' else 0
        print("{:c}".format(ord(char) - offset), end="")
    print()
