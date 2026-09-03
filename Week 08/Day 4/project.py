# WEEK 08 - DAY 4
# FINAL NLP MINI PROJECT
# CUSTOMER REVIEW SENTIMENT ANALYSIS

import os
import re
import string
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
from transformers import pipeline
warnings.filterwarnings("ignore")

# PROJECT PATHS
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)
RAW_DATASET = os.path.join(
    BASE_DIR,
    "raw_dataset.csv"
)
WORKING_DATASET = os.path.join(
    BASE_DIR,
    "dataset.csv"
)
CLEAN_DATASET = os.path.join(
    BASE_DIR,
    "clean_dataset.csv"
)
OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "output"
)
os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

# NLTK SETUP
print("\nDownloading/checking NLTK resources...")
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

stop_words = set(
    stopwords.words("english")
)
lemmatizer = WordNetLemmatizer()

# PART 1
# LOAD DATASET
if os.path.exists(WORKING_DATASET):
    print("\nProcessed dataset already exists.")
    print("Loading existing dataset...")
    df = pd.read_csv(
        WORKING_DATASET
    )
else:
    print("\nProcessed dataset does not exist.")
    print("Loading ORIGINAL 1.6 MILLION dataset...")
    print("This should happen ONLY ONCE.")
    df = pd.read_csv(
        RAW_DATASET,
        header=None,
        names=[
            "sentiment",
            "tweet_id",
            "date",
            "query",
            "username",
            "review"
        ],
        encoding="latin-1"
    )
    # Convert sentiment labels
    # Sentiment140:
    # 0 = Negative
    # 4 = Positive
    df["sentiment"] = df[
        "sentiment"
    ].map({
        0: "negative",
        4: "positive"
    })
    # Remove rows with invalid sentiment
    df = df.dropna(
        subset=["sentiment", "review"]
    )
    # Save complete working dataset
    df.to_csv(
        WORKING_DATASET,
        index=False
    )
    print("\nComplete dataset saved:")
    print(WORKING_DATASET)
print("\nDataset Shape:")
print(df.shape)

# BASIC INFORMATION
print("\nFirst 5 Rows:")
print(df.head())
print("\nColumn Names:")
print(df.columns.tolist())
print("\nDataset Info:")
df.info()
print("\nMissing Values:")
print(df.isnull().sum())

# DUPLICATES
print("\nDuplicate Reviews:")
duplicate_reviews = df[
    "review"
].duplicated().sum()
print(duplicate_reviews)

# SENTIMENT DISTRIBUTION
print("\nSentiment Distribution:")
sentiment_counts = df[
    "sentiment"
].value_counts()
print(
    sentiment_counts
)
print("\nSentiment Distribution Percentage:")
sentiment_percentage = (
    df["sentiment"]
    .value_counts(normalize=True)
    * 100
)
print(sentiment_percentage)

# REVIEW LENGTH
df["review_length"] = (
    df["review"]
    .astype(str)
    .str.len()
)
df["word_count"] = (
    df["review"]
    .astype(str)
    .str.split()
    .str.len()
)
print("\nReview Length Statistics:")
print(df["review_length"].describe())
print("\nWord Count Statistics:")
print(df["word_count"].describe())

# FREQUENT WORDS
print("\nFinding frequent words...")
all_words = Counter()
# Process in chunks to reduce memory pressure
for chunk in pd.read_csv(
    WORKING_DATASET,
    chunksize=50000
):
    for review in chunk["review"].astype(str):
        words = word_tokenize(
            review.lower())
        all_words.update(words)

print("\nTop 20 Frequent Words:")
print(all_words.most_common(20))

