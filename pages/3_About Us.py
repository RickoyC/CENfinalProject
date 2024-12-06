import streamlit as st
import pathlib

# Read the CSS file content in About Us.css file
with open("assets/css/About Us.css", "r", encoding="utf-8") as file:
    css_content = file.read()

# Read the HTML file content in About Us.html file
with open("assets/html/About Us.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Display html content in the Streamlit app
st.markdown(html_content, unsafe_allow_html=True)
# Display css in the Streamlit app
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)



