#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) < 1:
        return (0, None)
    lenght = len(sentence)
    first = sentence[0]
    return (lenght, first)
