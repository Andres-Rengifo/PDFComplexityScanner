from PyPDF2 import PdfReader
from collections import Counter
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('words')
from nltk.corpus import stopwords, words
import string
import re
import textstat

well_known_words = set(words.words())

#Extract the PDF file

def extract_text_pypdf2(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

pdf_file = "data/ComplexPDF.pdf"
text = extract_text_pypdf2(pdf_file)

#Tokenize the text for the current page and return the tokenized words and sentences.

def tokenize_text(text):
    words = nltk.word_tokenize(text)
    words = [word for word in words if word not in string.punctuation]
    sentences = nltk.sent_tokenize(text)
    return words, sentences

words, sentences = tokenize_text(text)

#A filter to be rid of unnecessary words int he PDF file.

def filter_stopwords(words):
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    filtered_words = [re.sub(r"[^\w]", "", word) for word in filtered_words if re.sub(r"[^\w]", "", word)]
    return filtered_words

filtered_words = filter_stopwords(words)
filtered_text = " ".join(filtered_words)

#Finding the most common words in the PDF. Will be needed at some point maybe later.

def word_frequency_analysis(words):
    frequency = Counter(words)
    return frequency.most_common(50)    

common_words = word_frequency_analysis(filtered_words)

# Getting all the well known words, and 'difficult words' from the text.

def get_well_known_words(filtered_words, well_known_words):
    return [word for word in filtered_words if word.lower() in well_known_words]
def get_non_well_known_words(filtered_words, well_known_words):
    return [word for word in filtered_words if word.lower() not in well_known_words]

well_known = get_well_known_words(filtered_words, well_known_words)
non_well_known = get_non_well_known_words(filtered_words, well_known_words)

print("Filtered Words:", filtered_words)
print(textstat.difficult_words(filtered_text))
print("well known words:", well_known)
print("non well known words:", non_well_known)