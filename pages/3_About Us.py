import streamlit as st
import pathlib


# `pathlib` allows for cross-compatibility between loonix and wankdows
css_path = pathlib.Path("assets/css/About Us.css")
html_path = pathlib.Path("assets/html/About Us.html")

with open(css_path, "r", encoding="utf-8") as css_file:
    css_content = css_file.read()

with open(html_path, "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

st.markdown(html_content, unsafe_allow_html=True)
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
