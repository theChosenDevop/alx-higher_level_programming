#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    else:
        count = 0
        for i in sentence:
            count += 1
        char = sentence[:1]
        return (count, char)
