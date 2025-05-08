import streamlit as st
from chatbot import get_response  # this should take a string and return a string

st.set_page_config(page_title="Car Assistant Chatbot", layout="centered")

st.title("🚗 Car Assistant Chatbot")
st.write("Ask about car features, settings, or common issues.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("You:", "")

# On submit
if user_input:
    st.session_state.chat_history.append(("You", user_input))
    bot_response = get_response(user_input)
    st.session_state.chat_history.append(("Bot", bot_response))

# Display chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**{speaker}:** {message}")
    else:
        # st.markdown(f"<div style='background-color:#f0f0f5; padding:10px; border-radius:5px'><strong>{speaker}:</strong> {message}</div>", unsafe_allow_html=True)
        st.markdown(f"""<div style="background-color:#263238;color:#ffffff;padding:12px;margin:8px 0;border-radius:8px;font-family:Arial;"><strong>{speaker}:</strong><br>{message}</div>""",unsafe_allow_html=True)
