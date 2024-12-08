import streamlit as st
import pathlib
import time

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
    background-image: url("https://s1.1zoom.me/big0/64/Dogs_Grass_Lying_down_Welsh_Corgi_Bokeh_585621_1280x853.jpg");
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

st.title("Donate")
st.header("All donations will go towards animal shelters")

# Use session state to control if the warning has been displayed
if "warning_shown" not in st.session_state:
    st.session_state.warning_shown = False

# Create a placeholder for the warning message
warning_placeholder = st.empty()

# Display the warning message only if it hasn't been shown yet
if not st.session_state.warning_shown:
    # Display the warning message
    warning_placeholder.warning("### This is a fake donation page, please do not enter any real credentials that can compromise your safety and privacy, thank you.")

    # Wait for 2 seconds and then clear the warning
    time.sleep(2)

    # Clear the warning message
    warning_placeholder.empty()

    # Set the session state to indicate the warning has been shown
    st.session_state.warning_shown = True

# Now display the input widgets
fName: list[str] = st.text_input("Full name:", placeholder="First Last").split()
bAddress: str = st.text_input("Enter your billing address as it appears on the card")
ccNumber: list[str] = st.text_input("Credit Card:").replace("-", " ").split()
cvc = st.text_input(
    "Enter the Card Verification Number (CVC)", type="password", placeholder="***"
)

# Updated to allow decimal values for the donation amount
amount = st.number_input("Please enter amount to donate:", min_value=0.0, format="%.2f")

# Validate the amount to ensure it's a valid number (greater than 0)
if amount <= 0:
    st.error("Please enter a valid amount greater than 0.")
else:
    if fName and bAddress and ccNumber and cvc:
        st.success(f"### Thank you, {fName[0]}, {fName[1]} for donating ${amount:.2f}!")

        # Ask the user if they would like to leave a rating after the donation
        if st.button("Would you like to leave a rating?"):
            # Pop-up for rating system (appear after donation)
            st.write("Please rate your donation experience:")

            # Create a rating system with a radio button
            rating = st.radio("Rate your experience", options=[1, 2, 3, 4, 5], format_func=lambda x: f"{x} Stars")

            # Handle the rating submission
            if rating:
                st.write(f"Thank you for your rating: {rating} Stars!")

                # Optionally, collect a review text (to allow written feedback)
                review = st.text_area("Leave a comment (optional):", placeholder="Your feedback here...")
                if review:
                    st.write("Thank you for your feedback!")
