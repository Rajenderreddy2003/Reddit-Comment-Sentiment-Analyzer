# Reddit Comment Sentiment Analyzer 🧠💬

This project is an end-to-end **Sentiment Analysis** application that analyzes Reddit comments and classifies them as **Positive**, **Negative**, or **Neutral**. Built using **Natural Language Processing (NLP)** and **Machine Learning**, the model is deployed as an interactive web app using **Streamlit** and hosted on **Hugging Face Spaces**.

## 🚀 Live Demo

🔗 [Click here to try the live app](https://huggingface.co/spaces/Rajenderreddy2003/Reddit-Comment-Sentiment-Analyzer)

---

## 📝 Problem Statement

Online platforms like Reddit are filled with user opinions that range across various emotions. Manually moderating or analyzing such data is tedious and inefficient. This project automates the process by classifying comments into three sentiment categories:

* **Positive**
* **Negative**
* **Neutral**

---

## 📂 Dataset

* Scraped Reddit comments using APIs and web scraping.
* Cleaned and preprocessed text data.
* Target variable: `sentiment` (categorical)

---

## ⚙️ Technologies Used

| Category         | Tools / Libraries                                                                 |
| ---------------- | --------------------------------------------------------------------------------- |
| Programming      | Python                                                                            |
| NLP              | `re`, `nltk`, `sklearn.feature_extraction.text.TfidfVectorizer`                   |
| Machine Learning | `sklearn` (LogisticRegression, DecisionTree, RandomForest, SVC), `imblearn.SMOTE` |
| Deployment       | `Streamlit`, `Hugging Face Spaces`                                                |

---

## 📊 Model Building

* Applied preprocessing (removing URLs, punctuations, special characters).
* Used **TF-IDF Vectorization** to convert text to numeric features.
* Handled class imbalance with **SMOTE (Synthetic Minority Oversampling Technique)**.
* Experimented with various classifiers:

  * Decision Tree
  * Random Forest
  * SVC
  * Logistic Regression ✅ *(Best performing model)*
* Created and saved the final model pipeline using `pickle`.

---

## 🧪 Evaluation

| Model              | Accuracy |
| ------------------ | -------- |
| LogisticRegression | ✅ Best   |
| Decision Tree      | Lower    |
| Random Forest      | Lower    |
| SVC                | Lower    |

---

## 💻 App Interface (Streamlit)

* Simple and intuitive UI.
* User inputs a Reddit comment.
* The app returns the predicted sentiment instantly.

---

## 🧠 What I Learned

* Real-world application of NLP
* Handling class imbalance with SMOTE
* Building and saving ML pipelines
* Model comparison and selection
* Streamlit deployment and UI integration
* Hosting on Hugging Face Spaces

---


## 📁 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/Reddit-Comment-Sentiment-Analyzer.git

# 2. Navigate to the project directory
cd Reddit-Comment-Sentiment-Analyzer

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

---

## 📌 Future Enhancements

* Use deep learning models like BERT
* Include sarcasm detection
* Improve neutral class predictions
* Allow batch comment predictions

---

## 📬 Contact

Made with ❤️ by **Rajender Reddy**
🔗 [LinkedIn](https://www.linkedin.com/in/rajenderreddy2003)
---
