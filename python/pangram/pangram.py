def is_pangram(sentence):
    sentence = [ord(i) for i in sentence.lower() if i.isalpha()]
    for i in range(97,123):
        try:
            sentence.remove(i)
        except:
            return False
    else:
        return True
