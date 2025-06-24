
# 🚢 Titanic Survival Prediction 🎯

A machine learning project to predict whether a passenger survived the Titanic disaster using real-world data from the [Kaggle Titanic Competition](https://www.kaggle.com/competitions/titanic).

---

## 📊 Overview

This project demonstrates a full ML pipeline:
- 📌 Data Cleaning & EDA
- 🧠 Feature Engineering
- 🔍 Model Training & Evaluation
- 🖥️ Streamlit Web App for Predictions

---

## 🧠 How It Works

The model predicts survival based on:
- Passenger Class (`Pclass`)
- Gender (`Sex`)
- Age
- Ticket Fare
- Port of Embarkation (`Embarked`)

🎓 Trained using **RandomForestClassifier** to learn from historical data:
- Women and children were more likely to survive
- First-class passengers had higher survival rates

---

## 🛠 Project Structure

```
titanic-survival-prediction/
├── data/
│   ├── train.csv
│   └── test.csv
├── model.pkl
├── columns.pkl
├── app.py                  # Streamlit app
├── train_and_save_model.py # Train & save model
├── Titanic_Survival_Prediction_Complete.ipynb
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 2️⃣ Train the Model

```bash
python train_and_save_model.py
```

### 3️⃣ Run the Web App

```bash
streamlit run app.py
```

---

## 🔍 Example Input for Prediction

```json
{
  "Pclass": 3,
  "Age": 22,
  "Fare": 7.25,
  "Sex_male": 1,
  "Embarked_Q": 0,
  "Embarked_S": 1
}
```

📌 Output: `0 = Did Not Survive`, `1 = Survived`

---

## 🧠 Model Info

- **Model:** Random Forest Classifier
- **Accuracy:** ~82% on validation set
- **Cross-validation:** 5-fold

---

## 🌐 Live Prediction Interface

Using Streamlit, users can input data and instantly receive predictions:
- Select class, age, gender, fare, and port
- One-click prediction interface
- Clean UI, deployable on Streamlit Cloud

---
![Screenshot (196)](https://github.com/user-attachments/assets/0c789181-8584-4e27-8513-f8ab040adbd3)



## 👩‍💻 Author

**Karishma Shinde**  
AI & Data Science Enthusiast  
📧 karishmashinde8010@gmail.com

---

## 📄 License

MIT License — Feel free to use, modify, and share!
