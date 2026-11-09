from datetime import datetime
import streamlit as st

st.set_page_config(page_title="FlashMart"page_icon="⚡",layout="centered",initial_sidebar_state="collapsed",)
    

# Inisialisasi State
if "_step" not in st.session_state:
    st.session_state._step = 1
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "points" not in st.session_state:
    st.session_state.points = 150
if "history" not in st.session_state:
    st.session_state.history = []
if "name" not in st.session_state:
    st.session_state.name = "Pelanggan Setia"
if "phone" not in st.session_state:
    st.session_state.phone = "08123456789"

# --- TAHAP 1: SPLASH SCREEN ---
if st.session_state._step == 1:
    st.markdown("<h1 style='text-align: center;'>⚡ FlashMart</h1>", unsafe_html=True)
    st.markdown("<p style='text-align: center;'>Belanja Cepat, Poin Melimpah!</p>", unsafe_html=True)
    st.write("")
    if st.button("Mulai Belanja 🚀", type="primary", use_container_width=True):
        st.session_state._step = 2
        st.rerun()

# --- TAHAP 2: LOGIN MEMBER ---
elif st.session_state._step == 2:
    st.subheader("Identitas Member ⚡")
    name = st.text_input("Nama Lengkap", value=st.session_state.name)
    phone = st.text_input("Nomor Member/HP", value=st.session_state.phone)
    st.write("")
    if st.button("Masuk Beranda ✨", type="primary", use_container_width=True):
        if name and phone:
            st.session_state.name = name
            st.session_state.phone = phone
            st.session_state._step = 3
            st.rerun()

# --- TAHAP 3: APLIKASI UTAMA ---
elif st.session_state._step == 3:
    menu = st.radio("Menu"["🏠 Beranda", "🛒 Keranjang", "📜 Riwayat", "👤 Akun"],horizontal=True,label_visibility="collapsed")
        
    st.divider()

    products = [
        {"id": 1, "name": "Minyak Goreng 2L", "price": 38000, "cat": "Sembako", "icon": "🍳"},
        {"id": 2, "name": "Beras Premium 5kg", "price": 69000, "cat": "Sembako", "icon": "🌾"},
        {"id": 3, "name": "Susu UHT 1L", "price": 19500, "cat": "Minuman", "icon": "🥛"},
        {"id": 4, "name": "Mie Instan (1 Dus)", "price": 115000, "cat": "Makanan", "icon": "📦"},
        {"id": 5, "name": "Sabun Mandi", "price": 24000, "cat": "Personal", "icon": "🧼"},
        {"id": 6, "name": "Shampoo", "price": 32000, "cat": "Personal", "icon": "🧴"}
    ]

    if menu == "🏠 Beranda":
        st.info(f"⚡ **{st.session_state.name}** | Poin A-Voucher: ⭐ **{st.session_state.points} Poin**")
        st.success("🔥 Voucher Diskon Aktif: **FLASHMARTINA** (Potongan Rp 10.000 saat checkout)")

        cat = st.selectbox("Kategori"["Semua", "Sembako", "Minuman", "Makanan", "Personal"],label_visibility="collapsed")
            
        filtered = products if cat == "Semua" else [p for p in products if p["cat"] == cat]

        cols = st.columns(2)
        for i, p in enumerate(filtered):
            with cols[i % 2]:
                st.write(f"### {p['icon']}")
                st.write(f"**{p['name']}**")
                st.text(f"Rp {p['price']:,}")
                
                b1, b2 = st.columns(2)
                with b1:
                    if st.button("➕", key=f"c_{p['id']}"):
                        if p['name'] in st.session_state.cart:
                            st.session_state.cart[p['name']]['qty'] += 1
                        else:
                            st.session_state.cart[p['name']] = {'price': p['price'], 'qty': 1}
                        st.toast(f"+ {p['name']}")
                with b2:
                    if st.button("⚡ Beli", key=f"b_{p['id']}"):
                        if p['name'] in st.session_state.cart:
                            st.session_state.cart[p['name']]['qty'] += 1
                        else:
                            st.session_state.cart[p['name']] = {'price': p['price'], 'qty': 1}
                        st.rerun()
                st.divider()

    elif menu == "🛒 Keranjang":
        st.subheader("🛒 Keranjang Belanja")
        if not st.session_state.cart:
            st.info("Keranjang kosong. Yuk belanja dulu di Beranda!")
        else:
            sub = 0
            rm = []
            for name, d in st.session_state.cart.items():
                tot = d['price'] * d['qty']
                sub += tot
                st.write(f"**{name}** (Rp {d['price']:,} x {d['qty']}) = **Rp {tot:,}**")
                
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("Kurangi", key=f"m_{name}"):
                        if d['qty'] > 1:
                            st.session_state.cart[name]['qty'] -= 1
                        else:
                            rm.append(name)
                        st.rerun()
                with c2:
                    if st.button("Tambah", key=f"p_{name}"):
                        st.session_state.cart[name]['qty'] += 1
                        st.rerun()
                st.markdown("---")
            
            for x in rm:
                del st.session_state.cart[x]
            
            v = st.text_input("Kode Voucher", placeholder="Ketik FLASHMARTINA")
            disc = 10000 if v.strip().upper() == "FLASHMARTINA" else 0
            if disc > 0:
                st.success("🎉 Voucher FLASHMARTINA Berhasil Digunakan! (-Rp 10.000)")
            
            grand = max(0, sub - disc)
            st.write(f"Subtotal: Rp {sub:,}")
            if disc > 0:
                st.write(f"Diskon: - Rp {disc:,}")
            st.markdown(f"### Total Pembayaran: Rp {grand:,}")
            
            if st.button("💳 Bayar Sekarang", type="primary", use_container_width=True):
                earned = int(grand // 10000)
                st.session_state.points += earned
                st.session_state.history.append({"time": datetime.now().strftime("%d/%m/%Y %H:%M")"items": dict(st.session_state.cart)"total": grand,"poin": earned})   
                st.session_state.cart = {}
                st.success(f"Pembayaran Berhasil! Kamu dapat +{earned} Poin ⭐")
                st.balloons()

    elif menu == "📜 Riwayat":
        st.subheader("📜 Riwayat Transaksi")
        if not st.session_state.history:
            st.info("Belum ada riwayat transaksi belanja.")
        else:
            for i, tx in enumerate(reversed(st.session_state.history)):
                with st.expander(f"Transaksi #{len(st.session_state.history)-i} ({tx['time']})"):
                    st.write(f"Total Bayar: **Rp {tx['total']:,}**")
                    st.write(f"Poin Didapat: **+{tx['poin']} Poin ⭐**")

    elif menu == "👤 Akun":
        st.subheader("👤 Profil Member")
        st.write(f"Nama: **{st.session_state.name}**")
        st.write(f"No HP: **{st.session_state.phone}**")
        st.write(f"Total Poin: **{st.session_state.points} Poin**")
        st.write("")
        if st.button("Ganti Akun", use_container_width=True):
            st.session_state._step = 2
            st.rerun()
            
