import streamlit as st
import datetime
import time

# Konfigurasi halaman
st.set_page_config(page_title="FlashMart Mobile", page_icon="⚡", layout="centered")

# --- KODE CSS KUSTOM ALA iOS & ONBOARDING ---
st.markdown("""
<style>
    .stApp {
        background-color: #F2F2F7;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Tombol Kustom Ala iOS */
    .stButton button {
        background-color: #007AFF;
        color: white;
        border-radius: 12px;
        font-weight: 600;
        border: none;
        padding: 10px 20px;
        width: 100%;
    }
    .stButton button:hover {
        background-color: #0056B3;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- INISIALISASI SESSION STATE UNTUK ALUR APLIKASI ---
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
    st.session_state.poin_member = 300

if 'riwayat_transaksi' not in st.session_state:
    st.session_state.riwayat_transaksi = []


# --- TAHAP 1: SPLASH SCREEN (LOGO MOTOR OJOL & PETIR) ---
if st.session_state.step_app == 1:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h1 style="font-size: 60px; margin: 0;">🛵⚡</h1>
            <h1 style="font-size: 36px; font-weight: 800; color: #1C1C1E; margin-top: 10px;">FlashMart</h1>
            <p style="color: #8E8E93; font-size: 16px;">Super Cepat, Super Praktis</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Mulai Sekarang ➔"):
        st.session_state.step_app = 2
        st.rerun()

# --- TAHAP 2: ONBOARDING / PETUNJUK APLIKASI (DENGAN TOMBOL NEXT) ---
elif st.session_state.step_app == 2:
    st.markdown("### 📖 Panduan FlashMart")
    
    # Kita buat slider/halaman petunjuk sederhana
    sub_step = st.selectbox("Pilih Halaman Petunjuk:", [
        "1. Belanja Kebutuhan Harian", 
        "2. Kumpulkan Poin & Hadiah", 
        "3. Pengiriman Super Kilat"
    ])
    
    if "1." in sub_step:
        st.info("🛍️ Temukan berbagai produk sembako, makanan, dan minuman lengkap layaknya minimarket modern dalam satu genggaman.")
    elif "2." in sub_step:
        st.info("⭐ Setiap transaksi belanja akan otomatis menambahkan poin member yang bisa disinkronkan dengan akun Alfamart.")
    else:
        st.info("⚡ Pesanan diantar dengan kecepatan kilat ala ojol berbalut teknologi mutakhir langsung ke tempatmu!")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tombol Next di pojok kanan bawah (menggunakan kolom)
    col_spacer, col_btn = st.columns([2, 1])
    with col_btn:
        if st.button("Next ➔"):
            st.session_state.step_app = 3
            st.rerun()

# --- TAHAP 3: HALAMAN LOGIN / SIGN UP ---
elif st.session_state.step_app == 3 and not st.session_state.logged_in:
    st.markdown("### 🔐 Masuk / Daftar Akun")
    st.markdown("<p style='color: #8E8E93; font-size: 14px;'>Hubungkan akun Google dan member Alfamart kamu.</p>", unsafe_allow_html=True)
    
    nama_user = st.text_input("Nama Lengkap", placeholder="Contoh: Nisfyu")
    no_alfamart = st.text_input("Nomor Member Alfamart", placeholder="Contoh: 899012345678")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Masuk ke Aplikasi"):
        if nama_user and no_alfamart:
            st.session_state.logged_in = True
            st.session_state.user_info = {"nama": nama_user, "alfamart": no_alfamart}
            st.session_state.step_app = 4
            st.success("🎉 Berhasil masuk!")
            time.sleep(0.8)
            st.rerun()
        else:
            st.warning("⚠️ Mohon lengkapi nama dan nomor member terlebih dahulu!")

# --- TAHAP 4: HALAMAN UTAMA APLIKASI (BERANDA & KATALOG) ---
else:
    st.markdown(f"""
        <div style="padding: 5px 0;">
            <h3 style="margin: 0; color: #1C1C1E;">⚡ FlashMart Mobile</h3>
            <p style="color: #8E8E93; margin: 0; font-size: 13px;">Halo, <b>{st.session_state.user_info.get('nama', 'User')}</b> | Member: {st.session_state.user_info.get('alfamart', '-')}</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    # Kartu Poin Member
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
            st.success(f"✅ Transaksi Berhasil! +{poin_didapat} Poin ditambahkan.")

    if st.session_state.riwayat_transaksi:
        st.markdown("### 📜 Riwayat Sesi Ini")
        for r in reversed(st.session_state.riwayat_transaksi):
            st.text(f"[{r['waktu']}] {r['item']} - Rp {r['total']:,}")
            
