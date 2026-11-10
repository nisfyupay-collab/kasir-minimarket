import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FlashMart - Ultimate Edition Pro",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

flashmart_html = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FlashMart Ultimate Pro</title>
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

        #splash-screen {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);
            display: flex; flex-direction: column; justify-content: center; align-items: center;
            z-index: 9999; color: white;
            animation: fadeOut 0.8s ease 1.5s forwards;
        }
        .splash-logo {
            font-size: 64px; background: white; color: #FF9800; width: 100px; height: 100px;
            display: flex; justify-content: center; align-items: center; border-radius: 25px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            animation: bounceIn 0.8s ease;
        }
        @keyframes bounceIn {
            0% { transform: scale(0); opacity: 0; }
            60% { transform: scale(1.1); opacity: 1; }
            100% { transform: scale(1); }
        }
        @keyframes fadeOut {
            to { opacity: 0; visibility: hidden; }
        }

        /* Modal Struk Belanja Estetik (Receiptify Style) */
        #success-modal {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.7); display: none; justify-content: center; align-items: center;
            z-index: 10000; backdrop-filter: blur(4px); overflow-y: auto; padding: 20px;
        }
        .receipt-card {
            background: #fff; color: #333; width: 100%; max-width: 340px; padding: 20px;
            border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); font-family: 'Courier New', Courier, monospace;
            position: relative; animation: popUp 0.4s ease; margin: auto;
        }
        .receipt-card::before {
            content: ""; position: absolute; top: -10px; left: 0; width: 100%; height: 10px;
            background: radial-gradient(circle, transparent, transparent 50%, #fff 50%, #fff 100%);
            background-size: 16px 20px;
        }
        @keyframes popUp {
            0% { transform: scale(0.7); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }

        .ripple-btn { position: relative; overflow: hidden; cursor: pointer; }
        .ripple {
            position: absolute; background: rgba(255, 255, 255, 0.7); border-radius: 50%;
            transform: scale(0); animation: rippleEffect 0.5s linear; pointer-events: none;
        }
        @keyframes rippleEffect { to { transform: scale(4); opacity: 0; } }

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
        
        .cart-item { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding: 10px 0; }
        .profile-card { background: linear-gradient(135deg, #FF9800 0%, #FFC107 100%); color: white; padding: 16px; border-radius: 16px; margin-bottom: 15px; }
        .tracker-box { background: var(--card-bg); border: 1px solid var(--border-color); padding: 12px; border-radius: 10px; margin-bottom: 10px; }
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

    <!-- SPLASH SCREEN -->
    <div id="splash-screen">
        <div class="splash-logo">⚡</div>
        <div style="font-size: 22px; font-weight: 800; margin-top: 15px;">FlashMart Ultimate Pro</div>
    </div>

    <!-- POP-UP MODAL STRUK BELANJA (RECEIPTIFY STYLE) -->
    <div id="success-modal">
        <div class="receipt-card">
            <h3 style="text-align: center; margin: 0 0 5px 0; font-size: 16px; font-weight: 900;">FLASHMART ULTIMATE</h3>
            <p style="text-align: center; font-size: 11px; margin: 0 0 10px 0; color: #666;">Jl. Raya Minimarket No. 88, Indonesia</p>
            <div style="font-size: 11px; border-bottom: 1px dashed #333; padding-bottom: 8px; margin-bottom: 8px;" id="receipt-meta">
                Waktu: 2026-11-10 09:00<br>
                Kasir: Auto-System v3.5
            </div>
            
            <div style="font-size: 11px; font-weight: bold; display: flex; justify-content: border-bottom; border-bottom: 1px dashed #333; padding-bottom: 4px; margin-bottom: 6px;">
                <span style="flex: 2;">ITEM</span>
                <span style="flex: 1; text-align: center;">QTY</span>
                <span style="flex: 1; text-align: right;">SUBTOTAL</span>
            </div>
            
            <div id="receipt-items-list" style="font-size: 11px; max-height: 140px; overflow-y: auto; margin-bottom: 8px; border-bottom: 1px dashed #333; padding-bottom: 8px;">
                <!-- Diisi via Javascript -->
            </div>

            <div style="font-size: 11px; line-height: 1.5;">
                <div style="display: flex; justify-content: space-between;"><span>SUBTOTAL:</span><span id="receipt-subtotal">Rp 0</span></div>
                <div style="display: flex; justify-content: space-between;" id="receipt-disc-row"><span>DISKON:</span><span id="receipt-discount">- Rp 0</span></div>
                <div style="display: flex; justify-content: space-between; font-weight: bold; font-size: 13px; margin: 4px 0;"><span>TOTAL:</span><span id="receipt-total">Rp 0</span></div>
                <div style="display: flex; justify-content: space-between;"><span>BAYAR (CASH):</span><span id="receipt-cash">Rp 0</span></div>
                <div style="display: flex; justify-content: space-between; font-weight: bold; color: #03AC03;" id="receipt-change-row"><span>KEMBALIAN:</span><span id="receipt-change">Rp 0</span></div>
            </div>

            <div style="text-align: center; margin-top: 15px; font-size: 10px; color: #555;">
                <p style="margin: 0 0 5px 0;">THANK YOU FOR SHOPPING!</p>
                <div style="font-family: 'Libre Barcode 39', cursive; font-size: 28px; letter-spacing: 2px;">*FLASHMART9988*</div>
                <span style="font-size: 9px; color: #888;">receiptify.flashmart.app</span>
            </div>

            <button class="ripple-btn" onclick="closeModal()" style="background: #03AC03; color: white; border: none; width: 100%; padding: 10px; border-radius: 6px; font-weight: bold; margin-top: 15px; font-size: 12px; font-family: sans-serif;">Selesai & Tutup Struk</button>
        </div>
    </div>

    <div class="app-container">
        
        <!-- BERANDA -->
        <div id="view-home" class="view-section active" style="padding: 0 0 15px 0;">
            <div class="header">
                <h3 style="margin:0;">⚡ FlashMart Store Pro</h3>
                <div class="search-bar">
                    <span>🔍</span>
                    <input type="text" id="search-box" placeholder="Cari kebutuhan harian / pulsa..." oninput="filterProducts()">
                </div>
            </div>

            <!-- PILIH TOKO ONLINE -->
            <div class="store-selector">
                <span>🏪 Pilih Toko:</span>
                <select id="store-select" onchange="changeStore()">
                    <option value="Pusat">FlashMart Pusat (Lengkap)</option>
                    <option value="Express">FlashMart Express (Kilat)</option>
                    <option value="Grosir">FlashMart Grosir (Partai Besar)</option>
                </select>
            </div>

            <!-- QUICK LINK PEMBELIAN PULSA & DIGITAL -->
            <div style="padding: 12px 15px 5px 15px; font-weight: bold; font-size: 13px;">📱 Layanan Pulsa & PPOB</div>
            <div class="digital-grid">
                <div class="digital-item ripple-btn" onclick="switchTab('pulsa', document.querySelectorAll('.nav-item')[3])">📱 Pulsa</div>
                <div class="digital-item ripple-btn" onclick="switchTab('pulsa', document.querySelectorAll('.nav-item')[3])">🌐 Kuota Data</div>
                <div class="digital-item ripple-btn" onclick="switchTab('pulsa', document.querySelectorAll('.nav-item')[3])">⚡ Token PLN</div>
                <div class="digital-item ripple-btn" onclick="switchTab('pulsa', document.querySelectorAll('.nav-item')[3])">🎮 E-Money</div>
            </div>

            <div class="category-scroll" id="category-container">
                <div class="cat-chip active" onclick="selectCategory('Semua', this)">Semua</div>
                <div class="cat-chip" onclick="selectCategory('Sembako', this)">Sembako</div>
                <div class="cat-chip" onclick="selectCategory('Minuman', this)">Minuman</div>
                <div class="cat-chip" onclick="selectCategory('Perawatan', this)">Perawatan</div>
                <div class="cat-chip" onclick="selectCategory('Elektronik', this)">Elektronik</div>
                <div class="cat-chip" onclick="selectCategory('Camilan', this)">Camilan</div>
            </div>

            <div class="banner">
                🔥 Gunakan Voucher <b>FLASHMARTINA</b> untuk Diskon Rp 10.000!
            </div>

            <div style="padding: 0 15px 10px 15px; font-weight: bold; font-size: 14px;" id="store-title-label">Katalog Produk - FlashMart Pusat</div>
            <div class="product-grid" id="product-list"></div>
        </div>

        <!-- KERANJANG & CHECKOUT -->
        <div id="view-cart" class="view-section">
            <h3>🛒 Keranjang Belanja</h3>
            <div id="cart-items-container">
                <p style="color: #777; text-align: center; margin-top: 30px;">Keranjang masih kosong.</p>
            </div>
            <div id="cart-summary" style="display:none; margin-top: 20px; border-top: 1px solid var(--border-color); padding-top: 15px;">
                <input type="text" id="voucher-input" placeholder="Kode Voucher (FLASHMARTINA)" class="admin-input">
                <button class="ripple-btn" onclick="applyVoucher()" style="background: #333; color: white; border: none; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-size: 12px; margin-bottom: 15px;">Gunakan Voucher</button>
                
                <div style="font-size: 14px; margin-bottom: 5px;">Subtotal: <span id="subtotal-text" style="float: right; font-weight: bold;">Rp 0</span></div>
                <div id="discount-row" style="font-size: 14px; margin-bottom: 5px; color: #03AC03; display: none;">Diskon: <span id="discount-text" style="float: right; font-weight: bold;">- Rp 0</span></div>
                
                <div style="margin: 15px 0;">
                    <label style="font-size: 13px; font-weight: bold;">Metode Pembayaran:</label>
                    <select id="payment-method" class="admin-input" style="margin-top: 5px;" onchange="toggleQR()">
                        <option value="Tunai">Tunai / Cash (Bayar di Kasir)</option>
                        <option value="QRIS">QRIS (Scan & Cashback Instant)</option>
                        <option value="Transfer Bank">Transfer Bank (BCA / Mandiri / BRI)</option>
                        <option value="COD">Bayar di Tempat (COD)</option>
                    </select>
                </div>

                <!-- INPUT UANG TUNAI & HITUNG KEMBALIAN OTOMATIS -->
                <div id="cash-payment-box" style="margin-bottom: 15px;">
                    <label style="font-size: 13px; font-weight: bold;">Nominal Uang Pembeli (Rp):</label>
                    <input type="number" id="cash-given" placeholder="Contoh: 100000" class="admin-input" style="margin-top: 5px;" oninput="calculateChange()">
                    <div style="font-size: 14px; font-weight: bold; color: #03AC03; margin-top: 4px;" id="change-text">Uang Kembalian: Rp 0</div>
                </div>

                <!-- DYNAMIC QR CODE BOX -->
                <div id="qris-display" class="qr-box" style="display: none;">
                    <div style="font-size: 12px; font-weight: bold; color: #333; margin-bottom: 5px;">Scan Kode QRIS Di Bawah Ini:</div>
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=FLASHMART-ULTIMATE-PAYMENT-QRIS-PRO" alt="QRIS Code">
                    <div style="font-size: 11px; color: #666; margin-top: 5px;">Dapat di-scan memakai GoPay, OVO, Dana, ShopeePay & M-Banking.</div>
                </div>

                <div style="font-size: 16px; font-weight: bold; margin-top: 10px; border-top: 1px dashed var(--border-color); padding-top: 10px;">Total: <span id="grandtotal-text" style="float: right; color: #FA591D;">Rp 0</span></div>
                
                <button class="ripple-btn" onclick="checkout()" style="background: #03AC03; color: white; border: none; width: 100%; padding: 12px; border-radius: 10px; font-weight: bold; margin-top: 15px; cursor: pointer;">💳 Selesaikan Transaksi & Cetak Struk</button>
            </div>
        </div>

        <!-- TAB ISI PULSA & DATA OPERATOR -->
        <div id="view-pulsa" class="view-section">
            <h3>📱 Isi Pulsa & Paket Data Online</h3>
            <div style="background: var(--card-bg); border: 1px solid var(--border-color); padding: 15px; border-radius: 12px; margin-bottom: 15px;">
                <label style="font-size: 13px; font-weight: bold;">1. Pilih Operator Sinyal:</label>
                <select id="pulsa-operator" class="admin-input" style="margin-top: 5px;">
                    <option value="Telkomsel">Telkomsel (Negeri / BUMN)</option>
                    <option value="Indosat">Indosat Ooredoo Hutchison</option>
                    <option value="XL">XL Axiata</option>
                    <option value="Tri">Tri (3)</option>
                    <option value="Smartfren">Smartfren Telecom</option>
                    <option value="Axis">Axis</option>
                </select>

                <label style="font-size: 13px; font-weight: bold;">2. Masukkan Nomor HP:</label>
                <input type="number" id="pulsa-phone" placeholder="Contoh: 081234567890" class="admin-input">

                <label style="font-size: 13px; font-weight: bold;">3. Pilih Nominal Pulsa / Kuota:</label>
                <select id="pulsa-nominal" class="admin-input" style="margin-top: 5px;">
                    <option value="11000">Pulsa 10.000 (Rp 11.000)</option>
                    <option value="26000">Pulsa 25.000 (Rp 26.000)</option>
                    <option value="51000">Pulsa 50.000 (Rp 51.000)</option>
                    <option value="101000">Pulsa 100.000 (Rp 101.000)</option>
                    <option value="35000">Paket Data 5GB 30 Hari (Rp 35.000)</option>
                    <option value="65000">Paket Data 15GB 30 Hari (Rp 65.000)</option>
                </select>

                <button class="ripple-btn" onclick="buyPulsa()" style="background: #03AC03; color: white; border: none; width: 100%; padding: 12px; border-radius: 10px; font-weight: bold; cursor: pointer; margin-top: 10px;">⚡ Beli Pulsa Sekarang</button>
            </div>
        </div>

        <!-- RIWAYAT & KURIR -->
        <div id="view-history" class="view-section">
            <h3>📜 Riwayat & Pelacakan Kurir</h3>
            <div id="history-container">
                <p style="color: #777; text-align: center; margin-top: 30px;">Belum ada riwayat transaksi.</p>
            </div>
        </div>

        <!-- AKUN & MANAJEMEN STOK -->
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

            <!-- FORM TAMBAH PRODUK BARU -->
            <div style="background: var(--card-bg); border: 1px solid var(--border-color); padding: 15px; border-radius: 12px; margin-bottom: 15px;">
                <h4 style="margin-top: 0; color: #03AC03;">📦 Tambah Produk Baru ke Toko Aktif</h4>
                <input type="text" id="new-name" placeholder="Nama Produk" class="admin-input">
                <input type="number" id="new-price" placeholder="Harga (Rp)" class="admin-input">
                <input type="number" id="new-stock" placeholder="Jumlah Stok" class="admin-input">
                <select id="new-category" class="admin-input">
                    <option value="Sembako">Sembako</option>
                    <option value="Minuman">Minuman</option>
                    <option value="Perawatan">Perawatan</option>
                    <option value="Elektronik">Elektronik</option>
                    <option value="Camilan">Camilan</option>
                </select>
                <input type="text" id="new-icon" placeholder="Emoji Ikon (Contoh: 🍪)" class="admin-input">
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
            <button class="nav-item active ripple-btn" onclick="switchTab('home', this)">
                <div>🏠</div>Beranda
            </button>
            <button class="nav-item ripple-btn" onclick="switchTab('cart', this)">
                <div>🛒</div>Keranjang
            </button>
            <button class="nav-item ripple-btn" onclick="switchTab('pulsa', this)">
                <div>📱</div>Pulsa
            </button>
            <button class="nav-item ripple-btn" onclick="switchTab('history', this)">
                <div>🚚</div>Lacakan
            </button>
            <button class="nav-item ripple-btn" onclick="switchTab('account', this)">
                <div>👤</div>Akun
            </button>
        </div>
    </div>

    <script>
        const storesData = {
            "Pusat": [
                { id: 101, name: "Minyak Goreng 2L", price: 38000, stock: 25, category: "Sembako", icon: "🍳" },
                { id: 102, name: "Beras Premium 5kg", price: 69000, stock: 15, category: "Sembako", icon: "🌾" },
                { id: 103, name: "Susu UHT Ultra 1L", price: 19500, stock: 30, category: "Minuman", icon: "🥛" },
                { id: 104, name: "Mie Instan (1 Dus)", price: 115000, stock: 12, category: "Sembako", icon: "📦" },
                { id: 105, name: "Telur Ayam Negeri 1kg", price: 28000, stock: 20, category: "Sembako", icon: "🥚" },
                { id: 106, name: "Kopi Bubuk Hitam 380g", price: 16500, stock: 18, category: "Minuman", icon: "☕" },
                { id: 107, name: "Sabun Mandi Cair 450ml", price: 24000, stock: 14, category: "Perawatan", icon: "🧼" },
                { id: 108, name: "Shampoo Anti-Dandruff", price: 32000, stock: 10, category: "Perawatan", icon: "🧴" },
                { id: 109, name: "Kipas Angin Meja Mini", price: 125000, stock: 5, category: "Elektronik", icon: "🌀" },
                { id: 110, name: "Keripik Singkong Balado", price: 12000, stock: 40, category: "Camilan", icon: "🍟" }
            ],
            "Express": [
                { id: 201, name: "Air Mineral 600ml (1 Dus)", price: 35000, stock: 50, category: "Minuman", icon: "💧" },
                { id: 202, name: "Roti Tawar Gandum", price: 18000, stock: 15, category: "Camilan", icon: "🍞" },
                { id: 203, name: "Susu Kotak Kecil 250ml", price: 6000, stock: 60, category: "Minuman", icon: "🧃" },
                { id: 204, name: "Cokelat Batang Premium", price: 15000, stock: 25, category: "Camilan", icon: "🍫" },
                { id: 205, name: "Baterai Alkali AA (Isi 2)", price: 22000, stock: 30, category: "Elektronik", icon: "🔋" },
                { id: 206, name: "Tisu Basah Antiseptik", price: 11000, stock: 35, category: "Perawatan", icon: "🧻" }
            ],
            "Grosir": [
                { id: 301, name: "Beras Karung 25kg", price: 330000, stock: 8, category: "Sembako", icon: "🛍️" },
                { id: 302, name: "Minyak Goreng Jerigen 5L", price: 92000, stock: 10, category: "Sembako", icon: "🛢️" },
                { id: 303, name: "Gula Pasir 10kg", price: 145000, stock: 12, category: "Sembako", icon: "🍬" },
                { id: 304, name: "Deterjen Bubuk 5kg", price: 68000, stock: 15, category: "Perawatan", icon: "🧼" },
                { id: 305, name: "Mie Instan (3 Dus Sekaligus)", price: 340000, stock: 6, category: "Sembako", icon: "📦" }
            ]
        };

        let currentStore = "Pusat";
        let cart = {};
        let points = 150;
        let history = [];
        let discountActive = false;
        let activeCategory = 'Semua';

        document.addEventListener('click', function (e) {
            const target = e.target.closest('.ripple-btn');
            if (target) {
                const circle = document.createElement('span');
                const diameter = Math.max(target.clientWidth, target.clientHeight);
                const radius = diameter / 2;
                circle.style.width = circle.style.height = diameter + 'px';
                circle.style.left = (e.clientX - target.getBoundingClientRect().left - radius) + 'px';
                circle.style.top = (e.clientY - target.getBoundingClientRect().top - radius) + 'px';
                circle.classList.add('ripple');
                target.appendChild(circle);
                setTimeout(() => circle.remove(), 500);
            }
        });

        function toggleQR() {
            const method = document.getElementById('payment-method').value;
            const qrisBox = document.getElementById('qris-display');
            const cashBox = document.getElementById('cash-payment-box');
            
            if (method === 'QRIS') {
                qrisBox.style.display = 'block';
                cashBox.style.display = 'none';
            } else if (method === 'Tunai') {
                qrisBox.style.display = 'none';
                cashBox.style.display = 'block';
            } else {
                qrisBox.style.display = 'none';
                cashBox.style.display = 'none';
            }
        }

        function calculateChange() {
            let subtotal = Object.values(cart).reduce((sum, item) => sum + (item.price * item.qty), 0);
            const discount = discountActive ? 10000 : 0;
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
                list.innerHTML = '<p style="grid-column: span 2; text-align: center; color: #777;">Tidak ada produk di toko ini.</p>';
                return;
            }
            list.innerHTML = listToRender.map(p => `
                <div class="product-card">
                    <div style="font-size: 34px;">` + p.icon + `</div>
                    <div class="product-title">` + p.name + `</div>
                    <div class="product-stock">Stok: ` + p.stock + `</div>
                    <div class="product-price">Rp ` + p.price.toLocaleString('id-ID') + `</div>
                    <div class="btn-group">
                        <button class="ripple-btn btn-cart" onclick="addToCart(` + p.id + `)">+ Keranjang</button>
                        <button class="ripple-btn btn-buy-now" onclick="buyNow(` + p.id + `)">Beli</button>
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
            element.classList.add('active');

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
            if (cart[id]) { cart[id].qty += 1; } 
            else { cart[id] = { ...prod, qty: 1, store: currentStore }; }
            filterProducts();
            alert(prod.name + " ditambahkan ke keranjang!");
        }

        function buyNow(id) {
            addToCart(id);
            switchTab('cart', document.querySelectorAll('.nav-item')[1]);
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
            let html = '';
            let subtotal = 0;

            keys.forEach(id => {
                const item = cart[id];
                const totalItem = item.price * item.qty;
                subtotal += totalItem;
                html += `
                    <div class="cart-item">
                        <div>
                            <div style="font-weight: bold; font-size: 13px;">` + item.icon + ` ` + item.name + `</div>
                            <div style="font-size: 11px; color: #03AC03; font-weight: bold;">Toko: FlashMart ` + item.store + `</div>
                            <div style="font-size: 12px; color: #888;">Rp ` + item.price.toLocaleString('id-ID') + ` x ` + item.qty + `</div>
                        </div>
                        <div>
                            <button onclick="changeQty(` + id + `, -1)">-</button>
                            <span style="margin: 0 8px; font-weight: bold;">` + item.qty + `</span>
                            <button onclick="changeQty(` + id + `, 1)">+</button>
                        </div>
                    </div>
                `;
            });
            container.innerHTML = html;
            updateSummary(subtotal);
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
                alert("🎉 Voucher FLASHMARTINA Berhasil Digunakan! Potongan Rp 10.000");
            } else {
                discountActive = false;
                alert("❌ Kode Voucher tidak valid.");
            }
            let subtotal = Object.values(cart).reduce((sum, item) => sum + (item.price * item.qty), 0);
            updateSummary(subtotal);
            calculateChange();
        }

        function updateSummary(subtotal) {
            const discount = discountActive ? 10000 : 0;
            const grandTotal = Math.max(0, subtotal - discount);
            document.getElementById('subtotal-text').innerText = 'Rp ' + subtotal.toLocaleString('id-ID');
            const discRow = document.getElementById('discount-row');
            if (discount > 0) {
                discRow.style.display = 'block';
                document.getElementById('discount-text').innerText = '- Rp ' + discount.toLocaleString('id-ID');
            } else { discRow.style.display = 'none'; }
            document.getElementById('grandtotal-text').innerText = 'Rp ' + grandTotal.toLocaleString('id-ID');
        }

        function checkout() {
            let subtotal = Object.values(cart).reduce((sum, item) => sum + (item.price * item.qty), 0);
            const discount = discountActive ? 10000 : 0;
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

            const now = new Date().toLocaleString('id-ID');

            // Render ke Struk Receiptify Style
            document.getElementById('receipt-meta').innerHTML = "Waktu: " + now + "<br>Metode: " + method;
            let receiptHtml = '';
            for (let id in cart) {
                const item = cart[id];
                receiptHtml += `<div style="display: flex; justify-content: space-between; margin-bottom: 2px;">
                    <span style="flex: 2;">${item.name}</span>
                    <span style="flex: 1; text-align: center;">${item.qty}</span>
                    <span style="flex: 1; text-align: right;">Rp ${(item.price * item.qty).toLocaleString('id-ID')}</span>
                </div>`;
            }
            document.getElementById('receipt-items-list').innerHTML = receiptHtml;
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
                date: now,
                total: grandTotal,
                payment: method,
                earned: earnedPoints,
                status: "Selesai & Lunas ✅"
            });

            cart = {};
            discountActive = false;
            document.getElementById('cash-given').value = '';

            // Tampilkan Struk
            document.getElementById('success-modal').style.display = 'flex';
        }

        function buyPulsa() {
            const op = document.getElementById('pulsa-operator').value;
            const phone = document.getElementById('pulsa-phone').value.trim();
            const price = parseInt(document.getElementById('pulsa-nominal').value);

            if (!phone || phone.length < 10) {
                alert("Masukkan nomor HP yang valid!");
                return;
            }

            const earnedPoints = Math.floor(price / 10000);
            points += earnedPoints;
            document.getElementById('user-points').innerText = points + ' Poin';
            const now = new Date().toLocaleString('id-ID');

            // Render Struk Pulsa
            document.getElementById('receipt-meta').innerHTML = "Waktu: " + now + "<br>Jenis: Pulsa / PPOB";
            document.getElementById('receipt-items-list').innerHTML = `
                <div style="display: flex; justify-content: space-between;">
                    <span style="flex: 2;">${op} (${phone})</span>
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
                date: now,
                total: price,
                payment: "Pulsa " + op,
                earned: earnedPoints,
                status: "Pulsa Sukses Terkirim 📱"
            });

            document.getElementById('pulsa-phone').value = '';
            document.getElementById('success-modal').style.display = 'flex';
        }

        function closeModal() {
            document.getElementById('success-modal').style.display = 'none';
            switchTab('history', document.querySelectorAll('.nav-item')[3]);
        }

        function renderHistory() {
            const container = document.getElementById('history-container');
            if (history.length === 0) {
                container.innerHTML = '<p style="color: #777; text-align: center; margin-top: 30px;">Belum ada riwayat transaksi.</p>';
                return;
            }

            container.innerHTML = history.map(tx => `
                <div class="tracker-box">
                    <div style="font-size: 11px; color: #888;">` + tx.date + ` • Metode: ` + tx.payment + `</div>
                    <div style="font-weight: bold; font-size: 14px; margin: 4px 0;">Total: Rp ` + tx.total.toLocaleString('id-ID') + `</div>
                    <div style="color: #FA591D; font-size: 12px; font-weight: bold;">Status: ` + tx.status + `</div>
                    <div class="stepper">
                        <span>📦 Proses</span>
                        <span>⚡ Dikonfirmasi</span>
                        <span>🏡 Selesai</span>
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

            alert("✅ Produk baru berhasil ditambahkan ke toko FlashMart " + currentStore + "!");
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
"""

components.html(flashmart_html, height=880, scrolling=True)
