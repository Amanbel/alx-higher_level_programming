#!/usr/bin/python3
def multiple_returns(sentence):
    len = 0
    for i in sentence:
        len += len(i)
    return (len, sentence[0][0])
