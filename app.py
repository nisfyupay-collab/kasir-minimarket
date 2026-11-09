import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FlashMart Tokopedia Edition",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Menyisipkan Full HTML, CSS, & JS ala E-Commerce Modern langsung ke Streamlit
flashmart_html = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FlashMart</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 0;
            color: #333;
        }
        .app-container {
            max-width: 480px;
            margin: 0 auto;
            background: #fff;
            min-height: 100vh;
            padding-bottom: 70px;
            box-shadow: 0 0 15px rgba(0,0,0,0.05);
        }
        .header {
            background: linear-gradient(135deg, #03AC03 0%, #42B549 100%);
            color: white;
            padding: 16px;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
        }
        .search-bar {
            background: white;
            padding: 10px 15px;
            border-radius: 25px;
            display: flex;
            align-items: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-top: 10px;
        }
        .search-bar input {
            border: none;
            outline: none;
            width: 100%;
            margin-left: 10px;
            font-size: 14px;
        }
        .banner {
            margin: 15px;
            background: linear-gradient(135deg, #ff8800, #ffbb00);
            color: white;
            padding: 15px;
            border-radius: 12px;
            font-weight: bold;
            text-align: center;
        }
        .product-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            padding: 0 15px;
        }
        .product-card {
            background: #fff;
            border: 1px solid #eee;
            border-radius: 12px;
            padding: 10px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.02);
        }
        .product-price {
            color: #FA591D;
            font-weight: bold;
            font-size: 15px;
            margin: 8px 0;
        }
        .btn-buy {
            background: #03AC03;
            color: white;
            border: none;
            padding: 8px;
            width: 100%;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
        }
        .bottom-nav {
            position: fixed;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            max-width: 480px;
            background: white;
            display: flex;
            justify-content: space-around;
            padding: 10px 0;
            border-top: 1px solid #eee;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
        }
        .nav-item {
            text-align: center;
            font-size: 11px;
            color: #666;
            cursor: pointer;
            text-decoration: none;
        }
        .nav-item div { font-size: 20px; }
    </style>
</head>
<body>
    <div class="app-container">
        <!-- Header -->
        <div class="header">
            <h3 style="margin:0;">⚡ FlashMart Store</h3>
            <div class="search-bar">
                <span>🔍</span>
                <input type="text" placeholder="Cari kebutuhan harianmu...">
            </div>
        </div>

        <!-- Banner Promo -->
        <div class="banner">
            🔥 Voucher Spesial: FLASHMARTINA (Diskon Rp 10rb)
        </div>

        <!-- Katalog Produk -->
        <div style="padding: 0 15px 10px 15px; font-weight: bold;">Rekomendasi Spesial</div>
        <div class="product-grid">
            <div class="product-card">
                <div style="font-size: 36px;">🍳</div>
                <div style="font-size: 13px; font-weight: 600; height: 35px;">Minyak Goreng 2L</div>
                <div class="product-price">Rp 38.000</div>
                <button class="btn-buy" onclick="alert('Berhasil masuk keranjang!')">+ Keranjang</button>
            </div>
            <div class="product-card">
                <div style="font-size: 36px;">🌾</div>
                <div style="font-size: 13px; font-weight: 600; height: 35px;">Beras Premium 5kg</div>
                <div class="product-price">Rp 69.000</div>
                <button class="btn-buy" onclick="alert('Berhasil masuk keranjang!')">+ Keranjang</button>
            </div>
        </div>

        <!-- Bottom Nav -->
        <div class="bottom-nav">
            <a href="#" class="nav-item"><div>🏠</div>Beranda</a>
            <a href="#" class="nav-item"><div>🛒</div>Keranjang</a>
            <a href="#" class="nav-item"><div>📜</div>Riwayat</a>
            <a href="#" class="nav-item"><div>👤</div>Akun</a>
        </div>
    </div>
</body>
</html>
"""

# Render ke Streamlit dengan ukuran tinggi yang pas untuk mobile view
components.html(flashmart_html, height=750, scrolling=True)

