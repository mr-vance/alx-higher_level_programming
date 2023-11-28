#!/usr/bin/python3
def uppercase(s):
    result = ''
    for char in s:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:
            upper_char = chr(ascii_val - 32)
            result += "{}".format(upper_char)
        else:
            result += "{}".format(char)
    print("{}".format(result))
