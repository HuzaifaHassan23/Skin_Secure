import streamlit as st

def show():
    if not st.session_state.get("is_logged_in", False):
        st.warning("Please login first.")
        st.session_state.current_page = "login"
        st.rerun()

    st.title("👤 Profile")
    st.write("Welcome to your profile page.")