# PART 1 GRAPH 1
# SENTIMENT DISTRIBUTION
plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind="bar")
plt.title("Sentiment Class Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.tight_layout()

plt.savefig(os.path.join(OUTPUT_DIR,"01_sentiment_distribution.png"),dpi=300)
plt.close()

# PART 2
# TEXT PREPROCESSING
def preprocess_text(text):
    text = str(text)
    # Lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(
        r"http\S+|www\S+|https\S+",
        "",
        text
    )
    # Remove usernames
    text = re.sub(
        r"@\w+",
        "",
        text
    )
    # Remove punctuation
    text = text.translate(
        str.maketrans(
            "",
            "",
            string.punctuation
        )
    )
    # Remove numbers and special characters
    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )
    # Tokenization
    tokens = word_tokenize(
        text
    )
    # Stopword removal
    tokens = [
        word
        for word in tokens
        if word not in stop_words
    ]
    # Lemmatization
    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]
    return " ".join(tokens)
print("\nPreprocessing complete dataset...")
print("This can take some time because the dataset contains",len(df),"reviews.")

# Process in chunks inside dataframe
CHUNK_SIZE = 10000
clean_reviews = []
for start in range(
    0,
    len(df),
    CHUNK_SIZE
):
    end = min(
        start + CHUNK_SIZE,
        len(df)
    )
    print(
        f"Processing rows {start:,} - {end:,}"
    )
    chunk_reviews = (
        df["review"]
        .iloc[start:end]
        .apply(preprocess_text)
        .tolist()
    )
    clean_reviews.extend(
        chunk_reviews
    )
df["clean_review"] = clean_reviews
print("\nPreprocessing completed!")

# REMOVE EMPTY CLEAN REVIEWS
empty_reviews = (
    df["clean_review"]
    .str.strip()
    == ""
).sum()
print(
    "\nEmpty Clean Reviews:",
    empty_reviews
)
df = df[
    df["clean_review"].str.strip() != ""
].copy()

# CLEAN WORD COUNT
df["clean_word_count"] = (
    df["clean_review"]
    .str.split()
    .str.len()
)

# SAVE CLEAN DATASET
print("\nSaving clean dataset...")
df.to_csv(CLEAN_DATASET,index=False)
print("Clean dataset saved:")
print(CLEAN_DATASET)

# DISPLAY CLEAN DATA
print("\nOriginal vs Clean Review:")
print(df[["review","clean_review"]].head(10))
print("\nOriginal Average Word Count:")
print(df["word_count"].mean())
print("\nClean Average Word Count:")
print(df["clean_word_count"].mean())

# PART 3
# TEXT ANALYSIS
# COMMON WORDS BY SENTIMENT
def get_common_words(
    text_series,
    top_n=20
):
    counter = Counter()
    for text in text_series:
        words = str(text).split()
        counter.update(words)
    return counter.most_common(top_n)
positive_words = get_common_words(
    df.loc[df["sentiment"] == "positive","clean_review"])
negative_words = get_common_words(
    df.loc[df["sentiment"] == "negative","clean_review"])
print("\nTop Positive Words:")
print(positive_words)
print("\nTop Negative Words:")
print(negative_words)

# BIGRAMS
from sklearn.feature_extraction.text import CountVectorizer
bigram_vectorizer = CountVectorizer(
    ngram_range=(2, 2),
    max_features=50
)
bigram_matrix = bigram_vectorizer.fit_transform(df["clean_review"])
bigram_counts = np.asarray(bigram_matrix.sum(axis=0)).ravel()
bigram_names = (bigram_vectorizer.get_feature_names_out())
bigram_df = pd.DataFrame({
    "bigram": bigram_names,
    "frequency": bigram_counts
}).sort_values(
    "frequency",
    ascending=False
)
print("\nTop 20 Frequent Bigrams:")
print(bigram_df.head(20))
# AVERAGE REVIEW LENGTH BY SENTIMENT
average_length = (
    df.groupby("sentiment")[
        "review_length"
    ]
    .mean()
)
print("\nAverage Review Length by Sentiment:")
print(average_length)

