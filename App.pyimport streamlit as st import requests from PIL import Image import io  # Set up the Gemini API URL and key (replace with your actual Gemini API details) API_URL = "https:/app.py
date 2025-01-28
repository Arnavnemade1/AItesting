import streamlit as st
import requests
from PIL import Image
import io

# Set up the Gemini API URL and key (replace with your actual Gemini API details)
API_URL = "https://your-gemini-api-endpoint"  # Replace with your actual Gemini API endpoint
API_KEY = "your_api_key"  # Replace with your actual API key

# Function to call the Gemini API
def get_gemini_response(text_input, image_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
    }
    # Assuming the Gemini API expects both text and image
    files = {
        "image": image_input,
    }
    data = {
        "text": text_input,
    }
    
    response = requests.post(API_URL, headers=headers, data=data, files=files)
    return response.json()

# Set up the Streamlit UI
st.title("Gemini API with Streamlit")
st.markdown("""
    This is a simple Streamlit app that takes text and an image, sends them to the Gemini API,
    and returns the processed results.
""")

# Text Input
text_input = st.text_area("Enter your text", placeholder="Type something here...")

# Image Input
image_input = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if text_input and image_input:
    st.image(image_input, caption="Uploaded Image", use_column_width=True)
    
    # Process the input using Gemini API
    with st.spinner("Processing..."):
        # Open the image as a PIL object
        image = Image.open(image_input)
        
        # Call the Gemini API
        response = get_gemini_response(text_input, image)
        
        # Display the response
        if response:
            st.subheader("Gemini API Response:")
            st.write(response)
else:
    st.warning("Please provide both text and an image.")

