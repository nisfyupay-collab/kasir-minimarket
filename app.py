import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FlashMart",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

flashmart_html = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FlashMart</title>
    <style>
        :root {
            --bg-color: #f8f9fa;
            --card-bg: #ffffff;
            --text-color: #333333;
            --nav-bg: #ffffff;
            --border-color: #eee;
        }
        [data-theme="dark"] {
            --bg-color: #121212;
            --card-bg: #1e1e1e;
            --text-color: #f1f1f1;
            --nav-bg: #1e1e1e;
            --border-color: #333333;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 0;
            transition: background 0.3s, color 0.3s;
        }

        /* SPLASH SCREEN ANIMASI HIDUP */
        #splash-screen {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(135deg, #03AC03 0%, #2E7D32 50%, #FF9800 100%);
            display: flex; flex-direction: column; justify-content: center; align-items: center;
            z-index: 9999; color: white;
            transition: opacity 0.6s ease, visibility 0.6s ease;
        }
        .splash-logo-container {
            position: relative;
            display: flex; justify-content: center; align-items: center;
            animation: pulseGlow 1.8s infinite alternate;
        }
        .splash-logo {
            font-size: 72px; background: white; color: #03AC03; width: 110px; height: 110px;
            display: flex; justify-content: center; align-items: center; border-radius: 30px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.25);
            animation: bounceInRotate 1s cubic-bezier(0.68, -0.55, 0.265, 1.55) forwards;
        }
        .splash-text {
            font-size: 26px; font-weight: 900; margin-top: 18px; letter-spacing: 1px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.2);
            animation: fadeInUp 1s ease 0.3s forwards; opacity: 0;
        }
        .splash-tagline {
            font-size: 13px; opacity: 0.85; margin-top: 6px;
            animation: fadeInUp 1s ease 0.5s forwards; opacity: 0;
        }

        @keyframes bounceInRotate {
            0% { transform: scale(0) rotate(-180deg); opacity: 0; }
            70% { transform: scale(1.15) rotate(15deg); opacity: 1; }
            100% { transform: scale(1) rotate(0deg); opacity: 1; }
        }
        @keyframes fadeInUp {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        @keyframes pulseGlow {
            0% { filter: drop-shadow(0 0 10px rgba(255,255,255,0.4)); }
            100% { filter: drop-shadow(0 0 25px rgba(255,255,255,0.9)); }
        }

        #success-modal, #tracking-detail-modal {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.7); display: none; justify-content: center; align-items: center;
            z-index: 10000; backdrop-filter: blur(4px); overflow-y: auto; padding: 20px;
        }
        .receipt-card, .tracking-card {
            background: var(--card-bg); color: var(--text-color); width: 100%; max-width: 360px; padding: 20px;
            border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); position: relative; margin: auto;
        }
        .receipt-card { font-family: 'Courier New', Courier, monospace; background: #fff; color: #333; }
        .receipt-card::before {
            content: ""; position: absolute; top: -10px; left: 0; width: 100%; height: 10px;
            background: radial-gradient(circle, transparent, transparent 50%, #fff 50%, #fff 100%);
            background-size: 16px 20px;
        }

        .ripple-btn { position: relative; overflow: hidden; cursor: pointer; }

        .app-container {
            max-width: 480px; margin: 0 auto; background: var(--bg-color); min-height: 100vh;
            padding-bottom: 90px; box-shadow: 0 0 15px rgba(0,0,0,0.05); position: relative;
        }
        .header {
            background: linear-gradient(135deg, #03AC03 0%, #42B549 100%);
            color: white; padding: 16px; border-bottom-left-radius: 20px; border-bottom-right-radius: 20px;
        }
        .search-bar {
            background: #fff; padding: 10px 15px; border-radius: 25px; display: flex; align-items: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-top: 10px;
        }
        .search-bar input { border: none; outline: none; width: 100%; margin-left: 10px; font-size: 14px; background: transparent; color: #333; }
        
        .store-selector {
            margin: 12px 15px 0 15px; background: var(--card-bg); border: 1px solid var(--border-color);
            padding: 8px 12px; border-radius: 10px; display: flex; justify-content: space-between; align-items: center; font-size: 13px; font-weight: bold;
        }
        .store-selector select { border: none; background: transparent; color: #03AC03; font-weight: bold; outline: none; cursor: pointer; font-size: 13px; }

        .category-scroll { display: flex; gap: 8px; overflow-x: auto; padding: 12px 15px; scrollbar-width: none; }
        .category-scroll::-webkit-scrollbar { display: none; }
        .cat-chip {
            background: var(--card-bg); border: 1px solid var(--border-color); padding: 6px 14px;
            border-radius: 20px; font-size: 12px; cursor: pointer; white-space: nowrap; color: var(--text-color); font-weight: 600;
        }
        .cat-chip.active { background: #03AC03; color: white; border-color: #03AC03; }

        .banner {
            margin: 0 15px 15px 15px; background: linear-gradient(135deg, #ff8800, #ffbb00); color: white;
            padding: 12px; border-radius: 12px; font-weight: bold; text-align: center; font-size: 12px;
        }
        
        .digital-grid {
            display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; padding: 0 15px 15px 15px; text-align: center;
        }
        .digital-item {
            background: var(--card-bg); border: 1px solid var(--border-color); padding: 10px 5px; border-radius: 10px;
            font-size: 11px; font-weight: bold; cursor: pointer; color: var(--text-color);
        }

        .product-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; padding: 0 15px; }
        .product-card {
            background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 12px; padding: 12px;
            text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.02); transition: transform 0.2s; position: relative;
        }
        .product-card:active { transform: scale(0.96); }
        .product-title { font-size: 13px; font-weight: 600; height: 35px; overflow: hidden; margin-bottom: 2px; color: var(--text-color); }
        .product-stock { font-size: 11px; color: #777; margin-bottom: 5px; }
        .product-price { color: #FA591D; font-weight: bold; font-size: 14px; margin-bottom: 8px; }
        
        .btn-group { display: flex; gap: 5px; }
        .btn-cart { background: #ff9800; color: white; border: none; padding: 7px; border-radius: 6px; font-weight: bold; font-size: 11px; flex: 1; cursor: pointer; }
        .btn-buy-now { background: #03AC03; color: white; border: none; padding: 7px; border-radius: 6px; font-weight: bold; font-size: 11px; flex: 1; cursor: pointer; }

        .bottom-nav {
            position: fixed; bottom: 0; left: 50%; transform: translateX(-50%);
            width: 100%; max-width: 480px; background: var(--nav-bg); display: flex; justify-content: space-around;
            padding: 10px 0; border-top: 1px solid var(--border-color); z-index: 100;
        }
        .nav-item { text-align: center; font-size: 11px; color: #777; cursor: pointer; background: none; border: none; outline: none; }
        .nav-item.active { color: #03AC03; font-weight: bold; }
        .nav-item div { font-size: 20px; }

        .view-section { display: none; padding: 15px; }
        .view-section.active { display: block; }
        
        /* KERANJANG ALA MARKETPLACE MODERN (SHOPEE STYLE) */
        .cart-store-group {
            background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 12px;
            margin-bottom: 12px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.03);
        }
        .cart-store-header {
            padding: 10px 12px; border-bottom: 1px solid var(--border-color); display: flex;
            align-items: center; gap: 8px; font-weight: bold; font-size: 13px; background: rgba(3, 172, 3, 0.04);
        }
        .cart-item-card {
            display: flex; align-items: center; gap: 10px; padding: 12px;
            border-bottom: 1px solid var(--border-color);
        }
        .cart-item-card:last-child { border-bottom: none; }
        .cart-checkbox { width: 18px; height: 18px; accent-color: #FA591D; cursor: pointer; flex-shrink: 0; }
        .cart-item-icon {
            font-size: 30px; width: 54px; height: 54px; background: var(--bg-color); border-radius: 10px;
            display: flex; justify-content: center; align-items: center; flex-shrink: 0; border: 1px solid var(--border-color);
        }
        .cart-item-info { flex: 1; min-width: 0; }
        .cart-item-title {
            font-weight: 600; font-size: 13px; color: var(--text-color); margin-bottom: 4px;
            white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
        }
        .cart-item-price { color: #FA591D; font-weight: bold; font-size: 13px; }
        .qty-stepper {
            display: inline-flex; align-items: center; border: 1px solid var(--border-color);
            border-radius: 6px; overflow: hidden; margin-top: 6px;
        }
        .qty-stepper button {
            background: var(--bg-color); border: none; color: var(--text-color); width: 24px; height: 24px;
            font-weight: bold; cursor: pointer; font-size: 13px;
        }
        .qty-stepper span { padding: 0 10px; font-size: 12px; font-weight: bold; }
        .btn-del-item {
            background: none; border: none; color: #999; font-size: 16px; cursor: pointer; padding: 4px;
        }
        .btn-del-item:hover { color: #FA591D; }
        .cart-select-all-bar {
            background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 10px;
            padding: 10px 12px; margin-bottom: 12px; display: flex; justify-content: space-between;
            align-items: center; font-size: 13px; font-weight: 600;
        }

        .profile-card { background: linear-gradient(135deg, #03AC03 0%, #42B549 100%); color: white; padding: 16px; border-radius: 16px; margin-bottom: 15px; }
        .tracker-box { 
            background: var(--card-bg); border: 1px solid var(--border-color); padding: 14px; border-radius: 12px; margin-bottom: 12px;
            cursor: pointer; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.03);
        }
        .tracker-box:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-color: #03AC03; }
        .stepper { display: flex; justify-content: space-between; margin-top: 10px; font-size: 11px; color: #03AC03; font-weight: bold; }
        
        .admin-input {
            width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 8px; border: 1px solid var(--border-color);
            background: var(--card-bg); color: var(--text-color); box-sizing: border-box;
        }

        .qr-box {
            background: white; border: 2px dashed #03AC03; padding: 15px; border-radius: 12px; text-align: center; margin: 10px 0;
        }
        .qr-box img { width: 160px; height: 160px; }
    </style>
</head>
<body data-theme="light">

    <!-- SPLASH SCREEN ANIMASI HIDUP -->
    <div id="splash-screen">
        <div class="splash-logo-container">
            <div class="splash-logo">⚡</div>
        </div>
        <div class="splash-text">FlashMart</div>
        <div class="splash-tagline">Belanja Cepat, Mudah & Terpercaya</div>
    </div>

    <!-- POP-UP MODAL STRUK BELANJA -->
    <div id="success-modal">
        <div class="receipt-card">
            <h3 style="text-align: center; margin: 0 0 5px 0; font-size: 16px; font-weight: 900;">FLASHMART</h3>
            <p style="text-align: center; font-size: 11px; margin: 0 0 10px 0; color: #666;">Jl. Raya Minimarket No. 88, Indonesia</p>
            <div style="font-size: 11px; border-bottom: 1px dashed #333; padding-bottom: 8px; margin-bottom: 8px;" id="receipt-meta">
                Waktu: 2026-11-10 09:00<br>Kasir: Auto-System v3.5
            </div>
            
            <div style="font-size: 11px; font-weight: bold; display: flex; border-bottom: 1px dashed #333; padding-bottom: 4px; margin-bottom: 6px;">
                <span style="flex: 2;">ITEM</span>
                <span style="flex: 1; text-align: center;">QTY</span>
                <span style="flex: 1; text-align: right;">SUBTOTAL</span>
            </div>
            
            <div id="receipt-items-list" style="font-size: 11px; max-height: 140px; overflow-y: auto; margin-bottom: 8px; border-bottom: 1px dashed #333; padding-bottom: 8px;"></div>

            <div style="font-size: 11px; line-height: 1.5;">
                <div style="display: flex; justify-content: space-between;"><span>SUBTOTAL:</span><span id="receipt-subtotal">Rp 0</span></div>
                <div style="display: flex; justify-content: space-between;" id="receipt-disc-row"><span>DISKON:</span><span id="receipt-discount">- Rp 0</span></div>
                <div style="display: flex; justify-content: space-between; font-weight: bold; font-size: 13px; margin: 4px 0;"><span>TOTAL:</span><span id="receipt-total">Rp 0</span></div>
                <div style="display: flex; justify-content: space-between;"><span>BAYAR:</span><span id="receipt-cash">Rp 0</span></div>
                <div style="display: flex; justify-content: space-between; font-weight: bold; color: #03AC03;" id="receipt-change-row"><span>KEMBALIAN:</span><span id="receipt-change">Rp 0</span></div>
            </div>

            <div style="text-align: center; margin-top: 15px; font-size: 10px; color: #555;">
                <p style="margin: 0 0 5px 0;">THANK YOU FOR SHOPPING!</p>
                <div style="font-size: 16px; letter-spacing: 2px;">*FLASHMART9988*</div>
            </div>

            <button class="ripple-btn" onclick="closeModal()" style="background: #03AC03; color: white; border: none; width: 100%; padding: 10px; border-radius: 6px; font-weight: bold; margin-top: 15px; font-size: 12px; cursor: pointer;">Selesai & Tutup Struk</button>
        </div>
    </div>

    <!-- MODAL DETAIL & PETA PELACAKAN KURIR -->
    <div id="tracking-detail-modal">
        <div class="tracking-card">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 10px; margin-bottom: 12px;">
                <h3 style="margin: 0; font-size: 16px; color: #03AC03;">📍 Detail Pelacakan Paket</h3>
                <button onclick="closeTrackingModal()" style="background: none; border: none; font-size: 18px; cursor: pointer; color: #777;">✕</button>
            </div>
            <div id="tracking-detail-content" style="font-size: 13px; line-height: 1.6;"></div>
            <button class="ripple-btn" onclick="closeTrackingModal()" style="background: #03AC03; color: white; border: none; width: 100%; padding: 10px; border-radius: 8px; font-weight: bold; margin-top: 15px; cursor: pointer; font-size: 13px;">Tutup</button>
        </div>
    </div>

    <div class="app-container">
        
        <!-- BERANDA -->
        <div id="view-home" class="view-section active" style="padding: 0 0 15px 0;">
            <div class="header">
                <h3 style="margin:0;">⚡ FlashMart Store</h3>
                <div class="search-bar">
                    <span>🔍</span>
                    <input type="text" id="search-box" placeholder="Cari baju, HP, sembako, skincare..." oninput="filterProducts()">
                </div>
            </div>

            <div class="store-selector">
                <span>🏪 Pilih Toko:</span>
                <select id="store-select" onchange="changeStore()">
                    <option value="Pusat">FlashMart Pusat (Super Lengkap)</option>
                    <option value="Express">FlashMart Express (Kilat)</option>
                    <option value="Grosir">FlashMart Grosir (Partai Besar)</option>
                </select>
            </div>

            <!-- QUICK LINK DIGITAL -->
            <div style="padding: 12px 15px 5px 15px; font-weight: bold; font-size: 13px;">📱 Layanan Pulsa & PPOB</div>
            <div class="digital-grid">
                <div class="digital-item ripple-btn" onclick="openDigital('Pulsa')">📱 Pulsa</div>
                <div class="digital-item ripple-btn" onclick="openDigital('Kuota Data')">🌐 Kuota Data</div>
                <div class="digital-item ripple-btn" onclick="openDigital('Token PLN')">⚡ Token PLN</div>
                <div class="digital-item ripple-btn" onclick="openDigital('E-Money')">🎮 E-Money</div>
            </div>

            <!-- KATEGORI SUPER LENGKAP -->
            <div class="category-scroll" id="category-container">
                <div class="cat-chip active" onclick="selectCategory('Semua', this)">Semua</div>
                <div class="cat-chip" onclick="selectCategory('Sembako', this)">🍚 Sembako</div>
                <div class="cat-chip" onclick="selectCategory('Fashion', this)">👕 Fashion</div>
                <div class="cat-chip" onclick="selectCategory('Elektronik', this)">📱 Elektronik</div>
                <div class="cat-chip" onclick="selectCategory('Skincare', this)">✨ Skincare</div>
                <div class="cat-chip" onclick="selectCategory('Minuman', this)">🧃 Minuman</div>
                <div class="cat-chip" onclick="selectCategory('Perabotan', this)">🪑 Perabotan</div>
                <div class="cat-chip" onclick="selectCategory('Camilan', this)">🍪 Camilan</div>
            </div>

            <div class="banner">
                🔥 Gunakan Voucher <b>FLASHMARTINA</b> untuk Diskon Rp 10.000!
            </div>

            <div style="padding: 0 15px 10px 15px; font-weight: bold; font-size: 14px;" id="store-title-label">Katalog Produk - FlashMart Pusat</div>
            <div class="product-grid" id="product-list"></div>
        </div>

        <!-- KERANJANG & CHECKOUT (MODEL KERANJANG SHOPEE) -->
        <div id="view-cart" class="view-section">
            <h3 style="margin-top: 0;">🛒 Keranjang Saya</h3>
            <div id="cart-items-container">
                <p style="color: #777; text-align: center; margin-top: 30px;">Keranjang masih kosong.</p>
            </div>
            <div id="cart-summary" style="display:none; margin-top: 15px; background: var(--card-bg); border: 1px solid var(--border-color); padding: 15px; border-radius: 12px;">
                <div style="font-size: 12px; font-weight: bold; margin-bottom: 6px; color: #FA591D;">🎟️ Voucher FlashMart</div>
                <div style="display: flex; gap: 6px; margin-bottom: 12px;">
                    <input type="text" id="voucher-input" placeholder="Masukkan kode (FLASHMARTINA)" class="admin-input" style="margin-bottom: 0; flex: 1;">
                    <button class="ripple-btn" onclick="applyVoucher()" style="background: #FA591D; color: white; border: none; padding: 0 14px; border-radius: 8px; cursor: pointer; font-size: 12px; font-weight: bold;">Pakai</button>
                </div>
                
                <div style="font-size: 13px; margin-bottom: 5px;">Subtotal Produk Dipilih: <span id="subtotal-text" style="float: right; font-weight: bold;">Rp 0</span></div>
                <div id="discount-row" style="font-size: 13px; margin-bottom: 5px; color: #03AC03; display: none;">Diskon Voucher: <span id="discount-text" style="float: right; font-weight: bold;">- Rp 0</span></div>
                
                <div style="margin: 12px 0;">
                    <label style="font-size: 13px; font-weight: bold;">Metode Pembayaran:</label>
                    <select id="payment-method" class="admin-input" style="margin-top: 5px;" onchange="toggleQR()">
                        <option value="Tunai">Tunai / Cash (Bayar di Kasir)</option>
                        <option value="QRIS">QRIS (Scan & Cashback Instant)</option>
                        <option value="Transfer Bank">Transfer Bank (BCA / Mandiri / BRI)</option>
                        <option value="COD">Bayar di Tempat (COD)</option>
                    </select>
                </div>

                <div id="cash-payment-box" style="margin-bottom: 12px;">
                    <label style="font-size: 13px; font-weight: bold;">Nominal Uang Pembeli (Rp):</label>
                    <input type="number" id="cash-given" placeholder="Contoh: 100000" class="admin-input" style="margin-top: 5px;" oninput="calculateChange()">
                    <div style="font-size: 13px; font-weight: bold; color: #03AC03; margin-top: 4px;" id="change-text">Uang Kembalian: Rp 0</div>
                </div>

                <div id="qris-display" class="qr-box" style="display: none;">
                    <div style="font-size: 12px; font-weight: bold; color: #333; margin-bottom: 5px;">Scan Kode QRIS Di Bawah Ini:</div>
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=FLASHMART-PAYMENT-QRIS" alt="QRIS Code">
                    <div style="font-size: 11px; color: #666; margin-top: 5px;">Dapat di-scan memakai GoPay, OVO, Dana & M-Banking.</div>
                </div>

                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 12px; border-top: 1px dashed var(--border-color); padding-top: 12px;">
                    <div>
                        <div style="font-size: 11px; color: #777;">Total Pembayaran</div>
                        <div id="grandtotal-text" style="font-size: 18px; font-weight: bold; color: #FA591D;">Rp 0</div>
                    </div>
                    <button class="ripple-btn" id="btn-checkout-main" onclick="checkout()" style="background: #FA591D; color: white; border: none; padding: 12px 20px; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 13px;">Checkout (0)</button>
                </div>
            </div>
        </div>

        <!-- TAB LAYANAN DIGITAL -->
        <div id="view-pulsa" class="view-section">
            <h3 id="digital-title-label">📱 Isi Pulsa & PPOB</h3>
            <div style="background: var(--card-bg); border: 1px solid var(--border-color); padding: 15px; border-radius: 12px; margin-bottom: 15px;">
                
                <div id="field-provider-group">
                    <label style="font-size: 13px; font-weight: bold;" id="label-provider">1. Pilih Operator / Provider:</label>
                    <select id="digital-provider" class="admin-input" style="margin-top: 5px;">
                        <option value="Telkomsel">Telkomsel</option>
                        <option value="Indosat">Indosat Ooredoo</option>
                        <option value="XL">XL Axiata</option>
                        <option value="Tri">Tri (3)</option>
                    </select>
                </div>

                <label style="font-size: 13px; font-weight: bold;" id="label-target">2. Masukkan Nomor HP / ID Pelanggan:</label>
                <input type="text" id="digital-target" placeholder="Contoh: 081234567890" class="admin-input" style="margin-top: 5px;">

                <label style="font-size: 13px; font-weight: bold;">3. Pilih Nominal / Produk:</label>
                <select id="digital-nominal" class="admin-input" style="margin-top: 5px;">
                    <option value="11000">Pulsa 10.000 (Rp 11.000)</option>
                    <option value="26000">Pulsa 25.000 (Rp 26.000)</option>
                    <option value="51000">Pulsa 50.000 (Rp 51.000)</option>
                    <option value="101000">Pulsa 100.000 (Rp 101.000)</option>
                </select>

                <div style="margin: 15px 0;">
                    <label style="font-size: 13px; font-weight: bold;">Pilih Metode Pembayaran Digital:</label>
                    <select id="digital-payment" class="admin-input" style="margin-top: 5px;" onchange="toggleDigitalQR()">
                        <option value="QRIS">QRIS (Instant & Auto-Confirm)</option>
                        <option value="Transfer Bank">Transfer Bank (BCA/Mandiri/BRI)</option>
                        <option value="Saldo Poin">Potong Saldo Poin / Dompet</option>
                    </select>
                </div>

                <div id="digital-qr-box" class="qr-box">
                    <div style="font-size: 12px; font-weight: bold; color: #333; margin-bottom: 5px;">Scan QRIS Pembayaran:</div>
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=160x160&data=FLASHMART-DIGITAL" alt="QRIS">
                </div>

                <button class="ripple-btn" onclick="processDigitalPayment()" style="background: #03AC03; color: white; border: none; width: 100%; padding: 12px; border-radius: 10px; font-weight: bold; cursor: pointer; margin-top: 10px;">⚡ Bayar & Proses Transaksi</button>
            </div>
        </div>

        <!-- RIWAYAT & PELACAKAN -->
        <div id="view-history" class="view-section">
            <h3>📜 Riwayat & Pelacakan Kurir</h3>
            <p style="font-size: 12px; color: #666; margin-bottom: 12px;">👉 Tekan salah satu kartu pesanan di bawah untuk melihat detail posisi kurir dan peta pengiriman!</p>
            <div id="history-container">
                <p style="color: #777; text-align: center; margin-top: 30px;">Belum ada riwayat transaksi.</p>
            </div>
        </div>

        <!-- AKUN -->
        <div id="view-account" class="view-section">
            <h3>👤 Akun & Kelola Stok</h3>
            <div class="profile-card">
                <div style="font-size: 18px; font-weight: bold;">⚡ Pelanggan Setia</div>
                <div style="font-size: 13px; opacity: 0.9; margin-top: 4px;">No: 08123456789 • Gold VIP</div>
                <div style="background: rgba(255,255,255,0.25); padding: 8px 12px; border-radius: 10px; margin-top: 12px; display: flex; justify-content: space-between; font-weight: bold;">
                    <span>⭐ Saldo Poin A-Voucher</span>
                    <span id="user-points">150 Poin</span>
                </div>
            </div>

            <div style="background: var(--card-bg); border: 1px solid var(--border-color); padding: 15px; border-radius: 12px; margin-bottom: 15px;">
                <h4 style="margin-top: 0; color: #03AC03;">📦 Tambah Produk Baru</h4>
                <input type="text" id="new-name" placeholder="Nama Produk" class="admin-input">
                <input type="number" id="new-price" placeholder="Harga (Rp)" class="admin-input">
                <input type="number" id="new-stock" placeholder="Jumlah Stok" class="admin-input">
                <select id="new-category" class="admin-input">
                    <option value="Sembako">Sembako</option>
                    <option value="Fashion">Fashion</option>
                    <option value="Elektronik">Elektronik</option>
                    <option value="Skincare">Skincare</option>
                    <option value="Minuman">Minuman</option>
                    <option value="Perabotan">Perabotan</option>
                    <option value="Camilan">Camilan</option>
                </select>
                <input type="text" id="new-icon" placeholder="Emoji Ikon (Contoh: 🧥)" class="admin-input">
                <button class="ripple-btn" onclick="addNewProduct()" style="background: #03AC03; color: white; border: none; width: 100%; padding: 10px; border-radius: 8px; font-weight: bold; cursor: pointer;">Simpan Produk</button>
            </div>

            <div style="background: var(--card-bg); border: 1px solid var(--border-color); padding: 15px; border-radius: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center; font-weight: bold;">
                    <span>🌙 Tampilan Mode Gelap</span>
                    <input type="checkbox" id="theme-toggle" onchange="toggleTheme()" style="width: 20px; height: 20px; cursor: pointer;">
                </div>
            </div>
        </div>

        <!-- NAVIGASI BAWAH -->
        <div class="bottom-nav">
            <button class="nav-item active" onclick="switchTab('home', this)">
                <div>🏠</div>Beranda
            </button>
            <button class="nav-item" onclick="switchTab('cart', this)">
                <div>🛒</div>Keranjang
            </button>
            <button class="nav-item" onclick="switchTab('pulsa', this)">
                <div>📱</div>Digital
            </button>
            <button class="nav-item" onclick="switchTab('history', this)">
                <div>🚚</div>Lacakan
            </button>
            <button class="nav-item" onclick="switchTab('account', this)">
                <div>👤</div>Akun
            </button>
        </div>
    </div>

    <script>
        window.addEventListener('load', function() {
            setTimeout(function() {
                const splash = document.getElementById('splash-screen');
                if (splash) {
                    splash.style.opacity = '0';
                    splash.style.visibility = 'hidden';
                }
            }, 1800);
        });

        const storesData = {
            "Pusat": [
                { id: 101, name: "Beras Premium Super 5kg", price: 69000, stock: 25, category: "Sembako", icon: "🌾" },
                { id: 102, name: "Minyak Goreng Pouch 2L", price: 38000, stock: 30, category: "Sembako", icon: "🍳" },
                { id: 103, name: "Gula Pasir Putih 1kg", price: 17500, stock: 40, category: "Sembako", icon: "🍬" },
                { id: 104, name: "Telur Ayam Negeri 1kg", price: 28000, stock: 20, category: "Sembako", icon: "🥚" },
                { id: 105, name: "Mie Instan Soto (1 Dus)", price: 115000, stock: 15, category: "Sembako", icon: "📦" },
                { id: 106, name: "Kemeja Flanel Casual Pria", price: 135000, stock: 12, category: "Fashion", icon: "👔" },
                { id: 107, name: "Kaos Polos Cotton Combed 30s", price: 55000, stock: 30, category: "Fashion", icon: "👕" },
                { id: 108, name: "Celana Jeans Slim Fit Pria", price: 185000, stock: 10, category: "Fashion", icon: "👖" },
                { id: 109, name: "Gamis Syari Wanita Modern", price: 195000, stock: 14, category: "Fashion", icon: "👗" },
                { id: 110, name: "Smartphone Android 4G RAM 4GB", price: 1450000, stock: 5, category: "Elektronik", icon: "📱" },
                { id: 111, name: "Powerbank Fast Charging 10000mAh", price: 185000, stock: 8, category: "Elektronik", icon: "🔋" },
                { id: 112, name: "Headset Gaming Extra Bass", price: 75000, stock: 12, category: "Elektronik", icon: "🎧" },
                { id: 113, name: "Smartwatch Fitness Tracker", price: 245000, stock: 7, category: "Elektronik", icon: "⌚" },
                { id: 114, name: "Skincare Brightening Serum 30ml", price: 85000, stock: 20, category: "Skincare", icon: "✨" },
                { id: 115, name: "Facial Wash Glowing 100ml", price: 35000, stock: 25, category: "Skincare", icon: "🧴" },
                { id: 116, name: "Sunscreen SPF 50 PA++++", price: 65000, stock: 18, category: "Skincare", icon: "☀️" },
                { id: 117, name: "Susu UHT Ultra Milk 1L", price: 19500, stock: 30, category: "Minuman", icon: "🥛" },
                { id: 118, name: "Kopi Hitam Robusta 380g", price: 16500, stock: 22, category: "Minuman", icon: "☕" },
                { id: 119, name: "Teh Kotak Melati Sosro 300ml", price: 4500, stock: 50, category: "Minuman", icon: "🧃" },
                { id: 120, name: "Blender Kaca Multifungsi 2L", price: 275000, stock: 6, category: "Perabotan", icon: "🧊" },
                { id: 121, name: "Set Panci Stainless Anti Lengket", price: 320000, stock: 5, category: "Perabotan", icon: "🍲" },
                { id: 122, name: "Keripik Singkong Balado Pedas", price: 12000, stock: 45, category: "Camilan", icon: "🍟" },
                { id: 123, name: "Biskuit Cokelat Kelapa Kaleng", price: 29000, stock: 18, category: "Camilan", icon: "🍪" }
            ],
            "Express": [
                { id: 201, name: "Air Mineral Botol 600ml (1 Dus)", price: 35000, stock: 50, category: "Minuman", icon: "💧" },
                { id: 202, name: "Roti Tawar Gandum Spesial", price: 18000, stock: 15, category: "Camilan", icon: "🍞" },
                { id: 203, name: "Masker Medis 3ply (Box isi 50)", price: 25000, stock: 40, category: "Skincare", icon: "😷" },
                { id: 204, name: "Kabel Data Type-C Fast Charge", price: 35000, stock: 25, category: "Elektronik", icon: "🔌" },
                { id: 205, name: "Cokelat Batang Premium Cadbury", price: 15000, stock: 30, category: "Camilan", icon: "🍫" },
                { id: 206, name: "Tisu Basah Antiseptik Travel", price: 11000, stock: 35, category: "Skincare", icon: "🧻" }
            ],
            "Grosir": [
                { id: 301, name: "Beras Karung Grosir 25kg", price: 330000, stock: 8, category: "Sembako", icon: "🛍️" },
                { id: 302, name: "Minyak Goreng Jerigen 5L", price: 92000, stock: 10, category: "Sembako", icon: "🛢️" },
                { id: 303, name: "Gula Pasir Karung 10kg", price: 145000, stock: 12, category: "Sembako", icon: "🍬" },
                { id: 304, name: "Deterjen Bubuk Cuci 5kg", price: 68000, stock: 15, category: "Perabotan", icon: "🧼" },
                { id: 305, name: "Mie Instan (3 Dus Sekaligus)", price: 340000, stock: 6, category: "Sembako", icon: "📦" },
                { id: 306, name: "Kardus Kaos Polos Grosir (Isi 10pcs)", price: 450000, stock: 4, category: "Fashion", icon: "👕" }
            ]
        };

        let currentStore = "Pusat";
        let cart = {};
        let points = 150;
        let history = [];
        let discountActive = false;
        let activeCategory = 'Semua';
        let currentDigitalType = 'Pulsa';

        function openDigital(type) {
            currentDigitalType = type;
            switchTab('pulsa', document.querySelectorAll('.nav-item')[2]);
            
            const titleLabel = document.getElementById('digital-title-label');
            const targetLabel = document.getElementById('label-target');
            const targetInput = document.getElementById('digital-target');
            const providerGroup = document.getElementById('field-provider-group');
            const nominalSelect = document.getElementById('digital-nominal');
            const labelProvider = document.getElementById('label-provider');

            if (type === 'Pulsa') {
                titleLabel.innerText = "📱 Isi Pulsa Seluler";
                targetLabel.innerText = "2. Masukkan Nomor HP:";
                targetInput.placeholder = "Contoh: 081234567890";
                providerGroup.style.display = 'block';
                labelProvider.innerText = "1. Pilih Operator Seluler:";
                document.getElementById('digital-provider').innerHTML = `
                    <option value="Telkomsel">Telkomsel</option>
                    <option value="Indosat">Indosat Ooredoo</option>
                    <option value="XL">XL Axiata</option>
                    <option value="Tri">Tri (3)</option>
                    <option value="Smartfren">Smartfren</option>
                    <option value="Axis">Axis</option>
                `;
                nominalSelect.innerHTML = `
                    <option value="11000">Pulsa 10.000 (Rp 11.000)</option>
                    <option value="26000">Pulsa 25.000 (Rp 26.000)</option>
                    <option value="51000">Pulsa 50.000 (Rp 51.000)</option>
                    <option value="101000">Pulsa 100.000 (Rp 101.000)</option>
                `;
            } else if (type === 'Kuota Data') {
                titleLabel.innerText = "🌐 Beli Paket Kuota Data Internet";
                targetLabel.innerText = "2. Masukkan Nomor HP / Modem:";
                targetInput.placeholder = "Contoh: 081234567890";
                providerGroup.style.display = 'block';
                labelProvider.innerText = "1. Pilih Provider Internet:";
                document.getElementById('digital-provider').innerHTML = `
                    <option value="Telkomsel Data">Telkomsel Data</option>
                    <option value="Indosat Freedom">Indosat Freedom</option>
                    <option value="XL Xtra Combo">XL Xtra Combo</option>
                    <option value="Tri AlwaysOn">Tri Aon</option>
                `;
                nominalSelect.innerHTML = `
                    <option value="25000">Paket Freedom 3GB (Rp 25.000)</option>
                    <option value="55000">Paket Internet 15GB (Rp 55.000)</option>
                    <option value="100000">Paket Jumbo 40GB (Rp 100.000)</option>
                `;
            } else if (type === 'Token PLN') {
                titleLabel.innerText = "⚡ Pembelian Token Listrik PLN";
                targetLabel.innerText = "1. Masukkan No. Meter / ID Pelanggan:";
                targetInput.placeholder = "Contoh: 32109876543";
                providerGroup.style.display = 'none';
                nominalSelect.innerHTML = `
                    <option value="20500">Token PLN 20.000 (Rp 20.500)</option>
                    <option value="50500">Token PLN 50.000 (Rp 50.500)</option>
                    <option value="100500">Token PLN 100.000 (Rp 100.500)</option>
                    <option value="200500">Token PLN 200.000 (Rp 200.500)</option>
                `;
            } else if (type === 'E-Money') {
                titleLabel.innerText = "🎮 Top Up E-Wallet & Games";
                targetLabel.innerText = "2. Masukkan No. Akun / User ID Game:";
                targetInput.placeholder = "Contoh: 081234567890 / ID Game / Zone ID";
                providerGroup.style.display = 'block';
                labelProvider.innerText = "1. Pilih E-Wallet / Game:";
                document.getElementById('digital-provider').innerHTML = `
                    <option value="GoPay">GoPay Customer</option>
                    <option value="DANA">DANA Dompet Digital</option>
                    <option value="OVO">OVO Cash</option>
                    <option value="ShopeePay">ShopeePay</option>
                    <option value="Mobile Legends">Mobile Legends (Moonton)</option>
                    <option value="Free Fire">Free Fire (Garena)</option>
                    <option value="PUBG Mobile">PUBG Mobile</option>
                `;
                nominalSelect.innerHTML = `
                    <option value="20000">Top Up Saldo / Voucher 20.000 (Rp 20.000)</option>
                    <option value="50000">Top Up Saldo / Voucher 50.000 (Rp 50.000)</option>
                    <option value="60000">Diamond / UC Special Item (Rp 60.000)</option>
                    <option value="100500">Token PLN 100.000 (Rp 100.500)</option>
                    <option value="200500">Token PLN 200.000 (Rp 200.500)</option>
                `;
            } else if (type === 'E-Money') {
                titleLabel.innerText = "🎮 Top Up E-Wallet & Games";
                targetLabel.innerText = "2. Masukkan No. Akun / User ID Game:";
                targetInput.placeholder = "Contoh: 081234567890 / ID Game / Zone ID";
                providerGroup.style.display = 'block';
                labelProvider.innerText = "1. Pilih E-Wallet / Game:";
                document.getElementById('digital-provider').innerHTML = `
                    <option value="GoPay">GoPay Customer</option>
                    <option value="DANA">DANA Dompet Digital</option>
                    <option value="OVO">OVO Cash</option>
                    <option value="ShopeePay">ShopeePay</option>
                    <option value="Mobile Legends">Mobile Legends (Moonton)</option>
                    <option value="Free Fire">Free Fire (Garena)</option>
                    <option value="PUBG Mobile">PUBG Mobile</option>
                `;
                nominalSelect.innerHTML = `
                    <option value="20000">Top Up Saldo / Voucher 20.000 (Rp 20.000)</option>
                    <option value="50000">Top Up Saldo / Voucher 50.000 (Rp 50.000)</option>
                    <option value="60000">Diamond / UC Special Item (Rp 60.000)</option>
                    <option value="105000">Top Up Besar 100.000 (Rp 105.000)</option>
                `;
            }
        }

        function toggleQR() {
            const method = document.getElementById('payment-method').value;
            document.getElementById('qris-display').style.display = (method === 'QRIS') ? 'block' : 'none';
            document.getElementById('cash-payment-box').style.display = (method === 'Tunai') ? 'block' : 'none';
        }

        function toggleDigitalQR() {
            const method = document.getElementById('digital-payment').value;
            document.getElementById('digital-qr-box').style.display = (method === 'QRIS' || method === 'Transfer Bank') ? 'block' : 'none';
        }

        function getSelectedSubtotal() {
            return Object.values(cart)
                .filter(item => item.selected)
                .reduce((sum, item) => sum + (item.price * item.qty), 0);
        }

        function calculateChange() {
            let subtotal = getSelectedSubtotal();
            const discount = (discountActive && subtotal > 0) ? 10000 : 0;
            const grandTotal = Math.max(0, subtotal - discount);
            const cashGiven = parseFloat(document.getElementById('cash-given').value) || 0;
            const change = cashGiven - grandTotal;

            const changeText = document.getElementById('change-text');
            if (change >= 0) {
                changeText.innerText = "Uang Kembalian: Rp " + change.toLocaleString('id-ID');
                changeText.style.color = "#03AC03";
            } else {
                changeText.innerText = "Uang Kurang: Rp " + Math.abs(change).toLocaleString('id-ID');
                changeText.style.color = "#FA591D";
            }
        }

        function changeStore() {
            currentStore = document.getElementById('store-select').value;
            document.getElementById('store-title-label').innerText = "Katalog Produk - FlashMart " + currentStore;
            activeCategory = 'Semua';
            document.querySelectorAll('.cat-chip').forEach((el, index) => {
                if (index === 0) el.classList.add('active');
                else el.classList.remove('active');
            });
            document.getElementById('search-box').value = '';
            filterProducts();
        }

        function renderProducts(listToRender) {
            const list = document.getElementById('product-list');
            if (listToRender.length === 0) {
                list.innerHTML = '<p style="grid-column: span 2; text-align: center; color: #777;">Tidak ada produk yang cocok.</p>';
                return;
            }
            list.innerHTML = listToRender.map(p => `
                <div class="product-card">
                    <div style="font-size: 34px;">` + p.icon + `</div>
                    <div class="product-title">` + p.name + `</div>
                    <div class="product-stock">Stok: ` + p.stock + `</div>
                    <div class="product-price">Rp ` + p.price.toLocaleString('id-ID') + `</div>
                    <div class="btn-group">
                        <button class="btn-cart ripple-btn" onclick="addToCart(` + p.id + `)">+ Keranjang</button>
                        <button class="btn-buy-now ripple-btn" onclick="buyNow(` + p.id + `)">Beli</button>
                    </div>
                </div>
            `).join('');
        }

        function selectCategory(category, element) {
            activeCategory = category;
            document.querySelectorAll('.cat-chip').forEach(el => el.classList.remove('active'));
            element.classList.add('active');
            filterProducts();
        }

        function filterProducts() {
            const query = document.getElementById('search-box').value.toLowerCase();
            const storeProducts = storesData[currentStore];
            const filtered = storeProducts.filter(p => {
                const matchCat = (activeCategory === 'Semua' || p.category === activeCategory);
                const matchQuery = p.name.toLowerCase().includes(query);
                return matchCat && matchQuery;
            });
            renderProducts(filtered);
        }

        function switchTab(tabName, element) {
            document.querySelectorAll('.view-section').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            document.getElementById('view-' + tabName).classList.add('active');
            if (element) element.classList.add('active');

            if (tabName === 'cart') renderCart();
            if (tabName === 'history') renderHistory();
        }

        function addToCart(id) {
            const prod = storesData[currentStore].find(p => p.id === id);
            if (prod.stock <= 0) {
                alert("Stok barang habis!");
                return;
            }
            prod.stock -= 1;
            if (cart[id]) { 
                cart[id].qty += 1; 
                cart[id].selected = true;
            } else { 
                cart[id] = { ...prod, qty: 1, store: currentStore, selected: true }; 
            }
            filterProducts();
            alert(prod.name + " ditambahkan ke keranjang!");
        }

        function buyNow(id) {
            addToCart(id);
            switchTab('cart', document.querySelectorAll('.nav-item')[1]);
        }

        function toggleSelectItem(id) {
            if (cart[id]) {
                cart[id].selected = !cart[id].selected;
                renderCart();
            }
        }

        function toggleSelectAll(checked) {
            for (let id in cart) {
                cart[id].selected = checked;
            }
            renderCart();
        }

        function toggleSelectStore(storeName, checked) {
            for (let id in cart) {
                if (cart[id].store === storeName) {
                    cart[id].selected = checked;
                }
            }
            renderCart();
        }

        function removeFromCart(id) {
            if (!cart[id]) return;
            for (let s in storesData) {
                let found = storesData[s].find(p => p.id == id);
                if (found) {
                    found.stock += cart[id].qty;
                    break;
                }
            }
            delete cart[id];
            renderCart();
            filterProducts();
        }

        function renderCart() {
            const container = document.getElementById('cart-items-container');
            const summary = document.getElementById('cart-summary');
            const keys = Object.keys(cart);

            if (keys.length === 0) {
                container.innerHTML = '<p style="color: #777; text-align: center; margin-top: 30px;">Keranjang masih kosong.</p>';
                summary.style.display = 'none';
                return;
            }

            summary.style.display = 'block';
            const allSelected = keys.every(id => cart[id].selected);
            const selectedCount = keys.filter(id => cart[id].selected).length;

            // Kelompokkan barang berdasarkan Toko (Gaya Keranjang Shopee)
            const groupedByStore = {};
            keys.forEach(id => {
                const item = cart[id];
                if (!groupedByStore[item.store]) groupedByStore[item.store] = [];
                groupedByStore[item.store].push(item);
            });

            let html = `
                <div class="cart-select-all-bar">
                    <label style="display: flex; align-items: center; gap: 8px; cursor: pointer;">
                        <input type="checkbox" class="cart-checkbox" ${allSelected ? 'checked' : ''} onchange="toggleSelectAll(this.checked)">
                        <span>Pilih Semua (${keys.length})</span>
                    </label>
                    <span style="font-size: 12px; color: #FA591D;">${selectedCount} dipilih</span>
                </div>
            `;

            for (let storeName in groupedByStore) {
                const storeItems = groupedByStore[storeName];
                const allStoreSelected = storeItems.every(it => it.selected);

                html += `
                    <div class="cart-store-group">
                        <div class="cart-store-header">
                            <input type="checkbox" class="cart-checkbox" ${allStoreSelected ? 'checked' : ''} onchange="toggleSelectStore('${storeName}', this.checked)">
                            <span>🏪 FlashMart ${storeName}</span>
                        </div>
                `;

                storeItems.forEach(item => {
                    html += `
                        <div class="cart-item-card">
                            <input type="checkbox" class="cart-checkbox" ${item.selected ? 'checked' : ''} onchange="toggleSelectItem(${item.id})">
                            <div class="cart-item-icon">${item.icon}</div>
                            <div class="cart-item-info">
                                <div class="cart-item-title">${item.name}</div>
                                <div class="cart-item-price">Rp ${item.price.toLocaleString('id-ID')}</div>
                                <div class="qty-stepper">
                                    <button onclick="changeQty(${item.id}, -1)">-</button>
                                    <span>${item.qty}</span>
                                    <button onclick="changeQty(${item.id}, 1)">+</button>
                                </div>
                            </div>
                            <button class="btn-del-item" title="Hapus barang" onclick="removeFromCart(${item.id})">🗑️</button>
                        </div>
                    `;
                });

                html += `</div>`;
            }

            container.innerHTML = html;
            let subtotal = getSelectedSubtotal();
            updateSummary(subtotal, selectedCount);
            calculateChange();
        }

        function changeQty(id, delta) {
            let prod = null;
            for (let s in storesData) {
                let found = storesData[s].find(p => p.id == id);
                if (found) { prod = found; break; }
            }

            if (delta > 0) {
                if (prod.stock <= 0) { alert("Stok habis!"); return; }
                prod.stock -= 1;
                cart[id].qty += 1;
            } else {
                prod.stock += 1;
                cart[id].qty -= 1;
                if (cart[id].qty <= 0) delete cart[id];
            }
            renderCart();
            filterProducts();
        }

        function applyVoucher() {
            const code = document.getElementById('voucher-input').value.trim().toUpperCase();
            if (code === 'FLASHMARTINA') {
                discountActive = true;
                alert("🎉 Voucher Berhasil Digunakan! Potongan Rp 10.000");
            } else {
                discountActive = false;
                alert("❌ Kode Voucher tidak valid.");
            }
            const selectedCount = Object.keys(cart).filter(id => cart[id].selected).length;
            updateSummary(getSelectedSubtotal(), selectedCount);
            calculateChange();
        }

        function updateSummary(subtotal, selectedCount) {
            const discount = (discountActive && subtotal > 0) ? 10000 : 0;
            const grandTotal = Math.max(0, subtotal - discount);
            document.getElementById('subtotal-text').innerText = 'Rp ' + subtotal.toLocaleString('id-ID');
            const discRow = document.getElementById('discount-row');
            if (discount > 0) {
                discRow.style.display = 'flex';
                document.getElementById('discount-text').innerText = '- Rp ' + discount.toLocaleString('id-ID');
            } else { discRow.style.display = 'none'; }
            document.getElementById('grandtotal-text').innerText = 'Rp ' + grandTotal.toLocaleString('id-ID');
            document.getElementById('btn-checkout-main').innerText = 'Checkout (' + selectedCount + ')';
        }

        function checkout() {
            const selectedIds = Object.keys(cart).filter(id => cart[id].selected);
            if (selectedIds.length === 0) {
                alert("Centang minimal 1 barang di keranjang terlebih dahulu untuk checkout!");
                return;
            }

            let subtotal = getSelectedSubtotal();
            const discount = (discountActive && subtotal > 0) ? 10000 : 0;
            const grandTotal = Math.max(0, subtotal - discount);
            const method = document.getElementById('payment-method').value;
            const cashGiven = parseFloat(document.getElementById('cash-given').value) || grandTotal;
            const change = cashGiven - grandTotal;

            if (method === 'Tunai' && cashGiven < grandTotal) {
                alert("Nominal uang tunai kurang dari total belanja!");
                return;
            }

            const earnedPoints = Math.floor(grandTotal / 10000);
            points += earnedPoints;
            document.getElementById('user-points').innerText = points + ' Poin';
            const now = new Date();
            const dateStr = now.toLocaleDateString('id-ID', { day: 'numeric', month: 'short', year: 'numeric' });
            const timeStr = now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' });
            
            let arrivalDate = new Date(now);
            arrivalDate.setDate(now.getDate() + 2);
            const arrivalStr = arrivalDate.toLocaleDateString('id-ID', { day: 'numeric', month: 'short', year: 'numeric' });

            let receiptHtml = '';
            let itemsSummaryArray = [];
            selectedIds.forEach(id => {
                const item = cart[id];
                itemsSummaryArray.push(item.name + ' (' + item.qty + 'x)');
                receiptHtml += `<div style="display: flex; justify-content: space-between; margin-bottom: 2px;">
                    <span style="flex: 2;">${item.name}</span>
                    <span style="flex: 1; text-align: center;">${item.qty}</span>
                    <span style="flex: 1; text-align: right;">Rp ${(item.price * item.qty).toLocaleString('id-ID')}</span>
                </div>`;
                delete cart[id]; // Hapus hanya item yang di-checkout
            });

            document.getElementById('receipt-items-list').innerHTML = receiptHtml;
            document.getElementById('receipt-meta').innerHTML = "Waktu: " + dateStr + " " + timeStr + "<br>Metode: " + method;
            document.getElementById('receipt-subtotal').innerText = "Rp " + subtotal.toLocaleString('id-ID');
            
            if (discount > 0) {
                document.getElementById('receipt-disc-row').style.display = 'flex';
                document.getElementById('receipt-discount').innerText = "- Rp " + discount.toLocaleString('id-ID');
            } else {
                document.getElementById('receipt-disc-row').style.display = 'none';
            }
            
            document.getElementById('receipt-total').innerText = "Rp " + grandTotal.toLocaleString('id-ID');
            document.getElementById('receipt-cash').innerText = "Rp " + cashGiven.toLocaleString('id-ID');
            document.getElementById('receipt-change').innerText = "Rp " + change.toLocaleString('id-ID');

            history.unshift({
                orderId: "FM-" + Math.floor(100000 + Math.random() * 900000),
                date: dateStr + " | " + timeStr,
                arrivalEst: arrivalStr,
                total: grandTotal,
                payment: method,
                items: itemsSummaryArray.join(', '),
                earned: earnedPoints,
                status: "Dalam Perjalanan Kurir 🚚",
                courier: "FlashExpress (Kurir VIP)",
                location: "Sorting Center Gudang Utama (Jakarta / Hub Terdekat)"
            });

            discountActive = false;
            document.getElementById('cash-given').value = '';
            document.getElementById('success-modal').style.display = 'flex';
        }

        function processDigitalPayment() {
            const target = document.getElementById('digital-target').value.trim();
            const provider = document.getElementById('digital-provider').value;
            const price = parseInt(document.getElementById('digital-nominal').value);
            const paymentMethod = document.getElementById('digital-payment').value;

            if (!target || target.length < 3) {
                alert("Masukkan nomor tujuan / ID akun yang valid!");
                return;
            }

            const earnedPoints = Math.floor(price / 10000);
            points += earnedPoints;
            document.getElementById('user-points').innerText = points + ' Poin';
            const now = new Date();
            const dateStr = now.toLocaleDateString('id-ID', { day: 'numeric', month: 'short', year: 'numeric' });
            const timeStr = now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' });

            document.getElementById('receipt-meta').innerHTML = "Waktu: " + dateStr + " " + timeStr + "<br>Layanan: " + currentDigitalType + " (" + provider + ")";
            document.getElementById('receipt-items-list').innerHTML = `
                <div style="display: flex; justify-content: space-between;">
                    <span style="flex: 2;">${currentDigitalType} - ${provider}<br><small>Tujuan: ${target}</small></span>
                    <span style="flex: 1; text-align: center;">1</span>
                    <span style="flex: 1; text-align: right;">Rp ${price.toLocaleString('id-ID')}</span>
                </div>
            `;
            document.getElementById('receipt-subtotal').innerText = "Rp " + price.toLocaleString('id-ID');
            document.getElementById('receipt-disc-row').style.display = 'none';
            document.getElementById('receipt-total').innerText = "Rp " + price.toLocaleString('id-ID');
            document.getElementById('receipt-cash').innerText = "Rp " + price.toLocaleString('id-ID');
            document.getElementById('receipt-change').innerText = "Rp 0";

            history.unshift({
                orderId: "PPOB-" + Math.floor(100000 + Math.random() * 900000),
                date: dateStr + " | " + timeStr,
                arrivalEst: "Instant (Detik Ini)",
                total: price,
           payment: currentDigitalType + " (" + paymentMethod + ")",
                items: currentDigitalType + " " + provider + " (" + target + ")",
                earned: earnedPoints,
                status: currentDigitalType + " Berhasil & Sukses ✅",
                courier: "Sistem Otomatis PPOB",
                location: "Server Pusat Operator (Online)"
            });

            document.getElementById('digital-target').value = '';
            document.getElementById('success-modal').style.display = 'flex';
        }

        function closeModal() {
            document.getElementById('success-modal').style.display = 'none';
            switchTab('history', document.querySelectorAll('.nav-item')[3]);
        }

        function closeTrackingModal() {
            document.getElementById('tracking-detail-modal').style.display = 'none';
        }

        function showTrackingDetail(index) {
            const tx = history[index];
            const detailModal = document.getElementById('tracking-detail-modal');
            const content = document.getElementById('tracking-detail-content');

            content.innerHTML = `
                <div style="background: var(--bg-color); padding: 10px; border-radius: 8px; margin-bottom: 10px;">
                    <strong>No. Resi / ID:</strong> ${tx.orderId}<br>
                    <strong>Waktu Pesan:</strong> ${tx.date}<br>
                    <strong>Estimasi Tiba:</strong> <span style="color: #03AC03; font-weight: bold;">${tx.arrivalEst}</span><br>
                    <strong>Kurir Pengantar:</strong> ${tx.courier}<br>
                    <strong>Metode Bayar:</strong> ${tx.payment}
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>Isi Paket:</strong><br>
                    <span style="color: #555;">${tx.items}</span>
                </div>
                <div style="background: #e8f5e9; color: #2e7d32; padding: 10px; border-radius: 8px; font-weight: bold; margin-bottom: 12px; font-size: 12px;">
                    📍 Posisi Terkini:<br>
                    ${tx.location}
                </div>
                <div style="border: 2px dashed #03AC03; border-radius: 8px; overflow: hidden; background: #fff; text-align: center;">
                    <iframe width="100%" height="160" style="border:0;" loading="lazy" allowfullscreen src="https://maps.google.com/maps?q=-6.2088,106.8456&z=14&output=embed"></iframe>
                    <div style="font-size: 11px; padding: 6px; color: #555; background: #f1f8e9;">🗺️ Simulasi Live Tracking Kurir FlashMart</div>
                </div>
            `;
            detailModal.style.display = 'flex';
        }

        function renderHistory() {
            const container = document.getElementById('history-container');
            if (history.length === 0) {
                container.innerHTML = '<p style="color: #777; text-align: center; margin-top: 30px;">Belum ada riwayat transaksi.</p>';
                return;
            }

            container.innerHTML = history.map((tx, idx) => `
                <div class="tracker-box" onclick="showTrackingDetail(${idx})">
                    <div style="display: flex; justify-content: space-between; font-size: 11px; color: #888;">
                        <span>📦 ${tx.orderId}</span>
                        <span>📅 Estimasi: ${tx.arrivalEst}</span>
                    </div>
                    <div style="font-weight: bold; font-size: 13px; margin: 4px 0; color: var(--text-color);">${tx.items}</div>
                    <div style="font-size: 12px; color: #666; margin-bottom: 4px;">Total: Rp ${tx.total.toLocaleString('id-ID')} (${tx.payment})</div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 6px;">
                        <span style="color: #03AC03; font-size: 12px; font-weight: bold;">Status: ${tx.status}</span>
                        <span style="font-size: 11px; background: #e8f5e9; color: #2e7d32; padding: 3px 8px; border-radius: 4px; font-weight: bold;">🔍 Cek Peta</span>
                    </div>
                </div>
            `).join('');
        }

        function addNewProduct() {
            const name = document.getElementById('new-name').value.trim();
            const price = parseInt(document.getElementById('new-price').value);
            const stock = parseInt(document.getElementById('new-stock').value);
            const category = document.getElementById('new-category').value;
            const icon = document.getElementById('new-icon').value.trim() || "📦";

            if (!name || isNaN(price) || isNaN(stock)) {
                alert("Mohon lengkapi data produk dengan benar!");
                return;
            }

            const newId = Date.now();
            storesData[currentStore].push({ id: newId, name, price, stock, category, icon });
            
            document.getElementById('new-name').value = '';
            document.getElementById('new-price').value = '';
            document.getElementById('new-stock').value = '';
            document.getElementById('new-icon').value = '';

            alert("✅ Produk baru berhasil ditambahkan!");
            filterProducts();
        }

        function toggleTheme() {
            const isDark = document.getElementById('theme-toggle').checked;
            document.body.setAttribute('data-theme', isDark ? 'dark' : 'light');
        }

        filterProducts();
    </script>
</body>
</html>
'''

components.html(flashmart_html, height=880, scrolling=True)
