import streamlit as st
import requests

API_BASE = "http://localhost:8000"

st.title("Welcome to Mastery on AI")
st.subheader("Live Hands-on training! ")

st.markdown("""
### In Day 2, you will build:

- A Backend service
- Connect to LLMs from that service
- Send prompt to Cloud-hosted LLMs and get response back
- Build a Front-end service
- Display chat results in a Frontend UI.
- Understand CI/CD by building a pipeline
- Then understand what is an AI Agent
""") 

tab1, tab2 = st.tabs(["🤖 Chat Assistant", "🧮 Calculator APIs"])

# =========================
# CHAT TAB
# =========================
with tab1:

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input("Ask something...")

    if prompt:

        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        response = requests.get(
            f"{API_BASE}/ask",
            params={"question": prompt}
        )

        data = response.json()
        st.write(data)
        answer = response.json()["answer"]

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

# =========================
# CALCULATOR TAB
# =========================
with tab2:

    st.subheader("Addition")

    a = st.number_input("First number", key="add_a")
    b = st.number_input("Second number", key="add_b")

    if st.button("Add"):
        response = requests.get(
            f"{API_BASE}/add",
            params={"a": a, "b": b}
        )
        st.success(f"Result: {response.json()['result']}")

    st.divider()

    st.subheader("Multiplication")

    x = st.number_input("First number ", key="mul_a")
    y = st.number_input("Second number ", key="mul_b")

    if st.button("Multiply"):
        response = requests.get(
            f"{API_BASE}/multiply",
            params={"a": x, "b": y}
        )
        st.success(f"Result: {response.json()['result']}")
