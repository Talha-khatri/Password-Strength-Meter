import streamlit as st
import re
import random
import string

def check_password_strength(password):
    length = len(password) >= 8
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    digits = bool(re.search(r'\d', password))
    special_char = bool(re.search(r'[@$!%*?&]', password))
    strength = sum([length, uppercase, lowercase, digits, special_char])
    
    if strength == 5:
        return "Strong", "Your password is strong!"
    elif strength == 4:
        return "Medium", "Your password is okay but can be improved."
    else:
        return "Weak", "Your password is weak. Consider improving it."

def suggest_password():
    password_length = 12
    characters = string.ascii_letters + string.digits + "@$!%*?&"
    random_password = ''.join(random.choice(characters) for _ in range(password_length))
    return random_password

st.title("PASSWORD STRENGTH METER ! 💪")
st.write("""
    This application helps you assess the strength of your password.
    You will also get suggestions to make your password stronger if needed.
""")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, message = check_password_strength(password)
    st.write(f"Password Strength: **{strength}**")
    st.write(message)

    if strength != "Strong":
        st.write("""
            ### Password Criteria:
            - At least 8 characters long.
            - Contains both uppercase and lowercase letters.
            - Includes at least one number.
            - Contains at least one special character (e.g., @, $, %, *, ?, &).

            ### Strong Password Suggestion:
        """)
        suggested_password = suggest_password()
        st.write(f"Suggested Strong Password: **{suggested_password}**")
else:
    st.write("Please enter a password to check its strength.")