# GRAPH 2
# REVIEW LENGTH DISTRIBUTION
plt.figure(figsize=(8, 5))
plt.hist(df["review_length"],bins=40)
plt.title("Review Length Distribution")
plt.xlabel("Characters")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR,"02_review_length_distribution.png"),dpi=300)
plt.close()
# GRAPH 3
# AVERAGE REVIEW LENGTH BY SENTIMENT

plt.figure(figsize=(8, 5))
average_length.plot(kind="bar")
plt.title("Average Review Length by Sentiment")
plt.xlabel("Sentiment")

plt.ylabel("Average Characters")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR,"03_average_length_by_sentiment.png"),dpi=300)
plt.close()

# GRAPH 4
# TOP POSITIVE WORDS

positive_df = pd.DataFrame(
    positive_words,
    columns=["word","frequency"])

plt.figure(figsize=(10, 6))
plt.bar(positive_df["word"],positive_df["frequency"])

plt.title("Top Positive Words")
plt.xlabel("Word")
plt.ylabel("Frequency")

plt.xticks(rotation=45,ha="right")
plt.tight_layout()

plt.savefig(os.path.join(OUTPUT_DIR,"04_top_positive_words.png"),dpi=300)
plt.close()

# GRAPH 5
# TOP NEGATIVE WORDS

negative_df = pd.DataFrame(negative_words,columns=["word","frequency"])

plt.figure(figsize=(10, 6))
plt.bar(negative_df["word"],negative_df["frequency"])
plt.title("Top Negative Words")

plt.xlabel("Word")
plt.ylabel("Frequency")

plt.xticks(rotation=45,ha="right")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR,"05_top_negative_words.png"),dpi=300)
plt.close()
# GRAPH 6
# TOP BIGRAMS

top_bigrams = bigram_df.head(20)
plt.figure(figsize=(12, 6))
plt.bar(top_bigrams["bigram"],top_bigrams["frequency"])

plt.title("Top 20 Frequent Bigrams")

plt.xlabel("Bigram")

plt.ylabel("Frequency")
plt.xticks(rotation=60,ha="right")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR,"06_top_bigrams.png"),dpi=300)
plt.close()

# PART 4
# TRADITIONAL NLP MODELS

# TRAIN / TEST SPLIT

X = df["clean_review"]
y = df["sentiment"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
print("\nTraining Samples:")
print(
    len(X_train)
)
print("\nTesting Samples:")
print(len(X_test))

# TF-IDF

print("\nCreating TF-IDF features...")
tfidf = TfidfVectorizer(
    max_features=50000,
    ngram_range=(1, 2),
    min_df=2,
    sublinear_tf=True
)
X_train_tfidf = tfidf.fit_transform(
    X_train
)
X_test_tfidf = tfidf.transform(X_test)
print("\nTF-IDF Training Shape:")
print(X_train_tfidf.shape)
print("\nTF-IDF Testing Shape:")
print(X_test_tfidf.shape)
# LOGISTIC REGRESSION

print("\nTraining Logistic Regression...")
logistic_model = LogisticRegression(
    max_iter=1000,
    n_jobs=-1
)
logistic_model.fit(
    X_train_tfidf,
    y_train
)
logistic_predictions = (
    logistic_model.predict(
        X_test_tfidf
    )
)
# NAIVE BAYES
print("\nTraining Naive Bayes...")
naive_bayes_model = MultinomialNB()
naive_bayes_model.fit(
    X_train_tfidf,
    y_train
)
naive_bayes_predictions = (
    naive_bayes_model.predict(
        X_test_tfidf
    )
)
# EVALUATION FUNCTION

def evaluate_model(
    model_name,
    y_true,
    y_pred
):
    accuracy = accuracy_score(
        y_true,
        y_pred
    )
    precision = precision_score(
        y_true,
        y_pred,
        pos_label="positive"
    )
    recall = recall_score(
        y_true,
        y_pred,
        pos_label="positive"
    )
    f1 = f1_score(
        y_true,
        y_pred,
        pos_label="positive"
    )
    print("\n")
    print(
        "=" * 50
    )
    print(
        model_name
    )
    print(
        "=" * 50
    )
    print(
        "Accuracy:",
        f"{accuracy:.4f}"
    )
    print(
        "Precision:",
        f"{precision:.4f}"
    )
    print(
        "Recall:",
        f"{recall:.4f}"
    )
    print(
        "F1 Score:",
        f"{f1:.4f}"
    )
    print("\nClassification Report:")
    print(
        classification_report(
            y_true,
            y_pred
        )
    )
    return {
        "Model": model_name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    }

# MODEL EVALUATION

logistic_results = evaluate_model(
    "Logistic Regression",
    y_test,
    logistic_predictions
)
naive_bayes_results = evaluate_model(
    "Naive Bayes",
    y_test,
    naive_bayes_predictions
)
results_df = pd.DataFrame([
    logistic_results,
    naive_bayes_results
])

# SAVE MODEL RESULTS

results_df.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "model_comparison.csv"
    ),
    index=False)
