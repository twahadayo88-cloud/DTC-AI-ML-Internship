import pandas as pd
import re
import string

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# 1. LOAD DATASET

df = pd.read_csv("Week 07/Day 4/dataset.csv")

print("\nDataset First 5 Rows:")
print(df.head())
print("\nDataset Shape:")
print(df.shape)
print("\nDataset Columns:")
print(df.columns)
print("\nDataset Information:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 3. CREATE TEXT CLEANING FUNCTION

def clean_text(text):

    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# 4. APPLY CLEANING
df["clean_text"] = df["review"].apply(clean_text)
print(df[["review", "clean_text"]].head())


# 5. HANDLE EMPTY TEXT
df = df.dropna(subset=["clean_text"])
df = df[df["clean_text"].str.strip() != ""]
print("\nDataset Shape After Cleaning:")
print(df.shape)

# 6. BAG OF WORDS USING COUNTVECTORIZER
count_vectorizer = CountVectorizer()
bow_matrix = count_vectorizer.fit_transform(
    df["clean_text"]
)
print("\nBag of Words Matrix:")
print(bow_matrix)

# 7. CHECK MATRIX DIMENSIONS
print("\nBag of Words Matrix Shape:")
print(bow_matrix.shape)
print("\nNumber of Documents:")
print(bow_matrix.shape[0])
print("\nVocabulary Size:")
print(bow_matrix.shape[1])

# 8. DISPLAY VOCABULARY
vocabulary = count_vectorizer.get_feature_names_out()
print("\nVocabulary:")
print(vocabulary)
print("\nVocabulary Size:")
print(len(vocabulary))

# 9. CONVERT BOW MATRIX TO DATAFRAME

bow_df = pd.DataFrame(
    bow_matrix.toarray(),
    columns=vocabulary
)
print("\nBag of Words DataFrame:")
print(bow_df.head())

# 10. FIND MOST FREQUENT TERMS
word_counts = bow_matrix.sum(axis=0).A1

frequency_df = pd.DataFrame({
    "word": vocabulary,
    "frequency": word_counts
})
frequency_df = frequency_df.sort_values(
    by="frequency",
    ascending=False
)
print("\nTop 20 Most Frequent Terms:")
print(frequency_df.head(20))

# 11. TF-IDF USING TFIDFVECTORIZER
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(
    df["clean_text"]
)
print("\nTF-IDF Matrix:")
print(tfidf_matrix)

# 12. CHECK TF-IDF MATRIX DIMENSIONS
print("\nTF-IDF Matrix Shape:")
print(tfidf_matrix.shape)
print("\nNumber of Documents:")
print(tfidf_matrix.shape[0])
print("\nVocabulary Size:")
print(tfidf_matrix.shape[1])


# 13. DISPLAY TF-IDF VOCABULARY
tfidf_vocabulary = (
    tfidf_vectorizer.get_feature_names_out()
)
print("\nTF-IDF Vocabulary:")
print(tfidf_vocabulary)

# 14. CONVERT TF-IDF MATRIX TO DATAFRAME
tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=tfidf_vocabulary
)
print("\nTF-IDF DataFrame:")
print(tfidf_df.head())

# 15. FIND HIGH TF-IDF TERMS
tfidf_scores = tfidf_matrix.sum(axis=0).A1
tfidf_terms_df = pd.DataFrame({
    "word": tfidf_vocabulary,
    "tfidf_score": tfidf_scores
})
tfidf_terms_df = tfidf_terms_df.sort_values(
    by="tfidf_score",
    ascending=False
)
print("\nTop 20 High TF-IDF Terms:")
print(tfidf_terms_df.head(20))

# 16. COMPARE BOW AND TF-IDF
print("\nBag of Words:")
print("Matrix Shape:", bow_matrix.shape)
print("Vocabulary Size:", len(vocabulary))
print("Matrix Type:", type(bow_matrix))
print("\nTF-IDF:")
print("Matrix Shape:", tfidf_matrix.shape)
print("Vocabulary Size:", len(tfidf_vocabulary))
print("Matrix Type:", type(tfidf_matrix))

# 17. CHECK SPARSE MATRIX INFORMATION
print("\nBag of Words Non-Zero Values:")
print(bow_matrix.nnz)
print("\nBag of Words Total Possible Values:")
print(
    bow_matrix.shape[0] *
    bow_matrix.shape[1]
)
print("\nTF-IDF Non-Zero Values:")
print(tfidf_matrix.nnz)
print("\nTF-IDF Total Possible Values:")
print(
    tfidf_matrix.shape[0] *
    tfidf_matrix.shape[1]
)
# 18. CALCULATE SPARSITY
bow_total_values = (
    bow_matrix.shape[0] *
    bow_matrix.shape[1]
)
bow_zero_values = (
    bow_total_values -
    bow_matrix.nnz
)
bow_sparsity = (
    bow_zero_values /
    bow_total_values
) * 100
tfidf_total_values = (
    tfidf_matrix.shape[0] *
    tfidf_matrix.shape[1]
)
tfidf_zero_values = (
    tfidf_total_values -
    tfidf_matrix.nnz
)
tfidf_sparsity = (
    tfidf_zero_values /
    tfidf_total_values
) * 100

print("\nBag of Words Sparsity:")
print(round(bow_sparsity, 2), "%")
print("\nTF-IDF Sparsity:")
print(round(tfidf_sparsity, 2), "%")

# 19. FINAL SUMMARY
print("\nTotal Documents:", len(df))
print("Bag of Words Vocabulary Size:",
      len(vocabulary))
print("TF-IDF Vocabulary Size:",
      len(tfidf_vocabulary))
print("Most Frequent Word:",
      frequency_df.iloc[0]["word"])
print("Frequency:",
      frequency_df.iloc[0]["frequency"])
print("Highest TF-IDF Term:",
      tfidf_terms_df.iloc[0]["word"])
print("TF-IDF Score:",
      round(
          tfidf_terms_df.iloc[0]["tfidf_score"],
          4
      ))