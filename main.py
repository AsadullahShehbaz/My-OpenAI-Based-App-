import streamlit as st
from openai import OpenAI

# --- Page Config ---
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# --- Custom CSS Styling ---
st.markdown(
    """
    <style>
        .main-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #6c757d;
            margin-bottom: 20px;
        }
        .stChatMessage {
            border-radius: 12px;
            padding: 12px;
            margin: 5px 0;
        }
        .sidebar-title {
            font-size: 22px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 15px;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            font-size: 14px;
            color: gray;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- App Title ---
st.markdown("<div class='main-title'>🤖 AI Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Built with ❤️ by Asadullah Shehbaz</div>", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.markdown("<div class='sidebar-title'>⚙️ Settings</div>", unsafe_allow_html=True)
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

st.sidebar.markdown("<div class='sidebar-title'>🔗 Connect With Me</div>", unsafe_allow_html=True)
st.sidebar.markdown(
    """
    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="https://www.linkedin.com/in/asadullah-shehbaz-18172a2bb/" target="_blank">
            <img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white">
        </a>
        <a href="https://github.com/AsadullahShehbaz" target="_blank">
            <img src="https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white">
        </a>
        <a href="https://www.kaggle.com/asadullahcreative" target="_blank">
            <img src="https://img.shields.io/badge/-Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white">
        </a>
        <a href="https://web.facebook.com/profile.php?id=61576230402114" target="_blank">
            <img src="https://img.shields.io/badge/-Facebook-1877F2?style=flat-square&logo=facebook&logoColor=white">
        </a>
        <a href="https://www.instagram.com/asad_ullahshehbaz/" target="_blank">
            <img src="https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Initialize OpenAI Client ---
if api_key:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
else:
    st.warning("⚠️ Please enter your API key in the sidebar to start chatting.")
    st.stop()

# --- Chat Memory ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

# --- Display Chat History ---
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- User Input ---
user_prompt = st.chat_input("Type your message...")

if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=st.session_state.messages,
            max_tokens=500,
        )
        reply = response.choices[0].message.content

        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)

    except Exception as e:
        st.error(f"❌ Error: {e}")

# --- Footer ---
st.markdown(
    "<div class='footer'>Made with Streamlit 🚀 | © 2025 Asadullah Shehbaz</div>",
    unsafe_allow_html=True
)
