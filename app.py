import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FlashMart - Tokopedia Edition",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Kode Lengkap dengan Animasi Splash Screen & Katalog Lengkap
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

        /* --- ANIMASI SPLASH SCREEN --- */
        #splash-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            color: white;
            animation: fadeOut 0.8s ease 2.2s forwards;
        }
        .splash-logo {
            font-size: 64px;
            background: white;
            color: #FF9800;
            width: 100px;
            height: 100px;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 25px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            animation: bounceIn 0.8s ease;
        }
        .splash-title {
            font-size: 24px;
            font-weight: 800;
            margin-top: 15px;
            letter-spacing: 0.5px;
            animation: fadeIn 1s ease;
        }

        @keyframes bounceIn {
            0% { transform: scale(0); opacity: 0; }
            60% { transform: scale(1.1); opacity: 1; }
            100% { transform: scale(1); }
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeOut {
            to { opacity: 0; visibility: hidden; }
        }

        /* --- TAMPILAN UTAMA APLIKASI --- */
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
            font-size: 13px;
        }
        .category-scroll {
            display: flex;
            gap: 10px;
            padding: 0 15px 15px 15px;
            overflow-x: auto;
        }
        .cat-chip {
            background: #f0f3f4;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            white-space: nowrap;
            cursor: pointer;
        }
        .cat-chip.active {
            background: #e8f5e9;
            color: #03AC03;
            border: 1px solid #03AC03;
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
            padding: 12px;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.02);
        }
        .product-title {
            font-size: 13px;
            font-weight: 600;
            height: 35px;
            overflow: hidden;
            margin-bottom: 5px;
        }
        .product-price {
            color: #FA591D;
            font-weight: bold;
            font-size: 14px;
            margin-bottom: 8px;
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
            box-shadow: -2px 0 10px rgba(0,0,0,0.05);
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

    <!-- SPLASH SCREEN ANIMASI MASUK -->
    <div id="splash-screen">
        <div class="splash-logo">⚡</div>
        <div class="splash-title">FlashMart</div>
    </div>

    <!-- KONTEN UTAMA APLIKASI -->
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
            🔥 Gunakan Voucher <b>FLASHMARTINA</b> untuk Diskon Rp 10.000!
        </div>

        <!-- Kategori Bar -->
        <div class="category-scroll">
            <div class="cat-chip active">Semua</div>
            <div class="cat-chip">Sembako</div>
            <div class="cat-chip">Minuman</div>
            <div class="cat-chip">Makanan</div>
            <div class="cat-chip">Perawatan</div>
            <div class="cat-chip">Rumah Tangga</div>
        </div>

        <!-- Katalog Produk Lengkap -->
        <div style="padding: 0 15px 10px 15px; font-weight: bold; font-size: 14px;">Produk Terlaris & Lengkap</div>
        <div class="product-grid">
            <div class="product-card">
                <div style="font-size: 36px;">🍳</div>
                <div class="product-title">Minyak Goreng 2L</div>
                <div class="product-price">Rp 38.000</div>
                <button class="btn-buy" onclick="alert('Minyak Goreng 2L berhasil dimasukkan ke keranjang!')">+ Keranjang</button>
            </div>
            <div class="product-card">
                <div style="font-size: 36px;">🌾</div>
                <div class="product-title">Beras Premium 5kg</div>
                <div class="product-price">Rp 69.000</div>
                <button class="btn-buy" onclick="alert('Beras Premium 5kg berhasil dimasukkan ke keranjang!')">+ Keranjang</button>
            </div>
            <div class="product-card">
                <div style="font-size: 36px;">🥛</div>
                <div class="product-title">Susu UHT Ultra 1L</div>
                <div class="product-price">Rp 19.500</div>
                <button class="btn-buy" onclick="alert('Susu UHT 1L berhasil dimasukkan ke keranjang!')">+ Keranjang</button>
            </div>
            <div class="product-card">
                <div style="font-size: 36px;">📦</div>
                <div class="product-title">Mie Instan (1 Dus)</div>
                <div class="product-price">Rp 115.000</div>
                <button class="btn-buy" onclick="alert('Mie Instan 1 Dus berhasil dimasukkan ke keranjang!')">+ Keranjang</button>
            </div>
            <div class="product-card">
                <div style="font-size: 36px;">🥚</div>
                <div class="product-title">Telur Ayam Negeri 1kg</div>
                <div class="product-price">Rp 28.000</div>
                <button class="btn-buy" onclick="alert('Telur Ayam berhasil dimasukkan ke keranjang!')">+ Keranjang</button>
            </div>
            <div class="product-card">
                <div style="font-size: 36px;">☕</div>
                <div class="product-title">Kopi Bubuk Hitam 380g</div>
                <div class="product-price">Rp 16.500</div>
                <button class="btn-buy" onclick="alert('Kopi Bubuk berhasil dimasukkan ke keranjang!')">+ Keranjang</button>
            </div>
            <div class="product-card">
                <div style="font-size: 36px;">🧼</div>
                <div class="product-title">Sabun Mandi Cair 450ml</div>
                <div class="product-price">Rp 24.000</div>
                <button class="btn-buy" onclick="alert('Sabun Mandi berhasil dimasukkan ke keranjang!')">+ Keranjang</button>
            </div>
            <div class="product-card">
                <div style="font-size: 36px;">🧴</div>
                <div class="product-title">Shampoo Anti-Dandruff</div>
                <div class="product-price">Rp 32.000</div>
                <button class="btn-buy" onclick="alert('Shampoo berhasil dimasukkan ke keranjang!')">+ Keranjang</button>
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

components.html(flashmart_html, height=850, scrolling=True)
