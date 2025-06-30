# 🍽️ Restaurant Review Sentiment Analyzer

This is a simple web app that allows users to enter restaurant reviews and classifies them as **Positive** or **Negative** using NLP and Machine Learning. Reviews and predictions are stored in an SQLite database.

## 🔧 Features

- Text preprocessing using NLTK
- Sentiment classification (Naive Bayes)
- SQLite DB to store reviews
- Streamlit-based interactive frontend

## 🚀 Run Locally

```bash
git clone https://github.com/mihirjain4/Restaurant-Review--analysis-.git
cd restaurant-review-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
