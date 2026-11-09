import streamlit as st
import datetime
import time

# Konfigurasi Halaman
st.set_page_config(page_title="FlashMart iOS 27 Edition", page_icon="⚡", layout="centered")

# --- CSS KUSTOM GLASSMORPHISM & FLOATING DOCK ALA iOS 27 / COLOROS 17 ---
css_code = """
<style>
    /* Dark Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0B0E14 0%, #171A26 50%, #221533 100%);
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif !important;
        color: #F5F5F7;
    }

    /* Glassmorphism Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-top: 1px solid rgba(255, 255, 255, 0.22);
        border-radius: 22px;
        padding: 16px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        margin-bottom: 12px;
        transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    .glass-card:active {
        transform: scale(0.97);
    }

    /* Header Box */
    .header-box {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(20px);
        border-radius: 18px;
        padding: 12px 16px;
        margin-bottom: 12px;
        border: 1px solid rgba(255, 255, 255, 0.12);
    }

    /* Floating Dock Navigasi Bawah */
    div.row-widget.stRadio > div {
        background: rgba(20, 20, 30, 0.85) !important;
        backdrop-filter: blur(35px) !important;
        -webkit-backdrop-filter: blur(35px) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 40px !important;
        padding: 6px 10px !important;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.7) !important;
        position: fixed !important;
        bottom: 15px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        width: 92% !important;
        max-width: 420px !important;
        z-index: 999999 !important;
    }

    div.row-widget.stRadio label input {
        display: none !important;
    }

    div.row-widget.stRadio label {
        background: transparent !important;
        border: none !important;
        padding: 6px 2px !important;
        text-align: center !important;
        border-radius: 20px !important;
        transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        cursor: pointer;
    }

    div.row-widget.stRadio label:active {
        transform: scale(0.9) !important;
    }

    /* Animasi Pop Tombol */
    .stButton button {
        background: linear-gradient(135deg, #007AFF 0%, #0056B3 100%);
        color: white !important;
        border-radius: 16px;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 12px 16px;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0, 122, 255, 0.4);
        transition: transform 0.15s cubic-bezier(0.34, 1.56, 0.64, 1), background 0.3s ease;
        cursor: pointer;
    }

    .stButton button:hover {
        background: linear-gradient(135deg, #0056B3 0%, #003D82 100%);
        transform: translateY(-2px);
    }

    .stButton button:active {
        transform: scale(0.92) !important;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# --- INISIALISASI SESSION STATE ---
if 'step_app' not in st.session_state:
    st.session_state.step_app = 1

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'user_info' not in st.session_state:
    st.session_state.user_info = {}

if 'keranjang' not in st.session_state:
    st.session_state.keranjang = []

if 'daftar_produk' not in st.session_state:
    st.session_state.daftar_produk = {
        "101": {"nama": "Beras Premium Sania 5kg", "kategori": "Sembako", "harga": 68000, "stok": 50},
        "102": {"nama": "Minyak Goreng Bimoli 2L", "kategori": "Sembako", "harga": 34000, "stok": 60},
        "103": {"nama": "Gula Pasir Gulaku 1kg", "kategori": "Sembako", "harga": 16500, "stok": 80},
        "104": {"nama": "Telur Ayam Negeri 1kg", "kategori": "Sembako", "harga": 28000, "stok": 45},
        "105": {"nama": "Tepung Terigu Segitiga Biru 1kg", "kategori": "Sembako", "harga": 14500, "stok": 40},
        "201": {"nama": "Mie Instan Indomie Goreng (1 Dus)", "kategori": "Makanan", "harga": 115000, "stok": 30},
        "202": {"nama": "Mie Instan Sedap Soto (1 Dus)", "kategori": "Makanan", "harga": 110000, "stok": 25},
        "203": {"nama": "Biskuit Roma Kaleng Assorted", "kategori": "Makanan", "harga": 48000, "stok": 35},
        "204": {"nama": "Chocolatos Drink Renceng", "kategori": "Makanan", "harga": 12000, "stok": 60},
        "301": {"nama": "Air Mineral Aqua 600ml (1 Dus)", "kategori": "Minuman", "harga": 42000, "stok": 100},
        "302": {"nama": "Susu UHT Ultra Milk Full Cream 1L", "kategori": "Minuman", "harga": 19000, "stok": 50},
        "303": {"nama": "Teh Kotak Sosro 300ml (1 Dus)", "kategori": "Minuman", "harga": 45000, "stok": 40},
        "304": {"nama": "Kopi Kapal Api Special 380g", "kategori": "Minuman", "harga": 32000, "stok": 35},
        "401": {"nama": "Kecap Manis Bango 550ml", "kategori": "Bumbu Dapur", "harga": 26000, "stok": 40},
        "402": {"nama": "Saus Sambal ABC 335ml", "kategori": "Bumbu Dapur", "harga": 17500, "stok": 45},
        "403": {"nama": "Penyedap Rasa Royco Ayam 230g", "kategori": "Bumbu Dapur", "harga": 9500, "stok": 60},
        "501": {"nama": "Sabun Mandi Cair Lifebuoy 450ml", "kategori": "Perawatan Diri", "harga": 23000, "stok": 40},
        "502": {"nama": "Shampoo Pantene Anti-Dandruff 160ml", "kategori": "Perawatan Diri", "harga": 21000, "stok": 30},
        "601": {"nama": "Deterjen Cair Rinso Anti Noda 750ml", "kategori": "Kebutuhan Rumah", "harga": 20500, "stok": 45},
        "603": {"nama": "Kabel Data Type-C Fast Charging", "kategori": "Elektronik", "harga": 35000, "stok": 20}
    }

if 'poin_member' not in st.session_state:
    st.session_state.poin_member = 520

if 'riwayat_transaksi' not in st.session_state:
    st.session_state.riwayat_transaksi = []


# --- TAHAP 1: SPLASH SCREEN ---
if st.session_state.step_app == 1:
    st.markdown('<div class="glass-card" style="text-align: center; padding: 50px 20px; margin-top: 50px;">', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 80px; margin-bottom: 10px;">🛵⚡</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-weight: 800; font-size: 38px; color: #00F2FE; margin: 0;">FlashMart</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #A1A1A6; font-size: 14px; margin-top: 5px;">iOS & ColorOS Mobile Experience</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Mulai Sekarang ➔"):
        st.session_state.step_app = 2
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAHAP 2: ONBOARDING WIZARD ---
elif st.session_state.step_app == 2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #00F2FE;'>✨ Panduan FlashMart</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #A1A1A6; font-size: 13px;'>Ekosistem Belanja On-Demand Super Kilat</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    onboarding_page = st.radio(
        "Pilih Petunjuk:", 
        [
            "🛍️ 1. Katalog Terlengkap Seluruh Indonesia", 
            "⭐ 2. Sinkronisasi Poin & Member Alfamart", 
            "⚡ 3. Pengiriman Kilat Motor Petir"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    if "1." in onboarding_page:
        st.info("🛍️ Akses jutaan produk mulai dari sembako, makanan, hingga elektronik dalam satu genggaman aplikasi.")
    elif "2." in onboarding_page:
        st.info("⭐ Kumpulkan poin di setiap transaksi dan nikmati integrasi penuh dengan sistem member Alfamart.")
    else:
        st.info("⚡ Pesanan langsung diantar dengan kecepatan kilat langsung ke lokasimu!")

    st.markdown("<br>", unsafe_allow_html=True)
    _, col_btn = st.columns([1.5, 1])
    with col_btn:
        if st.button("Next ➔"):
            st.session_state.step_app = 3
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAHAP 3: AUTHENTICATION (LOGIN/REGISTER) ---
elif st.session_state.step_app == 3 and not st.session_state.logged_in:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='color: #00F2FE;'>🔐 Masuk / Daftar Akun</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #A1A1A6; font-size: 13px;'>Hubungkan akun Google dan member Alfamart Anda.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    nama_user = st.text_input("Nama Lengkap / Akun Google", placeholder="Contoh: Nisfyu")
    no_alfamart = st.text_input("Nomor Member Alfamart", placeholder="Contoh: 899012345678")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Masuk ke Aplikasi"):
        if nama_user and no_alfamart:
            st.session_state.logged_in = True
            st.session_state.user_info = {"nama": nama_user, "alfamart": no_alfamart}
            st.session_state.step_app = 4
            st.success("🎉 Berhasil terhubung!")
            time.sleep(0.8)
            st.rerun()
        else:
            st.warning("⚠️ Mohon lengkapi nama dan nomor member terlebih dahulu!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAHAP 4: MAIN APP CONTAINER ---
else:
    st.markdown('<div style="padding-bottom: 
    
