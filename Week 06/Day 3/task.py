import pandas as pd #(dataset)
from sklearn.model_selection import train_test_split #(training and testng)
from sklearn.pipeline import Pipeline  #(complete ML workflow)
from sklearn.compose import ColumnTransformer  #(different colums par different preprocessing)
from sklearn.impute import SimpleImputer #(missing values ky liya)
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report
)

data = pd.read_csv("Week 06/Day 3/loan.csv")
print(data.head(5))
print(data.shape)
print(data.info())
print(data.describe())
print(data.isnull().sum())


x = data.drop("loan_approved", axis=1)
y= data["loan_approved"]

numeric_features=[
    "age",
    "income",
    "experience_years",
    "credit_score",
    "monthly_spending",
    "loan_amount"
]

categorical_features = [
    "education",
    "city",
    "job_type"
]

#now implementing the numerical preprocesing
numeric_pipeline= Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

#now implementing the categorical preprocessing
categorical_pipeline= Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

#now using the column transformer
preprocessor=ColumnTransformer([
    ("numical", numeric_pipeline,numeric_features),
    ("categorical", categorical_pipeline, categorical_features)
])

Pipeline = Pipeline([
    ("preprocessor",preprocessor),
    ("model", LogisticRegression(max_iter=1000))
])

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y   
)

Pipeline.fit(x_train, y_train)

y_pred = Pipeline.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

print("Classification Report:")
print(classification_report(y_test, y_pred))

print("\nLoan Predictions:")

for i in range(5):

    actual = "Loan Approved" if y_test.iloc[i] == 1 else "Loan Not Approved"
    predicted = "Loan Approved" if y_pred[i] == 1 else "Loan Not Approved"

    print(
        f"Applicant {i + 1}: "
        f"Actual = {actual} | "
        f"Predicted = {predicted}"
    )