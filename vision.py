from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones
model = genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(input,image):
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;  /* Light background color */
    }
    h1 {
        color: #4a90e2;  /* Blue color for the header */
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;  /* White input field */
        color: #333333;  /* Dark text color */
    }
    .stButton button {
        background-color: #4a90e2;  /* Blue button */
        color: white;  /* White button text */
        border-radius: 10px;  /* Rounded button */
        width: 200px;  /* Wider button */
        height: 50px;
        font-size: 16px;  /* Larger button text */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
st.markdown(
    """
    <style>
    footer {
        visibility: hidden;
    }
    </style>
    <div style='text-align: center; color: #4a90e2; font-size: 14px; margin-top: 50px;'> 
    Created with 💙 by Alpona Das
    </div>
    """,
    unsafe_allow_html=True
)
