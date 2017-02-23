import re
def is_palindrome(sentence):
    sentence = re.sub('[^a-z]', '', sentence.lower())
    return sentence == sentence[::-1]
