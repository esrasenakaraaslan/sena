import streamlit as st
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
# CSS stil tanımları
st.markdown(
    """
    <style>
        /* Arka plan rengi */
        body {
            background-color: #3498db; /* Mavi renk */
            background-image: url("https://i.pinimg.com/originals/2c/2d/1d/2c2d1dfca6979cb8d1a775983f9d781c.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
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
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Pozisyon sütununda en çok tekrar eden 20 pozisyon</p></div>', unsafe_allow_html=True)
    top_positions = df['Pozisyon'].value_counts().head(20)
    st.bar_chart(top_positions)

    # Çalışma Şekli ve Pozisyon Grafiği
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Çalışma şekli ve pozisyon sütunlarında en çok tekrar eden 5 pozisyonun çalışma şekillerine göre dağılımı</p></div>', unsafe_allow_html=True)
    top_5_positions = df['Pozisyon'].value_counts().head(5).index
    filtered_data = df[df['Pozisyon'].isin(top_5_positions)]
    plt.figure(figsize=(10, 6))
    sns.countplot(data=filtered_data, x='Pozisyon', hue='çalışma şekli', palette='viridis')
    plt.title('En Çok Tekrar Eden 5 Pozisyonun Çalışma Şekillerine Göre Dağılımı')
    plt.xlabel('Pozisyon')
    plt.ylabel('Sayı')
    st.pyplot(plt)
    # En çok tekrar eden konumlar ve pozisyonlar
    en_cok_tekrar_edilen_konumlar = df['Konum'].value_counts().head(10).index
    en_cok_tekrar_edilen_pozisyonlar = df['Pozisyon'].value_counts().head(10).index

    # Filtrelenmiş veri
    filtrelenmis_veri = df[
        df['Konum'].isin(en_cok_tekrar_edilen_konumlar) & 
        df['Pozisyon'].isin(en_cok_tekrar_edilen_pozisyonlar)
    ]

    # Çapraz tablo oluştur
    cross_table = pd.crosstab(index=filtrelenmis_veri['Konum'], columns=filtrelenmis_veri['Pozisyon'])

    # Streamlit ile görselleştirme
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">En Çok Tekrar Edilen İlk 10 Konum ve Pozisyon İlişkisi Heatmap</p></div>', unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))
    sns.heatmap(cross_table, cmap='rainbow', annot=True, fmt='d', linewidths=.5)
    plt.title('En Çok Tekrar Edilen İlk 10 Konum ve Pozisyon İlişkisi Heatmap')
    plt.xlabel('Pozisyon')
    plt.ylabel('Konum')
    st.pyplot(plt)
    # En çok tekrar eden konumlar ve çalışma şekilleri
    en_cok_tekrar_edilen_konumlar = df['Konum'].value_counts().head(10).index
    en_cok_tekrar_edilen_calisma_sekilleri = df['çalışma şekli'].value_counts().head(10).index

    # Filtrelenmiş veri
    filtrelenmis_veri = df[
        df['Konum'].isin(en_cok_tekrar_edilen_konumlar) & 
        df['çalışma şekli'].isin(en_cok_tekrar_edilen_calisma_sekilleri)
    ]

    # Çapraz tablo oluştur
    cross_table = pd.crosstab(index=filtrelenmis_veri['Konum'], columns=filtrelenmis_veri['çalışma şekli'])

    # Streamlit ile görselleştirme
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">En Çok Tekrar Edilen İlk 10 Konum ve Çalışma Şekli İlişkisi Heatmap</p></div>', unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))
    sns.heatmap(cross_table, cmap='rainbow', annot=True, fmt='d', linewidths=.5)
    plt.title('En Çok Tekrar Edilen İlk 10 Konum ve Çalışma Şekli İlişkisi Heatmap')
    plt.xlabel('Çalışma Şekli')
    plt.ylabel('Konum')
    st.pyplot(plt)
if st.button("İşveren Girişi", key="isveren_girisi_button"):
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Burada işveren giriş işlevi gelecek.</p></div>', unsafe_allow_html=True)
# Model dosyasının URL'si
model_url = "https://github.com/esrasenakaraaslan/sena/raw/main/.devcontainer/model%20(4).joblib"

# Modeli yükle
model = joblib.load(model_url)

# Meslek seçimini alma
selected_position = st.selectbox("Meslek Seçiniz", unique_positions)

# Tahmin et butonu
if st.button("Tahmin Et"):
    # Seçilen meslek için tahmin yap
    selected_data = df[df['Pozisyon'] == selected_position].drop(['Tarih'], axis=1)  # Seçilen pozisyonun verilerini al, tahmin yapabilmek için 'Tarih' sütununu kaldır
    model = joblib.load("model (4).joblib")  # Modeli yükle
    prediction = model.predict(selected_data)  # Tahmin yap
    predicted_year = int(prediction)  # Tahmin sonucunu tam sayıya dönüştür
    
    # Tahmin sonucunu göster
    st.write(f"{selected_position} mesleği için tahmin edilen yıl: {predicted_year}")


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
