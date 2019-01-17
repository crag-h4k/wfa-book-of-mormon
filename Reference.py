class Reference:
    def __init__(self, reference, text = []):
        self.reference = reference
        self.text = text.split(' ')

class Word_Count:

    def __init__(self, word, reference, count):

        return

def make_references(data):
    references = []

    for i in data:
        ref = i.get('reference')
        text = i.get('text')
        clean = clean_text(text)
        
        R = Reference(ref, clean)
    
        references.append(R)
    
    return references

if __name__ == '__main__':
#raw = get_data('book-of-mormon.json')
#print(raw[:5])
    raw = get_data(fname)
    data = get_raw_verses(raw)
    xdata = data[:10]
    references = make_references(xdata)
    print(references)
    for ref in references:
        print(ref.text)
