# 🔐 Password Strength Meter App using Streamlit

import streamlit as st  # For creating the web interface
import re               # For regular expressions (checking letters, digits, etc.)
import random           # For password generation

# Set of special characters allowed in a strong password
SPECIAL_CHARACTERS = "!@#$%^&*"

# Streamlit app configuration
st.set_page_config(
    page_title="Password Strength Meter",  # Browser tab title
    page_icon="🔑",                         # Tab icon
    layout="centered"                      # Centered layout
)

# ✅ Function to check password strength
def check_password_strength(password: str) -> tuple[int, str]:
    score = 0
    feedback = []

    # 1️⃣ Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Make your password at least 8 characters long.")

    # 2️⃣ Uppercase + lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔸 Include both uppercase and lowercase letters.")

    # 3️⃣ Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔸 Add at least one number (0-9).")

    # 4️⃣ Special character check
    if re.search(rf"[{re.escape(SPECIAL_CHARACTERS)}]", password):
        score += 1
    else:
        feedback.append(f"🔸 Include at least one special character ({SPECIAL_CHARACTERS}).")

    # ❌ Common weak password check
    common_passwords = ["password", "123456", "qwerty", "password123"]
    if password.lower() in common_passwords:
        return 1, "❌ Your password is too common! Choose a more unique password."

    # ✅ Final strength decision
    if score == 4:
        return 5, "✅ *Strong password!* Your password meets all security criteria."
    elif score == 3:
        return 4, "⚠ *Moderate password.* Try adding more complexity for better security."
    else:
        return score, "❌ *Weak password.* " + " ".join(feedback)

# 🔧 Function to generate a strong password
def generate_strong_password(length: int = 12) -> str:
    if length < 8:
        length = 8  # Enforce minimum length

    # Ensure all character types are included
    upper = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower = random.choice("abcdefghijklmnopqrstuvwxyz")
    digit = random.choice("0123456789")
    special = random.choice(SPECIAL_CHARACTERS)

    # Fill the remaining length with random choices
    all_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" + SPECIAL_CHARACTERS
    remaining = "".join(random.choices(all_chars, k=length - 4))

    # Combine and shuffle the password
    password = upper + lower + digit + special + remaining
    return ''.join(random.sample(password, len(password)))

# 🚀 Main function that runs the Streamlit app
def main():
    # 🔥 Custom CSS for UI styling
    st.markdown("""
        <style>
        body {
            background-color: #f2f2f2;
            color: #333333;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.1);
        }
        .stTextInput>div>div>input {
            background-color: #f9f9f9;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton>button {
            background-color: #0066cc;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stSlider {
            padding: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # 🎯 Page title
    st.title("🔐 Stylish Password Strength Meter")
    st.write("Use this tool to check your password strength and get suggestions!")

    # ✏️ Password input box
    password = st.text_input("🔑 Enter a password", type="password")

    # 📊 Show password strength result
    if password:
        score, message = check_password_strength(password)
        if score == 5:
            st.success(message)
        elif score >= 3:
            st.warning(message)
        else:
            st.error(message)

    # 🔁 Divider
    st.divider()

    # 🔧 Strong password generator
    st.subheader("🔧 Generate a Strong Password")
    length = st.slider("📏 Select password length", min_value=8, max_value=32, value=12)

    if st.button("⚙️ Generate Strong Password"):
        strong_password = generate_strong_password(length)
        st.text_input("✅ Strong Password", value=strong_password, disabled=True)

    # 🔚 Footer tip
    st.divider()
    st.markdown("✅ *Tip: Use a password manager and avoid reusing passwords.*")

# 🟢 Start the app
if __name__ == "__main__":
    main()
