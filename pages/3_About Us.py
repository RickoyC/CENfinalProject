import streamlit as st
import base64
import pathlib


# Convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


image_path = "assets/images/puppy place logo.jpg"
base64_image = get_base64_image(image_path)

# Embed in HTML
st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src='data:image/png;base64,{base64_image}' width='100'>
    </div>
    """,
    unsafe_allow_html=True,
)

# `pathlib` allows for cross-compatibility between loonix and wankdows
css_path = pathlib.Path("assets/css/About Us.css")
html_path = pathlib.Path("assets/html/About Us.html")

with open(css_path, "r", encoding="utf-8") as css_file:
    css_content = css_file.read()

with open(html_path, "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

st.markdown(html_content, unsafe_allow_html=True)
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
