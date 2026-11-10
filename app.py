import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FlashMart - Ultimate Edition Pro",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Membaca file index.html eksternal secara aman tanpa syntax error
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=880, scrolling=True)
except FileNotFoundError:
    st.error("File index.html tidak ditemukan di direktori repository GitHub Anda!")
    
