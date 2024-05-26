import streamlit as st
import requests

st.title("Mika Chatbot")

user_input = st.text_input("You: ", "")

if st.button("Send"):
    response = requests.post('http://localhost:3000/api/chat', json={"message": user_input})
    data = response.json()
    st.text_area("Mika: ", data['response'], height=200)
