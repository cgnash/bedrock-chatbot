import streamlit as st
import time

# Configure Streamlit for App Runner
st.set_page_config(
    page_title="Debug App", 
    page_icon="🔧",
    layout="centered"
)

# Add this to help with App Runner connectivity
st.markdown("""
<style>
    .stApp > header {
        background-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔧 Debug App - Version 3")
st.write(f"Current time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
st.success("✅ Streamlit is running!")

# Test basic functionality
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

if st.button("Test Button"):
    st.balloons()
    st.write("🎉 Everything works!")

# Add some debug info
st.write("---")
st.write("**Debug Info:**")
st.write(f"- Streamlit version: {st.__version__}")
st.write("- App is responding to requests ✅")
