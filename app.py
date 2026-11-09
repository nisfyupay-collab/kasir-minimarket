from datetime import datetime
import streamlit as st

st.set_page_config(
    page_title="FlashMart",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    body {background-color: #FFF9E6;}
    .main .block-container {max-width: 480px; padding-top: 0.5rem;}
    .member-card {
        background: linear-gradient(135deg, #FF9800 0%, #FFC107 100%);
        color: white; padding: 16px; border-radius: 16px; margin-bottom: 15px;
    }
    .promo-banner {
        background: linear-gradient(135deg, #FF5722 0%, #FF9800 100%);
        color: white; padding: 12px; border-radius: 12px; text-align: center;
        font-weight: bold; font-size: 13px; margin-bottom: 15px;
    }
    .product-card {
        background: white; padding: 10px; border-radius: 12px;
        border: 1px solid #FFE0B2; text-align: center; margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_html=True,
)

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

if st.session_state._step == 1:
  st.markdown(
      """<div style="text-align: center; padding: 60px 20px;">
      <div style="font-size: 60px;">⚡</div>
      <h1 style="color: #FF9800;">FlashMart</h1>
      <p style="color: #666;">Belanja Cepat, Poin Melimpah!</p></div>""",
      unsafe_html=True,
  )
  if st.button("Mulai Belanja 🚀", type="primary"):
    st.session_state._step = 2
    st.rerun()

elif st.session_state._step == 2:
  st.markdown(
      "<h2 style='color: #E65100; text-align: center;'>Identitas"
      " Member ⚡</h2>",
      unsafe_html=True,
  )
  name = st.text_input("Nama Lengkap", value=st.session_state.name)
  phone = st.text_input("Nomor Member/HP", value=st.session_state.phone)
  if st.button("Masuk Beranda ✨", type="primary"):
    if name and phone:
      st.session_state.name = name
      st.session_state.phone = phone
      st.session_state._step = 3
      st.rerun()

elif st.session_state._step == 3:
  menu = st.radio(
      "Menu",
      ["🏠 Beranda", "🛒 Keranjang", "📜 Riwayat", "👤 Akun"],
      horizontal=True,
      label_visibility="collapsed",
  )
  st.markdown("---")

  products = [
      {
          "id": 1,
          "name": "Minyak Goreng 2L",
          "price": 38000,
          "cat": "Sembako",
          "icon": "🍳",
      },
      {
          "id": 2,
          "name": "Beras Premium 5kg",
          "price": 69000,
          "cat": "Sembako",
          "icon": "🌾",
      },
      {
          "id": 3,
          "name": "Susu UHT 1L",
          "price": 19500,
          "cat": "Minuman",
          "icon": "🥛",
      },
      {
          "id": 4,
          "name": "Mie Instan (1 Dus)",
          "price": 115000,
          "cat": "Makanan",
          "icon": "📦",
      },
      {
          "id": 5,
          "name": "Sabun Mandi",
          "price": 24000,
          "cat": "Personal",
          "icon": "🧼",
      },
      {
          "id": 6,
          "name": "Shampoo",
          "price": 32000,
          "cat": "Personal",
          "icon": "🧴",
      },
  ]

  if menu == "🏠 Beranda":
    st.markdown(
        f"""
        <div class="member-card">
            <b>⚡ {st.session_state.name}</b><br>
            <span style="font-size:12px;">No: {st.session_state.phone}</span>
            <div style="background: rgba(255,255,255,0.2); padding: 6px; border-radius: 8px; margin-top: 8px; display: flex; justify-content: space-between;">
                <span>⭐ Poin A-Voucher</span><b>{st.session_state.points} Poin</b>
            </div>
        </div>
        """,
        unsafe_html=True,
    )
    st.markdown(
        """<div class="promo-banner">🔥 Voucher Diskon Aktif: <br><b>FLASHMARTINA</b></div>""",
        unsafe_html=True,
    )

    cat = st.selectbox(
        "Kategori",
        ["Semua", "Sembako", "Minuman", "Makanan", "Personal"],
        label_visibility="collapsed",
    )
    filtered = (
        products if cat == "Semua" else [p for p in products if p["cat"] == cat]
    )

    cols = st.columns(2)
    for i, p in enumerate(filtered):
      with cols[i % 2]:
        st.markdown(
            f"""
                <div class="product-card">
                    <div style="font-size: 30px;">{p['icon']}</div>
                    <div style="font-size: 13px; font-weight:600; height:34px; overflow:hidden;">{p['name']}</div>
                    <div style="color: #F57C00; font-weight: 700;">Rp {p['price']:,}</div>
                </div>
                """,
            unsafe_html=True,
        )
        b1, b2 = st.columns(2)
        with b1:
          if st.button("➕", key=f"c_{p['id']}"):
            if p["name"] in st.session_state.cart:
              st.session_state.cart[p["name"]]["qty"] += 1
            else:
              st.session_state.cart[p["name"]] = {
                  "price": p["price"],
                  "qty": 1,
              }
            st.toast(f"+ {p['name']}")
        with b2:
          if st.button("⚡", key=f"b_{p['id']}"):
            if p["name"] in st.session_state.cart:
              st.session_state.cart[p["name"]]["qty"] += 1
            else:
              st.session_state.cart[p["name"]] = {
                  "price": p["price"],
                  "qty": 1,
              }
            st.rerun()

  elif menu == "🛒 Keranjang":
    st.subheader("🛒 Keranjang Belanja")
    if not st.session_state.cart:
      st.info("Keranjang kosong.")
    else:
      sub = 0
      rm = []
      for name, d in st.session_state.cart.items():
        tot = d["price"] * d["qty"]
        sub += tot
        c1, c2, c3 = st.columns([3, 2, 1])
        with c1:
          st.write(f"**{name}**\nRp {d['price']:,} x {d['qty']}")
        with c2:
          if st.button("-", key=f"m_{name}"):
            if d["qty"] > 1:
              st.session_state.cart[name]["qty"] -= 1
            else:
              rm.append(name)
            st.rerun()
          if st.button("+", key=f"p_{name}"):
            st.session_state.cart[name]["qty"] += 1
            st.rerun()
        with c3:
          st.write(f"**Rp {tot:,}**")
        st.markdown("---")
      for x in rm:
        del st.session_state.cart[x]

      v = st.text_input("Kode Voucher", placeholder="FLASHMARTINA")
      disc = 10000 if v.strip().upper() == "FLASHMARTINA" else 0
      if disc > 0:
        st.success("Voucher FLASHMARTINA Berhasil!")
      grand = max(0, sub - disc)

      st.write(f"Subtotal: Rp {sub:,}")
      if disc > 0:
        st.write(f"Diskon: - Rp {disc:,}")
      st.markdown(f"### Total: Rp {grand:,}")

      if st.button("💳 Bayar Sekarang", type="primary"):
        earned = int(grand // 10000)
        st.session_state.points += earned
        st.session_state.history.append({
            "time": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "items": dict(st.session_state.cart),
            "total": grand,
            "poin": earned,
        })
        st.session_state.cart = {}
        st.success(f"Pembayaran Berhasil! +{earned} Poin")
        st.balloons()

  elif menu == "📜 Riwayat":
    st.subheader("📜 Riwayat Transaksi")
    if not st.session_state.history:
      st.info("Belum ada riwayat.")
    else:
      for i, tx in enumerate(reversed(st.session_state.history)):
        with st.expander(f"#{len(st.session_state.history)-i} ({tx['time']})"):
          st.write(f"Total: Rp {tx['total']:,} | Poin: +{tx['poin']}")

  elif menu == "👤 Akun":
    st.subheader("👤 Profil")
    st.write(f"Nama: **{st.session_state.name}**")
    st.write(f"No HP: **{st.session_state.phone}**")
    st.write(f"Poin: **{st.session_state.points}**")
    if st.button("Ganti Akun"):
      st.session_state._step = 2
      st.rerun()
      
