
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load pretrained tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english"
)
# Load pretrained classification model
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english"
)
print("Tokenizer loaded successfully!")
print("Pretrained Transformer model loading done!")

text = "This movie was absolutely amazing! I loved every moment of it."
token = tokenizer.tokenize(text)
print("\nOriginal Text:")
print(text)
print("\nTokens:")
print(token)

# Convert tokens to token IDs
token_ids = tokenizer.convert_tokens_to_ids(token)
print("\nToken IDs:")
print(token_ids)

#now attention mask is created to indicate which tokens should be attended to (1) and which should be ignored (0)
inputs = tokenizer(
    text,
    return_tensors="pt"
)
print("\nModel Inputs:")
print(inputs)
print("\nInput IDs:")
print(inputs["input_ids"])
print("\nAttention Mask:")
print(inputs["attention_mask"])

positive_text = "This movie was absolutely amazing and I really enjoyed it."
positive_inputs = tokenizer(
    positive_text,
    return_tensors="pt"
)
with torch.no_grad():
    positive_outputs = model(**positive_inputs)
positive_logits = positive_outputs.logits
positive_probabilities = torch.softmax(
    positive_logits,
    dim=1
)
positive_prediction = torch.argmax(
    positive_probabilities,
    dim=1
).item()
positive_confidence = positive_probabilities[
    0, positive_prediction
].item()

print("POSITIVE TEXT PREDICTION")

print("\nText:")
print(positive_text)
print("\nPredicted Label:")
print(model.config.id2label[positive_prediction])

print("\nConfidence:")
print(f"{positive_confidence:.4f}")


negative_text = "This movie was terrible and I really hated it."

negative_inputs = tokenizer(
    negative_text,
    return_tensors="pt"
)

with torch.no_grad():
    negative_outputs = model(**negative_inputs)

negative_logits = negative_outputs.logits

negative_probabilities = torch.softmax(
    negative_logits,
    dim=1
)

negative_prediction = torch.argmax(
    negative_probabilities,
    dim=1
).item()

negative_confidence = negative_probabilities[
    0, negative_prediction
].item()

print("NEGATIVE TEXT PREDICTION")

print("\nText:")
print(negative_text)

print("\nPredicted Label:")
print(model.config.id2label[negative_prediction])

print("\nConfidence:")
print(f"{negative_confidence:.4f}")


#===================================================================================================================
#TF-IDF VS TRANSFORMER PREDICTION COMPARISON
#===================================================================================================================

# TF-IDF VS TRANSFORMER COMPARISON
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

print("TF-IDF VS TRANSFORMER COMPARISON")

# 1. Load dataset
df = pd.read_csv("Week 08/Day 1/train_40k.csv")
print("\nDataset Shape:")
print(df.shape)

# 2. Remove missing reviews
df = df.dropna(subset=["Text"]).copy()

# 3. Create sentiment labels from Score
# Score 4 or 5 = Positive
# Score 1 or 2 = Negative
# Score 3 = Neutral, so remove it
df["sentiment"] = df["Score"].apply(
    lambda x: 1 if x >= 4 else (0 if x <= 2 else -1)
)
df = df[df["sentiment"] != -1].copy()
print("\nSentiment Distribution:")
print(df["sentiment"].value_counts())

# 4. Use review text as input
X = df["Text"]
y = df["sentiment"]

# 5. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# 6. TF-IDF Vectorization
tfidf = TfidfVectorizer(
    max_features=10000,
    stop_words="english"
)
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)
print("\nTF-IDF Training Shape:")
print(X_train_tfidf.shape)
print("\nTF-IDF Testing Shape:")
print(X_test_tfidf.shape)

# 7. Train Logistic Regression
tfidf_model = LogisticRegression(
    max_iter=1000
)
tfidf_model.fit(X_train_tfidf, y_train)
print("\nTF-IDF Logistic Regression model trained successfully!")

# 8. Create same examples used for Transformer
comparison_texts = [
    "This movie was absolutely amazing and I really enjoyed it.",
    "This movie was terrible and I really hated it."
]

# 9. Transformer Predictions
transformer_predictions = []
for text in comparison_texts:
    inputs = tokenizer(
        text,
        return_tensors="pt"
    )
    with torch.no_grad():
        outputs = model(**inputs)
    probabilities = torch.softmax(
        outputs.logits,
        dim=1
    )

    prediction = torch.argmax(
        probabilities,
        dim=1
    ).item()
    confidence = probabilities[
        0, prediction
    ].item()
    label = model.config.id2label[prediction]
    transformer_predictions.append(
        (label, confidence)
    )

# 10. TF-IDF Predictions
comparison_tfidf = tfidf.transform(comparison_texts)
tfidf_predictions = tfidf_model.predict(
    comparison_tfidf
)
tfidf_probabilities = tfidf_model.predict_proba(
    comparison_tfidf
)

# 11. Compare Results
print("\n" + "=" * 70)
print("FINAL COMPARISON")
print("=" * 70)
for i, text in enumerate(comparison_texts):

    transformer_label = transformer_predictions[i][0]
    transformer_confidence = transformer_predictions[i][1]

    tfidf_prediction = (
        "POSITIVE"
        if tfidf_predictions[i] == 1
        else "NEGATIVE"
    )

    tfidf_confidence = max(
        tfidf_probabilities[i]
    )
    print("\nText:")
    print(text)

    print("\nTransformer:")
    print("Prediction:", transformer_label)
    print(f"Confidence: {transformer_confidence:.4f}")

    print("\nTF-IDF + Logistic Regression:")
    print("Prediction:", tfidf_prediction)
    print(f"Confidence: {tfidf_confidence:.4f}")