import streamlit as st
import pathlib

st.title("Donate")
st.header("All donations will go towards animal shelters")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")


css_path = pathlib.Path("assets/css/style.css")
load_css(css_path)

# Add CSS for background, button area, and image slider styling
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpaperaccess.com/full/3019614.jpg");
    background-size: cover;  
    background-position: center;  
    background-attachment: local; 
}


.textbox {
    position: absolute;
    top: 100px; /* Adjust the distance from the top */
    left: 50%;
    transform: translateX(-50%);
    font-size: 40px;
    font-weight: bold;
    color: white;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Adds shadow for better visibility */
    z-index: 999; /* Ensure it's above other content */
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Add a textbox with "Adopt a Pet" text
# st.markdown(
#     """
#     <div class="textbox">
#         This is the donation page!
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

fName: list[str] = st.text_input("Full name:", placeholder="First Last").split()
bAddress: str = st.text_input("Enter your billing address as it appears on the card")
ccNumber: list[str] = st.text_input("Credit Card:").replace("-", " ").split()
cvc = st.text_input(
    "Enter the Card Verification Number (CVC)", type="password", placeholder="***"
)
amount = st.text_input("Please enter amount to donate:")

if fName and bAddress and ccNumber and cvc:
    st.success(f"Thank you, {fName[0]}, {fName[1]} for donating ${int(amount) ** 2}")
