from dotenv import load_dotenv
load_dotenv() ## load env varibles

import streamlit as st ## for frontend
import os # operating system
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## FUNCTION LOAD MODEL
model=genai.GenerativeModel("gemini-pro")
def get_gemini_model(question):
    response=model.generate_content(question)
    return response.text

import streamlit as st

# Set the page configuration with a custom title and layout settings
st.set_page_config(page_title="Gemini Q&A Demo", layout="centered", page_icon="✨")

# Customizing the page background color and text styles
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

# Display a header with a colorful emoji to make it more engaging
st.header("🌟 Gemini Q&A Application")

# Provide a short description of the app's purpose
st.write(
    """
    Welcome to the **Gemini Q&A App**, where you can ask any question, 
    and get responses powered by Gemini's capabilities.
    Just type your question below and hit **Ask the question**!
    """
)

# Adding a section divider for aesthetics
st.markdown("---")

# Create a text input field for the user to enter their question
input = st.text_input(
    "Ask your question here:",  # More descriptive input label
    key="input",
    placeholder="E.g., What is the capital of France?",  # Placeholder to guide users
)

# Create a larger, more noticeable button for submission
submit = st.button("Ask the question")

# Check if the button is clicked
if submit:

    # Simulate a Gemini response (replace this with the actual function in your app)
    response = get_gemini_model(input)

    # Add a colorful section to display the response
    st.subheader("🔍 The Response:")
    
    # Display the response with an eye-catching box
    st.markdown(f"""
    <div style="padding: 20px; background-color: #ffffff; border-radius: 10px; color: #4a90e2; border: 2px solid #4a90e2;">
    {response}
    </div>
    """, unsafe_allow_html=True)

# Adding a footer with some custom styling
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
