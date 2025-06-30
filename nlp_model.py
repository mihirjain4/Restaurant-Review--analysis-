# nlp_model.py

import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from utils import clean_text  # ✅ Use external utility

def train_model():
    data = {
        "Review": [
            "I love the food here!", 
            "Terrible service and bad food.",
            "The ambience is great", 
            "I will never come back", 
            "Delicious and satisfying"
        ],
        "Sentiment": [1, 0, 1, 0, 1]
    }
    df = pd.DataFrame(data)
    df["Cleaned"] = df["Review"].apply(clean_text)

    X = df["Cleaned"]
    y = df["Sentiment"]

    pipeline = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('classifier', MultinomialNB())
    ])

    pipeline.fit(X, y)

    with open("sentiment_model.pkl", "wb") as f:
        pickle.dump(pipeline, f)

def predict_sentiment(text):
    with open("sentiment_model.pkl", "rb") as f:
        model = pickle.load(f)
    cleaned = clean_text(text)
    prediction = model.predict([cleaned])[0]
    return int(prediction)
