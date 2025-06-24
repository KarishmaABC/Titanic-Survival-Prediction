import pandas as pd
import streamlit as st
import pickle

# Load model and columns
model = pickle.load(open('model.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

st.title('Titanic Survival Predictor')

# Input fields
Pclass = st.selectbox('Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)', [1, 2, 3])
Sex = st.selectbox('Sex', ['male', 'female'])
Age = st.slider('Age', 0, 100, 25)
Fare = st.slider('Fare', 0, 500, 50)
Embarked = st.selectbox('Port of Embarkation', ['C', 'Q', 'S'])

# Convert inputs to DataFrame
input_df = pd.DataFrame([{
    'Pclass': Pclass,
    'Age': Age,
    'Fare': Fare,
    'Sex_male': 1 if Sex == 'male' else 0,
    'Embarked_Q': 1 if Embarked == 'Q' else 0,
    'Embarked_S': 1 if Embarked == 'S' else 0
}], columns=columns)

# Prediction
if st.button('Predict'):
    result = model.predict(input_df)
    st.success('Survived' if result[0] == 1 else 'Did Not Survive')
