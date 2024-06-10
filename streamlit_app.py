import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from io import BytesIO
import joblib
import random
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Uygulama ayarları
st.set_page_config(page_title="FreshData", page_icon=":rocket:", layout="wide")

# CSS stil tanımları
st.markdown(
    """
    <style>
        body {
            background-color: #add8e6; /* Açık mavi */
            font-family: 'Roboto', sans-serif;
        }
        .stButton>button {
            background-color: #000080; /* Koyu mavi */
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #1E90FF; /* Daha koyu mavi */
        }
        .content-box {
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
        }
        .title {
            color: #000080; /* Koyu mavi */
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 30px;
            border-radius: 15px;
        }
        .subtitle {
            color: #333333;
            text-align: center;
            font-size: 24px;
            margin-bottom: 20px;
        }
        .custom-bullet {
            background-color: #f4d03f;
            color: #333;
            padding: 10px;
            border-radius: 50%;
            display: inline-block;
            margin: 0 10px;
        }
        .position-box {
            background-color: #e67e22;
            padding: 10px;
            margin: 5px;
            border-radius: 5px;
            color: white;
            transition: transform 0.3s;
        }
        .position-box:hover {
            transform: scale(1.05);
        }
        .chart-box {
            background: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Başlık
st.markdown('<div style="background-image: url(\'https://r.resimlink.com/USyYKmk.png\'); background-size: cover; padding: 50px; border-radius: 15px;">', unsafe_allow_html=True)
st.markdown('<h1 class="title" style="color: #000080;">FreshData İş İlanı Sitesi</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# GitHub'daki Excel dosyasının URL'si
url = "https://github.com/esrasenakaraaslan/web_sitesi/raw/main/.devcontainer/t%C3%BCm_veriler_d%C3%BCzenlenmi%C5%9F_y%C4%B1ll%C4%B1%20(4).xlsx"

# Excel dosyasını yükleyip okuma
@st.cache_data
def load_data(url):
    response = requests.get(url)
    file = BytesIO(response.content)
    return pd.read_excel(file)

# Veriyi yükle
df = load_data(url)

# Modeli yükle
model = joblib.load("model.joblib")

# Kullanıcı girişleri
konum = st.text_input("Konum")
pozisyon = st.text_input("Pozisyon")

# Kullanıcı girişlerini modele uygun formata dönüştürme
user_input = pd.DataFrame({'Konum': [konum], 'Pozisyon': [pozisyon]})

# One-Hot Encoding
categorical_features = ['Konum', 'Pozisyon']
preprocessor = ColumnTransformer(transformers=[('cat', OneHotEncoder(), categorical_features)], remainder='passthrough')
user_input_encoded = preprocessor.fit_transform(user_input)

# İş bulma ihtimalini tahmin etme
prediction = model.predict_proba(user_input_encoded)[0][1] * 100

# Sonucu gösterme
st.write(f"İş bulma ihtimali: %{prediction:.2f}")
