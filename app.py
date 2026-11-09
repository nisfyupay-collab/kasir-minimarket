import streamlit as st
import datetime
import time

# Konfigurasi Halaman
st.set_page_config(page_title="FlashMart iOS Slate Edition", page_icon="⚡", layout="centered")

# --- INISIALISASI SESSION STATE ---
if 'step_app' not in st.session_state:
    st.session_state.step_app = 1  # 1: Splash Awal, 2: Login Slate, 3: Loading Masuk, 4: Main App

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
        "201": {"nama": "Mie Instan Indomie Goreng (1 Dus)", "kategori": "Makanan", "harga": 115000, "stok": 30},
        "301": {"nama": "Air Mineral Aqua 600ml (1 Dus)", "kategori": "Minuman", "harga": 42000, "stok": 100},
        "401": {"nama": "Kecap Manis Bango 550ml", "kategori": "Bumbu Dapur", "harga": 26000, "stok": 40},
        "501": {"nama": "Sabun Mandi Cair Lifebuoy 450ml", "kategori": "Perawatan Diri", "harga": 23000, "stok": 40}
    }

if 'poin_member' not in st.session_state:
    st.session_state.poin_member = 520

if 'riwayat_transaksi' not in st.session_state:
    st.session_state.riwayat_transaksi = []

