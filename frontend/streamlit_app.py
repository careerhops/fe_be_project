import streamlit as st
import requests

st.title("Streamlit Frontend")

response = requests.get("http://localhost:8000")

st.write(response.json())

