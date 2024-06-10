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
st.markdown(
    """
    <style>
        body {
            background-color: #b3d9ff;
            background-image: radial-gradient(circle, #9b59b6 10%, transparent 10%),
                              radial-gradient(circle, #9b59b6 10%, transparent 10%);
            background-size: 50px 50px;
            background-position: 0 0, 25px 25px;
            background-attachment: fixed;
            height: 100%;
            margin: 0;
            overflow: hidden;
        }
        .stButton>button {
            background-color: #9b59b6;
            color: #f4d03f;
        }
        .stButton>button div div {
            color: #f4d03f;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Başlık
st.markdown('<h1 style="color: #9b59b6; text-align: center;">FreshData İş İlanı Sitesi</h1>', unsafe_allow_html=True)

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
st.write("Dosya İçeriği:")
st.write(df)

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
        <div style="position: absolute; width: 50px; height: 50px; background: #e67e22; border-radius: 50%; bottom: 0; left: 50%; transform: translate(-50%, 50%);"></div>
        <div style="position: absolute; width: 50px; height: 50px; background: #e67e22; border-radius: 50%; top: 25%; left: 25%; transform: translate(-50%, -50%);"></div>
        <div style="position: absolute; width: 50px; height: 50px; background: #e67e22; border-radius: 50%; top: 25%; right: 25%; transform: translate(50%, -50%);"></div>
        <div style="position: absolute; width: 50px; height: 50px; background: #e67e22; border-radius: 50%; bottom: 25%; left: 25%; transform: translate(-50%, 50%);"></div>
        <div style="position: absolute; width: 50px; height: 50px; background: #e67e22; border-radius: 50%; bottom: 25%; right: 25%; transform: translate(50%, 50%);"></div>
    </div>
    ''', unsafe_allow_html=True)

    # Rastgele renk oluşturucu
    def random_color():
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

    # Pozisyonları göster
    for position in unique_positions:
        color = random_color()
        st.markdown(f'<div style="background-color: {color}; padding: 10px; margin: 5px; border-radius: 5px; color: white;">{position}</div>', unsafe_allow_html=True)

if st.button("Türkiye'nin Geldiği Son Nokta", key="son_nokta_button"):
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Burada Türkiye\'nin geldiği son noktayla ilgili bilgiler yer alacak.</p></div>', unsafe_allow_html=True)

if st.button("Analiz"):
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Burada veri analizi işlevi gelecek.</p></div>', unsafe_allow_html=True)

if st.button("Grafikler"):
    st.write("Grafikler")

    # Konum Grafiği
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Konum sütununda en çok tekrar eden 5 konum</p></div>', unsafe_allow_html=True)
    top_locations = df['Konum'].value_counts().head(5)
    st.bar_chart(top_locations)

    # Çalışma Şekli Grafiği
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Çalışma şekli sütunu</p></div>', unsafe_allow_html=True)
    calisma_sekli_sayilari = df['çalışma şekli'].value_counts()
    st.bar_chart(calisma_sekli_sayilari)

    # Pozisyon Grafiği
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Pozisyon sütununda en çok tekrar eden 5 pozisyon</p></div>', unsafe_allow_html=True)
    top_positions = df['Pozisyon'].value_counts().head(5)
    st.bar_chart(top_positions)
