import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from io import BytesIO
import random

# Uygulama ayarları
st.set_page_config(page_title="FreshData", page_icon=":rocket:", layout="wide")

# CSS stil tanımları
st.markdown(
    """
    <style>
        body {
            background-image: url('https://r.resimlink.com/USyYKmk.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            font-family: 'Roboto', sans-serif;
            color: #ffffff; /* Beyaz metin */
        }
       .stApp {
    background-color: rgba(0, 0, 128, 0); /* Tamamen şeffaf arka plan */
}

        .stButton>button {
            background-color: #FFC0CB; /* Pembiş */
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #FF69B4; /* Daha koyu pembe */
        }
        .content-box {
            background: rgba(0, 0, 128, 0.7); /* Yarı saydam koyu mavi */
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
        }
       .title {
    color: #FFB6C1; /* Tatlış pembiş */
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    margin-bottom: 30px;
    background-color: rgba(255, 182, 193, 0.8); /* Saydam olmayan pembiş arka plan */
    padding: 20px;
    border-radius: 15px;
}

        .subtitle {
            color: #ADD8E6; /* Daha açık mavi */
            text-align: center;
            font-size: 24px;
            margin-bottom: 20px;
        }
        .custom-bullet {
            background-color: #FFC0CB; /* Pembiş */
            color: #333;
            padding: 30px; /* Boyutunu büyüttüm */
            border-radius: 50%;
            display: inline-block;
            margin: 0 10px;
            position: relative;
        }
        .custom-bullet:before {
            content: '✿';
            color: #FFC0CB; /* Çiçek simgesi pembe */
            font-size: 50px;
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 0;
        }
        .custom-bullet span {
            position: relative;
            z-index: 1;
        }
        .position-box {
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
            color: black; /* Grafikler için siyah metin */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Başlık
st.markdown('<h1 class="title">FreshData İş İlanı Sitesi</h1>', unsafe_allow_html=True)

# Örnek içerik
st.markdown('<div class="content-box"><p>Hoş geldiniz! Burada iş ilanlarını bulabilirsiniz.</p></div>', unsafe_allow_html=True)

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
            <span>{len(unique_positions)}</span>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Rastgele renk oluşturucu
    def random_blue_shade():
        blue_shades = [
            '#ADD8E6', '#B0E0E6', '#AFEEEE', '#87CEEB', '#87CEFA', 
            '#00BFFF', '#1E90FF', '#6495ED', '#4682B4', '#4169E1'
        ]
        return random.choice(blue_shades)

    # Pozisyonları göster
    for position in unique_positions:
        color = random_blue_shade()
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
