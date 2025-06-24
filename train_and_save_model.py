import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Step 1: Load data
df = pd.read_csv('data/train.csv')

# Step 2: Fill missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Step 3: Feature selection
features = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']
df = df[features + ['Survived']]

# Step 4: Encode categorical features
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# Step 5: Split into features and target
X = df.drop('Survived', axis=1)
y = df['Survived']

# Save column names (for Streamlit or API use)
columns = X.columns.tolist()

# Step 6: Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Step 7: Save model and columns
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('columns.pkl', 'wb') as f:
    pickle.dump(columns, f)

print("✅ Model and columns saved as 'model.pkl' and 'columns.pkl'")
