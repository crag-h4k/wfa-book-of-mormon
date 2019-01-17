from string import punctuation

from filemanip import normalize_str, compare_normalized

def clean_text(text):
    normalized = normalize_str(text)
    trans_tbl = str.maketrans('','', punctuation)
    return normalized.translate(trans_tbl)

if __name__ == '__main__':
    raw = get_data(fname)
    data = get_raw_verses(raw)
    xdata = data[:10]
    references = make_references(xdata)
    print(references)
    for ref in references:
        print(ref.text)
