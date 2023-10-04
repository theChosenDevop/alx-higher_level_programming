#!/usr/bin/python3

def uppercase(str):
    result = ''
    for char in str:
        if 'a' <= char <= 'z':
            upper_case = chr(ord(char) - 32)
            result += upper_case
        else:
            result += char
    print("{}".format(result))
