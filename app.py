import streamlit as st
import datetime
import time

# Konfigurasi halaman
st.set_page_config(page_title="FlashMart iOS Edition", page_icon="⚡", layout="centered")

# --- KODE CSS KUSTOM & ANIMASI KETIK + SLIDE ---
st.markdown("""
<style>
    .stApp {
        background-color: #F8F9FA;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #111111;
    }

    /* Animasi Pergeseran Halaman (Slide In) */
    @keyframes slideInRight {
        0% { opacity: 0; transform: translateX(50px); }
        100% { opacity: 1; transform: translateX(0); }
    }

    .slide-container {
        animation: slideInRight 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    /* Animasi Motor Ojol & Petir */
    @keyframes driveIn {
        0% { opacity: 0; transform: translateX(-80px) scale(0.8); }
        100% { opacity: 1; transform: translateX(0) scale(1); }
    }

    @keyframes pulseGlow {
        0% { transform: scale(1); filter: drop-shadow(0 0 4px rgba(255, 193, 7, 0.6)); }
        50% { transform: scale(1.15); filter: drop-shadow(0 0 15px rgba(255, 193, 7, 0.9)); }
        100% { transform: scale(1); filter: drop-shadow(0 0 4px rgba(255, 193, 7, 0.6)); }
    }

    .splash-logo {
        font-size: 70px;
        text-align: center;
        animation: driveIn 1s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        margin-bottom: 10px;
    }

    .lightning-effect {
        display: inline-block;
        animation: pulseGlow 1.4s infinite ease-in-out;
    }

    /* Efek Animasi Penulisan / Ketik Teks (Typing Effect) */
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }

    @keyframes blinkCaret {
        from, to { border-color: transparent; }
        50% { border-color: #007AFF; }
    }

    .typing-title {
        font-weight: 800;
        font-size: 38px;
        color: #000000;
        text-align: center;
        overflow: hidden;
        white-space: nowrap;
        margin: 0 auto;
        border-right: 3px solid #007AFF;
        width: 11ch; /* Menyesuaikan panjang teks FlashMart */
        animation: typing 1.5s steps(11, end), blinkCaret 0.75s step-end infinite;
    }

    .splash-subtitle {
        text-align: center;
        color: #555555;
        font-size: 16px;
        font-weight: 500;
        margin-top: 12px;
        animation: slideInRight 1.2s ease-out forwards;
    }

    /* Memastikan semua teks terlihat jelas */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #111111 !important;
    }

    /* Tombol Kustom Ala iOS */
    .stButton button {
        background-color: #007AFF;
        color: white !important;
        border-radius: 14px;
        font-weight: 600;
        border: none;
        padding: 12px 20px;
        width: 100%;
        box-shadow: 0 4px 12px rgba(0, 122, 255, 0.3);
    }
    .stButton button:hover {
        background-color: #0056B3;
        color: white !important;
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


# --- TAHAP 1: SPLASH SCREEN (DENGAN ANIMASI KETIK & MOTOR) ---
if st.session_state.step_app == 1:
    st.markdown('<div class="slide-container">', unsafe_allow_html=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="splash-logo">
            🛵<span class="lightning-effect">⚡</span>
        </div>
        <div style="display: flex; justify-content: center;">
            <div class="typing-title">FlashMart</div>
        </div>
        <div class="splash-subtitle">Belanja Super Kilat & Praktis Ala iOS</div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    if st.button("Mulai Sekarang ➔"):
        st.session_state.step_app = 2
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAHAP 2: ONBOARDING (DENGAN EFEK SLIDE MASUK) ---
elif st.session_state.step_app == 2:
    st.markdown('<div class="slide-container">', unsafe_allow_html=True)
    st.markdown("### ✨ Kenali FlashMart")
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
        st.info("🛍️ Akses berbagai produk sembako, makanan, dan minuman harian berkualitas langsung dari genggaman HP-mu.")
    elif "2." in onboarding_page:
        st.info("⭐ Kumpulkan poin di setiap transaksi dan nikmati sinkronisasi otomatis dengan akun member Alfamart.")
    else:
        st.info("⚡ Pesanan diantar dengan kecepatan maksimal layaknya ojol berteknologi kilat!")

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    _, col_btn = st.columns([1.5, 1])
    with col_btn:
        if st.button("Next ➔"):
            st.session_state.step_app = 3
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAHAP 3: LOGIN / SIGN UP ---
elif st.session_state.step_app == 3 and not st.session_state.logged_in:
    st.markdown('<div class="slide-container">', unsafe_allow_html=True)
    st.markdown("### 🔐 Masuk / Daftar Akun")
    st.markdown("<p style='color: #444444; font-size: 14px;'>Hubungkan akun Google dan member Alfamart kamu.</p>", unsafe_allow_html=True)
    
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
            st.warning("⚠️ Mohon lengkapi nama dan nomor member terlebih dahulu ya!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAHAP 4: HALAMAN UTAMA ---
else:
    st.markdown('<div class="slide-container">', unsafe_allow_html=True)
    st.markdown(f"""
        <div style="padding: 5px 0;">
            <h3 style="margin: 0; color: #111111;">⚡ FlashMart Mobile</h3>
            <p style="color: #555555; margin: 0; font-size: 13px;">Halo, <b>{st.session_state.user_info.get('nama', 'User')}</b> | Member: {st.session_state.user_info.get('alfamart', '-')}</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.info("👤 **Tier:** Gold Member")
    with col2:
        st.success(f"⭐ **Poin:** {st.session_state.poin_member} Pts")

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
            st.success(f"✅ Transaksi Berhasil! +{poin_didapat} Poin ditambahkan ke sistem Alfamart.")

    if st.session_state.riwayat_transaksi:
        st.markdown("### 📜 Riwayat Sesi Ini")
        for r in reversed(st.session_state.riwayat_transaksi):
            st.text(f"[{r['waktu']}] {r['item']} - Rp {r['total']:,}")
    st.markdown('</div>', unsafe_allow_html=True)
    
