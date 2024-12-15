import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
top_10_category_by_sales = pd.read_csv('top_10_category_by_sales.csv')
top_10_category_by_revenue = pd.read_csv('top_10_category_by_revenue.csv')
top_10_cities_by_orders = pd.read_csv('top_10_cities_by_orders.csv')
top_10_cities_by_revenue = pd.read_csv('top_10_cities_by_revenue.csv')
top_cities = pd.read_csv('top_cities.csv')
top_10_city_status = pd.read_csv('top_10_city_status.csv')
top_10_cities_by_active_customers = pd.read_csv('top_10_cities_by_active_customers.csv')
top_10_cities_by_non_active_customers = pd.read_csv('top_10_cities_by_non_active_customers.csv')
monthly_sales = pd.read_csv('monthly_sales.csv')
quarterly_data = pd.read_csv('quarterly_data.csv')

# Set judul dashboard
st.title("Dashboard Analisis E-Commerce Brasil")

# Menambahkan menu navigasi
nav_options = ["Pendahuluan", "Visualisasi", "Kesimpulan dan Rekomendasi", "Tentang Penulis"]
selected_nav = st.sidebar.selectbox("Pilih Bagian", nav_options)

# Deskripsi Bagian Sidebar
st.sidebar.write("### Deskripsi Bagian")
if selected_nav == "Pendahuluan":
    st.sidebar.write("""
    Bagian ini memperkenalkan dashboard, menjelaskan tujuan analisis,
    serta memberikan gambaran umum tentang Dataset E-Commerce Publik Brasil dari Olist.
    Tujuan dari analisis ini adalah untuk memahami pertanyaan bisnis utama yang mendasari eksplorasi data.
    """)
elif selected_nav == "Visualisasi":
    st.sidebar.write("""
    Bagian ini akan menampilkan berbagai visualisasi yang dihasilkan dari dataset.
    Visualisasi ini membantu menjawab pertanyaan bisnis dan mengungkap tren, pola, serta metrik penting yang terkait dengan pasar e-commerce Brasil.
    """)
elif selected_nav == "Kesimpulan dan Rekomendasi":
    st.sidebar.write("""
    Bagian ini merangkum temuan dari analisis yang dilakukan pada bagian Visualisasi.
    Di sini akan disajikan wawasan kunci serta rekomendasi yang dapat diambil berdasarkan data untuk membantu pengambilan keputusan bisnis.
    """)
elif selected_nav == "Tentang Penulis":
    st.sidebar.write("""
    Bagian ini memberikan informasi tentang penulis analisis, termasuk latar belakang dan motivasi dalam melakukan penelitian ini.
    """)

# Bagian Pendahuluan
if selected_nav == "Pendahuluan":
    st.header("Pendahuluan")
    st.write("""
    Tujuan utama dari analisis ini adalah untuk mengeksplorasi dan menemukan wawasan dari Dataset E-Commerce Publik Brasil yang disediakan oleh Olist.
    Melalui analisis data, kami berusaha mengidentifikasi tren dan pola utama yang dapat memberikan wawasan strategis bagi pengambilan keputusan bisnis.
    """)
    st.write("### Gambaran Umum Dataset")
    st.write("""
    Dataset E-Commerce Publik Brasil dari Olist berisi data sekitar 100.000 pesanan dari tahun 2016 hingga 2018.
    Dataset ini mencakup berbagai atribut terkait pesanan pelanggan, seperti status pesanan, rincian produk, metode pembayaran, dan informasi pelanggan.
    Memahami dataset ini sangat penting untuk mendapatkan wawasan tentang perilaku pelanggan, kinerja penjualan, dan efisiensi operasional di pasar e-commerce Brasil.
    """)
    
    st.write("### Pertanyaan Bisnis: ")
    st.write("""
    1. **Apa kategori produk dengan pesanan tertinggi dan paling menguntungkan?**  
       **Objective:** Mengidentifikasi kategori produk yang memberikan kontribusi terbesar pada total pesanan dan pendapatan, sebagai panduan dalam strategi inventaris dan pemasaran.

    2. **Wilayah dan kota mana yang memiliki penjualan atau profit tertinggi?**  
       **Objective:** Menganalisis kinerja penjualan berdasarkan lokasi geografis untuk menemukan pasar utama dan menargetkan area dengan potensi pertumbuhan.

    3. **Di mana wilayah atau kota dengan pelanggan paling aktif atau paling tidak aktif?**  
       **Objective:** Memahami tingkat keterlibatan pelanggan di berbagai lokasi, dengan fokus pada area dengan tingkat ketidakaktifan tinggi untuk menyusun strategi pemasaran yang lebih tepat.

    4. **Bagaimana tren penjualan dari waktu ke waktu?**  
       **Objective:** Menganalisis tren penjualan sepanjang waktu untuk menentukan pola musiman, mengidentifikasi bulan penjualan puncak, dan merencanakan strategi penjualan serta inventarisasi dengan lebih efektif.
    """)

