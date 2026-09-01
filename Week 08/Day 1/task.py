import os
import re
import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# STEP 1: File Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(BASE_DIR, "train_40k.csv")
embedding_path = os.path.join(BASE_DIR, "review_embeddings.npy")

# STEP 2: Load Dataset
df = pd.read_csv(dataset_path)
print("DATASET INFORMATION")
print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Shape:")
print(df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
print("\nDataset Information:")
print(df.info())
print("\nDataset Statistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())

# STEP 3: Display Sample Reviews
print("SAMPLE REVIEWS")
for i in range(5):
    print(f"\nReview {i + 1}:")
    print(df["Text"].iloc[i])

# STEP 4: Review Length
df["word_count"] = df["Text"].str.split().str.len()
print("WORD COUNT STATISTICS")
print(df["word_count"].describe())

# STEP 5: Check Empty Reviews
empty_reviews = (df["Text"].str.strip() == "").sum()
print("\nEmpty Reviews:", empty_reviews)

# STEP 6: Check Duplicate Reviews
duplicate_reviews = df["Text"].duplicated().sum()
print("Duplicate Reviews:", duplicate_reviews)

# STEP 7: Text Cleaning
def clean_text(text):
    text = str(text).lower()
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)
    return text.strip()

df["clean_text"] = df["Text"].apply(clean_text)
print("TEXT CLEANING")
print("\nOriginal Text:")
print(df["Text"].iloc[0])
print("\nCleaned Text:")
print(df["clean_text"].iloc[0])

# STEP 8: Load Pretrained Sentence Transformer
print("SENTENCE TRANSFORMER")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("\nSentence Transformer model loaded successfully!")

# STEP 9: Test Embedding on 5 Reviews
sample_texts = df["clean_text"].head(5).tolist()
sample_embeddings = model.encode(sample_texts)
print("\nSample Embedding Shape:")
print(sample_embeddings.shape)
print("\nFirst Review Embedding:")
print(sample_embeddings[0])
print("\nFirst Vector Length:")
print(len(sample_embeddings[0]))

# STEP 10: Cosine Similarity for 5 Reviews
sample_similarity = cosine_similarity(sample_embeddings)
print("COSINE SIMILARITY MATRIX")
print(sample_similarity)

# STEP 11: Load Existing Embeddings OR Generate Them
print("FULL DATASET EMBEDDINGS")
if os.path.exists(embedding_path):
    print("\nExisting embeddings found!")
    embeddings = np.load(embedding_path)
    print("Embeddings loaded successfully.")
else:
    print("\nEmbedding file not found.")
    print("Generating embeddings for 40,000 reviews...")
    print("This may take some time.")
    embeddings = model.encode(
        df["clean_text"].tolist(),
        batch_size=32,
        show_progress_bar=True
    )
    np.save(embedding_path, embeddings)
    print("\nEmbeddings generated and saved successfully!")
print("\nAll Embeddings Shape:")
print(embeddings.shape)

# STEP 12: Verify Dense Vector
print("DENSE VECTOR INFORMATION")
print("\nNumber of Reviews:", len(embeddings))
print("Vector Dimensions:", embeddings.shape[1])
print("\nFirst Review Dense Vector:")
print(embeddings[0])

# STEP 13: Document Similarity System
query_index = 1
query_text = df["Text"].iloc[query_index]
query_embedding = embeddings[query_index].reshape(1, -1)
# Calculate similarity with all reviews
similarities = cosine_similarity(
    query_embedding,
    embeddings
)[0]

# Ignore the query itself
similarities[query_index] = -1
# Get Top 5 similar reviews
top_indices = similarities.argsort()[-5:][::-1]
print("DOCUMENT SIMILARITY SYSTEM")
print("\nQUERY REVIEW:")
print(query_text)
print("TOP 5 MOST SIMILAR REVIEWS")
for rank, index in enumerate(top_indices, start=1):
    print(f"\nRank {rank}")
    print(f"Similarity Score: {similarities[index]:.4f}")
    print(f"Category: {df['Cat1'].iloc[index]}")
    print("Review:")
    print(df["Text"].iloc[index])

# STEP 14: Semantic Similarity Experiment
print("SEMANTIC SIMILARITY EXPERIMENT")
test_texts = [
    "I really enjoyed reading this book. The story was excellent.",
    "This novel was wonderful and I loved reading the story.",
    "The football team played an exciting match and scored three goals."
]

# Convert test sentences into embeddings
test_embeddings = model.encode(test_texts)
# Calculate cosine similarity
test_similarity = cosine_similarity(test_embeddings)
print("\nTest Sentences:")

for i, text in enumerate(test_texts, start=1):
    print(f"\nSentence {i}:")
    print(text)
print("\nSemantic Similarity Matrix:")
print(test_similarity)

# STEP 15: Pairwise Similarity Results
print("PAIRWISE SEMANTIC SIMILARITY")
print(
    f"\nSentence 1 ↔ Sentence 2: "
    f"{test_similarity[0][1]:.4f}"
)
print(
    f"Sentence 1 ↔ Sentence 3: "
    f"{test_similarity[0][2]:.4f}"
)
print(
    f"Sentence 2 ↔ Sentence 3: "
    f"{test_similarity[1][2]:.4f}"
)