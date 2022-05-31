#!/usr/bin/python3
def uppercase(str):
    for s in range(len(str)):
        uni_code = ord(str[s])
        if uni_code >= 97 and uni_code <= 122:
            uni_code = uni_code - 32
        print("{}".format(chr(uni_code)), end='')
    print()
