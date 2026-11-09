import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FlashMart Ultimate",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Versi HTML ringkas & aman tanpa terpotong
html_content = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FlashMart Ultimate</title>
    <style>
        body { font-family: sans-serif; background: #f8f9fa; margin: 0; padding: 0; color: #333; }
        .app-container { max-width: 480px; margin: 0 auto; background: #fff; min-height: 100vh; padding-bottom: 80px; }
        .header { background: linear-gradient(135deg, #03AC03, #42B549); color: white; padding: 16px; border-bottom-left-radius: 20px; border-bottom-right-radius: 20px; }
        .product-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; padding: 15px; }
        .product-card { background: #fff; border: 1px solid #eee; border-radius: 12px; padding: 12px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.02); }
        .btn-buy { background: #03AC03; color: white; border: none; padding: 8px; width: 100%; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 5px; }
        .bottom-nav { position: fixed; bottom: 0; left: 50%; transform: translateX(-50%); width: 100%; max-width: 480px; background: white; display: flex; justify-content: space-around; padding: 10px 0; border-top: 1px solid #eee; }
        .nav-item { text-align: center; font-size: 11px; color: #777; cursor: pointer; background: none; border: none; }
        .nav-item.active { color: #03AC03; font-weight: bold; }
        .view-section { display: none; padding: 15px; }
        .view-section.active { display: block; }
    </style>
</head>
<body>
    <div class="app-container">
        <!-- BERANDA -->
        <div id="view-home" class="view-section active" style="padding:0;">
            <div class="header">
                <h3 style="margin:0;">⚡ FlashMart Store</h3>
            </div>
            <div style="padding: 15px; font-weight: bold;">Katalog Produk</div>
            <div class="product-grid">
                <div class="product-card">
                    <div style="font-size: 30px;">🍳</div>
                    <div style="font-size: 13px; font-weight: bold;">Minyak Goreng 2L</div>
                    <div style="color: #FA591D; font-weight: bold; margin: 5px 0;">Rp 38.000</div>
                    <button class="btn-buy" onclick="alert('Berhasil dibeli!')">Beli Sekarang</button>
                </div>
                <div class="product-card">
                    <div style="font-size: 30px;">🌾</div>
                    <div style="font-size: 13px; font-weight: bold;">Beras Premium 5kg</div>
                    <div style="color: #FA591D; font-weight: bold; margin: 5px 0;">Rp 69.000</div>
                    <button class="btn-buy" onclick="alert('Berhasil dibeli!')">Beli Sekarang</button>
                </div>
            </div>
        </div>

        <!-- KERANJANG -->
        <div id="view-cart" class="view-section">
            <h3>🛒 Keranjang Belanja</h3>
            <p>Keranjang kamu kosong.</p>
        </div>

        <!-- LACAKAN -->
        <div id="view-history" class="view-section">
            <h3>🚚 Lacakan Kurir</h3>
            <p>Belum ada pengiriman aktif.</p>
        </div>

        <!-- AKUN -->
        <div id="view-account" class="view-section">
            <h3>👤 Pengaturan Akun</h3>
            <p>Pelanggan Setia (Gold VIP)</p>
        </div>

        <!-- NAVIGASI -->
        <div class="bottom-nav">
            <button class="nav-item active" onclick="switchTab('home', this)"><div>🏠</div>Beranda</button>
            <button class="nav-item" onclick="switchTab('cart', this)"><div>🛒</div>Keranjang</button>
            <button class="nav-item" onclick="switchTab('history', this)"><div>🚚</div>Lacakan</button>
            <button class="nav-item" onclick="switchTab('account', this)"><div>👤</div>Akun</button>
        </div>
    </div>

    <script>
        function switchTab(tabName, element) {
            document.querySelectorAll('.view-section').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            document.getElementById('view-' + tabName).classList.add('active');
            element.classList.add('active');
        }
    </script>
</body>
</html>
"""

components.html(flashmart_html, height=750, scrolling=True)
