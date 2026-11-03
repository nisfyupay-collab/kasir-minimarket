import streamlit as st
import datetime

if 'daftar_produk' not in st.session_state:
    st.session_state.daftar_produk = {
        "101": {"nama": "Beras 5kg", "harga": 68000, "stok": 15},
        "102": {"nama": "Minyak Goreng 2L", "harga": 34000, "stok": 20},
        "103": {"nama": "Gula Pasir 1kg", "harga": 16000, "stok": 30},
        "104": {"nama": "Mie Instan", "harga": 3100, "stok": 100},
        "105": {"nama": "Air Mineral 600ml", "harga": 4000, "stok": 50}
    }

st.title("🛒 Aplikasi Kasir Minimarket")
st.write("Selamat datang! Pilih produk dan lakukan transaksi langsung dari sini.")

st.subheader("Daftar Produk Tersedia")
data_tabel = []
for kode, item in st.session_state.daftar_produk.items():
    data_tabel.append({
        "Kode": kode,
        "Nama Barang": item["nama"],
        "Harga (Rp)": f"{item['harga']:,}",
        "Stok": item["stok"]
    })
st.table(data_tabel)

st.subheader("Form Transaksi")
pilihan_kode = st.selectbox("Pilih Kode Barang:", list(st.session_state.daftar_produk.keys()))
jumlah_beli = st.number_input("Jumlah Beli:", min_value=1, value=1, step=1)

produk_pilihan = st.session_state.daftar_produk[pilihan_kode]
st.write(f"Barang dipilih: **{produk_pilihan['nama']}**")
st.write(f"Harga satuan: Rp {produk_pilihan['harga']:,}")

if st.button("Beli / Checkout"):
    if jumlah_beli > produk_pilihan['stok']:
        st.error(f"❌ Stok tidak cukup! Stok tersisa: {produk_pilihan['stok']}")
    else:
        st.session_state.daftar_produk[pilihan_kode]['stok'] -= jumlah_beli
        subtotal = produk_pilihan['harga'] * jumlah_beli
        st.success(f"✅ Berhasil membeli {jumlah_beli}x {produk_pilihan['nama']}!")
        st.info(f"Total yang harus dibayar: **Rp {subtotal:,}**")
        st.write(f"Waktu Transaksi: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
      
