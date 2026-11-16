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
            overflow-x: hidden;
        }

        /* SPLASH SCREEN TEMA FLASHMART */
        #splash-screen {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(135deg, #03AC03 0%, #42B549 50%, #ff9800 100%);
            display: flex; flex-direction: column; justify-content: center; align-items: center;
            z-index: 9999; color: white;
            transition: opacity 0.7s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.7s;
        }
        .splash-brand {
            font-size: 42px; font-weight: 900; letter-spacing: 2px; color: #ffffff;
            text-shadow: 0 4px 10px rgba(0,0,0,0.2);
            opacity: 0; transform: translateY(15px);
            animation: fadeInText 0.8s ease 0.2s forwards;
        }
        .splash-tagline {
            font-size: 13px; color: #fff; margin-top: 8px; letter-spacing: 1.5px;
            font-weight: 600; background: rgba(0,0,0,0.15); padding: 4px 12px; border-radius: 20px;
            opacity: 0; transform: translateY(15px);
            animation: fadeInText 0.8s ease 0.5s forwards;
        }

        @keyframes fadeInText {
            to { opacity: 1; transform: translateY(0); }
        }

        /* ANIMASI TERBANG KE KERANJANG */
        .fly-item {
            position: fixed; z-index: 99999; font-size: 28px; pointer-events: none;
            transition: all 0.7s cubic-bezier(0.25, 1, 0.5, 1);
        }

        #success-modal, #tracking-detail-modal, #add-card-modal, #card-loading-modal {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.7); display: none; justify-content: center; align-items: center;
            z-index: 10000; backdrop-filter: blur(5px); overflow-y: auto; padding: 20px;
        }
        .receipt-card, .tracking-card, .modal-card {
            background: var(--card-bg); color: var(--text-color); width: 100%; max-width: 360px; padding: 20px;
            border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); position: relative; margin: auto;
            animation: modalPop 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        @keyframes modalPop {
            0% { transform: scale(0.8); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
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
            padding-bottom: 110px; box-shadow: 0 0 15px rgba(0,0,0,0.05); position: relative;
        }

        /* HEADER */
        .header-top {
            display: flex; justify-content: space-between; align-items: center; padding: 16px 15px 10px 15px;
        }
        .user-profile { display: flex; align-items: center; gap: 10px; }
        .user-avatar {
            width: 42px; height: 42px; background: #ddd; border-radius: 50%; overflow: hidden;
            border: 2px solid #03AC03; display: flex; align-items: center; justify-content: center; font-size: 20px;
        }
        .user-name { font-size: 15px; font-weight: bold; color: var(--text-color); }
        .user-sub { font-size: 11px; color: #777; }

        .search-container { padding: 0 15px 10px 15px; }
        .search-bar {
            background: var(--card-bg); border: 1px solid var(--border-color); padding: 10px 15px; border-radius: 25px; display: flex; align-items: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.04);
        }
        .search-bar input { border: none; outline: none; width: 100%; margin-left: 10px; font-size: 14px; background: transparent; color: var(--text-color); }
        
        .store-selector {
            margin: 0 15px 10px 15px; background: var(--card-bg); border: 1px solid var(--border-color);
            padding: 8px 12px; border-radius: 10px; display: flex; justify-content: space-between; align-items: center; font-size: 13px; font-weight: bold;
        }
        .store-selector select { border: none; background: transparent; color: #03AC03; font-weight: bold; outline: none; cursor: pointer; font-size: 13px; }

        /* KATEGORI SCROLL */
        .category-scroll { display: flex; gap: 10px; overflow-x: auto; padding: 5px 15px 12px 15px; scrollbar-width: none; }
        .category-scroll::-webkit-scrollbar { display: none; }
        .cat-chip {
            background: var(--card-bg); border: 1px solid var(--border-color); padding: 8px 16px;
            border-radius: 22px; font-size: 12px; cursor: pointer; white-space: nowrap; color: var(--text-color); font-weight: 600;
            transition: all 0.2s; box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        }
        .cat-chip.active { background: #03AC03; color: white; border-color: #03AC03; transform: scale(1.05); }

        /* BANNER PROMO */
        .promo-banner {
            margin: 0 15px 15px 15px; background: linear-gradient(135deg, #ff8800 0%, #ff6a00 100%); color: white;
            padding: 16px; border-radius: 16px; display: flex; justify-content: space-between; align-items: center;
            box-shadow: 0 6px 15px rgba(255,136,0,0.3);
        }
        .promo-text h4 { margin: 0 0 4px 0; font-size: 16px; font-weight: 800; }
        .promo-text p { margin: 0; font-size: 12px; opacity: 0.9; }
        .promo-icon { font-size: 38px; }

        /* GRID PRODUK */
        .section-title { padding: 0 15px 10px 15px; font-weight: bold; font-size: 15px; display: flex; justify-content: space-between; align-items: center; }
        .product-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; padding: 0 15px; }
        .product-card {
            background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 14px; padding: 12px;
            text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.03); transition: transform 0.2s, box-shadow 0.2s; position: relative;
        }
        .product-card:hover { transform: translateY(-3px); box-shadow: 0 6px 15px rgba(0,0,0,0.08); }
        
        .badge-sale {
            position: absolute; top: 10px; left: 10px; background: #FA591D; color: white;
            font-size: 9px; font-weight: bold; padding: 2px 6px; border-radius: 6px; text-transform: uppercase;
        }
        .product-icon-wrap { font-size: 44px; margin: 8px 0; }
        .product-title { font-size: 13px; font-weight: 700; height: 35px; overflow: hidden; margin-bottom: 2px; color: var(--text-color); }
        .product-rating { font-size: 11px; color: #888; margin-bottom: 6px; }
        .product-footer { display: flex; justify-content: space-between; align-items: center; margin-top: 6px; }
        .product-price { color: #FA591D; font-weight: bold; font-size: 14px; text-align: left; }
        
        .action-buttons { display: flex; gap: 5px; }
        .btn-mini-cart {
            width: 32px; height: 32px; background: #fff; border: 1px solid var(--border-color); border-radius: 50%;
            display: flex; align-items: center; justify-content: center; cursor: pointer; font-size: 14px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05); transition: transform 0.2s;
        }
        .btn-mini-cart:active { transform: scale(0.85); background: #eee; }
        
        .btn-mini-buy {
            background: #03AC03; color: white; border: none; padding: 6px 10px; border-radius: 8px;
            font-weight: bold; font-size: 11px; cursor: pointer; transition: transform 0.2s;
        }
        .btn-mini-buy:active { transform: scale(0.9); }

        /* WALLET / CARD UI STYLES (ALA VIDEO) */
        .virtual-card {
            width: 100%; height: 180px; border-radius: 16px; padding: 18px; color: white;
            box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2); margin-bottom: 12px; position: relative; overflow: hidden;
            transition: transform 0.3s;
        }
        .virtual-card:hover { transform: scale(1.02); }
        .card-chip { width: 36px; height: 26px; background: linear-gradient(135deg, #d4af37, #f3e5ab); border-radius: 4px; }
        .card-number { font-family: monospace; font-size: 15px; letter-spacing: 2px; font-weight: bold; }
        .card-footer { display: flex; justify-content: space-between; align-items: flex-end; font-size: 12px; }

        /* BOTTOM NAVIGATION */
        .bottom-nav {
            position: fixed; bottom: 12px; left: 50%; transform: translateX(-50%);
            width: 92%; max-width: 440px; background: var(--nav-bg); 
            display: flex; justify-content: space-around; align-items: center;
            padding: 8px 6px; border-radius: 35px; border: 1px solid var(--border-color);
            z-index: 100; box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        .nav-item {
            position: relative; display: flex; flex-direction: column; align-items: center; justify-content: center;
            width: 60px; height: 48px; background: transparent; border: none; outline: none; cursor: pointer;
            z-index: 2; transition: transform 0.2s ease;
        }
        .nav-icon { font-size: 18px; transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), color 0.3s; color: #777; }
        .nav-label { font-size: 10px; font-weight: 600; color: #777; margin-top: 2px; transition: opacity 0.3s, transform 0.3s; opacity: 1; }
        
        .nav-item.active .nav-icon { color: #ffffff; transform: translateY(-14px) scale(1.1); }
        .nav-item.active .nav-label { opacity: 0; transform: translateY(10px); pointer-events: none; }
        .nav-pill-bg {
            position: absolute; width: 44px; height: 44px; background: #03AC03;
            border-radius: 50%; top: 2px; left: calc(50% - 22px); z-index: 1;
            transition: transform 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55), left 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            box-shadow: 0 6px 15px rgba(3, 172, 3, 0.4);
        }

        /* VIEW SECTIONS */
        .view-section { 
            display: none; padding: 15px; opacity: 0; transform: translateY(12px);
            transition: opacity 0.35s ease, transform 0.35s ease;
        }
        .view-section.active { display: block; opacity: 1; transform: translateY(0); }
        
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
        .btn-del-item { background: none; border: none; color: #999; font-size: 16px; cursor: pointer; padding: 4px; }
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

    <!-- SPLASH SCREEN TEMA FLASHMART -->
    <div id="splash-screen">
        <div class="splash-brand">FlashMart</div>
        <div class="splash-tagline">⚡ All your needs in one place</div>
    </div>

    <!-- MODAL TAMBAH KARTU / E-WALLET (ALA VIDEO) -->
    <div id="add-card-modal">
        <div class="modal-card">
            <h3 style="margin-top:0; color: #03AC03;">💳 Tambah Kartu / E-Wallet</h3>
            <label style="font-size:12px; font-weight:bold;">Jenis / Nama Layanan:</label>
            <select id="card-type-input" class="admin-input" style="margin-top:5px;">
                <option value="Visa Debit">Visa Debit / Credit</option>
                <option value="Mastercard">Mastercard</option>
                <option value="DANA E-Wallet">DANA</option>
                <option value="GoPay">GoPay</option>
                <option value="OVO Cash">OVO</option>
            </select>

            <label style="font-size:12px; font-weight:bold;">Nomor Kartu / No. HP E-Wallet:</label>
            <input type="text" id="card-num-input" placeholder="4242 •••• •••• 4242" class="admin-input" style="margin-top:5px;">

            <label style="font-size:12px; font-weight:bold;">Nama Pemilik:</label>
            <input type="text" id="card-holder-input" placeholder="Jenny Leow" value="Jenny Leow" class="admin-input" style="margin-top:5px;">

            <label style="font-size:12px; font-weight:bold;">Warna Kartu:</label>
            <div style="display: flex; gap: 10px; margin-bottom: 10px; margin-top: 5px;">
                <div onclick="setCardColor('linear-gradient(135deg, #1e3c72, #2a5298)')" style="width:30px; height:30px; border-radius:50%; background:linear-gradient(135deg, #1e3c72, #2a5298); cursor:pointer; border:2px solid #fff;"></div>
                <div onclick="setCardColor('linear-gradient(135deg, #0f2027, #203a43, #2c5364)')" style="width:30px; height:30px; border-radius:50%; background:linear-gradient(135deg, #0f2027, #203a43, #2c5364); cursor:pointer;"></div>
                <div onclick="setCardColor('linear-gradient(135deg, #03AC03, #134e13)')" style="width:30px; height:30px; border-radius:50%; background:linear-gradient(135deg, #03AC03, #134e13); cursor:pointer;"></div>
                <div onclick="setCardColor('linear-gradient(135deg, #ff8c00, #e65100)')" style="width:30px; height:30px; border-radius:50%; background:linear-gradient(135deg, #ff8c00, #e65100); cursor:pointer;"></div>
            </div>

            <div style="display: flex; gap: 8px; margin-top: 15px;">
                <button class="ripple-btn" onclick="closeAddCardModal()" style="background: #ccc; color: #333; border: none; flex:1; padding:10px; border-radius:8px; font-weight:bold; cursor:pointer;">Batal</button>
                <button class="ripple-btn" onclick="submitNewCard()" style="background: #03AC03; color: white; border: none; flex:1; padding:10px; border-radius:8px; font-weight:bold; cursor:pointer;">Simpan Kartu</button>
            </div>
        </div>
    </div>

    <!-- MODAL LOADING ANIMASI KARTU (ALA VIDEO: Verifying -> Connect -> Secure -> Success) -->
    <div id="card-loading-modal">
        <div class="modal-card" style="text-align: center; padding: 25px;">
            <div style="font-size: 38px; margin-bottom: 10px;">🔒</div>
            <h3 style="margin: 0 0 5px 0;">Menambahkan Kartu</h3>
            <p style="font-size: 12px; color: #666; margin-bottom: 15px;">Mohon tunggu sebentar...</p>
            <div id="loading-steps" style="font-size: 13px; font-weight: bold; color: #03AC03; line-height: 1.8;">
                ✓ Verifying card details...<br>
                <span id="step-connect" style="opacity: 0.4;">⚡ Connecting to bank server...</span><br>
                <span id="step-secure" style="opacity: 0.4;">🛡️ Securing encryption token...</span>
            </div>
        </div>
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

    <!-- MODAL DETAIL / PELACAKAN -->
    <div id="tracking-detail-modal">
        <div class="tracking-card">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 10px; margin-bottom: 12px;">
                <h3 id="modal-title-header" style="margin: 0; font-size: 16px; color: #03AC03;">📍 Detail Transaksi</h3>
                <button onclick="closeTrackingModal()" style="background: none; border: none; font-size: 18px; cursor: pointer; color: #777;">✕</button>
            </div>
            <div id="tracking-detail-content" style="font-size: 13px; line-height: 1.6;"></div>
            <button class="ripple-btn" onclick="closeTrackingModal()" style="background: #03AC03; color: white; border: none; width: 100%; padding: 10px; border-radius: 8px; font-weight: bold; margin-top: 15px; cursor: pointer; font-size: 13px;">Tutup</button>
        </div>
    </div>

    <div class="app-container">
        
        <!-- BERANDA -->
        <div id="view-home" class="view-section active" style="padding: 0 0 15px 0;">
            <div class="header-top">
                <div class="user-profile">
                    <div class="user-avatar">👤</div>
                    <div>
                        <div class="user-name">Jenny Leow</div>
                        <div class="user-sub">FlashMart VIP Member</div>
                    </div>
                </div>
                <div onclick="switchTab('cart', 1, document.querySelectorAll('.nav-item')[1])" style="font-size: 22px; cursor: pointer; position: relative;">🛒</div>
            </div>

            <div class="search-container">
                <div class="search-bar">
                    <span>🔍</span>
                    <input type="text" id="search-box" placeholder="Cari 1.200+ barang real di pasaran..." oninput="filterProducts()">
                </div>
            </div>

            <div class="store-selector">
                <span>🏪 Pilih Toko:</span>
                <select id="store-select" onchange="changeStore()">
                    <option value="Pusat">FlashMart Pusat (1.200+ Barang)</option>
                    <option value="Express">FlashMart Express (Kilat)</option>
                    <option value="Grosir">FlashMart Grosir (Partai Besar)</option>
                </select>
            </div>

            <div class="promo-banner">
                <div class="promo-text">
                    <h4>Get 30% OFF</h4>
                    <p>On your first order with code <b>FLASHMARTINA</b></p>
                </div>
                <div class="promo-icon">🍔</div>
            </div>

            <!-- KATEGORI -->
            <div class="category-scroll" id="category-container">
                <div class="cat-chip active" onclick="selectCategory('Semua', this)">🔥 All</div>
                <div class="cat-chip" onclick="selectCategory('Burger', this)">🍔 Burger</div>
                <div class="cat-chip" onclick="selectCategory('Pizza', this)">🍕 Pizza</div>
                <div class="cat-chip" onclick="selectCategory('Sushi', this)">🍣 Sushi</div>
                <div class="cat-chip" onclick="selectCategory('Minuman', this)">🧃 Minuman</div>
                <div class="cat-chip" onclick="selectCategory('Sembako', this)">🍚 Sembako</div>
                <div class="cat-chip" onclick="selectCategory('Camilan', this)">🍪 Camilan</div>
                <div class="cat-chip" onclick="selectCategory('Skincare', this)">✨ Skincare</div>
                <div class="cat-chip" onclick="selectCategory('Elektronik', this)">📱 Elektronik</div>
            </div>

            <div class="section-title">
                <span id="store-title-label">Popular Now (1.200+ Items)</span>
                <span style="font-size: 12px; color: #03AC03; font-weight: bold;" id="total-count-badge">Menampilkan Semua</span>
            </div>
            
            <div class="product-grid" id="product-list"></div>
        </div>

        <!-- KERANJANG & CHECKOUT -->
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
                        <option value="Card">💳 Kartu / E-Wallet Tersimpan</option>
                        <option value="QRIS">QRIS (Scan & Cashback Instant)</option>
                        <option value="Transfer Bank">Transfer Bank (BCA / Mandiri / BRI)</option>
                        <option value="COD">Bayar di Tempat (COD)</option>
                    </select>
                </div>

                <!-- PILIHAN KARTU TERHUBUNG -->
                <div id="saved-card-payment-box" style="margin-bottom: 12px; display: none;">
                    <label style="font-size: 13px; font-weight: bold;">Pilih Kartu / E-Wallet Pembayaran:</label>
                    <select id="selected-saved-card" class="admin-input" style="margin-top: 5px;"></select>
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

        <!-- RIWAYAT & PESANAN -->
        <div id="view-history" class="view-section">
            <h3>📜 Riwayat Pesanan & Transaksi</h3>
            <p style="font-size: 12px; color: #666; margin-bottom: 12px;">👉 Tekan kartu pesanan untuk melihat detail lengkap transaksi atau status kurir pengiriman!</p>
            <div id="history-container">
                <p style="color: #777; text-align: center; margin-top: 30px;">Belum ada riwayat transaksi.</p>
            </div>
        </div>

        <!-- AKUN & PENGATURAN KARTU / E-WALLET -->
        <div id="view-account" class="view-section">
            <h3>👤 Akun & Dompet Kartu</h3>
            <div class="profile-card">
                <div style="font-size: 18px; font-weight: bold;">⚡ Jenny Leow (Gold VIP)</div>
                <div style="font-size: 13px; opacity: 0.9; margin-top: 4px;">No: 08123456789 • 1.200+ Barang Ready</div>
                <div style="background: rgba(255,255,255,0.25); padding: 8px 12px; border-radius: 10px; margin-top: 12px; display: flex; justify-content: space-between; font-weight: bold;">
                    <span>⭐ Saldo Poin A-Voucher</span>
                    <span id="user-points">150 Poin</span>
                </div>
            </div>

            <!-- SECTION DOMPET KARTU & E-WALLET -->
            <div style="background: var(--card-bg); border: 1px solid var(--border-color); padding: 15px; border-radius: 12px; margin-bottom: 15px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                    <h4 style="margin: 0; color: #03AC03;">💳 Kartu & E-Wallet Terhubung</h4>
                    <button class="ripple-btn" onclick="openAddCardModal()" style="background: #03AC03; color: white; border: none; padding: 6px 12px; border-radius: 8px; font-size: 12px; font-weight: bold; cursor: pointer;">+ Tambah Kartu</button>
                </div>
                <div id="saved-cards-container"></div>
            </div>

            <div style="background: var(--card-bg); border: 1px solid var(--border-color); padding: 15px; border-radius: 12px; margin-bottom: 15px;">
                <h4 style="margin-top: 0; color: #03AC03;">📦 Tambah Produk Baru</h4>
                <input type="text" id="new-name" placeholder="Nama Produk" class="admin-input">
                <input type="number" id="new-price" placeholder="Harga (Rp)" class="admin-input">
                <input type="number" id="new-stock" placeholder="Jumlah Stok" class="admin-input">
                <select id="new-category" class="admin-input">
                    <option value="Burger">Burger</option>
                    <option value="Pizza">Pizza</option>
                    <option value="Sushi">Sushi</option>
                    <option value="Minuman">Minuman</option>
                    <option value="Sembako">Sembako</option>
                    <option value="Camilan">Camilan</option>
                </select>
                <input type="text" id="new-icon" placeholder="Emoji Ikon (Contoh: 🍔)" class="admin-input">
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
            <div class="nav-pill-bg" id="nav-pill"></div>
            <button class="nav-item active" onclick="switchTab('home', 0, this)">
                <div class="nav-icon" id="icon-home">🏠</div>
                <div class="nav-label">Beranda</div>
            </button>
            <button class="nav-item" onclick="switchTab('cart', 1, this)">
                <div class="nav-icon" id="icon-cart">🛒</div>
                <div class="nav-label">Keranjang</div>
            </button>
            <button class="nav-item" onclick="switchTab('pulsa', 2, this)">
                <div class="nav-icon">📱</div>
                <div class="nav-label">Digital</div>
            </button>
            <button class="nav-item" onclick="switchTab('history', 3, this)">
                <div class="nav-icon">📜</div>
                <div class="nav-label">Riwayat</div>
            </button>
            <button class="nav-item" onclick="switchTab('account', 4, this)">
                <div class="nav-icon">👤</div>
                <div class="nav-label">Akun</div>
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
            }, 1400);
            movePill(0);
            renderSavedCards();
        });

        // DATA KARTU & E-WALLET TERHUBUNG
        let savedCards = [
            { id: 1, type: "Visa Debit", number: "4242 •••• •••• 8821", holder: "Jenny Leow", balance: "Rp 4.250.000", color: "linear-gradient(135deg, #1e3c72, #2a5298)" },
            { id: 2, type: "DANA E-Wallet", number: "0812-3456-7890", holder: "Jenny Leow", balance: "Rp 1.120.000", color: "linear-gradient(135deg, #0080ff, #004080)" }
        ];

        let selectedCardColor = "linear-gradient(135deg, #1e3c72, #2a5298)";

        function setCardColor(color) {
            selectedCardColor = color;
        }

        function openAddCardModal() {
            document.getElementById('add-card-modal').style.display = 'flex';
        }

        function closeAddCardModal() {
            document.getElementById('add-card-modal').style.display = 'none';
        }

        function submitNewCard() {
            const type = document.getElementById('card-type-input').value;
            const number = document.getElementById('card-num-input').value.trim() || "4242 •••• •••• 9999";
            const holder = document.getElementById('card-holder-input').value.trim() || "Jenny Leow";

            closeAddCardModal();
            
            // Tampilkan animasi loading verifikasi kartu ala video
            const loadingModal = document.getElementById('card-loading-modal');
            loadingModal.style.display = 'flex';

            setTimeout(() => {
                document.getElementById('step-connect').style.opacity = '1';
            }, 700);

            setTimeout(() => {
                document.getElementById('step-secure').style.opacity = '1';
            }, 1400);

            setTimeout(() => {
                loadingModal.style.display = 'none';
                savedCards.push({
                    id: Date.now(),
                    type: type,
                    number: number,
                    holder: holder,
                    balance: "Rp 2.500.000",
                    color: selectedCardColor
                });
                renderSavedCards();
                alert("🎉 Kartu / E-Wallet Berhasil Ditambahkan & Terverifikasi!");
            }, 2100);
        }

        function renderSavedCards() {
            const container = document.getElementById('saved-cards-container');
            const checkoutSelect = document.getElementById('selected-saved-card');

            if (savedCards.length === 0) {
                container.innerHTML = '<p style="font-size:12px; color:#777; text-align:center;">Belum ada kartu atau e-wallet yang ditambahkan.</p>';
                checkoutSelect.innerHTML = '<option value="">-- Belum ada kartu --</option>';
                return;
            }

            container.innerHTML = savedCards.map(c => `
                <div class="virtual-card" style="background: ${c.color};">
                    <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                        <div>
                            <div style="font-size:11px; opacity:0.8;">${c.type}</div>
                            <div style="font-size:15px; font-weight:bold;">${c.balance}</div>
                        </div>
                        <div class="card-chip"></div>
                    </div>
                    <div class="card-number">${c.number}</div>
                    <div class="card-footer">
                        <div>
                            <div style="font-size:9px; opacity:0.7;">CARD HOLDER</div>
                            <div style="font-size:12px; font-weight:bold;">${c.holder}</div>
                        </div>
                        <div style="font-size:16px; font-weight:bold; font-style:italic;">VISA / MC</div>
                    </div>
                </div>
            `).join('');

            checkoutSelect.innerHTML = savedCards.map(c => `
                <option value="${c.type} (${c.number})">${c.type} - ${c.number} (${c.balance})</option>
            `).join('');
        }

        // GENERATE 1.200+ BARANG DENGAN NAMA PRODUK ASLI DI PASARAN (TANPA SPESIAL EDITION BERULANG)
        function generateMassiveStore() {
            const rawCatalog = {
                "Burger": [
                    { name: "Beef Burger Deluxe", price: 35000, icon: "🍔" },
                    { name: "Cheese Burger Special", price: 40000, icon: "🍔" },
                    { name: "Double Crispy Chicken Burger", price: 45000, icon: "🍔" },
                    { name: "Spicy Volcano Burger", price: 48000, icon: "🍔" },
                    { name: "Egg Mayo Burger", price: 30000, icon: "🍔" },
                    { name: "Blackpepper Beef Burger", price: 52000, icon: "🍔" },
                    { name: "Fish Fillet Burger", price: 38000, icon: "🍔" },
                    { name: "Mushroom Melt Burger", price: 46000, icon: "🍔" }
                ],
                "Pizza": [
                    { name: "Pepperoni Supreme Pizza", price: 115000, icon: "🍕" },
                    { name: "Meat Lovers Pizza 12 inch", price: 130000, icon: "🍕" },
                    { name: "Cheese Mania Pizza", price: 95000, icon: "🍕" },
                    { name: "Tuna Melt Pizza", price: 110000, icon: "🍕" },
                    { name: "Hawaiian Chicken Pizza", price: 105000, icon: "🍕" },
                    { name: "BBQ Smoke Beef Pizza", price: 125000, icon: "🍕" },
                    { name: "Mushroom Truffle Pizza", price: 140000, icon: "🍕" }
                ],
                "Sushi": [
                    { name: "Salmon Mentai Sushi Roll", price: 65000, icon: "🍣" },
                    { name: "Tuna Salad Roll", price: 55000, icon: "🍣" },
                    { name: "Ebi Fry Maki Sushi", price: 58000, icon: "🍣" },
                    { name: "Dragon Roll Premium", price: 85000, icon: "🍣" },
                    { name: "California Roll (8 pcs)", price: 50000, icon: "🍣" },
                    { name: "Spicy Tuna Gunkan", price: 45000, icon: "🍣" },
                    { name: "Tamago Nigiri Set", price: 38000, icon: "🍣" }
                ],
                "Minuman": [
                    { name: "Aqua Botol Mineral 600ml", price: 4000, icon: "🧃" },
                    { name: "Teh Botol Sosro 450ml", price: 5500, icon: "🧃" },
                    { name: "Ultra Milk Cokelat 250ml", price: 6500, icon: "🧃" },
                    { name: "Kopi Kenangan Mantan", price: 22000, icon: "🧃" },
                    { name: "Green Tea Ichitan 310ml", price: 7000, icon: "🧃" },
                    { name: "Coca Cola / Sprite 390ml", price: 8000, icon: "🧃" },
                    { name: "Pocari Sweat Ion Supply", price: 8500, icon: "🧃" },
                    { name: "Susu Bear Brand Kaleng", price: 10500, icon: "🧃" },
                    { name: "Good Day Cappuccino Botol", price: 7500, icon: "🧃" }
                ],
                "Sembako": [
                    { name: "Beras Sentra Ramos 5kg", price: 68000, icon: "🍚" },
                    { name: "Minyak Goreng Bimoli 2L", price: 39000, icon: "🍳" },
                    { name: "Gula Pasir Gulaku 1kg", price: 17500, icon: "🍚" },
                    { name: "Telur Ayam Negeri 1kg", price: 28000, icon: "🍚" },
                    { name: "Tepung Terigu Segitiga Biru", price: 14000, icon: "🍚" },
                    { name: "Kecap Manis Bango 550ml", price: 26000, icon: "🍚" },
                    { name: "Saus Sambal Indofood 335ml", price: 15000, icon: "🍚" },
                    { name: "Mie Instan Indomie Goreng (1 Dus)", price: 115000, icon: "🍚" },
                    { name: "Garam Dapur Refina 500g", price: 5000, icon: "🍚" }
                ],
                "Camilan": [
                    { name: "Chitato Snack Sapi Panggang", price: 11000, icon: "🍪" },
                    { name: "Lays Rumput Laut Snack", price: 11500, icon: "🍪" },
                    { name: "Biskuit Roma Kelapa", price: 9500, icon: "🍪" },
                    { name: "Oreo Cokelat Vanilla 133g", price: 10000, icon: "🍪" },
                    { name: "SilverQueen Chocolate 62g", price: 18500, icon: "🍪" },
                    { name: "Qtela Keripik Singkong Balado", price: 9000, icon: "🍪" },
                    { name: "Tango Wafer Cokelat Besar", price: 12000, icon: "🍪" },
                    { name: "Nabati Richeese Ahh", price: 8000, icon: "🍪" }
                ],
                "Skincare": [
                    { name: "Wardah Facial Wash Aloe 100ml", price: 24000, icon: "✨" },
                    { name: "Skintific 5X Ceramide Moisturizer", price: 135000, icon: "✨" },
                    { name: "Emina Bright Stuff Serum", price: 49000, icon: "✨" },
                    { name: "Azarine Sunscreen SPF 45", price: 65000, icon: "✨" },
                    { name: "Hada Labo Gokujyun Lotion", price: 42000, icon: "✨" },
                    { name: "Garnier Bright Complete Serum", price: 78000, icon: "✨" }
                ],
                "Elektronik": [
                    { name: "Kabel Data Type-C Fast Charge", price: 35000, icon: "📱" },
                    { name: "Powerbank Vivan 10000mAh", price: 185000, icon: "📱" },
                    { name: "Headset Bluetooth TWS Pro", price: 145000, icon: "📱" },
                    { name: "Adaptor Charger 20W Fast", price: 95000, icon: "📱" },
                    { name: "Baterai ABC Alkaline AA (Isi 2)", price: 15000, icon: "📱" },
                    { name: "Flashdisk SanDisk 32GB USB 3.0", price: 75000, icon: "📱" }
                ]
            };

            let listPusat = [];
            let idCounter = 1000;
            const categories = Object.keys(rawCatalog);

            categories.forEach(cat => {
                rawCatalog[cat].forEach(item => {
                    listPusat.push({
                        id: idCounter++,
                        name: item.name,
                        price: item.price,
                        stock: 45,
                        category: cat,
                        icon: item.icon,
                        rating: (4.7 + (Math.random() * 0.2)).toFixed(1)
                    });
                });
            });

            // Daftar variasi nama produk natural harian di pasaran
            const productNamesBank = {
                "Burger": ["Beef Burger Patty", "Crispy Chicken Burger", "Double Cheese Burger", "Jumbo Beef Burger", "Spicy Chicken Burger", "Teriyaki Burger", "BBQ Burger"],
                "Pizza": ["Pepperoni Pizza Regular", "Meat Lovers Pizza", "Cheese Overflow Pizza", "Tuna Melt Pizza", "Supreme Chicken Pizza", "BBQ Beef Pizza"],
                "Sushi": ["Salmon Roll Sushi", "Tuna Maki Sushi", "Ebi Fry Roll", "Dragon Sushi Roll", "California Roll Set", "Spicy Salmon Gunkan"],
                "Minuman": ["Teh Pucuk Harum 350ml", "Aqua Botol 1.5L", "Sprite Botol 390ml", "Fanta Merah 390ml", "Cimory Yogurt Drink", "NutriSari Jeruk Peras", "Floridina Orange 360ml", "Teh Kotak Sosro 200ml"],
                "Sembako": ["Beras Ramos Super 10kg", "Minyak Goreng Sania 2L", "Gula Pasir Rose Brand", "Telur Ayam Omega 1kg", "Tepung Beras Rose Brand", "Santan Kara Instan 65ml", "Kecap Manis ABC 525ml", "Saus Tomat Indofood"],
                "Camilan": ["Chitato Rasa Sapi", "Tango Wafer Vanila", "Roma Malkist Crackers", "Beng Beng Chocolate", "Hello Panda Biscuit", "Good Time Cookies", "Garuda Pilus", "Kacang Dua Kelinci"],
                "Skincare": ["Wardah UV Shield Sunscreen", "Emina Moisturizing Cream", "Skintific Toner 100ml", "Garnier Micellar Water", "Implora Lip Matte", "Madame Gie Cushion"],
                "Elektronik": ["Kabel Micro USB Fast", "Charger HP Universal", "Earphone Wired Jack 3.5mm", "Stand Holder HP Meja", "Memory Card 16GB Class 10", "Kabel AUX Audio"]
            };

            for (let i = 1; i <= 1200; i++) {
                let cat = categories[i % categories.length];
                let namePool = productNamesBank[cat];
                let baseName = namePool[i % namePool.length];
                let baseObj = rawCatalog[cat][0];
                let priceRand = baseObj.price + ((i * 41) % 75000);

                listPusat.push({
                    id: idCounter++,
                    name: baseName + " V-" + (i % 99 + 1),
                    price: priceRand,
                    stock: 20 + (i % 35),
                    category: cat,
                    icon: baseObj.icon,
                    rating: (4.5 + ((i % 5) * 0.1)).toFixed(1)
                });
            }

            return {
                "Pusat": listPusat,
                "Express": listPusat.slice(0, 450).map(item => ({ ...item, price: item.price + 2000 })),
                "Grosir": listPusat.slice(0, 350).map(item => ({ ...item, price: Math.round(item.price * 0.9) }))
            };
        }

        const storesData = generateMassiveStore();
        let currentStore = "Pusat";
        let cart = {};
        let points = 150;
        let history = [];
        let discountActive = false;
        let activeCategory = 'Semua';
        let currentDigitalType = 'Pulsa';

        function movePill(index) {
            const pill = document.getElementById('nav-pill');
            const items = document.querySelectorAll('.nav-item');
            if(items[index]) {
                const itemWidth = items[index].offsetWidth;
                const itemLeft = items[index].offsetLeft;
                pill.style.left = (itemLeft + (itemWidth / 2) - 22) + 'px';
            }
        }

        // ANIMASI TERBANG KE KERANJANG
        function flyToCartAnimation(event) {
            const cartIcon = document.getElementById('icon-cart');
            if (!cartIcon) return;

            const targetRect = cartIcon.getBoundingClientRect();
            const flyer = document.createElement('div');
            flyer.className = 'fly-item';
            flyer.innerText = '🛒';
            flyer.style.left = event.clientX + 'px';
            flyer.style.top = event.clientY + 'px';
            document.body.appendChild(flyer);

            setTimeout(() => {
                flyer.style.left = (targetRect.left + 10) + 'px';
                flyer.style.top = (targetRect.top + 10) + 'px';
                flyer.style.transform = 'scale(0.3)';
                flyer.style.opacity = '0';
            }, 20);

            setTimeout(() => {
                flyer.remove();
            }, 750);
        }

        function openDigital(type) {
            currentDigitalType = type;
            switchTab('pulsa', 2, document.querySelectorAll('.nav-item')[2]);
            
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
                `;
            } else if (type === 'E-Money') {
                titleLabel.innerText = "🎮 Top Up E-Wallet & Games";
                targetLabel.innerText = "2. Masukkan No. Akun / User ID Game:";
                targetInput.placeholder = "Contoh: 081234567890 / ID Game";
                providerGroup.style.display = 'block';
                labelProvider.innerText = "1. Pilih E-Wallet / Game:";
                document.getElementById('digital-provider').innerHTML = `
                    <option value="GoPay">GoPay Customer</option>
                    <option value="DANA">DANA Dompet Digital</option>
                    <option value="Mobile Legends">Mobile Legends (Moonton)</option>
                    <option value="Free Fire">Free Fire (Garena)</option>
                `;
                nominalSelect.innerHTML = `
                    <option value="20000">Top Up Saldo 20.000 (Rp 20.000)</option>
                    <option value="50000">Top Up Saldo 50.000 (Rp 50.000)</option>
                    <option value="105000">Top Up 100.000 (Rp 105.000)</option>
                `;
            }
        }

        function toggleQR() {
            const method = document.getElementById('payment-method').value;
            document.getElementById('qris-display').style.display = (method === 'QRIS') ? 'block' : 'none';
            document.getElementById('cash-payment-box').style.display = (method === 'Tunai') ? 'block' : 'none';
            document.getElementById('saved-card-payment-box').style.display = (method === 'Card') ? 'block' : 'none';
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
            document.getElementById('store-title-label').innerText = "Popular Now (" + storesData[currentStore].length + "+ Items)";
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
            document.getElementById('total-count-badge').innerText = listToRender.length + " Barang";
            
            if (listToRender.length === 0) {
                list.innerHTML = '<p style="grid-column: span 2; text-align: center; color: #777;">Tidak ada barang yang cocok.</p>';
                return;
            }

            const displaySlice = listToRender.slice(0, 100);

            list.innerHTML = displaySlice.map(p => `
                <div class="product-card">
                    <div class="badge-sale">SALE</div>
                    <div class="product-icon-wrap">` + p.icon + `</div>
                    <div class="product-title">` + p.name + `</div>
                    <div class="product-rating">⭐ ` + p.rating + ` (Stok: ` + p.stock + `)</div>
                    <div class="product-footer">
                        <div class="product-price">Rp ` + p.price.toLocaleString('id-ID') + `</div>
                        <div class="action-buttons">
                            <button class="btn-mini-cart" title="Tambah ke Keranjang" onclick="addToCart(event, ` + p.id + `)">+</button>
                            <button class="btn-mini-buy ripple-btn" onclick="buyNowDirect(` + p.id + `)">Beli</button>
                        </div>
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

        function switchTab(tabName, tabIndex, element) {
            document.querySelectorAll('.view-section').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            document.getElementById('view-' + tabName).classList.add('active');
            if (element) element.classList.add('active');
            movePill(tabIndex);

            if (tabName === 'cart') renderCart();
            if (tabName === 'history') renderHistory();
            if (tabName === 'account') renderSavedCards();
        }

        function addToCart(event, id) {
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
            flyToCartAnimation(event);
        }

        function buyNowDirect(id) {
            const prod = storesData[currentStore].find(p => p.id === id);
            if (prod.stock <= 0) {
                alert("Stok barang habis!");
                return;
            }
            
            cart = {};
            prod.stock -= 1;
            cart[id] = { ...prod, qty: 1, store: currentStore, selected: true };

            filterProducts();
            switchTab('cart', 1, document.querySelectorAll('.nav-item')[1]);
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
            let method = document.getElementById('payment-method').value;
            
            if (method === 'Card') {
                const selectedCardName = document.getElementById('selected-saved-card').value;
                method = "Kartu: " + selectedCardName;
            }

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
                delete cart[id];
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

            let statusInfo = "Selesai / Lunas ✅";
            let arrivalEst = "Langsung Tersedia (Cashier/Digital)";
            let courier = "-";
            let location = "FlashMart Store (Offline Counter)";

            if (method.includes('COD')) {
                let arrivalDate = new Date(now);
                arrivalDate.setDate(now.getDate() + 2);
                arrivalEst = arrivalDate.toLocaleDateString('id-ID', { day: 'numeric', month: 'short', year: 'numeric' });
                statusInfo = "Dalam Perjalanan Kurir 🚚";
                courier = "FlashExpress (Kurir VIP COD)";
                location = "Sorting Center Gudang Utama (Jakarta / Hub Terdekat)";
            }

            history.unshift({
                orderId: "FM-" + Math.floor(100000 + Math.random() * 900000),
                date: dateStr + " | " + timeStr,
                arrivalEst: arrivalEst,
                total: grandTotal,
                payment: method,
                items: itemsSummaryArray.join(', '),
                earned: earnedPoints,
                status: statusInfo,
                courier: courier,
                location: location,
                isCod: method.includes('COD')
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
                location: "Server Pusat Operator (Online)",
                isCod: false
            });

            document.getElementById('digital-target').value = '';
            document.getElementById('success-modal').style.display = 'flex';
        }

        function closeModal() {
            document.getElementById('success-modal').style.display = 'none';
            switchTab('history', 3, document.querySelectorAll('.nav-item')[3]);
        }

        function closeTrackingModal() {
            document.getElementById('tracking-detail-modal').style.display = 'none';
        }

        function showDetailModal(index) {
            const tx = history[index];
            const detailModal = document.getElementById('tracking-detail-modal');
            const content = document.getElementById('tracking-detail-content');
            const titleHeader = document.getElementById('modal-title-header');

            if (tx.isCod) {
                titleHeader.innerText = "📍 Pelacakan Kurir & Pengiriman COD";
                content.innerHTML = `
                    <div style="background: var(--bg-color); padding: 10px; border-radius: 8px; margin-bottom: 10px;">
                        <strong>No. Pesanan / Resi:</strong> ${tx.orderId}<br>
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
                        📍 Posisi Terkini Kurir:<br>
                        ${tx.location}
                    </div>
                    <div style="border: 2px dashed #03AC03; border-radius: 8px; overflow: hidden; background: #fff; text-align: center;">
                        <iframe width="100%" height="160" style="border:0;" loading="lazy" allowfullscreen src="https://maps.google.com/maps?q=-6.2088,106.8456&z=14&output=embed"></iframe>
                        <div style="font-size: 11px; padding: 6px; color: #555; background: #f1f8e9;">🗺️ Simulasi Live Tracking Kurir FlashMart</div>
                    </div>
                `;
            } else {
                titleHeader.innerText = "🧾 Detail Transaksi & Pembayaran";
                content.innerHTML = `
                    <div style="background: var(--bg-color); padding: 10px; border-radius: 8px; margin-bottom: 10px;">
                        <strong>ID Transaksi:</strong> ${tx.orderId}<br>
                        <strong>Waktu:</strong> ${tx.date}<br>
                        <strong>Metode Pembayaran:</strong> <span style="color: #FA591D; font-weight: bold;">${tx.payment}</span><br>
                        <strong>Status:</strong> <span style="color: #03AC03; font-weight: bold;">${tx.status}</span>
                    </div>
                    <div style="margin-bottom: 10px;">
                        <strong>Rincian Item / Layanan:</strong><br>
                        <span style="color: #555;">${tx.items}</span>
                    </div>
                    <div style="background: #fff3e0; color: #e65100; padding: 10px; border-radius: 8px; font-weight: bold; font-size: 12px;">
                        💡 Keterangan:<br>
                        Transaksi diselesaikan secara sukses. Terima kasih telah berbelanja di FlashMart!
                    </div>
                `;
            }
            detailModal.style.display = 'flex';
        }

        function renderHistory() {
            const container = document.getElementById('history-container');
            if (history.length === 0) {
                container.innerHTML = '<p style="color: #777; text-align: center; margin-top: 30px;">Belum ada riwayat transaksi.</p>';
                return;
            }

            container.innerHTML = history.map((tx, idx) => `
                <div class="tracker-box" onclick="showDetailModal(${idx})">
                    <div style="display: flex; justify-content: space-between; font-size: 11px; color: #888;">
                        <span>📦 ${tx.orderId}</span>
                        <span>💳 ${tx.payment}</span>
                    </div>
                    <div style="font-weight: bold; font-size: 13px; margin: 4px 0; color: var(--text-color);">${tx.items}</div>
                    <div style="font-size: 12px; color: #666; margin-bottom: 4px;">Total: Rp ${tx.total.toLocaleString('id-ID')}</div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 6px;">
                        <span style="color: #03AC03; font-size: 12px; font-weight: bold;">Status: ${tx.status}</span>
                        <span style="font-size: 11px; background: ${tx.isCod ? '#e8f5e9' : '#fff3e0'}; color: ${tx.isCod ? '#2e7d32' : '#e65100'}; padding: 3px 8px; border-radius: 4px; font-weight: bold;">${tx.isCod ? '🔍 Cek Peta' : '📄 Lihat Struk'}</span>
                    </div>
                </div>
            `).join('');
        }

        function addNewProduct() {
            const name = document.getElementById('new-name').value.trim();
            const price = parseInt(document.getElementById('new-price').value);
            const stock = parseInt(document.getElementById('new-stock').value);
            const category = document.getElementById('new-category').value;
            const icon = document.getElementById('new-icon').value.trim() || "🍔";

            if (!name || isNaN(price) || isNaN(stock)) {
                alert("Mohon lengkapi data produk dengan benar!");
                return;
            }

            const newId = Date.now();
            storesData[currentStore].unshift({ id: newId, name, price, stock, category, icon, rating: "5.0" });
            
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

components.html(flashmart_html, height=920, scrolling=True)