# Bagian Visualisasi
elif selected_nav == "Visualisasi":
    st.header("Visualisasi dan Wawasan")

    # Membuat tab untuk setiap pertanyaan bisnis
    tab1, tab2, tab3, tab4 = st.tabs([
        "Kategori Produk Terlaris dan Paling Menguntungkan", 
        "Penjualan Berdasarkan Wilayah dan Kota", 
        "Jumlah Pelanggan", 
        "Tren Penjualan dari Waktu ke Waktu"
    ])

    # Tab 1: Kategori Produk Terlaris dan Paling Menguntungkan
    with tab1:
        st.subheader("Kategori Produk Terlaris dan Paling Menguntungkan")

        # Bar Chart: Top 10 Categories by Sales (Total Orders)
        st.write("#### Top 10 Categories by Total Orders")
        plt.figure(figsize=(12, 6))
        sns.barplot(
            data=top_10_category_by_sales,
            x='total_orders',
            y='product_category_name_english',
            hue='product_category_name_english',
            legend=False,
            palette='Blues_d'
        )
        plt.title('Top 10 Categories by Total Orders', fontsize=16)
        plt.xlabel('Total Orders', fontsize=12)
        plt.ylabel('Product Categories (English)', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)

        st.write("""
        **Top 10 Categories by Total Orders** menunjukkan kategori produk yang memiliki jumlah pesanan tertinggi di platform e-commerce Brasil.
        Kategori produk **bed_bath_table** (Cama, Mesa e Banho) menempati urutan pertama dengan total 8,687 pesanan, diikuti oleh kategori **health_beauty** (Beleza e Saúde) dengan 7,279 pesanan.
        Kategori-kategori ini memiliki permintaan tinggi dan memberikan kontribusi signifikan terhadap total pesanan yang diterima oleh platform.
        """)

        # Bar Chart: Top 10 Categories by Revenue (Total Revenue)
        st.write("#### Top 10 Categories by Total Revenue")
        plt.figure(figsize=(12, 6))
        sns.barplot(
            data=top_10_category_by_revenue,
            x='total_revenue',
            y='product_category_name_english',
            hue='product_category_name_english',
            legend=False,
            palette='Greens_d'
        )
        plt.title('Top 10 Categories by Total Revenue', fontsize=16)
        plt.xlabel('Total Revenue', fontsize=12)
        plt.ylabel('Product Categories (English)', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)

        st.write("""
        **Top 10 Categories by Total Revenue** menampilkan kategori produk yang menghasilkan pendapatan tertinggi di platform.
        Kategori **bed_bath_table** (Cama, Mesa e Banho) kembali menduduki posisi teratas dengan total pendapatan sebesar \$1,018,515.66.
        Kategori **sports_leisure** (Esporte e Lazer) dan **health_beauty** (Beleza e Saúde) juga menunjukkan kontribusi yang signifikan terhadap pendapatan.
        Pendapatan yang lebih tinggi ini mengindikasikan bahwa produk di kategori ini memiliki harga lebih tinggi atau permintaan yang lebih menguntungkan bagi penjual dan platform.
        """)

    # Tab 2: Penjualan Berdasarkan Wilayah dan Kota
    with tab2:
        st.subheader("Wilayah dan Kota dengan Penjualan atau Profit Tertinggi")

        # Bar Chart: Top 10 Cities by Total Orders
        st.write("#### Top 10 Cities by Total Orders")
        plt.figure(figsize=(10, 6))
        sns.barplot(x='customer_city', y='total_orders', data=top_10_cities_by_orders, hue='customer_city', palette='Blues_d')
        plt.title('Top 10 Cities by Total Orders')
        plt.xlabel('City')
        plt.xticks(rotation=35)
        plt.ylabel('Total Orders')
        plt.tight_layout()
        st.pyplot(plt)

        st.write("""
        Top 10 kota dengan pesanan tertinggi menunjukkan bahwa kota-kota besar seperti **São Paulo** dan **Rio de Janeiro** mendominasi daftar pesanan dengan **São Paulo** menghasilkan lebih dari 15 ribu pesanan. 
        Hal ini menunjukkan konsentrasi ekonomi dan populasi yang lebih besar di kota-kota tersebut. Berdasarkan data, **São Paulo** memimpin dengan **15.044 pesanan** dan total pendapatan sebesar **1.367.937,20**. 
        Kota-kota seperti **Belo Horizonte** dan **Curitiba** juga menunjukkan angka pesanan yang signifikan meskipun lebih rendah dibandingkan dengan kota besar lainnya.
        """)

        # Bar Chart: Top 10 Cities by Total Revenue
        st.write("#### Top 10 Cities by Total Revenue")
        plt.figure(figsize=(10, 6))
        sns.barplot(x='customer_city', y='total_revenue', data=top_10_cities_by_revenue, hue='customer_city', palette='viridis')
        plt.title('Top 10 Cities by Total Revenue')
        plt.xlabel('City')
        plt.xticks(rotation=35)
        plt.ylabel('Total Revenue')
        plt.tight_layout()
        st.pyplot(plt)

        st.write("""
        Kota-kota dengan pendapatan tertinggi hampir identik dengan daftar pesanan tertinggi, dengan **São Paulo** masih mendominasi baik dalam hal jumlah pesanan maupun pendapatan dengan **1.367.937,20**. 
        Hal ini mengindikasikan bahwa volume pesanan yang lebih tinggi di kota besar ini juga berkorelasi langsung dengan pendapatan yang lebih besar. 
        **Rio de Janeiro** juga menunjukkan kontribusi pendapatan yang signifikan, meskipun lebih rendah daripada **São Paulo**, yang mencerminkan adanya ketergantungan pada pasar besar untuk pertumbuhan pendapatan.
        """)

        # Scatter Plot: Total Orders vs Total Revenue by City
        st.write("#### Scatter Plot of Total Orders vs Total Revenue by City")
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x='total_orders', y='total_revenue', data=top_cities, hue='customer_city', palette='Set1', legend=False)
        plt.title('Scatter Plot of Total Orders vs Total Revenue by City')
        plt.xlabel('Total Orders')
        plt.ylabel('Total Revenue')
        plt.tight_layout()
        st.pyplot(plt)

        st.write("""
        Dari scatter plot, dapat dilihat bahwa terdapat hubungan positif antara **total orders** dan **total revenue**. 
        Kota-kota dengan pesanan yang lebih tinggi, seperti **São Paulo** dan **Rio de Janeiro**, juga menghasilkan pendapatan yang lebih besar. 
        Ini menunjukkan bahwa peningkatan jumlah pesanan sejalan dengan peningkatan pendapatan, yang menunjukkan bahwa platform e-commerce ini berhasil mengonversi volume pesanan menjadi pendapatan yang signifikan. 
        Titik-titik yang lebih tinggi pada grafik menggambarkan konsentrasi besar transaksi di kota-kota besar dengan daya beli yang lebih tinggi.
        """)

    # Tab 3: Jumlah Pelanggan
    with tab3:
        st.subheader("Jumlah Pelanggan")

        # Bar Chart: Top 10 Active Customers
        st.write("#### Top 10 Cities by Active Customers")
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Total Pelanggan Aktif', y='customer_city', data=top_10_cities_by_active_customers, palette='viridis')
        plt.title('Top 10 Cities by Active Customers')
        plt.xlabel('Total Active Customers')
        plt.ylabel('City')
        plt.tight_layout()
        st.pyplot(plt)

        # Bar Chart: Top 10 Non-Active Customers
        st.write("#### Top 10 Cities by Non-Active Customers")
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Total Pelanggan Tidak Aktif', y='customer_city', data=top_10_cities_by_non_active_customers, palette='magma')
        plt.title('Top 10 Cities by Non-Active Customers')
        plt.xlabel('Total Non-Active Customers')
        plt.ylabel('City')
        plt.tight_layout()
        st.pyplot(plt)

        st.write("""
        Analisis menunjukkan bahwa **São Paulo** mendominasi baik dalam jumlah pelanggan aktif maupun tidak aktif. 
        Hal ini menunjukkan potensi besar untuk mempertahankan pelanggan aktif di kota ini sekaligus peluang untuk re-engagement pelanggan tidak aktif.
        """)

    # Tab 4: Tren Penjualan dari Waktu ke Waktu
    with tab4:
        st.subheader("Tren Penjualan dari Waktu ke Waktu")

        # Line Chart: Monthly Sales
        st.write("#### Monthly Sales Trend")
        plt.figure(figsize=(12, 6))
        plt.plot(monthly_sales['year_month'], monthly_sales['total_revenue'], marker='o', linestyle='-', color='blue')
        plt.title('Monthly Sales Trend', fontsize=16)
        plt.xlabel('Month-Year', fontsize=12)
        plt.ylabel('Total Revenue', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        st.pyplot(plt)

        st.write("""
        Tren penjualan bulanan menunjukkan peningkatan yang signifikan selama bulan-bulan puncak seperti November dan Desember, yang kemungkinan besar dipengaruhi oleh promosi musiman seperti Black Friday.
        """)

        # Bar Chart: Quarterly Sales
        st.write("#### Quarterly Sales Trend")
        plt.figure(figsize=(12, 6))
        sns.barplot(x='quarter', y='total_revenue', data=quarterly_data, palette='coolwarm')
        plt.title('Quarterly Sales Trend', fontsize=16)
        plt.xlabel('Quarter', fontsize=12)
        plt.ylabel('Total Revenue', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)

        st.write("""
        Analisis per kuartal menunjukkan bahwa kuartal pertama (Q1) pada tahun 2018 mencatatkan pendapatan tertinggi, menyoroti momentum kuat dalam permintaan pelanggan pada periode tersebut.
        """)

# Bagian Kesimpulan dan Rekomendasi
elif selected_nav == "Kesimpulan dan Rekomendasi":
    st.header("Kesimpulan dan Rekomendasi Bisnis")
    st.write(""" 
    Berdasarkan analisis yang dilakukan, berikut adalah kesimpulan utama dan rekomendasi bisnis:

    ### Kesimpulan Utama
    1. **Kategori Produk:** Kategori **Bed, Bath & Table** dan **Health & Beauty** mendominasi baik dalam jumlah pesanan maupun pendapatan.
    2. **Wilayah & Kota:** **São Paulo** dan **Rio de Janeiro** adalah kontributor utama baik dalam jumlah pesanan maupun pendapatan.
    3. **Pelanggan Aktif & Tidak Aktif:** **São Paulo** memiliki jumlah pelanggan aktif dan tidak aktif tertinggi, menunjukkan potensi besar untuk re-engagement.
    4. **Tren Penjualan:** Penjualan meningkat signifikan selama bulan-bulan promosi seperti November, menunjukkan dampak positif dari kampanye musiman.

    ### Rekomendasi Bisnis
    - **Optimalisasi Inventaris:** Fokus pada kategori populer seperti **Bed, Bath & Table** dan **Health & Beauty** untuk memenuhi permintaan pelanggan.
    - **Targeting Regional:** Fokuskan upaya pemasaran di kota-kota besar seperti **São Paulo** dan **Rio de Janeiro** untuk memaksimalkan potensi pasar.
    - **Re-engagement Strategi:** Tingkatkan upaya pemasaran ulang di antara pelanggan tidak aktif di wilayah dengan konsentrasi tinggi, terutama di **São Paulo**.
    - **Promosi Musiman:** Perkuat promosi selama periode puncak seperti Black Friday untuk meningkatkan penjualan dan memanfaatkan momentum musiman.
    """)

# Bagian Tentang Penulis
elif selected_nav == "Tentang Penulis":
    st.header("Tentang Penulis")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("myphoto.jpeg", width=200, caption="Wardiansyah Fauzi Abdillah")

    st.write("""
    Nama saya Wardiansyah Fauzi Abdillah, mahasiswa Informatika di Universitas Gunadarma. 
    Saya tertarik dengan analisis data dan penerapannya dalam strategi bisnis serta pengambilan keputusan.
    Proyek ini bertujuan untuk memanfaatkan Dataset E-Commerce Publik Brasil untuk menemukan wawasan yang dapat membantu mengoptimalkan operasi e-commerce.
    """)
