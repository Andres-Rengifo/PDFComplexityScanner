from PyPDF2 import PdfReader
from collections import Counter
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import re

def extract_text_pypdf2(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

pdf_file = "data/ComplexPDF.pdf"
text = extract_text_pypdf2(pdf_file)

def tokenize_text(text):
    words = nltk.word_tokenize(text)
    words = [word for word in words if word not in string.punctuation]
    sentences = nltk.sent_tokenize(text)
    return words, sentences

words, sentences = tokenize_text(text)

def filter_stopwords(words):
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    filtered_words = [re.sub(r"[^\w]", "", word) for word in filtered_words if re.sub(r"[^\w]", "", word)]
    return filtered_words

filtered_words = filter_stopwords(words)

def word_frequency_analysis(words):
    frequency = Counter(words)
    return frequency.most_common(50)    

common_words = word_frequency_analysis(filtered_words)

print("Filtered Words:", filtered_words)
print("Common Words:", common_words)

