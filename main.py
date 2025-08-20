import streamlit as st
from openai import OpenAI

# --- Set page config ---
st.set_page_config(page_title="AI Assistant", page_icon="🤖", layout="centered")

# --- App title ---
st.title("🤖 Chatbot by Asadullah Shehbaz")

api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# --- Initialize OpenAI client ---
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# --- Chat input and memory ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]

# --- Display chat history ---
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Input from user ---
user_prompt = st.chat_input("Type your message...")

if user_prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })
    with st.chat_message("user"):
        st.markdown(user_prompt)

    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=st.session_state.messages,
            max_tokens=500,
        )
        reply = response.choices[0].message.content

        st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })
        with st.chat_message("assistant"):
            st.markdown(reply)

    except Exception as e:
        st.error(f"❌ Error: {e}")

 # --- Connect With Me Section ---
st.sidebar.markdown("### 🔗 Connect With Me")

st.sidebar.markdown(
    """
    <div style="display: flex; gap: 15px; flex-wrap: wrap;">
        <a href="https://www.linkedin.com/in/asadullah-shehbaz-18172a2bb/" target="_blank">
            <img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white">
        </a>
        <a href="https://github.com/AsadullahShehbaz" target="_blank">
            <img src="https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
        </a>
        <a href="https://www.kaggle.com/asadullahcreative" target="_blank">
            <img src="https://img.shields.io/badge/-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white">
        </a>
        <a href="https://web.facebook.com/profile.php?id=61576230402114" target="_blank">
            <img src="https://img.shields.io/badge/-Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white">
        </a>
        <a href="https://www.instagram.com/asad_ullahshehbaz/" target="_blank">
            <img src="https://img.shields.io/badge/-Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)