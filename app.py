import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FlashMart - Ultimate Edition",
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
    <title>FlashMart Ultimate</title>
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
            animation: fadeOut 0.8s ease 2s forwards;
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

        .ripple-btn {
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }
        .ripple {
            position: absolute;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 50%;
            transform: scale(0);
            animation: rippleEffect 0.5s linear;
            pointer-events: none;
        }
        @keyframes rippleEffect {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }

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
        .banner {
            margin: 15px; background: linear-gradient(135deg, #ff8800, #ffbb00); color: white;
            padding: 12px; border-radius: 12px; font-weight: bold; text-align: center; font-size: 12px;
        }
        .product-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; padding: 0 15px; }
        .product-card {
            background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 12px; padding: 12px;
            text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.02); transition: transform 0.2s;
        }
        .product-card:active { transform: scale(0.96); }
        .product-title { font-size: 13px; font-weight: 600; height: 35px; overflow: hidden; margin-bottom: 5px; color: var(--text-color); }
        .product-price { color: #FA591D; font-weight: bold; font-size: 14px; margin-bottom: 8px; }
        
        .btn-group { display: flex; gap: 5px; }
        .btn-cart { background: #ff9800; color: white; border: none; padding: 7px; border-radius: 6px; font-weight: bold; font-size: 11px; flex: 1; cursor: pointer; }
        .btn-buy-now { background: #03AC03; color: white; border: none; padding: 7px; border-radius: 6px; font-weight: bold; font-size: 11px; flex: 1; cursor: pointer; }

        .bottom-nav {
            position: fixed; bottom: 0; left: 50%; transform: translateX(-50%);
            width: 100%; max-width: 480px; background: var(--nav-bg); display: flex; justify-content: space-around;
            padding: 10px 0; border-top: 1px solid var(--border-color); z-index: 100;
        }
        .nav-item {
            text-align: center; font-size: 11px; color: #777; cursor: pointer; background: none; border: none; outline: none;
        }
        .nav-item.active { color: #03AC03; font-weight: bold; }
        .nav-item div { font-size: 20px; }

        .view-section { display: none; padding: 15px; }
        .view-section.active { display: block; }
        
        .cart-item { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding: 10px 0; }
        .profile-card {
            background: linear-gradient(135deg, #FF9800 0%, #FFC107 100%); color: white;
            padding: 16px; border-radius: 16px; margin-bottom: 15px;
        }
        .tracker-box { background: var(--card-bg); border: 1px solid var(--border-color); padding: 12px; border-radius: 10px; margin-bottom: 10px; }
        .stepper { display: flex; justify-content: space-between; margin-top: 10px; font-size: 11px; color: #03AC03; font-weight: bold; }
    </style>
</head>
<body data-theme="light">

    <div id="splash-screen">
        <div class="splash-logo">⚡</div>
        <div style="font-size: 22px; font-weight: 800; margin-top: 15px;">FlashMart Ultimate</div>
    </div>

    <div class="app-container">
        
        <div id="view-home" class="view-section active" style="padding: 0 0 15px 0;">
            <div class="header">
                <h3 style="margin:0;">⚡ FlashMart Store</h3>
                <div class="search-bar">
                    <span>🔍</span>
                    <input type="text" placeholder="Cari kebutuhan harianmu...">
                </div>
            </div>

            <div class="banner">
                🔥 Gunakan Voucher <b>FLASHMARTINA</b> untuk Diskon Rp 10.000!
            </div>

            <div style="padding: 0 15px 10px 15px; font-weight: bold; font-size: 14px;">Produk Terlaris</div>
            <div class="product-grid" id="product-list"></div>
        </div>

        <div id="view-cart" class="view-section">
            <h3>🛒 Keranjang Belanja</h3>
            <div id="cart-items-container">
                <p style="color: #777; text-align: center; margin-top: 30px;">Keranjang masih kosong.</p>
            </div>
            <div id="cart-summary" style="display:none; margin-top: 20px; border-top: 1px solid var(--border-color); padding-top: 15px;">
                <input type="text" id="voucher-input" placeholder="Kode Voucher (FLASHMARTINA)" style="width: 100%; padding: 10px; border: 1px solid var(--border-color); border-radius: 8px; margin-bottom: 10px; box-sizing: border-box; background: var(--card-bg); color: var(--text-color);">
                <button class="ripple-btn" onclick="applyVoucher()" style="background: #333; color: white; border: none; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-size: 12px; margin-bottom: 15px;">Gunakan Voucher</button>
                
                <div style="font-size: 14px; margin-bottom: 5px;">Subtotal: <span id="subtotal-text" style="float: right; font-weight: bold;">Rp 0</span></div>
                <div id="discount-row" style="font-size: 14px; margin-bottom: 5px; color: #03AC03; display: none;">Diskon: <span id="discount-text" style="float: right; font-weight: bold;">- Rp 0</span></div>
                
                <div style="margin: 15px 0;">
                    <label style="font-size: 13px; font-weight: bold;">Metode Pembayaran:</label>
                    <select id="payment-method" style="width: 100%; padding: 8px; margin-top: 5px; border-radius: 6px; background: var(--card-bg); color: var(--text-color); border: 1px solid var(--border-color);">
                        <option value="QRIS">QRIS (Instant Cashback)</option>
                        <option value="Transfer Bank">Transfer Bank (BCA/Mandiri)</option>
                        <option value="COD">Bayar di Tempat (COD)</option>
                    </select>
                </div>

                <div style="font-size: 16px; font-weight: bold; margin-top: 10px; border-top: 1px dashed var(--border-color); padding-top: 10px;">Total: <span id="grandtotal-text" style="float: right; color: #FA591D;">Rp 0</span></div>
                
                <button class="ripple-btn" onclick="checkout()" style="background: #03AC03; color: white; border: none; width: 100%; padding: 12px; border-radius: 10px; font-weight: bold; margin-top: 15px; cursor: pointer;">💳 Bayar Sekarang</button>
            </div>
        </div>

        <div id="view-history" class="view-section">
            <h3>📜 Riwayat & Pelacakan Kurir</h3>
            <div id="history-container">
                <p style="color: #777; text-align: center; margin-top: 30px;">Belum ada riwayat transaksi.</p>
            </div>
        </div>

        <div id="view-account" class="view-section">
            <h3>👤 Pengaturan Akun</h3>
            <div class="profile-card">
                <div style="font-size: 18px; font-weight: bold;">⚡ Pelanggan Setia</div>
                <div style="font-size: 13px; opacity: 0.9; margin-top: 4px;">No: 08123456789 • Gold VIP</div>
                <div style="background: rgba(255,255,255,0.25); padding: 8px 12px; border-radius: 10px; margin-top: 12px; display: flex; justify-content: space-between; font-weight: bold;">
                    <span>⭐ Saldo Poin A-Voucher</span>
                    <span id="user-points">150 Poin</span>
                </div>
            </div>

            <div style="background: var(--card-bg); border: 1px solid var(--border-color); padding: 15px; border-radius: 12px; margin-top: 15px;">
                <div style="display: flex; justify-content: space-between; align-items: center; font-weight: bold;">
                    <span>🌙 Tampilan Mode Gelap</span>
                    <input type="checkbox" id="theme-toggle" onchange="toggleTheme()" style="width: 20px; height: 20px; cursor: pointer;">
                </div>
            </div>
        </div>

        <div class="bottom-nav">
            <button class="nav-item active ripple-btn" onclick="switchTab('home', this)">
                <div>🏠</div>Beranda
            </button>
            <button class="nav-item ripple-btn" onclick="switchTab('cart', this)">
                <div>🛒</div>Keranjang
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
        const products = [
            { id: 1, name: "Minyak Goreng 2L", price: 38000, icon: "🍳" },
            { id: 2, name: "Beras Premium 5kg", price: 69000, icon: "🌾" },
            { id: 3, name: "Susu UHT Ultra 1L", price: 19500, icon: "🥛" },
            { id: 4, name: "Mie Instan (1 Dus)", price: 115000, icon: "📦" },
            { id: 5, name: "Telur Ayam Negeri 1kg", price: 28000, icon: "🥚" },
            { id: 6, name: "Kopi Bubuk Hitam 380g", price: 16500, icon: "☕" },
            { id: 7, name: "Sabun Mandi Cair 450ml", price: 24000, icon: "🧼" },
            { id: 8, name: "Shampoo Anti-Dandruff", price: 32000, icon: "🧴" }
        ];

        let cart = {};
        let points = 150;
        let history = [];
        let discountActive = false;

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

        function renderProducts() {
            const list = document.getElementById('product-list');
            list.innerHTML = products.map(p => `
                <div class="product-card">
                    <div style="font-size: 34px;">` + p.icon + `</div>
                    <div class="product-title">` + p.name + `</div>
                    <div class="product-price">Rp ` + p.price.toLocaleString('id-ID') + `</div>
                    <div class="btn-group">
                        <button class="ripple-btn btn-cart" onclick="addToCart(` + p.id + `)">+ Keranjang</button>
                        <button class="ripple-btn btn-buy-now" onclick="buyNow(` + p.id + `)">Beli</button>
                    </div>
                </div>
            `).join('');
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
            const prod = products.find(p => p.id === id);
            if (cart[id]) { cart[id].qty += 1; } 
            else { cart[id] = { ...prod, qty: 1 }; }
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
        }

        function changeQty(id, delta) {
            cart[id].qty += delta;
            if (cart[id].qty <= 0) delete cart[id];
            renderCart();
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

            const earnedPoints = Math.floor(grandTotal / 10000);
            points += earnedPoints;
            document.getElementById('user-points').innerText = points + ' Poin';

            history.unshift({
                date: new Date().toLocaleString('id-ID'),
                total: grandTotal,
                payment: method,
                earned: earnedPoints,
                status: "Kurir Menuju Lokasi 🛵"
            });

            cart = {};
            discountActive = false;
            alert("✅ Pembayaran via " + method + " Berhasil! Mendapatkan +" + earnedPoints + " Poin.");
            switchTab('history', document.querySelectorAll('.nav-item')[2]);
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
                        <span>📦 Dikemas</span>
                        <span>🛵 Diantar Kurir</span>
                        <span>🏡 Sampai</span>
               </div>
                </div>
            `).join('');
        }

        function toggleTheme() {
            const isDark = document.getElementById('theme-toggle').checked;
            document.body.setAttribute('data-theme', isDark ? 'dark' : 'light');
        }

        renderProducts();
    </script>
</body>
</html>
"""

components.html(flashmart_html, height=880
