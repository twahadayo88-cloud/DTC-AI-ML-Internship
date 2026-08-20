import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

#nltk tokenizer download karny ky lia
nltk.download('punkt')
nltk.download('punkt_tab')

data = pd.read_csv("Week 07/Day 1/customer.csv")

print(data.head())
print("Dataset Shape:", data.shape)
print("Column Name:", data.columns)
print("Missing Values:", data.isnull().sum())

#Word Tokenize
sample_text = data["ReviewText"].iloc[0]
print("Sample Text:", sample_text)

#Sentence Tokenize
sentences = sent_tokenize(sample_text)
print("Sentence Tokens:", sentences)

#Word Tokenize
words = word_tokenize(sample_text)
print("Work Tokens:")
print(words)
