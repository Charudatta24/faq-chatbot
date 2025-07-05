import streamlit as st
from ai_generator import get_gemini_response

st.set_page_config(page_title="FAQ AI Chatbot", page_icon="💬")

st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
    }

    .top-left-name {
        position: fixed;
        top: 10px;
        left: 20px;
        font-size: 16px;
        font-weight: bold;
        color: #ffffff;
        background-color: #ff4b4b;
        padding: 10px 15px;
        border-radius: 12px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.2);
        z-index: 9999;
    }

    .typing-title {
        width: 0;
        overflow: hidden;
        white-space: nowrap;
        border-right: 3px solid orange;
        animation: typing 3s steps(40, end) forwards, blink .75s step-end infinite;
        font-size: 2em;
        color: #ff4b4b;
        font-weight: bold;
        margin-bottom: 20px;
    }

    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }

    @keyframes blink {
        from, to { border-color: transparent }
        50% { border-color: orange; }
    }

    .fade-in {
        animation: fadeIn 2s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    div.stButton > button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 12px;
        padding: 0.5em 1em;
        transition: all 0.3s ease;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #ff7e67;
        transform: scale(1.05);
        cursor: pointer;
    }

    .loader {
        width: 100%;
        height: 5px;
        background: linear-gradient(-45deg, #ff4b4b, #fcb69f, #ffe1c5, #ff4b4b);
        background-size: 400% 400%;
        animation: loading 2s ease infinite;
        border-radius: 5px;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    @keyframes loading {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>

    <div class="top-left-name">👤 P.Govinda Charu Datta</div>
""", unsafe_allow_html=True)

st.markdown('<div class="typing-title">💬 AI Chatbot for FAQs</div>', unsafe_allow_html=True)

st.write("Ask me any frequently asked question!")

st.markdown('<div class="fade-in">', unsafe_allow_html=True)
user_input = st.text_area("Type your question here:", height=100)
st.markdown('</div>', unsafe_allow_html=True)

if st.button("Get Answer"):
    if user_input.strip() != "":
        st.markdown('<div class="loader"></div>', unsafe_allow_html=True)
        with st.spinner("Generating answer..."):
            response = get_gemini_response(user_input)
        st.success("Response:")
        st.write(response)
    else:
        st.warning("Please enter a question.")