# --- CSS STYLING & ANIMASI KUSTOM ---
css_code = """
<style>
    .stApp {
        background: linear-gradient(135deg, #090A0F 0%, #131722 50%, #1F1435 100%);
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif !important;
        color: #F5F5F7;
    }

    @keyframes iconMorph {
        0% { transform: scale(0.6) rotate(-10deg); opacity: 0; }
        50% { transform: scale(1.1) rotate(5deg); opacity: 1; }
        100% { transform: scale(1) rotate(0deg); opacity: 1; }
    }

    @keyframes pulseGlow {
        0% { filter: drop-shadow(0 0 10px rgba(0, 242, 254, 0.4)); }
        50% { filter: drop-shadow(0 0 30px rgba(0, 242, 254, 0.95)); }
        100% { filter: drop-shadow(0 0 10px rgba(0, 242, 254, 0.4)); }
    }

    .splash-icon-box {
        font-size: 80px;
        text-align: center;
        animation: iconMorph 1s cubic-bezier(0.175, 0.885, 0.32, 1.275) infinite alternate, pulseGlow 2s infinite ease-in-out;
        margin-bottom: 10px;
    }

    .slate-header {
        background: linear-gradient(180deg, #1A1D2A 0%, #090A0F 100%);
        border-bottom-left-radius: 35px;
        border-bottom-right-radius: 35px;
        padding: 35px 20px 25px 20px;
        text-align: center;
        margin-top: -60px;
        margin-left: -20px;
        margin-right: -20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-top: 1px solid rgba(255, 255, 255, 0.22);
        border-radius: 22px;
        padding: 18px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);
        margin-bottom: 14px;
        transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    .glass-card:active {
        transform: scale(0.97);
    }

    div.row-widget.stRadio > div {
        background: rgba(18, 20, 30, 0.88) !important;
        backdrop-filter: blur(35px) !important;
        -webkit-backdrop-filter: blur(35px) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 40px !important;
        padding: 6px 10px !important;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.75) !important;
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
        cursor: pointer;
    }

    .stButton button {
        background: linear-gradient(135deg, #007AFF 0%, #0056B3 100%);
        color: white !important;
        border-radius: 16px;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.25);
        padding: 12px 16px;
        width: 100%;
        box-shadow: 0 6px 20px rgba(0, 122, 255, 0.45);
        transition: transform 0.15s cubic-bezier(0.34, 1.56, 0.64, 1), background 0.3s ease;
        cursor: pointer;
    }

    .stButton button:hover {
        background: linear-gradient(135deg, #0056B3 100%, #003D82 100%);
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

# --- TAHAP 1: SPLASH SCREEN UTAMA ---
if st.session_state.step_app == 1:
    st.markdown('<div class="glass-card" style="text-align: center; padding: 60px 20px; margin-top: 40px;">', unsafe_allow_html=True)
    st.markdown('<div class="splash-icon-box">🛵⚡</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-weight: 800; font-size: 40px; background: linear-gradient(90deg, #00F2FE, #4FACFE); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0;">FlashMart</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #A1A1A6; font-size: 14px; margin-top: 6px;">Next-Gen On-Demand Retail Experience</p>', unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Mulai Belanja ➔"):
        st.session_state.step_app = 2
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAHAP 2: AUTH / LOGIN (GAYA SLATE APP MELENGKUNG) ---
elif st.session_state.step_app == 2 and not st.session_state.logged_in:
    st.markdown('<div class="slate-header">', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size: 30px; font-weight: 800; letter-spacing: 2px; color: #FFFFFF; margin: 0;">F L A S H M A R T</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #8E8E93; font-size: 13px; margin-top: 4px;">Masuk dan sinkronkan member Alfamart kamu.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #FFFFFF; margin-top:0;">🔐 Login Akun</h3>', unsafe_allow_html=True)
    
    nama_user = st.text_input("Nama Lengkap / Akun Google", placeholder="Contoh: Nisfyu")
    no_alfamart = st.text_input("Nomor Member Alfamart", placeholder="Contoh: 899012345678")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Masuk ke Aplikasi ➔"):
        if nama_user and no_alfamart:
            st.session_state.logged_in = True
            st.session_state.user_info = {"nama": nama_user, "alfamart": no_alfamart}
            st.session_state.step_app = 3  # Menuju Tahap Splash Animasi Masuk
            st.rerun()
        else:
            st.warning("⚠️ Mohon lengkapi nama dan nomor member terlebih dahulu!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAHAP 3: ANIMASI SPLASH PEMBUKAAN SETELAH LOGIN ---
elif st.session_state.step_app == 3:
    st.markdown('<div class="glass-card" style="text-align: center; padding: 60px 20px; margin-top: 50px;">', unsafe_allow_html=True)
    st.markdown('<div class="splash-icon-box">⚡🛒</div>', unsafe_allow_html=True)
    st.markdown(f'<h2 style="color: #00F2FE; margin-top: 10px;">Halo, {st.session_state.user_info.get("nama", "User")}!</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color: #A1A1A6; font-size: 14px;">Menyiapkan toko kilat untukmu...</p>', unsafe_allow_html=True)
    
    # Progress Bar Animasi Masuk
    bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        bar.progress(i + 1)
        
    st.session_state.step_app = 4  # Masuk ke Aplikasi Utama
    st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAHAP 4: MAIN APP CONTAINER ---
else:
    st.markdown('<div style="padding-bottom: 90px;">', unsafe_allow_html=True)
    
    user_nama = st.session_state.user_info.get('nama', 'User')
    user_member = st.session_state.user_info.get('alfamart', '-')
    user_poin = st.session_state.poin_member

    st.markdown('<div class="glass-card" style="padding: 14px 18px;">', unsafe_allow_html=True)
    st.markdown(f'<div style="display: flex; justify-content: space-between; align-items: center;"><div><b>{user_nama}</b><br><span style="color: #8E8E93; font-size: 12px;">Member: {user_member}</span></div><span style="background: rgba(0,242,254,0.18); padding: 4px 10px; border-radius: 12px; color: #00F2FE; font-weight: 600;">⭐ {user_poin} Pts</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    jumlah_di_keranjang = len(st.session_state.keranjang)
    label_keranjang = "🛍️ (" + str(jumlah_di_keranjang) + ")" if jumlah_di_keranjang > 0 else "🛍️ Keranjang"

    tab_pilihan = st.radio(
        "Navigasi:", 
        ["🏠 Beranda", "🛒 Belanja", label_keranjang, "🔥 Promo", "👤 Akun"],
        horizontal=True,
        label_visibility="collapsed"
    )
    st.markdown("<br>", unsafe_allow_html=True)

    if "Beranda" in tab_pilihan:
        st.markdown("### 🔍 Cari Produk")
        keyword_cari = st.text_input("Cari produk...", placeholder="Ketik nama produk...", label_visibility="collapsed")
        
        if keyword_cari:
            for kode, item in st.session_state.daftar_produk.items():
                if keyword_cari.lower() in item['nama'].lower():
                    st.markdown(f'<div class="glass-card"><b>{item["nama"]}</b><br><span style="color: #00F2FE;">Rp {item["harga"]:,}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="glass-card" style="background: linear-gradient(135deg, #FF416C, #FF4B2B); text-align: center;"><h3 style="margin:0; color:white;">🔥 FLASH SALE SEKARANG</h3><p style="margin:4px 0 0 0; font-size:12px; color:white;">Bebas ongkir kilat seluruh Indonesia!</p></div>', unsafe_allow_html=True)
            for kode, item in list(st.session_state.daftar_produk.items())[:3]:
                st.markdown(f'<div class="glass-card" style="display: flex; justify-content: space-between;"><div><b>{item["nama"]}</b><br><span style="color: #00F2FE;">Rp {item["harga"]:,}</span></div><div>Stok: {item["stok"]}</div></div>', unsafe_allow_html=True)

    elif "Belanja" in tab_pilihan:
        st.markdown("### 🛒 Katalog Produk")
        pilihan_kode = st.selectbox("Pilih Kode Produk:", list(st.session_state.daftar_produk.keys()))
        jumlah_beli = st.number_input("Jumlah Beli:", min_value=1, value=1, step=1)
        produk_pilihan = st.session_state.daftar_produk[pilihan_kode]
        subtotal = produk_pilihan['harga'] * jumlah_beli

        if st.button("Masukkan ke Keranjang 🛍️"):
            st.session_state.keranjang.append({
                "kode": pilihan_kode, "nama": produk_pilihan['nama'], "jumlah": jumlah_beli, "subtotal": subtotal
            })
            st.success(f"✅ **{produk_pilihan['nama']}** masuk keranjang!")

    elif "🛍️" in tab_pilihan:
        st.markdown("### 🛍️ Keranjang Belanja")
        if not st.session_state.keranjang:
            st.info("Keranjang belanja masih kosong.")
        else:
            total_belanja = 0
            for item_k in st.session_state.keranjang:
                total_belanja += item_k['subtotal']
                st.markdown(f'<div class="glass-card"><b>{item_k["nama"]}</b><br><span style="color: #00F2FE;">Jumlah: {item_k["jumlah"]} | Subtotal: Rp {item_k["subtotal"]:,}</span></div>', unsafe_allow_html=True)

            if st.button("Checkout Sekarang ⚡"):
                st.session_state.keranjang = []
                st.success("🎉 Pembayaran Berhasil!")
                time.sleep(1)
                st.rerun()

    elif "Promo" in tab_pilihan:
        st.markdown("### 🔥 Promo Spesial Hari Ini")
        st.markdown('<div class="glass-card"><h4>🎁 Voucher Diskon Belanja</h4><p style="color: #A1A1A6; font-size: 13px;">Gunakan kode <b>FLASHMARTINA</b></p></div>', unsafe_allow_html=True)

    else:
        st.markdown("### 👤 Profil Pengguna")
        st.markdown(f'<div class="glass-card"><b>{user_nama}</b><br><span style="color: #A1A1A6; font-size: 13px;">No. Member: {user_member}</span></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    
