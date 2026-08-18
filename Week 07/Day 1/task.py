import nltk
import pandas as pd
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

print("NLTK is ready!")

text = """
Artificial Intelligence is changing the world.
Machine learning helps businesses make better decisions.
Natural Language Processing allows computers to understand human language.
Python is widely used for data science and machine learning.
AI systems can analyze large amounts of text quickly.
"""

print("Original Text:")
print(text)

"""sentences = nltk.sent_tokenize(text)
print("\nTokenized Sentences:")
print(sentences)"""

words = nltk.word_tokenize(text)
print("\nTokenized Words:")
print(words)

print("\nTotal Tokens:", len(words))

frequency = FreqDist(words)
print("\nWord Frequency:")
print(frequency)

print("\nTop 10 Most Common Words:")

for word, count in frequency.most_common(10):
    print(word, ":", count)

stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.lower() not in stop_words]
print("\nAfter stopwords removal:")
print(filtered_words)

clean_words = [
    word for word in filtered_words
    if word not in string.punctuation
]

print("\nWords After Punctuation Removal:")
print(clean_words)

stemmer = PorterStemmer()

stemmed_words = [
    stemmer.stem(word)
    for word in clean_words
]

print("\nStemmed Words:")
print(stemmed_words)

lemmatizer = WordNetLemmatizer()

lemmatized_words = [
    lemmatizer.lemmatize(word)
    for word in clean_words
]

print("\nLemmatized Words:")
print(lemmatized_words)