# CONFUSION MATRIX — LOGISTIC REGRESSION

cm = confusion_matrix(
    y_test,
    logistic_predictions,
    labels=[
        "negative",
        "positive"
    ]
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[
        "Negative",
        "Positive"
    ]

)

fig, ax = plt.subplots(figsize=(7, 6))

disp.plot(ax=ax)
plt.title("Logistic Regression Confusion Matrix")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR,"07_logistic_confusion_matrix.png"),dpi=300)
plt.close()

# CONFUSION MATRIX — NAIVE BAYES

cm_nb = confusion_matrix(
    y_test,
    naive_bayes_predictions,
    labels=["negative","positive"])
disp_nb = ConfusionMatrixDisplay(
    confusion_matrix=cm_nb,
    display_labels=["Negative","Positive"])
fig, ax = plt.subplots(figsize=(7, 6))
disp_nb.plot(ax=ax)
plt.title("Naive Bayes Confusion Matrix")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR,"08_naive_bayes_confusion_matrix.png"),dpi=300)
plt.close()

# GRAPH 9
# MODEL METRICS COMPARISON

metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1 Score"
]
x = np.arange(len(metrics))
width = 0.35
plt.figure(figsize=(10, 6))

plt.bar(x - width / 2,results_df.iloc[0][metrics],width,label="Logistic Regression")
plt.bar(x + width / 2,results_df.iloc[1][metrics],width,label="Naive Bayes")
plt.xticks(x,metrics)
plt.ylim(0,1)
plt.title("Traditional NLP Model Comparison")
plt.ylabel("Score")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR,"09_model_metrics_comparison.png"),dpi=300)
plt.close()

# PART 5
# TRANSFORMER COMPARISON

transformer_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)
print("Transformer loaded successfully!")
# SELECT 20 TEST REVIEWS

comparison_reviews = (
    X_test.iloc[:20]
    .tolist()
)
comparison_actual = (
    y_test.iloc[:20]
    .tolist()
)
# Logistic predictions for same 20
comparison_logistic = (
    logistic_model.predict(
        tfidf.transform(
            comparison_reviews
        )
    )
)

# TRANSFORMER PREDICTIONS

transformer_output = (transformer_model(comparison_reviews))
transformer_labels = []

transformer_confidence = []

for prediction in transformer_output:
    if prediction["label"] == "POSITIVE":
        transformer_labels.append(
            "positive"
        )
    else:
        transformer_labels.append("negative")
    transformer_confidence.append(prediction["score"])

# COMPARISON DATAFRAME

comparison_df = pd.DataFrame({
    "review": comparison_reviews,
    "actual": comparison_actual,
    "logistic_regression": comparison_logistic,
    "transformer": transformer_labels,
    "transformer_confidence": transformer_confidence
})

