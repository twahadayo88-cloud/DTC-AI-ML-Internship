import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")



df = pd.read_csv("Week 07/Day 2/dataset.csv")
print(df.head())
print("Dataset Shape:", df.shape)
print("Columns name:", df.columns)
print("Dataset missing values:", df.isnull().sum())
print("Dataset info:", df.info())

duplicates = df["review"].duplicated().sum()
print("Duplicates review:", duplicates)

#duplicate rows dekhny ky lia 

print("Duplicate rows:", df[df["review"].duplicated(keep=False)].sort_values("review"))

df[["review", "sentiment"]].head(5)

df["clean_text"] = df["review"]
print(df.head())


#combining all reviews into ine test
all_text = " ".join(df["review"].astype(str))

#conver data into words
words = all_text.split()

#unique vocabulary
vocabulary = set(words)

print("Total words:", len(words))
print("Vocabulary Size:", len(vocabulary))

#average lenght of text in data
df["word_count_before"] = df["review"].apply(lambda x: len(str(x).split()))
print("Average word count before cleaning:", df["word_count_before"].mean())

#ab hum cleaning ffuntion banaein gy 
def clean_text(text):
    text = str(text)

    #covert karein gy text ko lowercase mai 
    text = text.lower()
    #remove karein gy data mai sy urls ko 
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    #remove karein gy punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    #ab remove karein gy spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text

df["clean_text"] = df["review"].apply(clean_text)

print(df[["review", "clean_text"]].head(10).to_string(index=False))

