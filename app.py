import streamlit as st
from password_checker import check_password

# Page Configuration
st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐",
    layout="centered"
)

# Title
st.title("🔐 Password Strength Analyzer")

st.write("Check the strength of your password.")

st.divider()

# Password Input
password = st.text_input(
    "Enter Your Password",
    type="password"
)

# Button
if st.button("Check Password"):

    if password == "":
        st.warning("⚠ Please enter a password.")

    else:

        score, suggestions = check_password(password)

        st.subheader("Password Score")

        st.progress(score / 100)

        st.write(f"Score : **{score}/100**")

        # Strength
        if score == 100:
            st.success("🟢 Strong Password")

        elif score >= 60:
            st.warning("🟡 Medium Password")

        else:
            st.error("🔴 Weak Password")

        # Suggestions
        if suggestions:

            st.subheader("Suggestions")

            for item in suggestions:
                st.write("✔", item)

        else:

            st.success("Excellent! Your password is very secure.")