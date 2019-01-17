from json import loads
from Verse import Verse

def find_word():
    return
def get_data(fname):
    with open(fname, 'r') as f:
        raw = f.read()
    return loads(raw)

#if __name__ == '__main__':
#raw = get_data('book-of-mormon.json')
#print(raw[:5])
