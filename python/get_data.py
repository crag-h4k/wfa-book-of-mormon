from pprint import pprint

from simplejson import loads

def get_raw_verses(raw_data):
    for key, value in raw_data.items() :
        if key == 'verses': return(value)
        
def get_data(fname):
    with open(fname, 'r') as f:
        raw = f.read()
    raw_data = loads(raw)
    return raw_data

if __name__ == '__main__':
    fname = '../json/book-of-mormon.json'
    xfname = '../json/book-of-mormon-flat.json'
    xdata = data[:10]
    references = make_references(xdata)
    print(references)
    for ref in references: 
        print(ref.reference, ref.text)
