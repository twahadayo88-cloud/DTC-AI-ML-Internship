import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)
# DOWNLOAD NLTK RESOURCES
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
# LOAD DATASET
df = pd.read_csv(
    "Week 07/Day 5/dataset.csv",
    encoding="latin-1"
)
# Select only required columns
df = df[["v1", "v2"]]
# Rename columns
df.columns = ["label", "message"]
print("First 5 Rows:\n")
print(df.head())
print("\nDataset Shape:")
print(df.shape)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nClass Distribution:")
print(df["label"].value_counts())

# TEXT CLEANING AND PREPROCESSING
stop_words = set(stopwords.words("english"))
def clean_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)
    # Remove numbers
    text = re.sub(r"\d+", "", text)
    # Remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )
    # Remove special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    # Tokenization
    tokens = word_tokenize(text)
    # Remove stopwords
    tokens = [
        word for word in tokens
        if word not in stop_words
    ]
    # Join tokens back into text
    return " ".join(tokens)

# Apply cleaning
df["clean_message"] = df["message"].apply(clean_text)

print(df[["message", "clean_message", "label"]].head())

# LABEL ENCODING
df["label_encoded"] = df["label"].map({"ham": 0,"spam": 1})

# FEATURES AND TARGET
X = df["clean_message"]
y = df["label_encoded"]

# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
print("\nTRAIN TEST SPLIT")
print("Training Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# TF-IDF VECTORIZATION
tfidf = TfidfVectorizer()
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)
print("TF-IDF Training Shape:")
print(X_train_tfidf.shape)
print("\nTF-IDF Testing Shape:")
print(X_test_tfidf.shape)

# MODEL 1: MULTINOMIAL NAIVE BAYES
nb_model = MultinomialNB()
nb_model.fit(
    X_train_tfidf,
    y_train
)
nb_predictions = nb_model.predict(
    X_test_tfidf
)
# Evaluation
nb_accuracy = accuracy_score(
    y_test,
    nb_predictions
)
nb_precision = precision_score(
    y_test,
    nb_predictions
)
nb_recall = recall_score(
    y_test,
    nb_predictions
)
nb_f1 = f1_score(
    y_test,
    nb_predictions
)

print("Accuracy:", nb_accuracy)
print("Precision:", nb_precision)
print("Recall:", nb_recall)
print("F1 Score:", nb_f1)
print("\nConfusion Matrix:\n")
print(confusion_matrix( y_test,nb_predictions
))

# MODEL 2: LOGISTIC REGRESSION
lr_model = LogisticRegression(
    max_iter=1000)
lr_model.fit(
    X_train_tfidf,
    y_train
)
lr_predictions = lr_model.predict(
    X_test_tfidf
)
# Evaluation
lr_accuracy = accuracy_score(
    y_test,
    lr_predictions
)
lr_precision = precision_score(
    y_test,
    lr_predictions
)
lr_recall = recall_score(
    y_test,
    lr_predictions
)
lr_f1 = f1_score(
    y_test,
    lr_predictions
)
print("Accuracy:", lr_accuracy)
print("Precision:", lr_precision)
print("Recall:", lr_recall)
print("F1 Score:", lr_f1)
print("\nConfusion Matrix:\n")
print(
    confusion_matrix(
        y_test,
        lr_predictions
    )
)

# MODEL COMPARISON
comparison = pd.DataFrame( {
        "Model": [
            "Multinomial Naive Bayes",
            "Logistic Regression"
        ],
        "Accuracy": [
            nb_accuracy,
            lr_accuracy
        ],
        "Precision": [
            nb_precision,
            lr_precision
        ],
        "Recall": [
            nb_recall,
            lr_recall
        ],
        "F1 Score": [
            nb_f1,
            lr_f1
        ]
    }
)
print("\nMODEL COMPARISON")
print(comparison)

# FIND BEST MODEL
best_model_name = comparison.loc[comparison["F1 Score"].idxmax(),"Model"]
print("\nBest Model:")
print(best_model_name)

# CUSTOM UNSEEN SENTENCES
def predict_message(message):
    # Clean message
    cleaned_message = clean_text(message)
    # Convert into TF-IDF
    message_tfidf = tfidf.transform(
        [cleaned_message]
    )
    # Select best model
    if best_model_name == "Multinomial Naive Bayes":
        prediction = nb_model.predict(
            message_tfidf
        )
    else:
        prediction = lr_model.predict(
            message_tfidf)
    # Convert prediction into label
    if prediction[0] == 1:
        result = "SPAM"
    else:
        result = "HAM"
    print("\nOriginal Message:")
    print(message)
    print("\nCleaned Message:")
    print(cleaned_message)
    print("\nPrediction:")
    print(result)
print("\nCUSTOM UNSEEN PREDICTIONS")
predict_message(
    "Congratulations! You have won a free iPhone. Claim now!"
)
predict_message(
    "Hey, are we meeting tomorrow for the project?"
)
predict_message("Urgent! Claim your free cash reward today.")
predict_message("Please send me the assignment notes when you are free.")