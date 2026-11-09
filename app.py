import streamlit as st
import datetime
import time

# Konfigurasi halaman
st.set_page_config(page_title="FlashMart iOS 27 Edition", page_icon="⚡", layout="centered")

# --- KODE CSS KUSTOM: LIQUID GLASS & GLASSMORPHISM CARD ---
st.markdown("""
<style>
    /* Latar Belakang Gradasi Mewah ala iOS */
    .stApp {
        background: linear-gradient(135deg, #0D0F18 0%, #16192B 50%, #251636 100%);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #F5F5F7;
    }

    /* Efek Liquid Glass & Glassmorphism Card Super Halus */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-top: 1px solid rgba(255, 255, 255, 0.25); /* Efek pantulan cahaya liquid glass */
        border-radius: 24px;
        padding: 22px;
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.45);
        margin-bottom: 16px;
    }

    /* Animasi Masuk Halaman */
    @keyframes slideInUp {
        0% { opacity: 0; transform: translateY(25px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .slide-container {
        animation: slideInUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    /* Animasi Motor Ojol & Petir */
    @keyframes driveIn {
        0% { opacity: 0; transform: translateX(-50px) scale(0.8); }
        100% { opacity: 1; transform: translateX(0) scale(1); }
    }

    @keyframes pulseGlow {
        0% { transform: scale(1); filter: drop-shadow(0 0 8px rgba(0, 242, 254, 0.6)); }
        50% { transform: scale(1.15); filter: drop-shadow(0 0 25px rgba(0, 242, 254, 0.95)); }
        100% { transform: scale(1); filter: drop-shadow(0 0 8px rgba(0, 242, 254, 0.6)); }
    }

    .splash-logo {
        font-size: 75px;
        text-align: center;
        animation: driveIn 1s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        margin-bottom: 5px;
    }

    .lightning-effect {
        display: inline-block;
        animation: pulseGlow 1.5s infinite ease-in-out;
    }

    .splash-title {
        font-weight: 800;
        font-size: 42px;
        background: linear-gradient(90deg, #00F2FE 0%, #4FACFE 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-top: 5px;
    }

    .splash-subtitle {
        text-align: center;
        color: #A1A1A6;
        font-size: 15px;
        font-weight: 400;
        margin-top: 8px;
    }

    /* Memastikan teks terlihat kontras */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #F5F5F7 !important;
    }

    /* Input Field Liquid Glass */
    .stTextInput input, .stSelectbox select {
        background: rgba(255, 255, 255, 0.07) !important;
        border: 1px solid rgba(255, 255, 255, 0.18) !important;
        color: white !important;
        border-radius: 14px !important;
    }

    /* Tombol Kustom Ala iOS Liquid Glass */
    .stButton button {
        background: linear-gradient(135deg, #007AFF 0%, #0056B3 100%);
        color: white !important;
        border-radius: 16px;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.25);
        padding: 12px 20px;
        width: 100%;
        box-shadow: 0 6px 20px rgba(0, 122, 255, 0.45);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #0056B3 100%, #003D82 100%);
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# --- INISIALISASI SESSION STATE ---
if 'step_app' not in st.session_state:
    st.session_state.step_app = 1  # 1: Splash, 2: Onboarding, 3: Login, 4: Beranda

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'user_info' not in st.session_state:
    st.session_state.user_info = {}

# Katalog Produk Lengkap ala Alfagift
if 'daftar_produk' not in st.session_state:
    st.session_state.daftar_produk = {
        "101": {"nama": "Beras Premium Sania 5kg", "kategori": "Sembako", "harga": 68000, "stok": 25},
        "102": {"nama": "Minyak Goreng Bimoli 2L", "kategori": "Sembako", "harga": 34000, "stok": 30},
        "103": {"nama": "Gula Pasir Gulaku 1kg", "kategori": "Sembako", "harga": 16500, "stok": 40},
        "104": {"nama": "Mie Instan Indomie Goreng (1 Dus)", "kategori": "Makanan", "harga": 115000, "stok": 15},
        "105": {"nama": "Air Mineral Aqua 600ml (1 Dus)", "kategori": "Minuman", "harga": 42000, "stok": 50},
        "106": {"nama": "Susu UHT Ultra Milk 1L", "kategori": "Minuman", "harga": 19000, "stok": 20},
        "107": {"nama": "Telur Ayam Negeri 1kg", "kategori": "Sembako", "harga": 28000, "stok": 18},
        "108": {"nama": "Kecap Manis Bango 550ml", "kategori": "Bumbu Dapur", "harga": 26000, "stok": 22},
        "109": {"nama": "Sabun Mandi Lifebuoy 450ml", "kategori": "Perawatan Diri", "harga": 23000, "stok": 35},
        "110": {"nama": "Shampoo Pantene 160ml", "kategori": "Perawatan Diri", "harga": 21000, "stok": 25},
        "111": {"nama": "Deterjen Rinso Liquid 750ml", "kategori": "Kebutuhan Rumah", "harga": 20500, "stok": 30},
        "112": {"nama": "Teh Celup Sosro Box", "kategori": "Minuman", "harga": 9500, "stok": 45}
    }

if 'poin_member' not in st.session_state:
    st.session_state.poin_member = 420

if 'riwayat_transaksi' not in st.session_state:
    st.session_state.riwayat_transaksi = []


# --- TAHAP 1: SPLASH SCREEN ---
if st.session_state.step_app == 1:
    st.markdown('<div class="slide-container"><div class="glass-card" style="text-align: center; padding: 45px 20px;">', unsafe_allow_html=True)
    st.markdown("""
        <div class="splash-logo">
            🛵<span class="lightning-effect">⚡</span>
        </div>
        <div class="splash-title">FlashMart</div>
        <div class="splash-subtitle">Next-Gen Mobile Retail Experience</div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Mulai Sekarang ➔"):
        st.session_state.step_app = 2
        st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- TAHAP 2: ONBOARDING ---
elif st.session_state.step_app == 2:
    st.markdown('<div class="slide-container"><div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #00F2FE !important;'>✨ Panduan FlashMart</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #A1A1A6; font-size: 13px;'>Eksplorasi Fitur Belanja Kilat</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    onboarding_page = st.radio(
        "Pilih Petunjuk:", 
        [
            "🛍️ 1. Katalog Super Lengkap Ala Alfagift", 
            "⭐ 2. Poin Member & Sinkronisasi Alfamart", 
            "⚡ 3. Pengiriman Super Kilat Motor Petir"
        ]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    if "1." in onboarding_page:
        st.info("🛍️ Temukan ratusan produk mulai dari sembako, makanan, hingga kebutuhan rumah tangga dengan harga terbaik.")
    elif "2." in onboarding_page:
        st.info("⭐ Kumpulkan poin di setiap transaksi dan nikmati sinkronisasi otomatis dengan kartu member Alfamart.")
    else:
        st.info("⚡ Belanjaan langsung diantar dengan kecepatan kilat langsung ke lokasi tujuanmu!")

    st.markdown("<br>", unsafe_allow_html=True)
    _, col_btn = st.columns([1.5, 1])
    with col_btn:
        if st.button("Next ➔"):
            st.session_state.step_app = 3
            st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- TAHAP 3: LOGIN / SIGN UP ---
elif st.session_state.step_app == 3 and not st.session_state.logged_in:
    st.markdown('<div class="slide-container"><div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='color: #00F2FE !important;'>🔐 Masuk / Daftar Akun</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #A1A1A6; font-size: 13px;'>Sinkronisasi akun Google & Member Alfamart Anda.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    nama_user = st.text_input("Nama Lengkap / Akun Google", placeholder="Contoh: Nisfyu")
    no_alfamart = st.text_input("Nomor Member Alfamart", placeholder="Contoh: 899012345678")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Masuk ke Aplikasi"):
        if nama_user and no_alfamart:
            st.session_state.logged_in = True
            st.session_state.user_info = {"nama": nama_user, "alfamart": no_alfamart}
            st.session_state.step_app = 4
            st.success("🎉 Berhasil terhubung ke sistem!")
            time.sleep(0.8)
            st.rerun()
        else:
            st.warning("⚠️ Mohon lengkapi nama dan nomor member terlebih dahulu!")
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- TAHAP 4: HALAMAN UTAMA (KATALOG LENGKAP & CHECKOUT) ---
else:
    st.markdown('<div class="slide-container">', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="glass-card" style="padding: 15px 20px;">
            <h3 style="margin: 0; color: #00F2FE !important;">⚡ FlashMart Mobile</h3>
            <p style="color: #A1A1A6; margin: 0; font-size: 13px;">Halo, <b>{st.session_state.user_info.get('nama', 'User')}</b> | Member: {st.session_state.user_info.get('alfamart', '-')}</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.info("👤 **Tier:** Gold Member")
    with col2:
        st.success(f"⭐ **Poin:** {st.session_state.poin_member} Pts")

    # Katalog Produk Lengkap
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 🛒 Katalog Produk Lengkap")
    
    kategori_pilihan = st.selectbox("Filter Kategori:", ["Semua", "Sembako", "Makanan", "Minuman", "Bumbu Dapur", "Perawatan Diri", "Kebutuhan Rumah"])

    data_tabel = []
    for kode, item in st.session_state.daftar_produk.items():
        if kategori_pilihan == "Semua" or item["kategori"] == kategori_pilihan:
            data_tabel.append({
                "Kode": kode,
                "Produk": item["nama"],
                "Kategori": item["kategori"],
                "Harga": f"Rp {item['harga']:,}",
                "Stok": item["stok"]
            })

    st.table(data_tabel)
    st.markdown('</div>', unsafe_allow_html=True)

    # Checkout & Transaksi
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 💳 Checkout Belanja")
    pilihan_kode = st.selectbox("Pilih Kode Produk:", list(st.session_state.daftar_produk.keys()))
    jumlah_beli = st.number_input("Jumlah Beli:", min_value=1, value=1, step=1)

    produk_pilihan = st.session_state.daftar_produk[pilihan_kode]
    subtotal = produk_pilihan['harga'] * jumlah_beli

    st.write(f"Barang: **{produk_pilihan['nama']}** | Subtotal: **Rp {subtotal:,}**")

    if st.button("Bayar Sekarang"):
        if jumlah_beli > produk_pilihan['stok']:
            st.error("❌ Stok tidak mencukupi!")
        else:
            st.session_state.daftar_produk[pilihan_kode]['stok'] -= jumlah_beli
            poin_didapat = int(subtotal // 10000)
            st.session_state.poin_member += poin_didapat
            
            waktu = datetime.datetime.now().strftime('%H:%M:%S')
            st.session_state.riwayat_transaksi.append({
                "waktu": waktu, "item": produk_pilihan['nama'], "total": subtotal
            })
            st.success(f"✅ Transaksi Berhasil! +{poin_didapat} Poin ditambahkan ke akun Alfamart.")

    if st.session_state.riwayat_transaksi:
        st.markdown("---")
        st.markdown("### 📜 Riwayat Sesi Ini")
        for r in reversed(st.session_state.riwayat_transaksi):
            st.text(f"[{r['waktu']}] {r['item']} - Rp {r['total']:,}")
    st.markdown('</div></div>', unsafe_allow_html=True)
    
