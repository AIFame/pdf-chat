import streamlit as st

import public
from handlers.userinput import handle_userinput
from .sidebar import sidebar


def home():
    st.write(public.css_index, unsafe_allow_html=True)

    # initial session_state in order to avoid refresh
    if 'conversation' not in st.session_state:
        st.session_state.conversation = None
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    st.header('Chat based on PDF you provided :books:')
    user_question = st.text_input('Ask a question about your documents:')

    if user_question:
        handle_userinput(user_question)

    sidebar()
