#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = str[0:n] + str[n + 1:len(str)]
    return str2
