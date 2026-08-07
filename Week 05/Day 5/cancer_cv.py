import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import(
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold




#load dataset
data = pd.read_csv("Week 05/Day 5/cancer_imbalanced_1000.csv")
print("\nData Set:")
print(data.head())
print("\nDataset Information:")
print(data.info())
print("\nDataset Shape:")
print(data.shape)
print("\nMissing Values:")
print(data.isnull().sum())
print("\nStatistical Summary:")
print(data.describe())
print("\nCancer Class Distribution:")
print(data["Cancer"].value_counts())
print("\nCancer Class Percentage:")
print(data["Cancer"].value_counts(normalize=True) * 100)


x = data.drop("Cancer", axis=1)
y = data["Cancer"]

print("\nFeatures:")
print(x.head())

print("\nTarget:")
print(y.head())

print("\nX Shape:")
print(x.shape)

print("\ny Shape:")
print(y.shape)

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


model = RandomForestClassifier(
    random_state=42
)

model.fit(x_train,y_train)

y_prediction = model.predict(x_test)



accuracy = accuracy_score(y_test, y_prediction)
print("\nTest Accuracy:")
print(accuracy)

print("\nPrecision:")
print(precision_score(y_test, y_prediction))
print("\nRecall:")
print(recall_score(y_test, y_prediction))

print("\nF1 Score:")
print(f1_score(y_test, y_prediction))

cm = confusion_matrix(y_test, y_prediction)
print("\n COnfusion Matrix:")
print(cm)

print("\nclasification Report:")
print(classification_report(
    y_test,
    y_prediction,
    zero_division=0
))

cv_score = cross_val_score(
    model,
    x_train,
    y_train,
    cv =5,
    scoring="accuracy"

)
print("\nCross Validation accuray score")
print(cv_score)

print("\nMean cross validation accuracy")
print(cv_score.mean())

print("\nStandard deviation")
print(cv_score.std())

cv_recall = cross_val_score(
    model,
    x_train,
    y_train,
    cv=5,

)

print("\nCross Validation Recall Scores:")
print(cv_recall)

print("\nMean Cross Validation Recall:")
print(cv_recall.mean())

print("\nRecall Standard Deviation:")
print(cv_recall.std())

cv_precision = cross_val_score(
    model,
    x_train,
    y_train,
    cv=5,
    scoring="precision"
)

print("\nCross Validation Precision Scores:")
print(cv_precision)

print("\nMean Cross Validation Precision:")
print(cv_precision.mean())

cv_f1 = cross_val_score(
    model,
    x_train,
    y_train,
    cv=5,
    scoring="f1"
)

print("\nCross Validation F1 Scores:")
print(cv_f1)

print("\nMean Cross Validation F1:")
print(cv_f1.mean())

skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

for fold, (train_index, validation_index) in enumerate(
    skf.split(x_train, y_train),
    start=1
):

    y_train_fold = y_train.iloc[train_index]
    y_validation_fold = y_train.iloc[validation_index]

    print(f"\nFold {fold}")

    print("Training class distribution:")
    print(y_train_fold.value_counts())

    print("Validation class distribution:")
    print(y_validation_fold.value_counts())


#--------------------------------------------------------
"""import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# ============================================================
# 1. LOAD DATASET
# ============================================================

data = pd.read_csv(
    "Week 05/Day 5/cancer_imbalanced_1000.csv"
)

print("\nData Set:")
print(data.head())


print("\nDataset Information:")
print(data.info())


print("\nDataset Shape:")
print(data.shape)


print("\nMissing Values:")
print(data.isnull().sum())


print("\nStatistical Summary:")
print(data.describe())


print("\nCancer Class Distribution:")
print(data["Cancer"].value_counts())


print("\nCancer Class Percentage:")
print(
    data["Cancer"].value_counts(normalize=True) * 100
)


# ============================================================
# 2. FEATURES AND TARGET
# ============================================================

x = data.drop("Cancer", axis=1)
y = data["Cancer"]


print("\nFeatures:")
print(x.head())


print("\nTarget:")
print(y.head())


print("\nX Shape:")
print(x.shape)


print("\ny Shape:")
print(y.shape)


# ============================================================
# 3. TRAIN / TEST SPLIT
# ============================================================

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("\nTraining Data Shape:")
print(x_train.shape)

print("\nTesting Data Shape:")
print(x_test.shape)


print("\nTraining Class Distribution:")
print(y_train.value_counts())


print("\nTesting Class Distribution:")
print(y_test.value_counts())


# ============================================================
# 4. BASELINE RANDOM FOREST MODEL
# ============================================================

model = RandomForestClassifier(
    random_state=42
)


model.fit(
    x_train,
    y_train
)


y_prediction = model.predict(
    x_test
)


# ============================================================
# 5. BASELINE TEST METRICS
# ============================================================

accuracy = accuracy_score(
    y_test,
    y_prediction
)

print("\nTest Accuracy:")
print(accuracy)


print("\nPrecision:")
print(
    precision_score(
        y_test,
        y_prediction,
        zero_division=0
    )
)


print("\nRecall:")
print(
    recall_score(
        y_test,
        y_prediction,
        zero_division=0
    )
)


print("\nF1 Score:")
print(
    f1_score(
        y_test,
        y_prediction,
        zero_division=0
    )
)


# ============================================================
# 6. CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(
    y_test,
    y_prediction
)

print("\nConfusion Matrix:")
print(cm)


# ============================================================
# 7. CLASSIFICATION REPORT
# ============================================================

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_prediction,
        zero_division=0
    )
)


# ============================================================
# 8. 5-FOLD CROSS VALIDATION - ACCURACY
# ============================================================

cv_score = cross_val_score(
    model,
    x_train,
    y_train,
    cv=5,
    scoring="accuracy"
)


print("\nCross Validation Accuracy Scores:")
print(cv_score)


print("\nMean Cross Validation Accuracy:")
print(cv_score.mean())


print("\nAccuracy Standard Deviation:")
print(cv_score.std())


# ============================================================
# 9. 5-FOLD CROSS VALIDATION - RECALL
# ============================================================

cv_recall = cross_val_score(
    model,
    x_train,
    y_train,
    cv=5,
    scoring="recall"
)


print("\nCross Validation Recall Scores:")
print(cv_recall)


print("\nMean Cross Validation Recall:")
print(cv_recall.mean())


print("\nRecall Standard Deviation:")
print(cv_recall.std())


# ============================================================
# 10. 5-FOLD CROSS VALIDATION - PRECISION
# ============================================================

cv_precision = cross_val_score(
    model,
    x_train,
    y_train,
    cv=5,
    scoring="precision"
)


print("\nCross Validation Precision Scores:")
print(cv_precision)


print("\nMean Cross Validation Precision:")
print(cv_precision.mean())


print("\nPrecision Standard Deviation:")
print(cv_precision.std())


# ============================================================
# 11. 5-FOLD CROSS VALIDATION - F1
# ============================================================

cv_f1 = cross_val_score(
    model,
    x_train,
    y_train,
    cv=5,
    scoring="f1"
)


print("\nCross Validation F1 Scores:")
print(cv_f1)


print("\nMean Cross Validation F1:")
print(cv_f1.mean())


print("\nF1 Standard Deviation:")
print(cv_f1.std())


# ============================================================
# 12. MANUAL STRATIFIED K-FOLD
# ============================================================

skf = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


fold_accuracies = []
fold_precisions = []
fold_recalls = []
fold_f1_scores = []


for fold, (train_index, validation_index) in enumerate(
    skf.split(x_train, y_train),
    start=1
):

    print("\n===================================")
    print(f"FOLD {fold}")
    print("===================================")


    # --------------------------------------------------------
    # Get training and validation data
    # --------------------------------------------------------

    X_fold_train = x_train.iloc[train_index]
    X_fold_validation = x_train.iloc[validation_index]

    y_fold_train = y_train.iloc[train_index]
    y_fold_validation = y_train.iloc[validation_index]


    # --------------------------------------------------------
    # Show class distribution
    # --------------------------------------------------------

    print("\nTraining Class Distribution:")
    print(y_fold_train.value_counts())


    print("\nValidation Class Distribution:")
    print(y_fold_validation.value_counts())


    # --------------------------------------------------------
    # Create a NEW model for this fold
    # --------------------------------------------------------

    fold_model = RandomForestClassifier(
        random_state=42
    )


    # --------------------------------------------------------
    # Train model
    # --------------------------------------------------------

    fold_model.fit(
        X_fold_train,
        y_fold_train
    )


    # --------------------------------------------------------
    # Make validation predictions
    # --------------------------------------------------------

    fold_prediction = fold_model.predict(
        X_fold_validation
    )


    # --------------------------------------------------------
    # Calculate metrics
    # --------------------------------------------------------

    fold_accuracy = accuracy_score(
        y_fold_validation,
        fold_prediction
    )


    fold_precision = precision_score(
        y_fold_validation,
        fold_prediction,
        zero_division=0
    )


    fold_recall = recall_score(
        y_fold_validation,
        fold_prediction,
        zero_division=0
    )


    fold_f1 = f1_score(
        y_fold_validation,
        fold_prediction,
        zero_division=0
    )


    # --------------------------------------------------------
    # Store results
    # --------------------------------------------------------

    fold_accuracies.append(
        fold_accuracy
    )

    fold_precisions.append(
        fold_precision
    )

    fold_recalls.append(
        fold_recall
    )

    fold_f1_scores.append(
        fold_f1
    )


    # --------------------------------------------------------
    # Print fold results
    # --------------------------------------------------------

    print("\nFold Accuracy:")
    print(fold_accuracy)


    print("\nFold Precision:")
    print(fold_precision)


    print("\nFold Recall:")
    print(fold_recall)


    print("\nFold F1 Score:")
    print(fold_f1)


# ============================================================
# 13. MANUAL CROSS VALIDATION SUMMARY
# ============================================================

print("\n")
print("==========================================")
print("MANUAL CROSS VALIDATION SUMMARY")
print("==========================================")


print("\nAll Fold Accuracies:")
print(fold_accuracies)


print("\nMean Accuracy:")
print(
    sum(fold_accuracies)
    / len(fold_accuracies)
)


print("\nAll Fold Precisions:")
print(fold_precisions)


print("\nMean Precision:")
print(
    sum(fold_precisions)
    / len(fold_precisions)
)


print("\nAll Fold Recalls:")
print(fold_recalls)


print("\nMean Recall:")
print(
    sum(fold_recalls)
    / len(fold_recalls)
)


print("\nAll Fold F1 Scores:")
print(fold_f1_scores)


print("\nMean F1 Score:")
print(
    sum(fold_f1_scores)
    / len(fold_f1_scores)
)


# ============================================================
# 14. BALANCED RANDOM FOREST
# ============================================================

balanced_model = RandomForestClassifier(
    random_state=42,
    class_weight="balanced"
)


# ============================================================
# 15. BALANCED MODEL - 5 FOLD CROSS VALIDATION
# ============================================================

balanced_accuracy = cross_val_score(
    balanced_model,
    x_train,
    y_train,
    cv=5,
    scoring="accuracy"
)


balanced_precision = cross_val_score(
    balanced_model,
    x_train,
    y_train,
    cv=5,
    scoring="precision"
)


balanced_recall = cross_val_score(
    balanced_model,
    x_train,
    y_train,
    cv=5,
    scoring="recall"
)


balanced_f1 = cross_val_score(
    balanced_model,
    x_train,
    y_train,
    cv=5,
    scoring="f1"
)


print("\n")
print("==========================================")
print("BALANCED MODEL CROSS VALIDATION")
print("==========================================")


print("\nBalanced Accuracy Scores:")
print(balanced_accuracy)

print("\nMean Balanced Accuracy:")
print(balanced_accuracy.mean())


print("\nBalanced Precision Scores:")
print(balanced_precision)

print("\nMean Balanced Precision:")
print(balanced_precision.mean())


print("\nBalanced Recall Scores:")
print(balanced_recall)

print("\nMean Balanced Recall:")
print(balanced_recall.mean())


print("\nBalanced F1 Scores:")
print(balanced_f1)

print("\nMean Balanced F1:")
print(balanced_f1.mean())


# ============================================================
# 16. FINAL MODEL
# ============================================================

final_model = RandomForestClassifier(
    random_state=42,
    class_weight="balanced"
)


# Train final model on ALL training data

final_model.fit(
    x_train,
    y_train
)


# ============================================================
# 17. FINAL MODEL ON UNSEEN TEST DATA
# ============================================================

test_prediction = final_model.predict(
    x_test
)


print("\n")
print("==========================================")
print("FINAL MODEL - UNSEEN TEST DATA")
print("==========================================")


final_accuracy = accuracy_score(
    y_test,
    test_prediction
)


final_precision = precision_score(
    y_test,
    test_prediction,
    zero_division=0
)


final_recall = recall_score(
    y_test,
    test_prediction,
    zero_division=0
)


final_f1 = f1_score(
    y_test,
    test_prediction,
    zero_division=0
)


print("\nFinal Test Accuracy:")
print(final_accuracy)


print("\nFinal Test Precision:")
print(final_precision)


print("\nFinal Test Recall:")
print(final_recall)


print("\nFinal Test F1 Score:")
print(final_f1)


# ============================================================
# 18. FINAL CONFUSION MATRIX
# ============================================================

final_cm = confusion_matrix(
    y_test,
    test_prediction
)


print("\nFinal Confusion Matrix:")
print(final_cm)


# ============================================================
# 19. FINAL CLASSIFICATION REPORT
# ============================================================

print("\nFinal Classification Report:")

print(
    classification_report(
        y_test,
        test_prediction,
        zero_division=0
    )
)


# ============================================================
# 20. ACTUAL VS PREDICTED CANCER CASES
# ============================================================

print("\nActual Cancer Cases in Test Data:")
print(y_test.sum())


print("\nPredicted Cancer Cases:")
print(test_prediction.sum())


# ============================================================
# 21. COMPLETELY NEW PATIENT
# ============================================================

new_patient = pd.DataFrame([{
    "Age": 58,
    "Tumor_Size_mm": 48.5,
    "Cell_Density": 0.92,
    "Irregularity": 0.88,
    "Marker_Level": 0.97
}])


new_prediction = final_model.predict(
    new_patient
)


print("\n")
print("==========================================")
print("NEW PATIENT PREDICTION")
print("==========================================")


print("\nNew Patient Data:")
print(new_patient)


print("\nNew Patient Prediction:")
print(new_prediction)


if new_prediction[0] == 1:

    print("\nPrediction: Cancer")

else:

    print("\nPrediction: No Cancer")"""