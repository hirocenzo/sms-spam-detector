import streamlit as st
import joblib
import os

st.set_page_config(page_title="SMS Spam Detector", page_icon="📱", layout="centered")

st.title("📱 SMS Spam Detector")
st.markdown("""
Welcome! Paste any SMS message below and find out if it's **Spam** or **Ham** (not spam).  
Built using a machine learning model trained on real-world SMS data.
""")

# Load model with error handling
pipeline = None
model_path = "spam_pipeline.pkl"
if os.path.exists(model_path):
    pipeline = joblib.load(model_path)
else:
    st.error("🚨 Model file not found! Please ensure 'spam_pipeline.pkl' is present.")

# UI Layout
col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_area("Enter or paste your SMS message:", height=100, help="E.g. 'Congratulations! You've won a free iPhone. Reply WIN to claim.'")

with col2:
    if st.button("Clear Input"):
        st.rerun()

st.markdown("")

if pipeline:
    if st.button("Predict", type="primary"):
        if user_input.strip():
            prediction = pipeline.predict([user_input])[0]
            prob = pipeline.predict_proba([user_input])[0].max()
            label = "🚫 SPAM" if prediction == 1 else "✅ HAM (Not Spam)"
            color = "#ffcccc" if prediction == 1 else "#d2f7c5"
            st.markdown(
                f'<div style="background-color: {color}; padding: 1.5em; border-radius: 10px; text-align: center; font-size: 1.3em;">'
                f'<b>{label}</b><br>'
                f'<span style="font-size:0.9em;">Confidence: {prob:.2%}</span>'
                f'</div>', unsafe_allow_html=True
            )
        else:
            st.warning("Please enter an SMS message to classify.")

    with st.expander("🔎 See Example Messages"):
        st.code("WINNER!! As a valued network customer you have been selected to receive a £900 prize reward!", language="text")
        st.code("Hey, are we still meeting for coffee later?", language="text")

st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; font-size:0.9em; color:gray;'>
    Created by Paul Tristan Dujali. Powered by Streamlit.<br>
    <a href="https://github.com/hirocenzo/sms-spam-detector" target="_blank">View on GitHub</a>
    </div>
    """, unsafe_allow_html=True
)