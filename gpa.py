import streamlit as st
import time

st.title("⏱️ Study Timer")

seconds = st.number_input("Enter time (seconds)", min_value=1)

if st.button("Start Timer"):
    for i in range(int(seconds), 0, -1):
        st.write(f"Time left: {i} sec")
        time.sleep(1)
    st.success("Time's up! 🎉")