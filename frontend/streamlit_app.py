import streamlit as st
import requests

st.title("Calculator UI")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

if st.button("Add"):
    response = requests.get(
        "http://localhost:8000/add",
        params={"a": a, "b": b}
    )
    st.write("Result:", response.json()["result"])


if st.button("Multiply"):
    response = requests.get(
        "http://localhost:8000/multiply",
        params={"a": a, "b": b}
    )
    st.write("Result:", response.json()["result"])

