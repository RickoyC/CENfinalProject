import streamlit as st
import pathlib
# Page Configuration
st.set_page_config(page_title="About Us - Dog Adoption", page_icon="🐶", layout="wide")

# Centered Title
st.markdown(
    """
    <h1 style="text-align: center;">About Us 🐾</h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="text-align: center;">
    Welcome to <b>Puppy Place</b>, where we believe every dog deserves a loving home. 
    We're a dedicated team of animal lovers working to connect wonderful dogs with caring adopters like you.
    </p>
    """,
    unsafe_allow_html=True
)

# About Us Section
st.markdown(
    """
    <h2 style="text-align: center;">Our Mission</h2>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <p style="text-align: center;">
    Our mission is simple: to rescue, rehabilitate, and rehome dogs in need. We work with shelters and foster networks 
    across the country to provide these furry friends with the love and care they deserve.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h2 style="text-align: center;">What We Do</h2>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <p style="text-align: center;">
    - <b>Rescue:</b> Partnering with local shelters to save dogs at risk.<br>
    - <b>Rehoming:</b> Matching dogs with the perfect families based on lifestyle and needs.
    </p>
    """,
    unsafe_allow_html=True
)

# Team Section
st.markdown(
    """
    <h2 style="text-align: center;">Meet Our Team</h2>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <p style="text-align: center;">
    Our team consists of veterinarians, trainers, volunteers, and adoption specialists, all driven by 
    a passion for animal welfare. We’re here to guide you through every step of the adoption process.
    </p>
    """,
    unsafe_allow_html=True
)

# Call to Action
st.markdown(
    """
    <h2 style="text-align: center;">Get Involved</h2>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <p style="text-align: center;">
    Ready to make a difference? Here’s how you can help:<br>
    - <b>Adopt:</b> Browse our available dogs and find your new best friend.<br>
    - <b>Donate:</b> Support our efforts to save more dogs.
    </p>
    """,
    unsafe_allow_html=True
)

# Contact Section
st.markdown(
    """
    <h2 style="text-align: center;">Contact Us</h2>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <p style="text-align: center;">
    Have questions or want to learn more? Reach out to us!<br>
    - <b>Email:</b> 📧 MichaelSMills@jourrapide.com<br>
    - <b>Phone:</b> 📞 +1 (201)-271-5719<br>
    - <b>Address:</b> 🏠 3268 West Side Avenue, Union City, NJ 07087
    </p>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown("---")
st.markdown(
    """
    <p style="text-align: center;">
    💜 Thank you for supporting dog adoption. Together, we can make a difference! 🐶
    </p>
    """,
    unsafe_allow_html=True
)



def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
css_path = pathlib.Path("assets/css/style.css")
load_css(css_path)