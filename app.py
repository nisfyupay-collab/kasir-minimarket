import streamlit as st
import datetime
import time

st.set_page_config(page_title="FlashMart iOS Slate Edition", page_icon="⚡", layout="centered")

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
        "101": {
            "nama": "Beras Premium Sania 5kg", 
            "kategori": "Sembako", 
            "harga": 68000, 
            "stok": 50, 
            "foto": "https://images.unsplash.com/photo-1586201375761-83865001e31c?auto=format&fit=crop&w=400&q=80"
        },
        "102": {
            "nama": "Minyak Goreng Bimoli 2L", 
            "kategori": "Sembako", 
            "harga": 34000, 
            "stok": 60, 
            "foto": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=400&q=80"
        },
        "103": {
            "nama": "Gula Pasir Gulaku 1kg", 
            "kategori": "Sembako", 
            "harga": 16500, 
            "stok": 80, 
            "foto": "https://images.unsplash.com/photo-1581441363689-1f3c3c3dbf91?auto=format&fit=crop&w=400&q=80"
        },
        "201": {
            "nama": "Mie Instan Indomie Goreng (1 Dus)", 
            "kategori": "Makanan", 
            "harga": 115000, 
            "stok": 30, 
            "foto": "https://images.unsplash.com/photo-1612929633738-8fe46f7ec841?auto=format&fit=crop&w=400&q=80"
        },
        "202": {
            "nama": "Biskuit Cokelat Roma Kelapa", 
            "kategori": "Makanan", 
            "harga": 12500, 
            "stok": 45, 
            "foto": "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?auto=format&fit=crop&w=400&q=80"
        },
        "301": {
            "nama": "Air Mineral Aqua 600ml (1 Dus)", 
            "kategori": "Minuman", 
            "harga": 42000, 
            "stok": 100, 
            "foto": "https://images.unsplash.com/photo-1548839140-29a749e1cf4d?auto=format&fit=crop&w=400&q=80"
        },
        "302": {
            "nama": "Susu UHT Ultra Milk Full Cream 1L", 
            "kategori": "Minuman", 
            "harga": 19000, 
            "stok": 40, 
            "foto": "https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&fit=crop&w=400&q=80"
        },
        "401": {
            "nama": "Skintific 5X Ceramide Facewash", 
            "kategori": "Facewash", 
            "harga": 89000, 
            "stok": 25, 
            "foto": "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=400&q=80"
        },
        "402": {
            "nama": "Cetaphil Gentle Skin Cleanser", 
            "kategori": "Facewash", 
            "harga": 145000, 
            "stok": 20, 
            "foto": "https://images.unsplash.com/photo-1563178406-4cdc2923acbc?auto=format&fit=crop&w=400&q=80"
        },
        "501": {
            "nama": "Wardah Matte Lip Cream & Cushion", 
            "kategori": "Makeup", 
            "harga": 115000, 
            "stok": 30, 
            "foto": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=400&q=80"
        },
        "502": {
            "nama": "Maybelline Waterproof Mascara", 
            "kategori": "Makeup", 
            "harga": 98000, 
            "stok": 25, 
            "foto": "https://images.unsplash.com/photo-1631729371254-42c2892f0e6e?auto=format&fit=crop&w=400&q=80"
        },
        "601": {
            "nama": "Deterjen Cair Rinso Anti Noda", 
            "kategori": "Kebutuhan", 
            "harga": 20500, 
            "stok": 45, 
            "foto": "https://images.unsplash.com/photo-1585421514284-efb74c2b69ba?auto=format&fit=crop&w=400&q=80"
        },
        "602": {
            "nama": "Sabun Mandi Cair Lifebuoy 450ml", 
            "kategori": "Kebutuhan", 
            "harga": 23000, 
            "stok": 40, 
            "foto": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=400&q=80"
        }
    }

if 'poin_member' not in st.session_state:
    st.session_state.poin_member = 520

if 'riwayat_transaksi' not in st.session_state:
    st.session_state.riwayat_transaksi = []