print("\n20 Review Comparison:")
print(comparison_df.to_string(index=False))

# TRANSFORMER ACCURACY

transformer_accuracy = accuracy_score(comparison_actual,transformer_labels)

logistic_accuracy_20 = accuracy_score(comparison_actual,comparison_logistic)

print("\nTransformer Accuracy on 20 Reviews:",f"{transformer_accuracy:.2%}")

print("Logistic Regression Accuracy on 20 Reviews:",f"{logistic_accuracy_20:.2%}")

# MODEL AGREEMENT

agreement = (comparison_df["logistic_regression"]==comparison_df["transformer"]).sum()
print("\nModels Agreed On:",f"{agreement}/20")
print("Agreement Percentage:",f"{agreement / 20:.2%}")

# SAVE TRANSFORMER RESULTS

comparison_df.to_csv(
os.path.join(OUTPUT_DIR,"transformer_comparison.csv"),index=False)

# GRAPH 10
# TRANSFORMER VS LOGISTIC

transformer_comparison = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Transformer"
    ],
    "Accuracy": [logistic_accuracy_20,transformer_accuracy]
})

plt.figure(figsize=(8, 5))

plt.bar(transformer_comparison["Model"],transformer_comparison["Accuracy"])

plt.title("Transformer vs Logistic Regression")
plt.ylabel("Accuracy")

plt.ylim(0,1)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR,"10_transformer_vs_logistic.png"),dpi=300)
plt.close()

# PART 6
# CUSTOM PREDICTION

def predict_custom_review(
    review
):
    clean_review = preprocess_text(
        review
    )
    review_tfidf = tfidf.transform(
        [clean_review]
    )
    prediction = logistic_model.predict(
        review_tfidf
    )[0]
    probabilities = logistic_model.predict_proba(
        review_tfidf
    )[0]
    class_index = list(
        logistic_model.classes_
    ).index(
        prediction
    )
    confidence = probabilities[
        class_index
    ]
    return (
        prediction,
        confidence,
        clean_review
    )

print("\nEnter your own customer reviews.")
print(
    "Type 'exit' when you want to stop."
)

while True:
    user_review = input(
        "\nEnter review: "
    )

    if user_review.lower().strip() == "exit":
        print(
            "\nCustom prediction stopped."
        )
        break

    if user_review.strip() == "":
        print(
            "Please enter a review."
        )
        continue

    prediction, confidence, clean_review = (
        predict_custom_review(
            user_review
        )
    )
    print(
        "\nOriginal Review:"
    )
    print(
        user_review
    )
    print(
        "\nClean Review:"
    )
    print(
        clean_review
    )
    print(
        "\nPredicted Sentiment:"
    )
    print(
        prediction.upper()
    )
    print(
        "\nConfidence:"
    )
    print(f"{confidence:.2%}")

# PART 7
# ERROR ANALYSIS

# CREATE ERROR DATAFRAME

error_probabilities = (
    logistic_model.predict_proba(
        X_test_tfidf
    )
)

error_confidence = (
    error_probabilities.max(
        axis=1))

error_df = pd.DataFrame({
    "review": X_test.values,
    "actual_sentiment": y_test.values,
    "predicted_sentiment":
        logistic_predictions,
    "confidence":
        error_confidence
})
error_df["correct"] = (
    error_df[
        "actual_sentiment"
    ]
    ==
    error_df["predicted_sentiment"])
# CORRECT / INCORRECT COUNTS

correct_count = (error_df["correct"].sum())

incorrect_count = (error_df["correct"] == False).sum()
print("\nTotal Test Reviews:", len(error_df))
print("Correct Predictions:", correct_count)
print("Incorrect Predictions:", incorrect_count)
print("Accuracy:", f"{correct_count / len(error_df):.2%}")
# FIVE CORRECT EXAMPLES

