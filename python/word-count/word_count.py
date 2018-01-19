from collections import Counter
import re

def word_count(phrase):
    txt = re.findall(r"\w+\'*\w?", phrase.lower().replace("_"," "))
    return dict(Counter(txt))

