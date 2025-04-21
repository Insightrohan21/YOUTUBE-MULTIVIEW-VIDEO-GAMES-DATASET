import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("yt_multiview_model.pkl")

st.title("🎮 YouTube Video Views Predictor")

# Input fields
likes = st.slider("Likes", 0, 10000, 1000)
dislikes = st.slider("Dislikes", 0, 1000, 100)
comments = st.slider("Comments", 0, 3000, 300)
duration = st.slider("Duration (minutes)", 1.0, 60.0, 10.0)

category = st.selectbox("Game Category", ['Action', 'Sports', 'Puzzle', 'Strategy'])
view_type = st.selectbox("View Type", ['Single View', 'Split View', 'Third-person'])

# Manual one-hot encoding for categories
input_data = {
    'likes': likes,
    'dislikes': dislikes,
    'comments': comments,
    'duration': duration,
    'category_Sports': int(category == 'Sports'),
    'category_Puzzle': int(category == 'Puzzle'),
    'category_Strategy': int(category == 'Strategy'),
    'multiview_type_Split View': int(view_type == 'Split View'),
    'multiview_type_Third-person': int(view_type == 'Third-person'),
}

input_array = np.array([list(input_data.values())])

if st.button("Predict Views"):
    prediction = model.predict(input_array)
    st.success(f"Estimated Views: {int(prediction[0]):,}")
