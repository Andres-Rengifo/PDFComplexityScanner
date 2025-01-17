from PyPDF2 import PdfReader
from collections import Counter
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
import string

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
    words = [word for word in words if word.isalnum()]
    sentences = nltk.sent_tokenize(text)
    return words, sentences

words, sentences = tokenize_text(text)

def word_frequency_analysis(words):
    frequency = Counter(words)
    return frequency.most_common(10)

common_words = word_frequency_analysis(words)

def filter_stopwords(words):
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return filtered_words

filtered_words = filter_stopwords(words)
print("Filtered Words:", filtered_words)