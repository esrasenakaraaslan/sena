import streamlit as st
import pandas as pd
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns

# Uygulama ayarları
st.set_page_config(page_title="FreshData", page_icon=":rocket:", layout="wide")

# Başlık
st.markdown('<h1 style="color: #9b59b6; text-align: center;">FreshData İş İlanı Sitesi</h1>', unsafe_allow_html=True)

# GitHub'daki Excel dosyasının URL'si
url = "https://github.com/esrasenakaraaslan/web_sitesi/raw/main/.devcontainer/t%C3%BCm_veriler_d%C3%BCzenlenmi%C5%9F_y%C4%B1ll%C4%B1%20(4).xlsx"
response = requests.get(url)
file = BytesIO(response.content)

# Excel dosyasını yükleyip okuma
@st.cache_data
def load_data(file):
    return pd.read_excel(file)

# Veriyi yükle
df = load_data(file)

# Streamlit ile veriyi görüntüleme
st.write("Dosya İçeriği:")
st.write(df)

# Arka plan rengi ve site ismi rengi
st.markdown(
    """
    <style>
    .stApp {
        background-color: #aed6f1; /* Arka plan rengi */
    }
    .stButton>button {
        color: #f4d03f; /* Buton içindeki yazı rengi (sarı) */
        background-color: #9b59b6; /* Buton rengi (mor) */
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Burada grafikler çizme işlevi gelecek.</p></div>', unsafe_allow_html=True)
    
    if st.button("Konum Grafiği", key="konum_grafik_button"):
         st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Konum sütununda en çok tekrar eden 10 konumu çubuk grafiğine dök.</p></div>', unsafe_allow_html=True)
         # Çubuk grafiği çizme işlevi
         konum_sayilari = df['Konum'].value_counts().head(10)
         plt.figure(figsize=(10, 6))
         sns.barplot(x=konum_sayilari.index, y=konum_sayilari.values, palette="viridis")
         plt.title('Konumların Sayısı')
         plt.xlabel('Konumlar')
         plt.ylabel('Sayı')
         plt.xticks(rotation=45)
         st.pyplot(plt)

     if st.button("Çalışma Şekli Grafiği", key="calisma_sekli_grafik_button"):
         st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Çalışma şekli sütununda en çok tekrar edenleri çubuk grafiğine dök.</p></div>', unsafe_allow_html=True)
         # Çubuk grafiği çizme işlevi
         calisma_sekli_sayilari = df['Çalışma Şekli'].value_counts()
         plt.figure(figsize=(10, 6))
         sns.barplot(x=calisma_sekli_sayilari.index, y=calisma_sekli_sayilari.values, palette="viridis")
         plt.title('Çalışma Şeklinin Dağılımı')
         plt.xlabel('Çalışma Şekli')
         plt.ylabel('Sayı')
         plt.xticks(rotation=45)
         st.pyplot(plt)

    # Verinin varlığını kontrol etme
    if df is not None:
        # Grafikleri çizme işlevini çağırma
        draw_seaborn_chart(df)   

if st.button("İşveren Girişi", key="isveren_girisi_button"):
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Burada işveren giriş işlevi gelecek.</p></div>', unsafe_allow_html=True)

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
