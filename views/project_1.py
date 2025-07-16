import streamlit as st
import os

# ------------------- PAGE TITLE -------------------
st.title("📉 Customer Churn Classification using ANN")

# ------------------- PROJECT DESCRIPTION -------------------
st.markdown("""
This project predicts whether a customer is likely to churn (leave the service) using an **Artificial Neural Network (ANN)**.

It is trained on a structured dataset with features like credit score, geography, age, tenure, balance, etc.  
The ANN is built using **Keras (TensorFlow backend)** and deployed with **Streamlit Cloud** for real-time prediction.
""")

# ------------------- TOOLS USED -------------------
st.markdown("### 🛠 Tools & Libraries Used")
st.markdown("""
- Python  
- pandas, numpy  
- scikit-learn for preprocessing  
- TensorFlow & Keras for model building  
- Streamlit for web app deployment  
""")

# ------------------- MODEL OVERVIEW -------------------
st.markdown("### 🧠 Model Architecture")
st.markdown("""
- **Input Layer:** 11 input features  
- **Hidden Layers:** 2 Dense layers (ReLU activation)  
- **Output Layer:** Sigmoid activation (binary classification)  
- **Loss Function:** Binary Crossentropy  
- **Optimizer:** Adam  
""")

# ------------------- GITHUB REPO -------------------
st.markdown("### 🔗 GitHub Repository")
st.markdown("""
[![GitHub](https://img.shields.io/badge/View_on-GitHub-black?logo=github)](https://github.com/code-with-krish/ANN-Classification-in-Churn)
""", unsafe_allow_html=True)

# ------------------- LIVE STREAMLIT APP -------------------
st.markdown("### 🚀 Live Streamlit App")
st.markdown("""
[![Open in Streamlit](https://img.shields.io/badge/Open_App-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://ann-classification-in-churn.streamlit.app)
""", unsafe_allow_html=True)

# ------------------- SCREENSHOT (OPTIONAL) -------------------
# Option 1: Use relative path if image is inside project folder
image_path = "assets/Customer_Churn_Prediction_Models_in_Machine_Learning.png"

# Option 2: Use absolute path if outside project folder
# image_path = r"F:\STREAMLIT\assets\Customer_Churn_Prediction_Models_in_Machine_Learning.png"

if os.path.exists(image_path):
    st.image(image_path, caption="Deployed Churn Classifier App", use_container_width=True)
else:
    st.warning(f"⚠️ Image not found at: {image_path}")

