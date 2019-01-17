from json import loads
from string import punctuation

from filemanip import normalize_str, compare_normalized

from Reference import Reference

def find_word(R, word):
    text = R.text
    if word in text:
        print(word)
        print(R.reference)
    return

if __name__ == '__main__':
    return