correct_examples =(error_df[error_df["correct"] == True ].head(5))
for i, (_, row) in enumerate(
    correct_examples.iterrows(),
    start=1
):
    print(f"\nExample {i}")
    print("Review:", row["review"])
    print("Actual:", row["actual_sentiment"])
    print("Predicted:", row["predicted_sentiment"])
    print("Confidence:", f"{row['confidence']:.2%}")

# FIVE INCORRECT EXAMPLES
incorrect_examples = (error_df[error_df["correct"] == False].head(5))

for i, (_, row) in enumerate(

    incorrect_examples.iterrows(),
    start=1
):
    print(f"\nExample {i}")
    print("Review:", row["review"])
    print("Actual:", row["actual_sentiment"])
    print("Predicted:", row["predicted_sentiment"])
    print("Confidence:", f"{row['confidence']:.2%}")

# FALSE POSITIVES
false_positives = error_df[(error_df["actual_sentiment"] == "negative")&(error_df["predicted_sentiment"] == "positive")]
print("\n")
print("False Positives:",len(false_positives))

# FALSE NEGATIVES
false_negatives = error_df[(error_df["actual_sentiment"] == "positive")&(error_df["predicted_sentiment"] == "negative")]
print("False Negatives:",len(false_negatives))

# LOW CONFIDENCE PREDICTIONS

low_confidence = (error_df.sort_values("confidence").head(10))

print(low_confidence.to_string(index=False))

# HIGH CONFIDENCE WRONG PREDICTIONS

high_confidence_wrong = (
error_df[error_df["correct"] == False]
.sort_values("confidence",ascending=False).head(10))

print(high_confidence_wrong.to_string(index=False))

# ERROR ANALYSIS REASONS


print("""
1. Mixed Sentiment
   A review can contain both positive and negative opinions.
2. Context
   The meaning of a word depends on surrounding words.
3. Ambiguity
   Some reviews do not clearly express one sentiment.
4. Sarcasm
   Sarcastic language can be difficult for traditional
   machine-learning models.
5. Unusual Wording
   Slang, abbreviations, spelling mistakes and informal
   Twitter language can reduce model performance.
6. Negation
   Phrases such as "not good" can be difficult because
   "good" is normally associated with positive sentiment.
7. Limited Context Understanding
   TF-IDF mainly represents word importance and does not
   deeply understand relationships between words.
8. Short Reviews
   Very short reviews may not contain enough information
   for reliable classification.
""")

# SAVE ERROR ANALYSIS

error_df.to_csv(
    os.path.join(OUTPUT_DIR,"error_analysis.csv"),index=False)
correct_examples.to_csv(os.path.join(OUTPUT_DIR,"correct_predictions.csv"),index=False)
incorrect_examples.to_csv(os.path.join(OUTPUT_DIR,"incorrect_predictions.csv"),index=False)

# GRAPH 11
# CORRECT VS INCORRECT

prediction_counts = pd.Series({"Correct":correct_count,"Incorrect":incorrect_count})

plt.figure(figsize=(8, 5))
plt.bar(prediction_counts.index,prediction_counts.values)

plt.title("Correct vs Incorrect Predictions")
plt.xlabel("Prediction Type")
plt.ylabel("Number of Reviews")
plt.tight_layout()

plt.savefig(os.path.join(OUTPUT_DIR,"11_correct_vs_incorrect.png"),dpi=300)
plt.close()

# FINAL OUTPUT SUMMARY

print("\nFiles created:")
print("\nClean Dataset:")
print(CLEAN_DATASET)
print("\nOutput Folder:")
print(OUTPUT_DIR)
print("\nSaved Graphs:")
for file in sorted(os.listdir(OUTPUT_DIR)):
    if file.endswith(".png"):print(" -",file)

print("\nSaved CSV Results:")
for file in sorted(os.listdir(OUTPUT_DIR)):
    if file.endswith(".csv"):
        print(" -",file)
