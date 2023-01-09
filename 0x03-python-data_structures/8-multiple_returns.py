#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        t = (0, None)
        return t
    leng = 0
    for i in sentence:
        leng += len(i)
    t = (leng, sentence[0][0])
    return t
    
