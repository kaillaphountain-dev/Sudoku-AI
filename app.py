import streamlit as st
from groq import Groq

# --- 1. CONFIGURATION & BRANDING ---
st.set_page_config(page_title="Sudoku AI", page_icon="∞", layout="centered")

# Professional UI Styling
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .publisher-info { font-size: 14px; color: #00ffa2; font-weight: bold; }
    .logo-text { font-size: 40px; font-weight: 800; margin-bottom: 0px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR (The "About" Section) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>∞</h2>", unsafe_allow_html=True)
    st.title("Sudoku AI")
    st.markdown("---")
    st.markdown("**Publisher:**")
    st.markdown("<div class='publisher-info'>NotMewMine</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.info("Sudoku is a high-performance LLM designed for advanced reasoning, coding, and creative tasks.")

# --- 3. MAIN INTERFACE ---
st.markdown("<div class='logo-text'>∞ Sudoku</div>", unsafe_allow_html=True)
st.caption("Powered by Advanced Neural Inference")

# --- 4. API SETUP ---
# Replace with your actual Groq Key
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# --- 5. CHAT LOGIC ---
if "messages" not in st.session_state:
    # This "System" message tells the AI who it is!
    st.session_state.messages = [
        {"role": "system", "content": "You are Sudoku, an advanced AI assistant published by NotMewMine. You are as capable as Claude Pro. Be concise, intelligent, and helpful."}
    ]

# Display chat history (excluding the system message)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask Sudoku..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response from Groq
    with st.chat_message("assistant"):
        try:
            chat_completion = client.chat.completions.create(
                # We use Llama 3 70B for "Claude Pro" level intelligence
                messages=st.session_state.messages,
                model="llama-3.3-70b-versatile",
                stream=True,
            )

            full_response = ""
            placeholder = st.empty()

            for chunk in chat_completion:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    placeholder.markdown(full_response + "▌")

            placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"Connection Error: {e}"
# See the space here?
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
