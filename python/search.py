from json import loads
from string import punctuation

from tqdm import tqdm

from filemanip import normalize_str, compare_normalized
from get_data import get_raw_verses, get_data
from Reference import Reference

def find_valid_refs(Rs, flag):
    valid_refs = []
    
    norm_flag = normalize_str(flag)
    for R in Rs:
        verse = R.text
        for word in verse:
            norm_word = normalize_str(word)
            if compare_normalized(norm_flag, norm_word):
                valid_refs.append(R)

    return valid_refs

def get_all_words(Rs):
    raw_all_words = []
    
    for R in Rs:
        for word in R.text:
            raw_all_words.append(word)
        
    return raw_all_words.sort()

def find_unique_words(raw_all_words):
    unique_words = []
    for word in tqdm(raw_all_words):
        if word in unique_words: continue
        else: unique_words.append(word)
    
    return unique_words


if __name__ == '__main__':
    fname = '../json/book-of-mormon.json'
    xfname = '../json/book-of-mormon-flat.json'
    raw = get_data(xfname)
    data = get_raw_verses(raw)
    references = make_references(data)
    valid_refs = find_valid_refs(references, 'hell')
    for ref in v_refs: print(ref.reference, ref.text)
