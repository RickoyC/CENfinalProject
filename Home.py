import pathlib
import base64
import requests

# Importing a custom font
import streamlit as st


# Convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


image_path = "assets/images/puppy place logo.jpg"
base64_image = get_base64_image(image_path)

# Embed in HTML
st.markdown(
    f"""
    <div style="display: flex; flex-direction: column; align-items: center;">
        <img src='data:image/png;base64,{base64_image}' width='100'>
    </div>
    """,
    unsafe_allow_html=True,
)

css_path = pathlib.Path("assets/css/style.css")
html_path = pathlib.Path("assets/html/index.html")

# Read the CSS and HTML content
with open(css_path, "r", encoding="utf-8") as css_file:
    css_content = css_file.read()

with open(html_path, "r", encoding="utf-8") as html_file:
    html_content = html_file.read()

# TODO: Clean this up somehow
st.html(f"<style>{css_content}</style>")
st.markdown(html_content, unsafe_allow_html=True)


# Find a way to integrate dog fact fetch textbox html + css into index and css files.
# Find out how to make dog fact textbox render before footer.
# Fetch a random dog fact from a public API
def fetch_dog_fact():
    try:
        response = requests.get("https://dog-api.kinduff.com/api/facts")
        if response.status_code == 200:
            data = response.json()
            return data["facts"][0]  # The fact is inside a list
        else:
            return "Couldn't fetch a dog fact at the moment. Please try again later!"
    except Exception as e:
        return f"Error: {str(e)}"


# add the new textbox for the dog fact
dog_fact = fetch_dog_fact()
st.markdown(
    f"""
    <div class="howtoadopt-info">
        <div class="howtoadopt-header">Did You Know?</div>
        <div class="howtoadopt-body">{dog_fact}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.success("Select a page above.")
