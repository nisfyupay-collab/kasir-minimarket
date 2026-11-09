import streamlit as st
import datetime
import time

# Konfigurasi halaman
st.set_page_config(page_title="FlashMart iOS 27 Edition", page_icon="⚡", layout="centered")

# --- KODE CSS KUSTOM: GRADASI MEWAH & EFEK GLASSMORPHISM (BLUR ALA IPHONE) ---
st.markdown("""
<style>
    /* Latar Belakang Gradasi Mewah */
    .stApp {
        background: linear-gradient(135deg, #0A0A12 0%, #1A1C29 50%, #2A1B3D 100%);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #F5F5F7;
    }

    /* Efek Kartu Kaca (Glassmorphism Blur) */
    .glass-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 16px;
    }

    /* Animasi Pergeseran Halaman (Slide In) */
    @keyframes slideInUp {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .slide-container {
        animation: slideInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    /* Animasi Motor Ojol & Petir */
    @keyframes driveIn {
        0% { opacity: 0; transform: translateX(-60px) scale(0.8); }
        100% { opacity: 1; transform: translateX(0) scale(1); }
    }

    @keyframes pulseGlow {
        0% { transform: scale(1); filter: drop-shadow(0 0 8px rgba(0, 242, 254, 0.6)); }
        50% { transform: scale(1.12); filter: drop-shadow(0 0 22px rgba(0, 242, 254, 0.95)); }
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
        letter-spacing: 0.5px;
    }

    /* Memastikan teks terlihat kontras dan jelas */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #F5F5F7 !important;
    }

    /* Tombol Kustom Ala iOS Glass */
    .stButton button {
        background: linear-gradient(135deg, #007AFF 0%, #0056B3 100%);
        color: white !important;
        border-radius: 16px;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 12px 20px;
        width: 100%;
        box-shadow: 0 4px 20px rgba(0, 122, 255, 0.4);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #0056B3 0%, #003D82 100%);
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

if 'daftar_produk' not in st.session_state:
    st.session_state.daftar_produk = {
        "101": {"nama": "Beras Premium 5kg", "kategori": "Sembako", "harga": 68000, "stok": 15},
        "102": {"nama": "Minyak Goreng 2L", "kategori": "Sembako", "harga": 34000, "stok": 20},
        "103": {"nama": "Gula Pasir 1kg", "kategori": "Sembako", "harga": 16000, "stok": 30},
        "104": {"nama": "Mie Instan (1 Dus)", "kategori": "Makanan", "harga": 95000, "stok": 10},
        "105": {"nama": "Air Mineral 600ml", "kategori": "Minuman", "harga": 4000, "stok": 50}
    }

if 'poin_member' not in st.session_state:
    st.session_state.poin_member = 350

if 'riwayat_transaksi' not in st.session_state:
    st.session_state.riwayat_transaksi = []


# --- TAHAP 1: SPLASH SCREEN ---
if st.session_state.step_app == 1:
    st.markdown('<div class="slide-container"><div class="glass-card" style="text-align: center; padding: 40px 20px;">', unsafe_allow_html=True)
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
    st.markdown("<h3 style='text-align: center;'>✨ Panduan FlashMart</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    onboarding_page = st.radio(
        "Pilih Petunjuk:", 
        [
            "1. Belanja Kebutuhan Harian Lengkap", 
            "2. Poin Member & Sinkronisasi Alfamart", 
            "3. Pengiriman Kilat Motor Petir"
        ]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    if "1." in onboarding_page:
        st.info("🛍️ Akses berbagai produk sembako dan kebutuhan harian langsung dari genggaman.")
    elif "2." in onboarding_page:
        st.info("⭐ Kumpulkan poin dan nikmati sinkronisasi otomatis dengan akun member Alfamart.")
    else:
        st.info("⚡ Pesanan diantar dengan kecepatan maksimal ala motor petir ojol!")

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
    st.markdown("<h3>🔐 Masuk / Daftar Akun</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #A1A1A6; font-size: 13px;'>Hubungkan akun Google dan member Alfamart kamu.</p>", unsafe_allow_html=True)
    
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
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- TAHAP 4: HALAMAN UTAMA ---
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

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 🛒 Katalog Produk")
    kategori_pilihan = st.selectbox("Kategori:", ["Semua", "Sembako", "Makanan", "Minuman"])

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

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 💳 Checkout Belanja")
    pilihan_kode = st.selectbox("Pilih Kode Produk:", list(st.session_state.daftar_produk.keys()))
    jumlah_beli = st.number_input("Jumlah:", min_value=1, value=1, step=1)

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
            st.success(f"✅ Transaksi Berhasil! +{poin_didapat} Poin ditambahkan.")

    if st.session_state.riwayat_transaksi:
        st.markdown("---")
        st.markdown("### 📜 Riwayat Sesi Ini")
        for r in reversed(st.session_state.riwayat_transaksi):
            st.text(f"[{r['waktu']}] {r['item']} - Rp {r['total']:,}")
    st.markdown('</div></div>', unsafe_allow_html=True)
    
