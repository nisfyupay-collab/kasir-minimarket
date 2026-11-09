import streamlit as st
import datetime
import time

# Konfigurasi halaman
st.set_page_config(page_title="FlashMart iOS Edition", page_icon="⚡", layout="centered")

# --- KODE CSS KUSTOM ALA iOS & ANIMASI PEMBUKA ---
st.markdown("""
<style>
    /* Background dan Tema Umum */
    .stApp {
        background-color: #F2F2F7;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Animasi Splash Screen / Welcome */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .welcome-container {
        text-align: center;
        padding: 40px 20px;
        animation: fadeIn 1.2s ease-in-out;
    }
    
    .welcome-title {
        font-size: 28px;
        font-weight: 300;
        color: #8E8E93;
        letter-spacing: 1px;
    }
    
    .brand-title {
        font-size: 42px;
        font-weight: 700;
        color: #000000;
        margin-top: -5px;
    }

    /* Kartu Produk ala iOS Glassmorphism */
    .ios-card {
        background: rgba(255, 255, 255, 0.8);
        padding: 16px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        margin-bottom: 12px;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# --- INISISASI SESSION STATE ---
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
    st.session_state.poin_member = 250

if 'riwayat_transaksi' not in st.session_state:
    st.session_state.riwayat_transaksi = []

# --- HALAMAN LOGIN / AUTHENTICATION (GOOGLE & ALFAMART) ---
if not st.session_state.logged_in:
    st.markdown("""
        <div class="welcome-container">
            <div class="welcome-title">Welcome to</div>
            <div class="brand-title">⚡ FlashMart</div>
            <p style="color: #6C6C70; margin-top: 10px;">Next-Gen Mobile Shopping Experience</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔐 Masuk ke Akun Anda")
    nama_user = st.text_input("Nama Lengkap / Akun Google", placeholder="Contoh: Nisfyu")
    no_alfamart = st.text_input("Nomor Member Alfamart / Alfacart", placeholder="Contoh: 899012345678")
    
    if st.button("Masuk dengan Akun & Sinkronisasi", use_container_width=True):
        if nama_user and no_alfamart:
            st.session_state.logged_in = True
            st.session_state.user_info = {
                "nama": nama_user,
                "alfamart": no_alfamart
            }
            st.success("🎉 Berhasil terhubung ke Google & Sistem Alfamart!")
            time.sleep(1)
            st.rerun()
        else:
            st.warning("⚠️ Mohon isi nama dan nomor member terlebih dahulu ya!")

else:
    # --- HALAMAN UTAMA APLIKASI SETELAH LOGIN ---
    
    # Header ala iOS
    st.markdown(f"""
        <div style="padding: 10px 0;">
            <h2 style="margin: 0; color: #1C1C1E;">⚡ FlashMart</h2>
            <p style="color: #8E8E93; margin: 0; font-size: 14px;">Halo, <b>{st.session_state.user_info['nama']}</b> | Member: {st.session_state.user_info['alfamart']}</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    # Kartu Poin Member (Glassmorphism Style)
    col1, col2 = st.columns(2)
    with col1:
        st.info("👤 **Tier:** Gold Member")
    with col2:
        st.success(f"⭐ **Poin:** {st.session_state.poin_member} Pts")

    st.markdown("### 🛒 Katalog Produk")
    
    # Filter Kategori
    kategori_pilihan = st.selectbox("Kategori Pilihan:", ["Semua", "Sembako", "Makanan", "Minuman"])

    # Tampilkan Produk
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

    # Form Transaksi
    st.markdown("### 💳 Checkout Belanja")
    pilihan_kode = st.selectbox("Pilih Kode Produk:", list(st.session_state.daftar_produk.keys()))
    jumlah_beli = st.number_input("Jumlah:", min_value=1, value=1, step=1)

    produk_pilihan = st.session_state.daftar_produk[pilihan_kode]
    subtotal = produk_pilihan['harga'] * jumlah_beli

    st.write(o:=f"Barang: **{produk_pilihan['nama']}** | Subtotal: **Rp {subtotal:,}**")

    if st.button("Bayar Sekarang", use_container_width=True):
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

    # Riwayat Transaksi
    if st.session_state.riwayat_transaksi:
        st.markdown("### 📜 Riwayat Sesi Ini")
        for r in reversed(st.session_state.riwayat_transaksi):
            st.text(f"[{r['waktu']}] {r['item']} - Rp {r['total']:,}")
            
