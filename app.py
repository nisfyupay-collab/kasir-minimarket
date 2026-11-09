from datetime import datetime
import streamlit as st

# Konfigurasi Halaman (Mobile Native Layout)
st.set_page_config(
    page_title="FlashMart - Mobile Edition",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- CSS STYLING: TEMA ORANYE & KUNING ALA RETAIL MODERN ---
st.markdown(
    """
    <style>
    /* Sembunyikan Header & Footer Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    body {
        background-color: #FFF9E6;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    .main .block-container {
        padding-top: 0.5rem;
        padding-bottom: 6rem;
        max-width: 480px;
    }

    /* Splash / Header Card Oranye-Kuning */
    .member-card {
        background: linear-gradient(135deg, #FF9800 0%, #FFC107 100%);
        color: #fff;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 6px 20px rgba(255, 152, 0, 0.3);
        margin-bottom: 15px;
    }
    .member-name {
        font-size: 19px;
        font-weight: 800;
    }
    .member-info {
        font-size: 13px;
        opacity: 0.95;
    }
    .points-box {
        background: rgba(255, 255, 255, 0.25);
        padding: 8px 12px;
        border-radius: 12px;
        margin-top: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 14px;
        font-weight: 700;
    }

    /* Banner Promo */
    .promo-banner {
        background: linear-gradient(135deg, #FF5722 0%, #FF9800 100%);
        color: white;
        padding: 14px;
        border-radius: 14px;
        text-align: center;
        font-weight: bold;
        font-size: 13px;
        margin-bottom: 15px;
        box-shadow: 0 4px 12px rgba(255, 87, 34, 0.2);
    }

    /* Kartu Produk */
    .product-card {
        background: white;
        padding: 12px;
        border-radius: 14px;
        border: 1px solid #FFE0B2;
        text-align: center;
        margin-bottom: 12px;
        box-shadow: 0 2px 8px rgba(255, 152, 0, 0.05);
    }
    .product-title {
        font-size: 13px;
        font-weight: 600;
        color: #333;
        margin-bottom: 4px;
        height: 36px;
        overflow: hidden;
    }
    .product-price {
        color: #F57C00;
        font-weight: 800;
        font-size: 14px;
        margin-bottom: 8px;
    }

    /* Tombol Kustom */
    div.stButton > button {
        border-radius: 10px;
        font-weight: 600;
        width: 100%;
        background-color: #FF9800;
        color: white;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #F57C00;
        color: white;
    }
    </style>
""",
    unsafe_html=True,
)

# --- INISIALISASI STATE APLIKASI ---
if "_app_step" not in st.session_state:
  st.session_state._app_step = (
      1  # 1: Splash, 2: Login/Member, 3: Menu Utama App
  )
if "cart" not in st.session_state:
  st.session_state.cart = {}
if "points" not in st.session_state:
  st.session_state.points = 150
if "history" not in st.session_state:
  st.session_state.history = []
if "member_name" not in st.session_state:
  st.session_state.member_name = "Pelanggan Setia"
if "no_alfamart" not in st.session_state:
  st.session_state.no_alfamart = "08123456789"

# ================= TAHAP 1: SPLASH SCREEN =================
if st.session_state._app_step == 1:
  st.markdown(
      """
        <div style="text-align: center; padding: 80px 20px;">
            <div style="font-size: 64px; margin-bottom: 15px;">⚡</div>
            <h1 style="color: #FF9800; font-weight: 900; font-size: 32px;">FlashMart</h1>
            <p style="color: #666; font-size: 14px; margin-bottom: 30px;">Belanja Cepat, Poin Melimpah, Hemat Setiap Hari!</p>
    """,
      unsafe_html=True,
  )
  if st.button("Mulai Belanja 🚀", type="primary"):
    st.session_state._app_step = 2
    st.rerun()
  st.markdown("</div>", unsafe_html=True)

# ================= TAHAP 2: LOGIN / MEMBER FORM =================
elif st.session_state._app_step == 2:
  st.markdown(
      """
        <div style="padding: 20px 0;">
            <h2 style="color: #E65100; text-align: center;">Identitas Member ⚡</h2>
            <p style="text-align: center; font-size: 13px; color: #666;">Masukkan data dirimu untuk mulai mengumpulkan poin belanja.</p>
        </div>
    """,
      unsafe_html=True,
  )

  nama_input = st.text_input("Nama Lengkap", value=st.session_state.member_name)
  no_input = st.text_input(
      "Nomor Member / HP", value=st.session_state.no_alfamart
  )

  if st.button("Masuk ke Beranda Utama ✨", type="primary"):
    if nama_input.strip() and no_input.strip():
      st.session_state.member_name = nama_input
      st.session_state.no_alfamart = no_input
      st.session_state._app_step = 3
      st.success("Berhasil masuk!")
      st.rerun()
    else:
      st.error("Mohon isi nama dan nomor member terlebih dahulu!")

# ================= TAHAP 3: APLIKASI UTAMA (DENGAN NAVIGASI BAWAH) =================
elif st.session_state._app_step == 3:

  # Navigasi Menu Bawah (Tabs)
  menu = st.radio(
      "Navigasi",
      ["🏠 Beranda", "🛒 Keranjang", "📜 Riwayat", "👤 Akun"],
      horizontal=True,
      label_visibility="collapsed",
  )
  st.markdown("---")

  # --- TAB 1: BERANDA ---
  if menu == "🏠 Beranda":
    # Member Card Oranye-Kuning
    st.markdown(
        f"""
            <div class="member-card">
                <div class="member-name">⚡ {st.session_state.member_name}</div>
                <div class="member-info">No: {st.session_state.no_alfamart} • Gold VIP</div>
                <div class="points-box">
                    <span>⭐ Saldo Poin A-Voucher</span>
                    <span style="font-size: 16px;">{st.session_state.points} Poin</span>
                </div>
            </div>
        """,
        unsafe_html=True,
    )

    # Banner Promo
    st.markdown(
        """
            <div class="promo-banner">
                🔥 PROMO SPESIAL HARI INI! Gunakan kode voucher <b>FLASHMARTINA</b> saat checkout untuk potongan langsung!
            </div>
        """,
        unsafe_html=True,
    )

    st.subheader("🛍️ Katalog Produk FlashMart")

    # Katalog Produk Lengkap dengan Gambar/Icon
    products = [
        {
            "id": 1,
            "name": "Minyak Goreng 2L",
            "price": 38000,
            "category": "Sembako",
            "foto": "🍳",
        },
        {
            "id": 2,
            "name": "Beras Premium 5kg",
            "price": 69000,
            "category": "Sembako",
            "foto": "🌾",
        },
        {
            "id": 3,
            "name": "Susu UHT Ultra 1L",
            "price": 19500,
            "category": "Minuman",
            "foto": "🥛",
        },
        {
            "id": 4,
            "name": "Mie Instan (1 Dus)",
            "price": 115000,
            "category": "Makanan",
            "foto": "📦",
        },
        {
            "id": 5,
            "name": "Sabun Mandi Cair",
            "price": 24000,
            "category": "Personal Care",
            "foto": "🧼",
        },
        {
            "id": 6,
            "name": "Shampoo Anti-Dandruff",
            "price": 32000,
            "category": "Personal Care",
            "foto": "🧴",
        },
    ]

    selected_cat = st.selectbox(
        "Kategori",
        ["Semua", "Sembako", "Minuman", "Makanan", "Personal Care"],
        label_visibility="collapsed",
    )

    cols = st.columns(2)
    filtered = (
        products
        if selected_cat == "Semua"
        else [p for p in products if p["category"] == selected_cat]
    )

    for idx, prod in enumerate(filtered):
      with cols[idx % 2]:
        st.markdown(
            f"""
                    <div class="product-card">
                        <div style="font-size: 34px; margin-bottom: 6px;">{prod['foto']}</div>
                        <div class="product-title">{prod['name']}</div>
                        <div class="product-price">Rp {prod['price']:,}</div>
                    </div>
                """,
            unsafe_html=True,
        )

        # Dua Tombol: Tambah Keranjang & Beli Sekarang
        b1, b2 = st.columns(2)
        with b1:
          if st.button("➕ Keranjang", key=f"c_{prod['id']}"):
            if prod["name"] in st.session_state.cart:
              st.session_state.cart[prod["name"]]["qty"] += 1
            else:
              st.session_state.cart[prod["name"]] = {
                  "price": prod["price"],
                  "qty": 1,
              }
            st.toast(f"Masuk keranjang: {prod['name']}")
        with b2:
          if st.button("⚡ Beli", key=f"b_{prod['id']}"):
            if prod["name"] in st.session_state.cart:
              st.session_state.cart[prod["name"]]["qty"] += 1
            else:
              st.session_state.cart[prod["name"]] = {
                  "price": prod["price"],
                  "qty": 1,
              }
            st.rerun()

  # --- TAB 2: KERANJANG & CHECKOUT ---
  elif menu == "🛒 Keranjang":
    st.subheader("🛒 Keranjang Belanja Anda")

    if not st.session_state.cart:
      st.info(
          "Keranjang masih kosong. Yuk pilih produk favoritmu di menu Beranda!"
      )
    else:
      subtotal = 0
      to_delete = []

      for item_name, details in st.session_state.cart.items():
        item_total = details["price"] * details["qty"]
        subtotal += item_total

        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
          st.write(f"**{item_name}**")
          st.text(f"Rp {details['price']:,} x {details['qty']}")
        with col2:
          cc1, cc2 = st.columns(2)
          with cc1:
            if st.button("-", key=f"minus_{item_name}"):
              if details["qty"] > 1:
                st.session_state.cart[item_name]["qty"] -= 1
              else:
                to_delete.append(item_name)
              st.rerun()
          with cc2:
            if st.button("+", key=f"plus_{item_name}"):
              st.session_state.cart[item_name]["qty"] += 1
              st.rerun()
        with col3:
          st.write(f"**Rp {item_total:,}**")
        st.markdown("---")

      for item in to_delete:
        del st.session_state.cart[item]

      # Voucher Input
      st.markdown("### 🎟️ Kode Voucher Diskon")
      voucher_code = st.text_input(
          "Masukkan Kode",
          placeholder="Cth: FLASHMARTINA",
          label_visibility="collapsed",
      )

      discount = 0
      if voucher_code:
        if voucher_code.strip().upper() == "FLASHMARTINA":
          discount = 10000
          st.success("🎉 Voucher **FLASHMARTINA** Aktif! Potongan Rp 10.000")
        else:
          st.error("❌ Kode Voucher tidak valid.")

      grand_total = max(0, subtotal - discount)

      st.markdown("### 📝 Ringkasan Pembayaran")
      st.write(f"Subtotal: **Rp {subtotal:,}**")
      if discount > 0:
        st.write(f"Diskon: **- Rp {discount:,}**")
      st.markdown(f"### Total Akhir: Rp {grand_total:,}")

      if st.button("💳 Bayar Sekarang & Kumpul Poin", type="primary"):
        earned = int(grand_total // 10000)
        st.session_state.points += earned

        st.session_state.history.append({
            "waktu": datetime.now().strftime("%d %b %Y, %H:%M"),
            "items": dict(st.session_state.cart),
            "total": grand_total,
            "poin": earned,
        })
        st.session_state.cart = {}
        st.success(
            f"✅ Pembayaran Berhasil! Selamat, Anda mendapatkan +{earned} Poin"
            " A-Voucher."
        )
        st.balloons()

  # --- TAB 3: RIWAYAT TRANSAKSI ---
  elif menu == "📜 Riwayat":
    st.subheader("📜 Riwayat Struk Belanja")

    if not st.session_state.history:
      st.info("Belum ada riwayat transaksi belanja.")
    else:
      for i, tx in enumerate(reversed(st.session_state.history)):
        with st.expander(
            f"Transaksi #{len(st.session_state.history)-i} — {tx['waktu']} (Rp"
            f" {tx['total']:,})"
        ):
          st.write(f"**Waktu:** {tx['waktu']}")
          st.write("**Daftar Barang:**")
          for name, det in tx["items"].items():
            st.text(
                f" • {name} x{det['qty']} (Rp {det['price']*det['qty']:,})"
            )
          st.markdown(f"**Total Pembayaran:** Rp {tx['total']:,}")
          st.markdown(f"**Poin Didapat:** +{tx['poin']} ⭐")

  # --- TAB 4: AKUN MEMBER ---
  elif menu == "👤 Akun":
    st.subheader("👤 Profil Member")
    st.markdown(
        f"""
            <div class="member-card">
                <div class="member-name">⚡ {st.session_state.member_name}</div>
                <div class="member-info">No. Anggota: {st.session_state.no_alfamart}</div>
                <div class="points-box">
                    <span>⭐ Saldo Poin Anda</span>
                    <span style="font-size: 16px;">{st.session_state.points} Poin</span>
                </div>
            </div>
        """,
        unsafe_html=True,
    )

    if st.button("Keluar / Ganti Akun"):
      st.session_state._app_step = 2
      st.rerun()

    st.markdown("---")
    st.markdown(
        "**FlashMart Retail App** — Versi Oranye & Kuning Cerah Bergaya Alfagift."
    )
