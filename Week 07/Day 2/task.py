import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

# 1. LOAD DATASET

df = pd.read_csv("Week 07/Day 2/dataset.csv")

print(df.head())
print("Dataset Shape:", df.shape)
print("Columns name:", df.columns)
print("Dataset missing values:", df.isnull().sum())
print("Dataset info:")
print(df.info())

# 2. FIND DUPLICATES

duplicates = df["review"].duplicated().sum()

print("Duplicates review:", duplicates)

print(
    "Duplicate rows:",
    df[df["review"].duplicated(keep=False)].sort_values("review")
)


# 3. CREATE CLEAN TEXT COLUMN

df["clean_text"] = df["review"]

print(df.head())


# 4. TEXT STATISTICS BEFORE CLEANING

# Combining all reviews into one text
all_text = " ".join(df["review"].astype(str))

# Convert data into words
words = all_text.split()

# Unique vocabulary
vocabulary = set(words)

print("Total words:", len(words))
print("Vocabulary Size:", len(vocabulary))


# Average length of text
df["word_count_before"] = df["review"].apply(
    lambda x: len(str(x).split())
)

average_length_before = df["word_count_before"].mean()

print("Average Word Count Before:", average_length_before)

# 5. LOAD STOPWORDS

stop_words = set(stopwords.words("english"))

print("Number of stopwords:", len(stop_words))
print(list(stop_words)[:20])


# 6. TEXT CLEANING FUNCTION

def clean_text(text):

    text = str(text)

    # Convert text to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Replace punctuation with spaces
    text = text.translate(
        str.maketrans(
            string.punctuation,
            " " * len(string.punctuation)
        )
    )

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Remove stopwords
    words = text.split()

    words = [
        word for word in words
        if word not in stop_words
    ]

    # Join words back into text
    text = " ".join(words)

    return text


# Apply cleaning function
df["clean_text"] = df["review"].apply(clean_text)


# Display original and cleaned text
print(
    df[["review", "clean_text"]]
    .head(10)
    .to_string(index=False)
)


# 7. TEXT STATISTICS AFTER CLEANING

# Combine all cleaned text
cleaned_all_text = " ".join(
    df["clean_text"].astype(str)
)

# Split into words
cleaned_words = cleaned_all_text.split()

# Unique vocabulary
cleaned_vocabulary = set(cleaned_words)

print("Total words after cleaning:", len(cleaned_words))
print(
    "Vocabulary size after cleaning:",
    len(cleaned_vocabulary)
)


# 8. AVERAGE WORD COUNT AFTER CLEANING

df["word_count_after"] = df["clean_text"].apply(
    lambda x: len(str(x).split())
)

average_length_after = df["word_count_after"].mean()

print("Average Word Count Before:", average_length_before)
print("Average Word Count After:", average_length_after)

# 9. ORIGINAL VS CLEANED TEXT

comparison = df[["review", "clean_text"]].head(15)

print(
    comparison.to_string(index=False)
)

# 10. SAVE CLEANED DATASET
df.to_csv(
    "Week 07/Day 2/cleaned_dataset.csv",
    index=False
)

print("Cleaned dataset saved successfully!")