import streamlit as st
import requests
import json
import re  # For pattern matching

# Read the CSS file content in Adopt.css file
with open("assets/css/Adopt.css", "r", encoding="utf-8") as file:
    css_content = file.read()

# Display css in the Streamlit app
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# Define the API endpoint
url = 'https://api.rescuegroups.org/v5/public/animals/search/available/dogs/'

# Set up the headers
headers = {
    'Authorization': 'I9CW09wc',  # Replace with your actual API key
    'Content-Type': 'application/json'  # Specify that you're sending JSON data
}

# Function to fetch data based on zip code and page number
def fetch_data(zip_code, page):
    # Prepare the data you want to send, including the zip code
    data = {
        "limit": 10,  # Number of results to return
        "page": page,  # Page number
        "fields": {
            "animals": [
                "name", "ageString", "breedString", "sex",
                "adoptionFeeString", "pictureThumbnailUrl", "rescueId", "url"
            ]  # Fields to return
        },
        "filters": {
            "location": {
                "zip": zip_code
            }
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# Function to validate the rescue ID
def is_valid_rescue_id(rescue_id):
    # Check if the rescue ID is a valid numeric or alphanumeric ID
    if rescue_id and re.match(r'^[a-zA-Z0-9-]+$', rescue_id.strip()):
        return True
    return False

# A text box that says "Find Dogs for Adoption Near You".
st.markdown(
    """
    <div style="
        background-color: rgba(255, 255, 255, 0.9);
        padding: 10px 20px; 
        border-radius: 10px; 
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
        text-align: center; 
        width: 50%; 
        margin: 0 auto;
        position: relative;">
        <img src="https://cdn-icons-png.flaticon.com/512/1998/1998627.png" 
            style="position: absolute; left: -150px; top: 50%; transform: translateY(-50%); width: 80px; height: 80px;" />
        <h1 style="font-size: 30px; color: black;">
            Find Dogs for Adoption Near You
        </h1>
        <img src="https://cdn-icons-png.flaticon.com/512/1998/1998627.png" 
            style="position: absolute; right: -150px; top: 50%; transform: translateY(-50%); width: 80px; height: 80px;" />
    </div>
    """,
    unsafe_allow_html=True
)


# Get user input for zip code
zip_code = st.text_input("Enter your zip code (5 digits):", "")

# Validate the zip code (must be exactly 5 digits)
if zip_code and not re.match(r'^\d{5}$', zip_code):
    st.error("Please enter a valid 5-digit zip code.")
else:
    if zip_code:
        valid_dogs = []  # List to store valid dog results
        page = 1  # Start from the first page

        # Loop until we have 20 valid results
        while len(valid_dogs) < 20:
            # Fetch the data based on the provided zip code and current page
            data = fetch_data(zip_code, page)

            # Check if there is any data returned
            if 'data' in data and data['data']:
                for animal in data['data']:
                    attributes = animal['attributes']
                    name = attributes.get('name', 'Unknown')
                    age = attributes.get('ageString', 'Unknown')
                    breed = attributes.get('breedString', 'Unknown')
                    gender = attributes.get('sex', 'Not specified')  # Male or Female
                    photo = attributes.get('pictureThumbnailUrl')  # Thumbnail URL
                    adoption_fee = attributes.get('adoptionFeeString', 'Unknown')
                    rescue_id = attributes.get('rescueId', None)  # Rescue ID
                    info_url = attributes.get('url', '#')  # Dog's webpage URL

                    # Validate rescue ID
                    valid_rescue_id = rescue_id if is_valid_rescue_id(rescue_id) else None

                    # Check if the dog has a valid photo
                    if photo and photo.strip():
                        valid_dogs.append({
                            'name': name,
                            'age': age,
                            'breed': breed,
                            'gender': gender,
                            'photo': photo,
                            'adoption_fee': adoption_fee,
                            'rescue_id': valid_rescue_id,
                            'url': info_url
                        })

                    # Stop if we have enough valid results
                    if len(valid_dogs) >= 20:
                        break

            # Increment the page number for the next request
            page += 1

            # If no more data is returned, break the loop
            if not data.get('data'):
                break

        # Display the valid results in three columns
        if valid_dogs:
            cols = st.columns(3)  # Create three columns
            for i, dog in enumerate(valid_dogs):
                with cols[i % 3]:  # Use modulo to cycle through columns
                    st.subheader(f'[Name: {dog["name"]}]({dog["url"]})')  # Name with link
                    if dog['photo']:
                        st.image(dog['photo'], caption=dog['name'], use_container_width=True)  # Display image
                    st.write(f'**Age:** {dog["age"] if dog["age"] != "Unknown" else "Not specified"}')
                    st.write(f'**Breed:** {dog["breed"] if dog["breed"] != "Unknown" else "Not specified"}')
                    st.write(f'**Gender:** {dog["gender"]}')
                    st.write(f'**Adoption Fee:** {dog["adoption_fee"]}')
                    if dog['rescue_id']:  # Only display rescue ID if it passes validation
                        st.write(f'**Rescue ID:** {dog["rescue_id"]}')
                    st.write(f'**URL:** [View More Info]({dog["url"]})')  # Clickable URL for dog

                    # Add a line separator at the end of each row
                    st.markdown("---")  # Horizontal line to separate rows

        else:
            st.write("No valid dogs found.")
