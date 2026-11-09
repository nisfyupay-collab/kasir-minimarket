import streamlit as st
import datetime

# Konfigurasi halaman
st.set_page_config(page_title="FlashMart", page_icon="⚡", layout="centered")

# Inisialisasi Session State untuk Produk, Keranjang, dan Poin Member
if 'daftar_produk' not in st.session_state:
    st.session_state.daftar_produk = {
        "101": {"nama": "Beras Premium 5kg", "kategori": "Sembako", "harga": 68000, "stok": 15},
        "102": {"nama": "Minyak Goreng 2L", "kategori": "Sembako", "harga": 34000, "stok": 20},
        "103": {"nama": "Gula Pasir 1kg", "kategori": "Sembako", "harga": 16000, "stok": 30},
        "104": {"nama": "Mie Instan (1 Dus)", "kategori": "Makanan", "harga": 95000, "stok": 10},
        "105": {"nama": "Air Mineral 600ml", "kategori": "Minuman", "harga": 4000, "stok": 50}
    }

if 'poin_member' not in st.session_state:
    st.session_state.poin_member = 150  # Bonus poin member awal ala FlashMart

if 'riwayat_transaksi' not in st.session_state:
    st.session_state.riwayat_transaksi = []

# Header / Tampilan Utama ala FlashMart
st.title("⚡ FlashMart Mobile")
st.markdown("---")

# Kartu Informasi Member
col1, col2 = st.columns(2)
with col1:
    st.info("👤 **Status:** Flash Member")
with col2:
    st.success(f"⭐ **Poin Anda:** {st.session_state.poin_member} Poin")

st.markdown("### 🛒 Katalog Produk")

# Filter Kategori
kategori_pilihan = st.selectbox("Pilih Kategori:", ["Semua", "Sembako", "Makanan", "Minuman"])

# Tampilkan Produk dalam bentuk tabel rapi
data_tabel = []
for kode, item in st.session_state.daftar_produk.items():
    if kategori_pilihan == "Semua" or item["kategori"] == kategori_pilihan:
        data_tabel.append({
            "Kode": kode,
            "Nama Produk": item["nama"],
            "Kategori": item["kategori"],
            "Harga (Rp)": f"Rp {item['harga']:,}",
            "Stok": item["stok"]
        })

st.table(data_tabel)

# Form Transaksi / Belanja
st.markdown("### 💳 Form Transaksi")
pilihan_kode = st.selectbox("Pilih Kode Barang:", list(st.session_state.daftar_produk.keys()))
jumlah_beli = st.number_input("Jumlah Beli:", min_value=1, value=1, step=1)

produk_pilihan = st.session_state.daftar_produk[pilihan_kode]
subtotal = produk_pilihan['harga'] * jumlah_beli

st.write(f"Barang dipilih: **{produk_pilihan['nama']}**")
st.write(f"Subtotal: **Rp {subtotal:,}**")

if st.button("Bayar / Checkout"):
    if jumlah_beli > produk_pilihan['stok']:
        st.error(f"❌ Stok tidak cukup! Stok tersisa: {produk_pilihan['stok']}")
    else:
        # Kurangi stok
        st.session_state.daftar_produk[pilihan_kode]['stok'] -= jumlah_beli
        
        # Tambah poin member
        poin_didapat = int(subtotal // 10000)
        st.session_state.poin_member += poin_didapat
        
        # Catat riwayat
        waktu = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        st.session_state.riwayat_transaksi.append({
            "waktu": waktu,
            "item": produk_pilihan['nama'],
            "jumlah": jumlah_beli,
            "total": subtotal
        })
        
        st.success(f"✅ Transaksi Berhasil! Kamu Mendapatkan {poin_didapat} Poin 🎉")
        st.info(f"Total Bayar: **Rp {subtotal:,}** | Poin Total Sekarang: **{st.session_state.poin_member}**")

# Riwayat Belanja Terakhir
if st.session_state.riwayat_transaksi:
    st.markdown("### 📜 Riwayat Transaksi Sesi Ini")
    for r in reversed(st.session_state.riwayat_transaksi):
        st.text(f"[{r['waktu']}] Beli {r['jumlah']}x {r['item']} - Rp {r['total']:,}")
    
