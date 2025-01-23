from PyPDF2 import PdfReader
from collections import Counter
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import re
from nltk.corpus import cmudict
nltk.download('cmudict')
syllable_dict = cmudict.dict()

words = ['example', 'word', 'thats', 'unique', 'its']

def count_syllables(word):
    word = word.lower()
    if word.lower() not in syllable_dict: 
        print(f"Word '{word}' not found in syllable dictionary.")   # search for lower case version of the word in dictionary 
        return 0
    syllable_info = syllable_dict[word.lower()]
    return [len(list(y for y in x if y[-1].isdigit())) for x in syllable_dict[word.lower()]][0]

def is_complex(word):
    syllable_count = count_syllables(word)
    return syllable_count > 2

for word in words:
    print(f"Is '{word}' complex? {is_complex(word)}")
