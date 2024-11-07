import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Text input
name = st.text_input("Enter your name:")

# Slider input
age = st.slider("Select your age:", 0, 100, 25)

# Button to submit
if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old.")

# A little extra content
st.write("This is a simple Streamlit app to demonstrate basic UI elements.")
