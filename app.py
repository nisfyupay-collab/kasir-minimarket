import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIG HALAMAN ---
st.set_page_config(
    page_title="FlashMart Ultimate Pro",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (ANIMASI & STYLING SMOOTH) ---
st.markdown("""
<style>
    /* Transisi Halus Global */
    * {
        transition: all 0.25s ease-in-out;
    }

    :root {
        --primary-green: #03AC03;
        --primary-orange: #FF9800;
    }

    /* Tombol Utama Kustom */
    .stButton>button {
        background-color: var(--primary-green) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold !important;
        padding: 0.5rem 1rem !important;
        box-shadow: 0 4px 6px rgba(3, 172, 3, 0.2);
    }
    
    .stButton>button:hover {
        background-color: #028a02 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(3, 172, 3, 0.3);
    }

    /* Card Produk */
    .product-card {
        background: white;
        border-radius: 12px;
        padding: 16px;
        border: 1px solid #e0e0e0;
        margin-bottom: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    .product-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        border-color: var(--primary-green);
    }

    /* Struk Belanja Custom */
    .receipt-box {
        background-color: #fffbe6;
        border: 2px dashed var(--primary-orange);
        padding: 20px;
        border-radius: 10px;
        font-family: 'Courier New', Courier, monospace;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if 'cart' not in st.session_state:
    st.session_state.cart = []

if 'products' not in st.session_state:
    st.session_state.products = [
        {"id": 1, "nama": "Kopi Moka 250ml", "kategori": "Minuman", "harga": 12000, "stok": 15},
        {"id": 2, "nama": "Roti Tawar Premium", "kategori": "Makanan", "harga": 15000, "stok": 10},
        {"id": 3, "nama": "Keripik Kentang Keju", "kategori": "Camilan", "harga": 9500, "stok": 20},
        {"id": 4, "nama": "Susu UHT Cokelat 1L", "kategori": "Minuman", "harga": 18500, "stok": 8},
        {"id": 5, "nama": "Mie Instan Goreng", "kategori": "Makanan", "harga": 3100, "stok": 50},
        {"id": 6, "nama": "Sabun Mandi Cair 400ml", "kategori": "Kebutuhan Rumah", "harga": 24000, "stok": 12},
    ]

if 'transactions' not in st.session_state:
    st.session_state.transactions = []

# --- VOUCHER DISKON ---
VOUCHERS = {
    "FLASHMART10": 0.10,
    "HEMAT20": 0.20,
    "SUPER50": 0.50
}

# --- HEADER APLIKASI ---
st.title("🛒 FlashMart Ultimate Pro")
st.caption("Sistem Kasir Minimarket Modern dengan Manajemen Stok & Laporan Penjualan")
st.divider()

# --- SIDEBAR NAVIGASI ---
menu = st.sidebar.selectbox("📂 Menu Utama", ["Kasir (POS)", "Kelola Stok Produk", "Riwayat & Laporan Penjualan"])
st.sidebar.divider()
st.sidebar.info("💡 **Tips**: Gunakan menu 'Kelola Stok' untuk menambah produk baru ke dalam aplikasi.")

# ==================== MENU 1: KASIR (POS) ====================
if menu == "Kasir (POS)":
    col_produk, col_kasir = st.columns([1.6, 1.2])

    with col_produk:
        st.subheader("🛍️ Katalog Produk")
        
        c_search, c_filter = st.columns([2, 1])
        search_query = c_search.text_input("🔍 Cari produk...", "")
        categories = ["Semua"] + list(set([p["kategori"] for p in st.session_state.products]))
        selected_cat = c_filter.selectbox("📁 Kategori", categories)

        # Filter Logic
        filtered_products = st.session_state.products
        if selected_cat != "Semua":
            filtered_products = [p for p in filtered_products if p["kategori"] == selected_cat]
        if search_query:
            filtered_products = [p for p in filtered_products if search_query.lower() in p["nama"].lower()]

        # Grid Produk
        st.markdown("<br>", unsafe_allow_html=True)
        if not filtered_products:
            st.warning("Produk tidak ditemukan.")
        else:
            grid_cols = st.columns(2)
            for index, prod in enumerate(filtered_products):
                with grid_cols[index % 2]:
                    stok_badge = f"<span style='color: red;'>Stok menipis: {prod['stok']}</span>" if prod['stok'] <= 5 else f"Stok: {prod['stok']} unit"
                    st.markdown(f"""
                    <div class="product-card">
                        <span style="background: #e8f5e9; color: #2e7d32; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">{prod['kategori']}</span>
                        <h4 style="margin: 8px 0 4px 0;">{prod['nama']}</h4>
                        <p style="color: #FF9800; font-weight: bold; font-size: 16px; margin: 0;">Rp {prod['harga']:,}</p>
                        <small style="color: #757575;">{stok_badge}</small>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"➕ Tambah", key=f"btn_{prod['id']}"):
                        if prod['stok'] > 0:
                            existing = next((item for item in st.session_state.cart if item['id'] == prod['id']), None)
                            if existing:
                                existing['qty'] += 1
                            else:
                                st.session_state.cart.append({"id": prod['id'], "nama": prod['nama'], "harga": prod['harga'], "qty": 1})
                            prod['stok'] -= 1
                            st.toast(f"{prod['nama']} ditambahkan!", icon="✅")
                            st.rerun()
                        else:
                            st.error("Stok habis!")

    with col_kasir:
        st.subheader("📋 Keranjang Belanja")
        
        if not st.session_state.cart:
            st.info("Keranjang masih kosong. Silakan pilih produk.")
        else:
            for item in st.session_state.cart:
                c1, c2, c3 = st.columns([3, 1, 1])
                c1.write(f"**{item['nama']}**\nRp {item['harga']:,} x {item['qty']}")
                c2.write(f"**Rp {item['harga'] * item['qty']:,}**")
                if c3.button("❌", key=f"del_{item['id']}"):
                    for p in st.session_state.products:
                        if p['id'] == item['id']:
                            p['stok'] += item['qty']
                    st.session_state.cart.remove(item)
                    st.rerun()
            st.divider()

            # Voucher
            voucher_input = st.text_input("🏷️ Kode Voucher Diskon", "").upper()
            discount_rate = 0.0
            if voucher_input in VOUCHERS:
                discount_rate = VOUCHERS[voucher_input]
                st.success(f"Voucher Berhasil! Diskon {int(discount_rate * 100)}%")
            elif voucher_input != "":
                st.warning("Kode voucher tidak valid.")

            # Perhitungan Total
            subtotal = sum(item['harga'] * item['qty'] for item in st.session_state.cart)
            diskon = subtotal * discount_rate
            total_akhir = subtotal - diskon

            st.markdown(f"**Subtotal:** Rp {subtotal:,}")
            if diskon > 0:
                st.markdown(f"**Diskon:** -Rp {int(diskon):,}")
            st.markdown(f"### **Total: Rp {int(total_akhir):,}**")
            
            st.divider()
            bayar = st.number_input("💵 Uang Pembayaran (Rp)", min_value=0, step=1000)
            kembalian = bayar - total_akhir
            
            if bayar > 0:
                if kembalian >= 0:
                    st.success(f"Kembalian: **Rp {int(kembalian):,}**")
                else:
                    st.error(f"Uang kurang: **Rp {int(abs(kembalian)):,}**")

            if st.button("🏁 Selesaikan & Cetak Struk"):
                if bayar < total_akhir:
                    st.error("Gagal! Uang pembayaran belum cukup.")
                else:
                    st.balloons()
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    # Simpan ke riwayat transaksi
                    transaction_data = {
                        "Waktu": now,
                        "Total Item": sum(i['qty'] for i in st.session_state.cart),
                        "Total Belanja": int(total_akhir),
                        "Bayar": bayar,
                        "Kembalian": int(kembalian)
                    }
                    st.session_state.transactions.append(transaction_data)

                    # Tampilkan Struk
                    st.markdown("### 📄 Struk Pembayaran")
                    struk_html = f"""
                    <div class="receipt-box">
                        <h3 style="text-align: center; margin:0;">FLASHMART ULTIMATE</h3>
                        <p style="text-align: center; margin:0; font-size:12px;">Jl. Raya Minimarket No. 88</p>
                        <p style="text-align: center; font-size:12px;">{now}</p>
                        <hr>
                    """
                    for item in st.session_state.cart:
                        struk_html += f"<div style='display:flex; justify-content:space-between;'><span>{item['nama']} x{item['qty']}</span><span>Rp {item['harga']*item['qty']:,}</span></div>"
                    
                    struk_html += f"""
                        <hr>
                        <div style='display:flex; justify-content:space-between;'><span>Total:</span><span>Rp {int(total_akhir):,}</span></div>
                        <div style='display:flex; justify-content:space-between;'><span>Bayar:</span><span>Rp {bayar:,}</span></div>
                        <div style='display:flex; justify-content:space-between;'><span>Kembali:</span><span>Rp {int(kembalian):,}</span></div>
                        <hr>
                        <p style="text-align: center; margin-top:10px;">-- Terima Kasih Telah Berbelanja! --</p>
                    </div>
                    """
                    st.markdown(struk_html, unsafe_allow_html=True)
                    st.session_state.cart = []

# ==================== MENU 2: KELOLA STOK PRODUK ====================
elif menu == "Kelola Stok Produk":
    st.subheader("📦 Manajemen Stok & Tambah Produk Baru")
    
    with st.form("add_product_form"):
        st.markdown("#### Tambah Barang Baru ke Katalog")
        col1, col2 = st.columns(2)
        with col1:
            new_nama = st.text_input("Nama Produk")
            new_kategori = st.selectbox("Kategori", ["Makanan", "Minuman", "Camilan", "Kebutuhan Rumah", "Lainnya"])
        with col2:
            new_harga = st.number_input("Harga Satuan (Rp)", min_value=0, step=500)
            new_stok = st.number_input("Jumlah Stok Awal", min_value=1, step=1)
            
        submit_prod = st.form_submit_button("💾 Simpan Produk Baru")
        if submit_prod:
            if new_nama.strip() == "":
                st.error("Nama produk tidak boleh kosong!")
            else:
                new_id = len(st.session_state.products) + 1
                st.session_state.products.append({
                    "id": new_id,
                    "nama": new_nama,
                    "kategori": new_kategori,
                    "harga": new_harga,
                    "stok": new_stok
                })
                st.success(f"Produk '{new_nama}' berhasil ditambahkan!")

    st.divider()
    st.markdown("#### Daftar Stok Barang Saat Ini")
    df_prod = pd.DataFrame(st.session_state.products)
    st.dataframe(df_prod, use_container_width=True)

# ==================== MENU 3: RIWAYAT & LAPORAN PENJUALAN ====================
elif menu == "Riwayat & Laporan Penjualan":
    st.subheader("📊 Laporan & Riwayat Transaksi")
    
    if not st.session_state.transactions:
        st.info("Belum ada transaksi yang tercatat hari ini.")
    else:
        df_trans = pd.DataFrame(st.session_state.transactions)
        
        # Metrik Ringkasan
        total_omzet = df_trans['Total Belanja'].sum()
        total_trx = len(df_trans)
        
        m1, m2 = st.columns(2)
        m1.metric("💰 Total Omzet Penjualan", f"Rp {total_omzet:,}")
        m2.metric("🛍️ Total Transaksi Selesai", f"{total_trx} Transaksi")
        
        st.divider()
        st.markdown("#### Detail Log Transaksi")
        st.dataframe(df_trans, use_container_width=True)
                    
