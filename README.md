# 📱 SMS Spam Detector

A modern web app for detecting SMS spam using machine learning.  
Built with [Streamlit](https://streamlit.io/), this app classifies text messages as **Spam** or **Ham** (not spam) in real time, based on a model trained on thousands of real-world SMS messages.

---

## 🚀 Features

- **Easy-to-use interface:** Just paste any SMS message and get instant results.
- **Machine learning powered:** Utilizes a Naive Bayes classifier with TF-IDF text features.
- **Confidence score:** See how sure the model is about each prediction.
- **Responsive UI:** Clean layout, suitable for both desktop and mobile.
- **Example messages:** Test the app with real-world SMS examples.

---

## 📸 App Screenshot

![SMS Spam Detector Screenshot](screenshot.png)

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/hirocenzo/sms-spam-detector.git
cd sms-spam-detector
```

### 2. (Recommended) Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model (Optional)

If `spam_pipeline.pkl` is not included or you want to retrain:

```bash
python train_model.py
```

### 5. Run the App

```bash
streamlit run app.py
```

Open the provided local URL in your browser (usually http://localhost:8501).

---

## 🌐 Deploying Online

Deploy this app publicly with [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push your code and all required files (including `spam_pipeline.pkl`) to a public GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your repo.
3. Deploy following the prompts—your app will be live and shareable.

---

## 📂 Project Structure

```
sms-spam-detector/
├── app.py                # Main Streamlit app
├── train_model.py        # Script to train and export the ML model
├── requirements.txt      # List of dependencies
├── spam_pipeline.pkl     # Pre-trained ML model (binary)
├── screenshot.png        # App screenshot
├── README.md             # This file
└── venv/                 # (Optional) Virtual environment folder
```

---

## ✏️ Example SMS Messages

Test your app with these examples:

- `WINNER!! As a valued network customer you have been selected to receive a £900 prize reward!`
- `Hey, are we still meeting for coffee later?`

---

## 🙏 Credits

- SMS Spam dataset: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)
- App author: Paul Tristan Dujali ([hirocenzo on GitHub](https://github.com/hirocenzo))

---

## 📄 License

This project is for educational purposes and demonstration.  
You are free to fork, modify, and use for non-commercial projects.

---
