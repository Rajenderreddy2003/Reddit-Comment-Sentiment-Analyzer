import streamlit as st
import pickle
import os

# Load the pipeline
model_path = "text_pipeline.pkl"
if not os.path.exists(model_path):
    st.error("Model file text_pipeline.pkl not found.")
    st.stop()

with open(model_path, 'rb') as file:
    pipeline = pickle.load(file)

# ---------------------
# Streamlit UI Elements
# ---------------------

st.title("Reddit Comment Sentiment Analyzer")
st.markdown("""
### 📌 Project Title:
**Reddit Sentiment Analysis using Machine Learning**

### 🧠 Problem Statement:
In today's digital age, understanding public sentiment on social media platforms like Reddit is critical for gaining insights into public opinion. This project aims to automatically classify Reddit comments as **Positive**, **Negative**, or **Neutral** using machine learning.

### 🛠 What Was Done:
- **Web Scraping**: Collected Reddit comments using Reddit API
- **Text Preprocessing**: Cleaned text (removed URLs, special characters, etc.)
- **Feature Extraction**: TF-IDF Vectorization
- **Balancing**: Used SMOTE to handle class imbalance
- **Modeling**: Built and evaluated multiple ML models

### 🧪 Model Selection:
Tested several models:
- Decision Tree
- Random Forest
- Support Vector Classifier (SVC)
- Logistic Regression ✅ (Best Accuracy)

➡️ Logistic Regression was chosen for the final model as it outperformed others in terms of accuracy and generalization.

---
""")

# Prediction Section
st.header("🔮 Try It Yourself!")
user_input = st.text_area("Enter a Reddit comment here:", height=150)

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a comment before predicting.")
    else:
        prediction = pipeline.predict([user_input])[0]
        st.success(f"Predicted Sentiment: **{prediction.capitalize()}**")
