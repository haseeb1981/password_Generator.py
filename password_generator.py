import streamlit as st # importing the streamLit Library for creating the web app
import random #importing the random Library for generating random characters
import string #importing the string Library for using string characters

# Function to generate a password based on the user's preferences
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters #Inculde all letters(a-z, A-Z)

    if use_digits:
        characters += string.digits  # Adds numbers (0-9) if selected

    if use_special:
        characters += string.punctuation  # Adds special characters (!, @, $, #, %, *, &, ~, ^)

     # Generates  a random password  of the specified length using the character defined above 
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI & title of the web app
st.title("🔐 Password Generator")

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits (0-9)")

use_special = st.checkbox("Include Special Characters (!, @, #, $, %, etc)")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")  # Display password with backticks

    # Correct way to display the divider line

st.write("---")
st.write("Built with ❤️ by [Haseeb Abbasi] ")
