import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from io import BytesIO
import joblib
import random

# Uygulama ayarları
st.set_page_config(page_title="FreshData", page_icon=":rocket:", layout="wide")

# CSS stil tanımları
st.markdown("""
<style>
body {
  background-image: url('https://r.resimlink.com/USyYKmk.png');  /* New background image */
  background-size: cover;
  background-repeat: no-repeat;  /* Prevent tiling */
  font-family: 'Roboto', sans-serif;
  color: #000080;  /* Dark blue color for text */
}
.stButton>button {
  background-color: #ff6347;
  color: white;
  border-radius: 10px;
  padding: 10px 20px;
  font-size: 16px;
  transition: background-color 0.3s;
}
.stButton>button:hover {
  background-color: #ff4500;
}
.content-box {
  background: rgba(255, 255, 255, 0.8);
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin: 20px 0;
}
.title {  /* Remove background image from title */
  text-align: center;
  font-size: 48px;
  font-weight: bold;
  margin-bottom: 30px;
  padding: 50px;
  border-radius: 15px;
}
.subtitle {
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
""", unsafe_allow_html=True)

# Başlık
st.markdown('<h1 class="title">FreshData İş İlanı Sitesi</h1>', unsafe_allow_html=True)

# ... (rest of your code remains the same)
