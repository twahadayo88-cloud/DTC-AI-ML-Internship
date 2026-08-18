import nltk
import pandas as pd
from nltk.probability import FreqDist

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