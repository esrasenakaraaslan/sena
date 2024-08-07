import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import joblib
from io import BytesIO
import random
import pickle
import requests
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

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
         .content-box h2 {
            font-size: 28px; /* Yazı boyutunu büyüt */
            color: #FFC0CB; /* Buton rengiyle aynı renk */
        }
   .title {
    color: #FFB6C1; /* Tatlış pembiş */
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    margin-bottom: 30px;
    background-color: #FF69B4; /* Daha koyu pembe */
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

# Dosya İçeriği
st.markdown('<div class="content-box">', unsafe_allow_html=True)
st.write(df)
st.markdown('</div>', unsafe_allow_html=True)

# 'DIGITURK' satırını çıkar
df = df[df['Tarih'] != 'DIGITURK']

# Tarih sütununu uygun bir tarih veri tipine dönüştürme
df['Tarih'] = pd.to_datetime(df['Tarih'], format='%d/%m/%Y', errors='coerce')

# Özellikler ve hedef değişkeni ayarla
X = df[['Tarih']]  # 'Tarih' sütunu bağımsız değişken
y = df['Pozisyon']  # 'Pozisyon' sütunu hedef değişken

# Eğitim ve test verilerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluştur ve eğit
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Modelin performansını değerlendir
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)

# Eğitilmiş modeli kaydet
joblib.dump(model, "model.joblib")

# Başlık
st.title("GELECEKTE BİLİSİM SEKTÖRÜ")

# Pozisyonları al
positions = df['Pozisyon'].unique()


# Pozisyon Seçme Kutusu
st.markdown('<div class="position-box">', unsafe_allow_html=True)
selected_position = st.selectbox("Pozisyon Seçiniz", positions)
st.markdown('</div>', unsafe_allow_html=True)


# Yıl Seçme Kutusu
st.markdown('<div class="position-box">', unsafe_allow_html=True)
selected_year = st.number_input("Yıl Seçiniz", min_value=2020, max_value=2023)
st.markdown('</div>', unsafe_allow_html=True)

# Modeli yükle
model_path = "model.joblib"
model = joblib.load(model_path)

if st.button("Tahmin Et!!"):
    # Tarih tahmini için gerekli fonksiyon
    def predict_position(model, year):
        return model.predict([[year]])[0]  # Tahmin sonucunu listenin ilk öğesi olarak al

    # Tahmin edilen pozisyon
    predicted_position = predict_position(model, selected_year)
    
    # Tahmin sonucunu göster
    st.write(f"Seçilen yıl: {selected_year}")
    st.write(f"Tahmini Pozisyon: {predicted_position}")
    
    # Tahmin sonucunu değerlendir
    if predicted_position == selected_position:
        st.success("Doğru Tahmin!")
    else:
        st.error("Yanlış Tahmin!")
        

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



# Footer
st.markdown('<div class="content-box">', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle" style="color: #FFB6C1;">© 2024 FreshData. Tüm hakları saklıdır.</h2>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
