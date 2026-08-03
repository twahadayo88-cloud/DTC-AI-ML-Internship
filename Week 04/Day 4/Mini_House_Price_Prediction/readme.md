# 🏡 House Price Prediction using Machine Learning

A complete Machine Learning mini project developed as part of my "AI & Machine Learning Internship. This project demonstrates the complete workflow of building a predictive model for house prices, starting from raw data cleaning to model training, evaluation, and comparison.

---

# 📌 Project Overview

The objective of this project is to predict house prices using different machine learning algorithms and compare their performance.

The project follows a complete Machine Learning pipeline including:

- Data Loading
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Encoding
- Train-Test Split
- Model Training
- Model Prediction
- Model Evaluation
- Performance Comparison
- Exporting Results

---

# 📂 Project Structure

House_Price_Prediction/
│
├── images/
│   ├── price_distribution.png
│   ├── residential_area_vs_price.png
│   ├── rooms_vs_price.png
│   ├── crime_rate_vs_price.png
│   └── correlation_matrix.png
│
├── house_price_raw.csv
├── comparison_results.csv
├── practical.py
├── README.md
└── requirements.txt


# 🛠 Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn


# 📚 Python Libraries

python
pandas
matplotlib
scikit-learn
os


Install the required libraries:

bash
"""pip install pandas matplotlib scikit-learn




# 📊 Dataset

The dataset contains information about houses including various features such as:

- Crime Rate
- Residential Area
- Number of Rooms
- Airport Availability
- Bus Terminal Availability
- Waterbody
- Price

Target Variable:


price

---

# ⚙️ Project Workflow

## 1️⃣ Load Dataset

The dataset is loaded using Pandas.

```python
df = pd.read_csv("house_price_raw.csv")
```

---

## 2️⃣ Data Exploration

Basic information is displayed:

- First Five Rows
- Dataset Shape
- Data Types
- Statistical Summary
- Missing Values
- Duplicate Rows

---

## 3️⃣ Data Cleaning

The project performs:

- Remove Duplicate Rows
- Fill Missing Numeric Values using Mean
- Fill Missing Categorical Values using Mode

---

## 4️⃣ Exploratory Data Analysis (EDA)

Several visualizations are created to understand the data.

### ✔ Price Distribution

Shows how house prices are distributed.

---

### ✔ Residential Area vs Price

Analyzes relationship between residential area and price.

---

### ✔ Rooms vs Price

Shows how the number of rooms affects house prices.

---

### ✔ Crime Rate vs Price

Analyzes whether crime rate impacts house prices.

---

### ✔ Correlation Matrix

Displays relationships between all numerical features.

---

# 🖼 Generated Charts

The following charts are automatically generated and saved:

- price_distribution.png
- residential_area_vs_price.png
- rooms_vs_price.png
- crime_rate_vs_price.png
- correlation_matrix.png

---

# 🔄 Data Preprocessing

Categorical variables are converted into numerical values.

### Label Encoding

```
Airport

YES → 1

NO → 0
```

```
Bus Terminal

YES → 1

NO → 0
```

### One Hot Encoding

```
Waterbody
```

is converted into multiple binary columns using:

```python
pd.get_dummies()
```

---

# 🎯 Feature Selection

Features (X):

All columns except:

```
price
```

Target (y):

```
price
```

---

# ✂️ Train Test Split

Dataset is divided into:

- 80% Training Data
- 20% Testing Data

```python
train_test_split(
    test_size=0.20,
    random_state=42
)
```

---

# 🤖 Machine Learning Models

## 1. Linear Regression

A Linear Regression model is trained to predict house prices.

```python
LinearRegression()
```

---

## 2. Decision Tree Regressor

A Decision Tree model is also trained.

```python
DecisionTreeRegressor()
```

---

# 📈 Model Prediction

Both models generate predictions for the testing dataset.

Example:

```
Actual Price

Linear Prediction

Tree Prediction
```

---

# 📊 Model Evaluation

The project compares both models using:

```
Model Score (R² Score)
```

The model with the better score is selected as the better-performing model.

---

# 💾 Output Files

The project automatically generates:

```
comparison_results.csv
```

This file contains:

- Actual Price
- Linear Regression Prediction
- Decision Tree Prediction

---

# 🚀 Features of this Project

✔ Data Cleaning

✔ Missing Value Handling

✔ Duplicate Removal

✔ Exploratory Data Analysis

✔ Data Visualization

✔ Correlation Analysis

✔ Feature Encoding

✔ Train-Test Split

✔ Linear Regression

✔ Decision Tree Regression

✔ Prediction

✔ Model Evaluation

✔ CSV Export

---

# ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/House_Price_Prediction.git
```

Go to the project folder:

```bash
cd House_Price_Prediction
```

Install dependencies:

```bash
pip install pandas matplotlib scikit-learn
```

Run the project:

```bash
python practical.py
```

---

# 📸 Sample Output

The program displays:

- Dataset Information
- Missing Values
- Data Cleaning Results
- Correlation Matrix
- Model Predictions
- Comparison Table
- Linear Regression Score
- Decision Tree Score
- Best Performing Model

It also saves:

- Five Graph Images
- Comparison CSV File

---

# 🎯 Learning Outcomes

Through this project, I learned how to:

- Load real-world datasets
- Clean and preprocess data
- Handle missing values
- Remove duplicate records
- Perform Exploratory Data Analysis (EDA)
- Create data visualizations using Matplotlib
- Encode categorical features
- Split data into training and testing sets
- Train Machine Learning models
- Compare multiple algorithms
- Evaluate model performance
- Export prediction results

---

# 👨‍💻 Author

**Muhammad Twaha**

AI & Machine Learning Intern

BS Computer Science Student

Passionate about Artificial Intelligence, Machine Learning, Data Science, and Full Stack Development.

---

# ⭐ If you found this project helpful, don't forget to give it a Star!