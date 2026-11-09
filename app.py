import streamlit as st
import datetime
import time

# Konfigurasi Halaman
st.set_page_config(page_title="FlashMart iOS 27 Edition", page_icon="⚡", layout="centered")

# --- CSS KUSTOM GLASSMORPHISM & FLOATING DOCK ---
css_code = """
<style>
    .stApp {
        background: linear-gradient(135deg, #0B0E14 0%, #171A26 50%, #221533 100%);
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif !important;
        color: #F5F5F7;
    }

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

    .header-box {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(20px);
        border-radius: 18px;
        padding: 12px 16px;
        margin-bottom: 12px;
        border: 1px solid rgba(255, 255, 255, 0.12);
    }

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
        cursor: pointer;
    }

    .stButton button {
        background: linear-gradient(135deg, #007AFF 0%, #0056B3 100%);
        color: white !important;
        border-radius: 16px;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 12px 16px;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0, 122, 255, 0.4);
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
        "301": {"nama": "Air Mineral Aqua 600ml (1 Dus)", "kategori": "Minuman", "harga": 42000, "stok": 100},
        "302": {"nama": "Susu UHT Ultra Milk Full Cream 1L", "kategori": "Minuman", "harga": 19000, "stok": 50},
        "401": {"nama": "Kecap Manis Bango 550ml", "kategori": "Bumbu Dapur", "harga": 26000, "stok": 40},
        "501": {"nama": "Sabun Mandi Cair Lifebuoy 450ml", "kategori": "Perawatan Diri", "harga": 23000, "stok": 40},
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
        st.info("🛍️ Akses jutaan produk mulai dari sembako, makanan, hingga elektronik.")
    elif "2." in onboarding_page:
        st.info("⭐ Kumpulkan poin di setiap transaksi dan integrasikan dengan member Alfamart.")
    else:
        st.info("⚡ Pesanan diantar dengan kecepatan kilat langsung ke lokasimu!")

    st.markdown("<br>", unsafe_allow_html=True)
    _, col_btn = st.columns([1.5, 1])
    with col_btn:
        if st.button("Next ➔"):
            st.session_state.step_app = 3
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAHAP 3: AUTHENTICATION ---
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
    st.markdown('<div style="padding-bottom: 90px;">', unsafe_allow_html=True)
    
    user_nama = st.session_state.user_info.get('nama', 'User')
    user_member = st.session_state.user_info.get('alfamart', '-')
    user_poin = st.session_state.poin_member

    st.markdown('<div class="header-box">', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 12px; color: #A1A1A6;">📍 Lokasi Pengiriman</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-weight: 600; font-size: 14px; color: #FFFFFF;">Makassar, Sulawesi Selatan ⚡</div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-color: rgba(255,255,255,0.1); margin: 8px 0;">', unsafe_allow_html=True)
    st.markdown(f'<div style="display: flex; justify-content: space-between; align-items: center; font-size: 13px;"><span>Halo, <b>{user_nama}</b></span><span style="background: rgba(0,242,254,0.2); padding: 2px 8px; border-radius: 8px; color: #00F2FE; font-weight: 600;">⭐ {user_poin} Pts</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    jumlah_di_keranjang = len(st.session_state.keranjang)
    label_keranjang = "🛍️ Keranjang (" + str(jumlah_di_keranjang) + ")" if jumlah_di_keranjang > 0 else "🛍️ Keranjang"

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
            st.markdown(f"#### Hasil Pencarian untuk: '{keyword_cari}'")
            hasil_ketemu = False
            for kode, item in st.session_state.daftar_produk.items():
                if keyword_cari.lower() in item['nama'].lower():
                    hasil_ketemu = True
                    st.markdown(f'<div class="glass-card"><b>{item["nama"]}</b><br><span style="color: #00F2FE;">Rp {item["harga"]:,}</span></div>', unsafe_allow_html=True)
            if not hasil_ketemu:
                st.warning("❌ Produk tidak ditemukan.")
        else:
            st.markdown('<div class="glass-card" style="background: linear-gradient(135deg, #FF416C, #FF4B2B); text-align: center;"><h3 style="margin:0;">🔥 NASIONAL FLASH SALE</h3><p style="margin: 4px 0 0 0; font-size: 12px;">Diskon & Gratis Ongkir Kilat!</p></div>', unsafe_allow_html=True)
            
            st.markdown("### 🛒 Produk Unggulan")
            for kode, item in list(st.session_state.daftar_produk.items())[:4]:
                st.markdown(f'<div class="glass-card" style="display: flex; justify-content: space-between; align-items: center;"><div><b>{item["nama"]}</b><br><span style="color: #00F2FE; font-weight: 700;">Rp {item["harga"]:,}</span></div><div>Stok: {item["stok"]}</div></div>', unsafe_allow_html=True)

    elif "Belanja" in tab_pilihan:
        st.markdown("### 🛒 Katalog Produk")
        kategori_filter = st.selectbox("Pilih Kategori:", ["Semua", "Sembako", "Makanan", "Minuman", "Bumbu Dapur", "Perawatan Diri", "Kebutuhan Rumah", "Elektronik"])

        data_tabel = []
        for kode, item in st.session_state.daftar_produk.items():
            if kategori_filter == "Semua" or item["kategori"] == kategori_filter:
                data_tabel.append({
                    "Kode": kode,
                    "Produk": item["nama"],
                    "Kategori": item["kategori"],
                    "Harga": f"Rp {item['harga']:,}",
                    "Stok": item["stok"]
                })
        st.table(data_tabel)

        st.markdown("### ➕ Tambah ke Keranjang")
        pilihan_kode = st.selectbox("Pilih Kode Produk:", list(st.session_state.daftar_produk.keys()))
        jumlah_beli = st.number_input("Jumlah Beli:", min_value=1, value=1, step=1)

        produk_pilihan = st.session_state.daftar_produk[pilihan_kode]
        subtotal = produk_pilihan['harga'] * jumlah_beli
        st.write(f"Barang: **{produk_pilihan['nama']}** | Subtotal: **Rp {subtotal:,}**")

        if st.button("Masukkan ke Keranjang 🛍️"):
            if jumlah_beli > produk_pilihan['stok']:
                st.error("❌ Stok tidak mencukupi!")
            else:
                st.session_state.keranjang.append({
                    "kode": pilihan_kode,
                    "nama": produk_pilihan['nama'],
                    "jumlah": jumlah_beli,
                    "subtotal": subtotal
                })
                st.success(f"✅ **{produk_pilihan['nama']}** masuk keranjang!")

    elif "Keranjang" in tab_pilihan:
        st.markdown("### 🛍️ Keranjang Belanja Anda")
        if not st.session_state.keranjang:
            st.info("Keranjang belanja masih kosong.")
        else:
            total_belanja = 0
            for item_k in st.session_state.keranjang:
                total_belanja += item_k['subtotal']
                st.markdown(f'<div class="glass-card"><b>{item_k["nama"]}</b><br><span style="color: #00F2FE;">Jumlah: {item_k["jumlah"]} | Subtotal: Rp {item_k["subtotal"]:,}</span></div>', unsafe_allow_html=True)

            st.markdown(f"#### Total Pembayaran: Rp {total_belanja:,}")
            
            if st.button("Checkout & Bayar Sekarang ⚡"):
                poin_didapat = int(total_belanja // 10000)
                st.session_state.poin_member += poin_didapat
                
                waktu = datetime.datetime.now().strftime('%H:%M:%S')
                for item_k in st.session_state.keranjang:
                    st.session_state.daftar_produk[item_k['kode']]['stok'] -= item_k['jumlah']
                    st.session_state.riwayat_transaksi.append({
                        "waktu": waktu, "item": f"{item_k['nama']} (x{item_k['jumlah']})", "total": item_k['subtotal']
                    })
                
                st.session_state.keranjang = []
                st.success(f"🎉 Pembayaran Berhasil! +{poin_didapat} Poin ditambahkan.")
                time.sleep(1)
                st.rerun()

    elif "Promo" in tab_pilihan:
        st.markdown("### 🔥 Promo Spesial Hari Ini")
        st.markdown('<div class="glass-card"><h4>🎁 Voucher Diskon Belanja</h4><p style="color: #A1A1A6; font-size: 13px;">Gunakan kode <b>FLASHMARTINA</b> untuk diskon 25%!</p></div>', unsafe_allow_html=True)

    else:
        st.markdown("### 👤 Profil Pengguna")
        st.markdown(f'<div class="glass-card"><b>{user_nama}</b><br><span style="color: #A1A1A6; font-size: 13px;">No. Member: {user_member}</span><hr style="border-er: rgba(255,255,255,0.1);"><div style="font-size: 14px;">⭐ Poin: <b>{user_poin} Pts</b></div></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
            
