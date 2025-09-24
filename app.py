import streamlit as st
import time

st.set_page_config(page_title="Debug App", page_icon="🔧")

st.title("🔧 Debug App")
st.write(f"Current time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
st.success("✅ Streamlit is running!")

# Test basic functionality
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

if st.button("Test Button"):
    st.balloons()
    st.write("🎉 Everything works!")
