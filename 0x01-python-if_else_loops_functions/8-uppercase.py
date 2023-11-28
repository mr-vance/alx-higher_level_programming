#!/usr/bin/python3
def uppercase(s):
    for char in s:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:
            upper_char = chr(ascii_val - 32)
            print("{}".format(upper_char), end="")
        else:
            print("{}".format(char), end="")
    print()
