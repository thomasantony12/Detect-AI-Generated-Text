import streamlit as st
import joblib


# Load the trained model and vectorizer
model = joblib.load('./Model/Jupyter files/models/ai_text_detector.pkl')
vectorizer = joblib.load('./Model/Jupyter files/models/vectorizer.pkl')

def predict_text_type(text):
    # Transform the text using the vectorizer
    text_vectorized = vectorizer.transform([text])
    
    # Predict using the loaded model
    prediction = model.predict(text_vectorized)
    
    # Interpret the result
    result = 'AI-generated' if prediction[0] == 1 else 'Human-written'
    return result

if st.button("LogOut"):
    st.switch_page("./login.py")
st.title("Ai Text Detection")
st.subheader("Enter your desired text", divider=True)
in_text = st.text_area(label="")

if st.button("Recognize"):
    out_text = predict_text_type(in_text)
    st.divider()
    st.header(out_text)