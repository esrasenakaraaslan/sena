import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import requests
from io import BytesIO

# Uygulama ayarları
st.set_page_config(page_title="FreshData", page_icon=":rocket:", layout="wide")

# CSS stil tanımları
st.markdown(
    """
    <style>
        /* Arka plan rengi */
        body {
            background-color: #3498db; /* Mavi renk */
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
@st.cache
def load_data(url):
    return pd.read_excel(url)

# Veriyi yükle
df = load_data(url)

# Streamlit ile veriyi görüntüleme
st.write("Dosya İçeriği:")
st.write(df)

# İşlev butonları ve içerikleri
if st.button("İş Bul", key="iş_bul_button"):
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Burada iş bulma işlevi gelecek.</p></div>', unsafe_allow_html=True)

if st.button("Meslek Grupları", key="meslek_grupları_button"):
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Burada meslek gruplarına göre iş arama işlevi gelecek.</p></div>', unsafe_allow_html=True)

if st.button("Türkiye'nin Geldiği Son Nokta", key="son_nokta_button"):
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Burada Türkiye\'nin geldiği son noktayla ilgili bilgiler yer alacak.</p></div>', unsafe_allow_html=True)

if st.button("Analiz"):
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Burada veri analizi işlevi gelecek.</p></div>', unsafe_allow_html=True)

if st.button("Grafikler"):
    st.write("Grafikler")
    # Grafiklerin altında buton ekleme
    if st.button("Grafiklere Git", key="grafiklere_git_button"):
        if st.button("Konum Sütunu Grafik"):
            # Konum Grafiği
            st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Konum sütununda en çok tekrar eden 5 konum</p></div>', unsafe_allow_html=True)
            # Çubuk grafiği çizme işlevi
            top_locations = df['Konum'].value_counts().head(5)
            st.bar_chart(top_locations)

        if st.button("Çalışma Şekli Sütunu Grafik"):
            # Çalışma Şekli Grafiği
            st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Çalışma şekli sütunu</p></div>', unsafe_allow_html=True)
            # Çubuk grafiği çizme işlevi
            calisma_sekli_sayilari = df['çalışma şekli'].value_counts()
            st.bar_chart(calisma_sekli_sayilari)
      
        if st.button("Pozisyon Sütunu Grafik"):
            # Pozisyon Grafiği
            st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Pozisyon sütununda en çok tekrar eden 20 pozisyon</p></div>', unsafe_allow_html=True)
            # Çubuk grafiği çizme işlevi
            top_positions = df['Pozisyon'].value_counts().head(20)
            st.bar_chart(top_positions)

if st.button("İşveren Girişi", key="isveren_girisi_button"):
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Burada işveren giriş işlevi gelecek.</p></div>', unsafe_allow_html=True)

if st.button("Regresyon"):
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Burada regresyon analizi yapılacak.</p></div>', unsafe_allow_html=True)

# Makaleler bölümü
st.markdown('<h2 style="color: #9b59b6; text-align: center;">Makaleler</h2>', unsafe_allow_html=True)

# Makale 1
if st.button("Makale 1"):
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><h3 style="color: #f4d03f;">Başlık 1</h3><p style="color: #f4d03f;">Burada makale içeriği yer alacak.</p></div>', unsafe_allow_html=True)

# Makale 2
if st.button("Makale 2"):
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><h3 style="color: #f4d03f;">Başlık 2</h3><p style="color: #f4d03f;">Burada makale içeriği yer alacak.</p></div>', unsafe_allow_html=True)

# Hakkımızda bölümü
if st.button("Hakkımızda"):
    st.markdown('''
    ## Bilişim Sektöründe Gelecek: Veri Analizi ve İş İlanları
    ...
    ''')

# Footer
st.markdown('<p style="text-align: center; font-size: 12px; color: #888;">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)
