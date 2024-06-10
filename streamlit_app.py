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
            background-image: url('https://r.resimlink.com/USyYKmk.png'); /* Görsel URL'si */
            background-size: cover;
            background-repeat: no-repeat;
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
    st.markdown('<div class="content-box">', unsafe_allow_html=True
    st.markdown('<h2 class="subtitle">Grafikler</h2>', unsafe_allow_html=True)

    # Konum Grafiği
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<h3 class="subtitle">Konum sütununda en çok tekrar eden 5 konum</h3>', unsafe_allow_html=True)
    top_locations = df['Konum'].value_counts().head(5)
    st.bar_chart(top_locations)
    st.markdown('</div>', unsafe_allow_html=True)

    # Çalışma Şekli Grafiği
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<h3 class="subtitle">Çalışma şekli sütunu</h3>', unsafe_allow_html=True)
    calisma_sekli_sayilari = df['çalışma şekli'].value_counts()
    st.bar_chart(calisma_sekli_sayilari)
    st.markdown('</div>', unsafe_allow_html=True)

    # Pozisyon Grafiği
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<h3 class="subtitle">Pozisyon sütununda en çok tekrar eden 20 pozisyon</h3>', unsafe_allow_html=True)
    top_positions = df['Pozisyon'].value_counts().head(20)
    st.bar_chart(top_positions)
    st.markdown('</div>', unsafe_allow_html=True)

    # Çalışma Şekli ve Pozisyon Grafiği
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<h3 class="subtitle">Çalışma şekli ve pozisyon sütunlarında en çok tekrar eden 5 pozisyonun çalışma şekillerine göre dağılımı</h3>', unsafe_allow_html=True)
    top_5_positions = df['Pozisyon'].value_counts().head(5).index
    filtered_data = df[df['Pozisyon'].isin(top_5_positions)]
    plt.figure(figsize=(10, 6))
    sns.countplot(data=filtered_data, x='Pozisyon', hue='çalışma şekli', palette='viridis')
    plt.title('En Çok Tekrar Eden 5 Pozisyonun Çalışma Şekillerine Göre Dağılımı')
    plt.xlabel('Pozisyon')
    plt.ylabel('Sayı')
    st.pyplot(plt)
    st.markdown('</div>', unsafe_allow_html=True)

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
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<h3 class="subtitle">En Çok Tekrar Edilen İlk 10 Konum ve Pozisyon İlişkisi Heatmap</h3>', unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))
    sns.heatmap(cross_table, cmap='rainbow', annot=True, fmt='d', linewidths=.5)
    plt.title('En Çok Tekrar Edilen İlk 10 Konum ve Pozisyon İlişkisi Heatmap')
    plt.xlabel('Pozisyon')
    plt.ylabel('Konum')
    st.pyplot(plt)
    st.markdown('</div>', unsafe_allow_html=True)

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
    st.markdown('<div class="chart-box">', unsafe_allow_html=True)
    st.markdown('<h3 class="subtitle">En Çok Tekrar Edilen İlk 10 Konum ve Çalışma Şekli İlişkisi Heatmap</h3>', unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))
    sns.heatmap(cross_table, cmap='rainbow', annot=True, fmt='d', linewidths=.5)
    plt.title('En Çok Tekrar Edilen İlk 10 Konum ve Çalışma Şekli İlişkisi Heatmap')
    plt.xlabel('Çalışma Şekli')
    plt.ylabel('Konum')
    st.pyplot(plt)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if st.button("İşveren Girişi", key="isveren_girisi_button"):
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    st.markdown('<h2 class="subtitle">İşveren Girişi</h2>', unsafe_allow_html=True)
    st.markdown('<p>Burada işveren giriş işlevi gelecek.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<p style="text-align: center; font-size: 12px; color: #ffffff;">© 2024 FreshData. Tüm hakları saklıdır.</p>', unsafe_allow_html=True)
