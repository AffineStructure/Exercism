from collections import Counter

def is_isogram(string):
    string = ''.join([i.lower() for i in string if i.isalpha()])
    return all(i == 1 for i in Counter(string).values())