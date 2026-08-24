import pandas as pd 
import nltk

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk.probability import FreqDist

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("omw-1.4")

df = pd.read_csv("Week 07/Day 3/dataset.csv")

print(df.head())
print("Dataset Shape:", df.shape)
print("Columns:", df.columns)
print("Missing Values:", df.isnull().sum())
print("Duplicate Reviews:", df["review"].duplicated().sum())

stemmer = PorterStemmer() 

sample_text = "playing played studies studying"
tokens = word_tokenize(sample_text)
stemmed_words = [stemmer.stem(word) for word in tokens]
print("Orignal words:", tokens)
print("Stemmed Words:", stemmed_words)

def stem_text(text):
    tokens = word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in tokens]
    return " ".join(stemmed_words)

df["stemmed_text"] = df["clean_text"].apply(stem_text)

print("Orignal cleaned text and stemmed text:", df[["clean_text", "stemmed_text"]].head(10))

lemmatizer = WordNetLemmatizer()

"""sample_text = "playing played studies studying"
tokens = word_tokenize(sample_text)
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]

print("original words:", tokens)
print("lemmatized_words:", lemmatized_words)"""


def lemmatize_text(text):
    tokens = word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(lemmatized_words)

df["lemmatized_text"] = df["clean_text"].apply(lemmatize_text)
print("Orignal Cleaned Text and Lemmatized Text:")
print(df[["clean_text", "lemmatized_text"]].head(10))


#compare all the 3 text columns for better understanding
pd.set_option("display.max_columns",None)
pd.set_option("display.width",None)

print("comparison of cleaned, stemmed and lemmatized text:")
print(
    df[["clean_text","stemmed_text","lemmatized_text"]
    ].head(10))

all_words = []

for text in df["lemmatized_text"]:
    tokens = word_tokenize(text)
    all_words.extend(tokens)

print("First 20 Unigrams:")
print(all_words[:20])
print("Total Numbers of Unigrams:")
print(len(all_words))


unigram_freq = FreqDist(all_words)
top_20_unigrams = unigram_freq.most_common(20)
print("Top 20 most Frequent Unigrams:")
for word, freuency in top_20_unigrams:
    print(word, ":", freuency)


all_bigrams = []
for text in df["lemmatized_text"]:
    tokens = word_tokenize(text)
    bigrams_list = list(ngrams(tokens,2))
    all_bigrams.extend(bigrams_list)

print("\nFirst 20 Bigrams:")
print(all_bigrams[:20])

print("\nTotal Number of Bigrams:")
print(len(all_bigrams))

from nltk.util import trigrams

all_trigrams = []

for text in df["lemmatized_text"]:
    words = nltk.word_tokenize(text)
    text_trigrams = list(trigrams(words))
    all_trigrams.extend(text_trigrams)

print("First 20 Trigrams:")
print(all_trigrams[:20])

print("Total Number of Trigrams:")
print(len(all_trigrams))

bigram_freq = FreqDist(all_bigrams)

print("\nTop 20 Most Frequent Bigrams:")

for bigram, frequency in bigram_freq.most_common(20):
    print(bigram, ":", frequency)


#trigram frequency
trigram_freq = FreqDist(all_trigrams)

print("\nTop 20 Most Frequent Trigrams:")

for trigram, frequency in trigram_freq.most_common(20):
    print(trigram, ":", frequency)

#vocabulary size
original_vocabulary = set()

for text in df["review"]:
    words = nltk.word_tokenize(text.lower())
    original_vocabulary.update(words)

cleaned_vocabulary = set()

for text in df["clean_text"]:
    words = nltk.word_tokenize(text)
    cleaned_vocabulary.update(words)

stemmed_vocabulary = set()

for text in df["stemmed_text"]:
    words = nltk.word_tokenize(text)
    stemmed_vocabulary.update(words)

lemmatized_vocabulary = set()

for text in df["lemmatized_text"]:
    words = nltk.word_tokenize(text)
    lemmatized_vocabulary.update(words)

print("\nVocabulary Size Comparison:")

print("Original Vocabulary:", len(original_vocabulary))
print("Cleaned Vocabulary:", len(cleaned_vocabulary))
print("Stemmed Vocabulary:", len(stemmed_vocabulary))
print("Lemmatized Vocabulary:", len(lemmatized_vocabulary))

#final comparison karty hn ab !
print("NLP Preprocessing Summary:")
print("Orignal Vocabulary:", len(original_vocabulary))
print("Cleaned Vocabulary:", len(cleaned_vocabulary))
print("Stemmed Vocabulary:", len(stemmed_vocabulary))
print("Lemmatized Vocabulary:", len(lemmatized_vocabulary))
print("Total Bigrams:", len(all_bigrams))
print("Total Trigrams:", len(all_trigrams))