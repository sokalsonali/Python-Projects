import json
from difflib import get_close_matches

data = json.load(open('data.json'))

word = input('Enter a word: ')

# Input: My name's sonali sokal.
# Output My Name's Sonali Sokal.
import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
     lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(), s)


def translate(w):
    w = w.lower()
    if w in data.keys():
        return data[w]
    elif w.title() in data.keys():
        return data[w.title()]
    elif w.upper() in data.keys():
        return data[w.upper()]
    elif get_close_matches(w, data.keys(), cutoff=0.8):
        choice = input("Did you mean %s enter Y for yes N for N: " % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        if choice == 'Y':
            return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
        else:
            return 'Word Not found'
    else:
        return 'Word Not found'


result = translate(word)
if type(result) == list:
    for i in result:
        print(i)
else:
    print(result)


