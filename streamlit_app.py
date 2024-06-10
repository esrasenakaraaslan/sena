[16:04, 10.06.2024] ‘reyyan: import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from io import BytesIO
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import random
import joblib


# Uygulama ayarları
st.set_page_config(page_title="FreshData", page_icon=":rocket:", layout="wide")
# CSS stil tanımları
st.markdown(
    """
    <style>
        /* Arka plan rengi ve mor yuvarlaklar */
        body {
            background-color: #b3d9ff; /* Tatlı mavi renk */
            background-image: radial-gradient(circle, #9b59b6 10%, transparent 10%), 
                              radial-gradient(circle, #9b59b6 10%, transparent 10%);
            background-size: 50px 50px;
            background-position: 0 0, 25px 25px;
            background-attachment: fixed;
            height: 100%;
            margin: 0;
            overflow: hidden;
        }
        /* Butonların rengi */
        .stButton>button {
            background-color: #9b59b6; /* Mor renk */
            color: #f4d03f; /* Sarı renk */
        }
        /* Butonların üstündeki metin rengi */
        .stButton>button div div {
            color: #f4d03f; /* Sarı renk */
        }
    </style>
    """,
    unsafe_allow_html=True
)
# Başlık
st.markdown('<h1 style="color: #9b59b6; text-align: center;">FreshData İş İlanı Sitesi</h1>', unsafe_allow_html=True)

# GitHub'daki Excel dosyasının URL'si
url = "https://github.com/esrasenakaraaslan/web_sitesi/raw/main/.devcontainer/t%C3%BCm_veriler_d%C3%BCzenlenmi%C5%9F_y%C4%B1ll%C4%B1%20(4).xlsx"
response = requests.get(url)
file = BytesIO(response.content)

# Excel dosyasını yükleyip okuma
@st.cache_data
def load_data(url):
    return pd.read_excel(url)

# Veriyi yükle
df = load_data(url)

# Streamlit ile veriyi görüntüleme
st.write("Dosya İçeriği:")
st.write(df)
import random

# Meslek Grupları butonunun durumunu takip eden bir oturum durumu (session state) belirle
if 'meslek_gruplari_acik' not in st.session_state:
    st.session_state.meslek_gruplari_acik = False

# Meslek Grupları butonuna tıklama durumu
if st.button("Meslek Grupları", key="meslek_grupları_button"):
    st.session_state.meslek_gruplari_acik = not st.session_state.meslek_gruplari_acik

# Meslek Grupları durumuna göre içeriği göster veya gizle
if st.session_state.meslek_gruplari_acik:
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Meslek Grupları</p></div>', unsafe_allow_html=True)
    
    # Veri setinden pozisyonları al ve benzersiz olanları seç
    unique_positions = df['Pozisyon'].unique()

    # Meslek gruplarının sayısını çiçek şeklinde gösteren başlık
    st.markdown(f'''
    <div style="position: relative; width: 200px; height: 200px; margin: 20px auto;">
        <div style="position: absolute; width: 100px; height: 100px; background: #e67e22; border-radius: 50%; top: 50%; left: 50%; transform: translate(-50%, -50%); display: flex; align-items: center; justify-content: center; color: white; font-size: 24px;">
            {len(unique_positions)}
        </div>
        <div style="position: absolute; width: 50px; height: 50px; background: #e67e22; border-radius: 50%; top: 0; left: 50%; transform: translate(-50%, -50%);"></div>
        <div style="position: absolute; width: 50px; height: 50px; background: #e67e22; border-radius: 50%; top: 50%; left: 0; transform: translate(-50%, -50%);"></div>
        <div style="position: absolute; width: 50px; height: 50px; background: #e67e22; border-radius: 50%; top: 50%; right: 0; transform: translate(50%, -50%);"></div>
        <div style="position: absolute; width: 50px; height: 50px; background: #e67e22; border-radius: 50%; bottom: 0; left: 5…
[16:42, 10.06.2024] ‘reyyan: import streamlit as st
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
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #8360c3, #2ebf91);
            font-family: 'Roboto', sans-serif;
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
        .title {
            color: #ffffff;
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 30px;
            background-image: url('https://r.resimlink.com/USyYKmk.png'); /* Görsel URL'si */
            background-size: cover;
            background-position: center;
            padding: 50px;
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
st.markdown('<h1 class="title">FreshData İş İlanı Sitesi</h1>', unsafe_allow_html=True)

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

# Veriyi görüntüleme
st.markdown('<div class="content-box">', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">Dosya İçeriği:</h2>', unsafe_allow_html=True)
st.write(df)
st.markdown('</div>', unsafe_allow_html=True)

# Meslek Grupları butonunun durumunu takip eden bir oturum durumu (session state) belirle
if 'meslek_gruplari_acik' not in st.session_state:
    st.session_state.meslek_gruplari_acik = False

# Meslek Grupları butonuna tıklama durumu
if st.button("Meslek Grupları", key="meslek_grupları_button"):
    st.session_state.meslek_gruplari_acik = not st.session_state.meslek_gruplari_acik

# Meslek Grupları durumuna göre içeriği göster veya gizle
if st.session_state.meslek_gruplari_acik:
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.markdown('<h2 class="subtitle">Meslek Grupları</h2>', unsafe_allow_html=True)

    # Veri setinden pozisyonları al ve benzersiz olanları seç
    unique_positions = df['Pozisyon'].unique()

    # Meslek gruplarının sayısını çiçek şeklinde gösteren başlık
    st.markdown(f'''
    <div style="position: relative; width: 200px; height: 200px; margin: 20px auto;">
        <div class="custom-bullet">
            {len(unique_positions)}
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Rastgele renk oluşturucu
    def random_color():
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

    # Pozisyonları göster
    for position in unique_positions:
        color = random_color()
        st.markdown(f'<div class="position-box" style="background-color: {color};">{position}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if st.button("Türkiye'nin Geldiği Son Nokta", key="son_nokta_button"):
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.markdown('<h2 class="subtitle">Türkiye\'nin Geldiği Son Nokta</h2>', unsafe_allow_html=True)
    st.markdown('<p>Burada Türkiye\'nin geldiği son noktayla ilgili bilgiler yer alacak.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if st.button("Analiz"):
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.markdown('<h2 class="subtitle">Analiz</h2>', unsafe_allow_html=True)
    st.markdown('<p>Burada veri analizi işlevi gelecek.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if st.button("Grafikler"):
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.markdown('<h2 class="subtitle">Grafikler</h2>', unsafe_allow_html=True)

    # Konum Grafiği
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<h3>Konum sütununda en çok tekrar eden 5 konum</h3>', unsafe_allow_html=True)
    top_locations = df['Konum'].value_counts().head(5)
    st.bar_chart(top_locations)
    st.markdown('</div>', unsafe_allow_html=True)

    # Çalışma Şekli Grafiği
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<h3>Çalışma şekli sütunu</h3>', unsafe_allow_html=True)
    calisma_sekli_sayilari = df['çalışma şekli'].value_counts()
    st.bar_chart(calisma_sekli_sayilari)
    st.markdown('</div>', unsafe_allow_html=True)

    # Pozisyon Grafiği
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<h3>Pozisyon sütununda en çok tekrar eden 5 pozisyon</h3>', unsafe_allow_html=True)
    top_positions = df['Pozisyon'].value_counts().head(5)
    st.bar_chart(top_positions)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
