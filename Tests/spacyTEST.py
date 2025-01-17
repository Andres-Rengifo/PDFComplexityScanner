
from collections import Counter
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
def tokenize_text(text):
    words = nltk.word_tokenize(text)
    sentences = nltk.sent_tokenize(text)
    return words, sentences

sample_text = "This is a a test. We are analyzing text difficulty"
words, sentences = tokenize_text(sample_text)

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