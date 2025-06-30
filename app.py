# main.py

import streamlit as st
from nlp_model import predict_sentiment, train_model
from database import create_table, insert_review, view_reviews

# Train model once
train_model()
create_table()

st.set_page_config(page_title="Restaurant Review Analyzer", page_icon="🍽️")
st.title("🍽️ Restaurant Review Sentiment Analyzer")

menu = ["Add Review", "View Reviews"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Review":
    st.subheader("📝 Enter Your Review")
    review = st.text_area("Write your restaurant experience here:")

    if st.button("Analyze & Save"):
        if review.strip():
            prediction = predict_sentiment(review)
            sentiment_text = "Positive 😊" if prediction == 1 else "Negative 😞"
            insert_review(review, prediction)
            st.success(f"Sentiment: {sentiment_text}")
        else:
            st.warning("Please enter a review before submitting.")

elif choice == "View Reviews":
    st.subheader("📋 All Stored Reviews")
    data = view_reviews()
    if data:
        for row in data:
            st.write(f"📝 **Review:** {row[1]}")
            st.write(f"🔎 **Sentiment:** {'Positive 😊' if row[2] == 1 else 'Negative 😞'}")
            st.markdown("---")
    else:
        st.info("No reviews yet.")
