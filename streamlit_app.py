import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
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


if st.button("Meslek Grupları", key="meslek_grupları_button"):
    st.markdown('<div style="background-color: #9b59b6; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"><p style="color: #f4d03f;">Burada meslek gruplarına göre iş arama işlevi gelecek.</p></div>', unsafe_allow_html=True)

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
# Makine Öğrenmesi Kısmı
if st.button("Makine Öğrenmesi"):
    st.write("Makine Öğrenmesi Modeli")
    # Veriyi yükleme ve kontrol etme
    df = load_data(url)
    st.write(df.head(3))

    # 'Tarih' sütununun veri tipini kontrol etme
    st.write(df['Tarih'].dtype)

    # 'Tarih' sütununu dizeye dönüştürme
    df['Tarih'] = df['Tarih'].astype(str)

    # Virgüllerin kaldırılması
    df['Tarih'] = df['Tarih'].str.replace(',', '')

    # Sütun adlarını yazdırma
    st.write("Sütun Adları:")
    st.write(df.columns) 
    # Hedef ve özellik değişkenleri
    try:
        y = df["Tarih"]
        X = df.drop(columns=["Tarih"])

        # Eğitim ve test verilerine ayırma
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Rastgele Orman Sınıflandırıcısı modelini oluşturma ve eğitme
        rf = RandomForestClassifier()
        model = rf.fit(X_train, y_train)

        # Modelin doğruluk puanını yazdırma
        st.write("Test verisi doğruluk puanı:", model.score(X_test, y_test))
        st.write("Eğitim verisi doğruluk puanı:", model.score(X_train, y_train))

        # Örnek bir veri üzerinde modeli test etme
        sample_data_index = 1500
        sample_data = np.array(X.iloc[sample_data_index]).reshape(1, -1)
        prediction = model.predict(sample_data)
        st.write("Tahmin:", prediction)
        st.write("Gerçek Değer:", y.iloc[sample_data_index])

    except KeyError as e:
        st.error("Veri setinde belirtilen sütun adı bulunamadı: {}".format(e))
    except Exception as e:
        st.error("Beklenmeyen bir hata oluştu: {}".format(e)) 

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
