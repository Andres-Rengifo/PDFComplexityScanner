from PyPDF2 import PdfReader
from collections import Counter
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import re

words = ['example', 'word', 'thats', 'unique', 'its']