css_code = """
<style>
    .stApp {
        background: linear-gradient(135deg, #090A0F 0%, #131722 50%, #1F1435 100%);
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif !important;
        color: #F5F5F7;
    }
    @keyframes zoomInScreen {
        0% { transform: scale(0.85); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    .screen-transition {
        animation: zoomInScreen 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    @keyframes pulseGlow {
        0% { transform: scale(1); box-shadow: 0 0 15px rgba(255, 65, 108, 0.4); }
        50% { transform: scale(1.02); box-shadow: 0 0 30px rgba(255, 75, 43, 0.85); }
        100% { transform: scale(1); box-shadow: 0 0 15px rgba(255, 65, 108, 0.4); }
    }
    .promo-banner {
        background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
        border-radius: 20px;
        padding: 16px;
        text-align: center;
        color: white;
        margin-bottom: 16px;
        animation: pulseGlow 2.5s infinite ease-in-out;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    .splash-logo-box {
        background: linear-gradient(135deg, #007AFF 0%, #0056B3 100%);
        width: 110px;
        height: 110px;
        border-radius: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 55px;
        margin: 0 auto 20px auto;
        box-shadow: 0 15px 35px rgba(0, 122, 255, 0.5);
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
        padding: 16px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);
        margin-bottom: 14px;
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
    div.row-widget.stRadio label input { display: none !important; }
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
        cursor: pointer;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

if st.session_state.step_app == 1:
    st.markdown('<div class="screen-transition">', unsafe_allow_html=True)
    st.markdown('<div class="glass-card" style="text-align: center; padding: 70px 20px; margin-top: 30px;">', unsafe_allow_html=True)
    st.markdown('<div class="splash-logo-box">⚡</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="font-weight: 800; font-size: 38px; color: #FFFFFF; margin: 0;">FlashMart</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #8E8E93; font-size: 14px; margin-top: 6px;">Next-Gen On-Demand Retail</p>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Mulai Aplikasi ➔"):
        st.session_state.step_app = 2
        st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

elif st.session_state.step_app == 2 and not st.session_state.logged_in:
    st.markdown('<div class="screen-transition">', unsafe_allow_html=True)
    st.markdown('<div class="slate-header">', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size: 28px; font-weight: 800; letter-spacing: 2px; color: #FFFFFF; margin: 0;">F L A S H M A R T</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color: #8E8E93; font-size: 13px; margin-top: 4px;">Masuk dan sinkronkan member Alfamart kamu.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #FFFFFF; margin-top:0;">🔐 Login Akun</h3>', unsafe_allow_html=True)
    
    nama_user = st.text_input("Nama Lengkap / Akun Google", placeholder="Contoh: Nisfyu")
    no_alfamart = st.text_input("Nomor Member Alfamart", placeholder="Contoh: 899012345678")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Masuk ke Utama ➔"):
        if nama_user and no_alfamart:
            st.session_state.logged_in = True
            st.session_state.user_info = {"nama": nama_user, "alfamart": no_alfamart}
            st.session_state.step_app = 3
            st.rerun()
        else:
            st.warning("⚠️ Mohon lengkapi nama dan nomor member terlebih dahulu!")
    st.markdown('</div></div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="screen-transition" style="padding-bottom: 90px;">', unsafe_allow_html=True)
    
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
        st.markdown("""
            <div class="promo-banner">
                <h3 style="margin: 0; font-size: 16px; font-weight: 800;">🚨 FLASH SALE KILAT HARI INI! ⚡</h3>
                <p style="margin: 4px 0 0 0; font-size: 12px; opacity: 0.9;">Barang impianmu diskon gila-gilaan sampai 90%! Jangan sampai kehabisan atau nyesel belakangan!</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🔍 Cari Produk")
        keyword_cari = st.text_input("Cari produk...", placeholder="Ketik nama produk...", label_visibility="collapsed")
        
        if keyword_cari:
            for kode, item in st.session_state.daftar_produk.items():
                if keyword_cari.lower() in item['nama'].lower():
                    st.markdown(f"""
                        <div class="glass-card" style="display: flex; align-items: center; gap: 14px;">
                            <img src="{item['foto']}" style="width: 70px; height: 70px; border-radius: 14px; object-fit: cover;">
                            <div>
                                <b style="font-size: 14px;">{item['nama']}</b><br>
                                <span style="color: #00F2FE; font-weight: 600;">Rp {item['harga']:,}</span>
                                <div style="font-size: 11px; color: #8E8E93;">Kategori: {item['kategori']} | Stok: {item['stok']}</div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown("### 🏷️ Kategori Pilihan")
            col_cat1, col_cat2, col_cat3, col_cat4 = st.columns(4)
            selected_cat = None
            with col_cat1:
                if st.button("🍔 Makanan"): selected_cat = "Makanan"
            with col_cat2:
                if st.button("🧼 Facewash"): selected_cat = "Facewash"
            with col_cat3:
                if st.button("💄 Makeup"): selected_cat = "Makeup"
            with col_cat4:
                if st.button("🛍️ Kebutuhan"): selected_cat = "Kebutuhan"

            if selected_cat:
                st.markdown(f"#### Kategori: {selected_cat}")
                for kode, item in st.session_state.daftar_produk.items():
                    if item['kategori'] == selected_cat:
                        st.markdown(f"""
                            <div class="glass-card" style="display: flex; align-items: center; gap: 14px;">
                                <img src="{item['foto']}" style="width: 60px; height: 60px; border-radius: 12px; object-fit: cover;">
                                <div>
                                    <b style="font-size: 13px;">{item['nama']}</b><br>
                                    <span style="color: #00F2FE; font-size: 12px;">Rp {item['harga']:,}</span>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
            else:
                st.markdown("### 🛒 Produk Unggulan Terlaris")
                for kode, item in list(st.session_state.daftar_produk.items())[:3]:
                    st.markdown(f"""
                        <div class="glass-card" style="display: flex; align-items: center; gap: 14px;">
                            <img src="{item['foto']}" style="width: 65px; height: 65px; border-radius: 12px; object-fit: cover;">
                            <div style="flex-grow: 1;">
                                <b style="font-size: 14px;">{item['nama']}</b><br>
                                <span style="color: #00F2FE; font-weight: 600;">Rp {item['harga']:,}</span>
                            </div>
                            <div style="font-size: 11px; color: #8E8E93; text-align: right;">Stok: {item['stok']}</div>
                        </div>
                    """, unsafe_allow_html=True)

    elif "Belanja" in tab_pilihan:
        st.markdown("### 🛒 Katalog & Kategori Produk")
        pilihan_kategori = st.selectbox("Filter Kategori:", ["Semua", "Sembako", "Makanan", "Minuman", "Facewash", "Makeup", "Kebutuhan"])
        
        produk_terfilter = {k: v for k, v in st.session_state.daftar_produk.items() if pilihan_kategori == "Semua" or v['kategori'] == pilihan_kategori}
        
        if not produk_terfilter:
            st.warning("❌ Belum ada produk di kategori ini.")
        else:
            pilihan_kode = st.selectbox("Pilih Produk:", list(produk_terfilter.keys()), format_func=lambda x: produk_terfilter[x]['nama'])
            
            prod_aktif = st.session_state.daftar_produk[pilihan_kode]
            st.markdown(f"""
                <div class="glass-card" style="text-align: center;">
                    <img src="{prod_aktif['foto']}" style="width: 140px; height: 140px; border-radius: 18px; object-fit: cover; margin-bottom: 10px;">
                    <h3 style="margin: 0; font-size: 16px;">{prod_aktif['nama']}</h3>
                    <p style="color: #00F2FE; font-weight: 700; font-size: 15px; margin: 4px 0;">Rp {prod_aktif['harga']:,}</p>
                    <p style="color: #8E8E93; font-size: 12px; margin: 0;">Kategori: {prod_aktif['kategori']} | Stok: {prod_aktif['stok']}</p>
                </div>
            """, unsafe_allow_html=True)

            jumlah_beli = st.number_input("Jumlah Beli:", min_value=1, value=1, step=1)
            subtotal = prod_aktif['harga'] * jumlah_beli

            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button("➕ Keranjang"):
                    if jumlah_beli > prod_aktif['stok']:
                        st.error("❌ Stok tidak mencukupi!")
                    else:
                        st.session_state.keranjang.append({
                            "kode": pilihan_kode, "nama": prod_aktif['nama'], "jumlah": jumlah_beli, "subtotal": subtotal, "foto": prod_aktif['foto']
                        })
                        st.success("✅ Masuk keranjang!")
            with col_btn2:
                if st.button("⚡ Beli Sekarang"):
                    if jumlah_beli > prod_aktif['stok']:
                        st.error("❌ Stok tidak mencukupi!")
                    else:
                        poin_didapat = int(subtotal // 10000)
                        st.session_state.poin_member += poin_didapat
                        st.session_state.daftar_produk[pilihan_kode]['stok'] -= jumlah_beli
                        waktu = datetime.datetime.now().strftime('%H:%M:%S')
                        st.session_state.riwayat_transaksi.append({
                            "waktu": waktu, "item": f"{prod_aktif['nama']} (x{jumlah_beli})", "total": subtotal
                        })
                        st.success(f"🎉 Pembayaran Kilat Berhasil! +{poin_didapat} Pts")
                        time.sleep(1)
                        st.rerun()

    elif "🛍️" in tab_pilihan:
        st.markdown("### 🛍️ Keranjang Belanja Anda")
        if not st.session_state.keranjang:
            st.info("Keranjang belanja masih kosong. Yuk pilih produk di menu Belanja!")
        else:
            total_belanja = 0
            for item_k in st.session_state.keranjang:
                total_belanja += item_k['subtotal']
                st.markdown(f"""
                    <div class="glass-card" style="display: flex; align-items: center; gap: 12px;">
                        <img src="{item_k['foto']}" style="width: 55px; height: 55px; border-radius: 10px; object-fit: cover;">
                        <div>
                            <b style="font-size: 13px;">{item_k['nama']}</b><br>
                            <span style="color: #00F2FE; font-size: 12px;">Qty: {item_k['jumlah']} | Subtotal: Rp {item_k['subtotal']:,}</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown(f"#### Total Pembayaran: Rp {total_belanja:,}")
            if st.button("Checkout & Bayar Sekarang ⚡"):
                st.session_state.keranjang = []
                st.success("🎉 Pembayaran Berhasil! Pesanan sedang diantar kurir kilat.")
                time.sleep(1)
                st.rerun()

    elif "Promo" in tab_pilihan:
        st.markdown("### 🔥 Promo Spesial Har
