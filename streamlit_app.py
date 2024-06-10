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
            background-image: url('https://r.resimlink.com/USyYKmk.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
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
            background: rgba(173, 216, 230, 0.8); /* Tatlı mavi */
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

# Modeli Yükleme
@st.cache(allow_output_mutation=True)
def load_model(url):
    response = requests.get(url)
    file = BytesIO(response.content)
    model = joblib.load(file)  # Örnek olarak joblib kullanıldı, sizin modelinizin formatına göre değişebilir
    return model

model_url = "https://github.com/esrasenakaraaslan/sena/raw/main/model%20(4)%20(3)%20(1).joblib"  # Eğitilmiş model dosyasının yolu
model = load_model(model_url)

# Giriş Verisini Alın
konum = st.text_input("Konum:")
pozisyon = st.text_input("Pozisyon:")

# Modeli Kullanarak Tahmin Yapma
if st.button("Tahmin Yap"):
    # Tahmin işlemi yapılacak
    prediction = model.predict([[konum, pozisyon]])  # Giriş verisi üzerinde tahmin yapın
    st.write("İş bulma ihtimaliniz:", prediction)
