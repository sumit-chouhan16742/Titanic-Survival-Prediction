# Titanic Survival Prediction

This is a simple machine learning project where I built a model to predict whether a passenger on the Titanic would have survived based on different details like age, gender, passenger class, fare, and family information.

The model is trained using the Titanic dataset from Seaborn and deployed with Streamlit so users can enter passenger details and get a prediction instantly.

---

## Features

- Predicts passenger survival
- Simple and interactive Streamlit interface
- Uses a trained Random Forest model
- Easy to run locally

---

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle

---

## Project Structure

```
Titanic-Survival-Prediction/
│
├── app.py
├── titanic_model.pkl
├── titanic.ipynb
├── requirements.txt
└── README.md
```

---

## How to Run

1. Clone the repository

```bash
git clone <your-repository-link>
```

2. Go to the project folder

```bash
cd Titanic-Survival-Prediction
```

3. Install the required libraries

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## Model Details

The project uses a **Random Forest Classifier** trained on the Titanic dataset after preprocessing and encoding the required features.

The prediction is based on:

- Passenger Class
- Gender
- Age
- Fare
- Number of Siblings/Spouses
- Number of Parents/Children
- Embarked Port
- Adult Male
- Travelling Alone
- Passenger Type

---

## Learning Outcome

This project helped me understand the complete machine learning workflow, including:

- Data preprocessing
- Feature encoding
- Model training
- Saving the trained model
- Building a simple web app using Streamlit

---

## Note

This project was built for learning and practice purposes.