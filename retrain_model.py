import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# Load dataset
df = pd.read_csv("insurance.csv")

# Drop any nulls
df.dropna(inplace=True)

# Features and target
X = df.drop(['claim'], axis=1)
y = df['claim']

# Preprocessing
categorical_cols = ['gender', 'diabetic', 'smoker', 'region']
numerical_cols = ['age', 'bmi', 'bloodpressure', 'children']

# Define transformers
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numerical_transformer, numerical_cols),
    ('cat', categorical_transformer, categorical_cols)
])

# Final pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

# Train
pipeline.fit(X, y)

# Save
joblib.dump(pipeline, "insurance.pkl")
print("✅ Model retrained and saved as insurance.pkl")
