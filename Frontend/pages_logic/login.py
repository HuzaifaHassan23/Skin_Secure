from urllib import response

import requests
import streamlit as st
from utils.helpers import get_translation, COLORS, init_session_state
from utils.styles import login_styles

def show():
    login_styles()
    
    # --- MAIN LAYOUT ---
    left, right = st.columns([1, 1.1]) # Adjusted ratio to give right side slightly more room

    # LEFT SIDE
    with left:
        st.markdown("""
        <div class="card-left">
            <h1>Skin Secure</h1>
            <div class="card-left-sub">Your AI-powered preliminary skin check system.</div>
            <div class="card-left-footer">Private • Fast • Bilingual Support</div>
        </div>
        """, unsafe_allow_html=True)

    # RIGHT SIDE
    with right:
        # Wrap the heading in our custom class to target it safely
        st.markdown(f"""
        <div class="login-header">
            <h2>{get_translation("sign_in")}</h2>
        </div>
        """, unsafe_allow_html=True)

        # border=False is available in newer versions of Streamlit to remove the box
        with st.form("login_form", border=False):
            email = st.text_input(get_translation("email"), key="login_email")
            password = st.text_input(get_translation("password"), type="password", key="login_password")

            submitted = st.form_submit_button(get_translation("login"), key="login_submit", use_container_width=True)

            if submitted:
                payload = {
                    "email": email,
                    "password": password
                }
                try:
                    response = requests.post("http://127.0.0.1:8000/login", json=payload)
                    if response.status_code == 200:
                        data = response.json()
                        
                        # Store JWT token (the proof of login)
                        st.session_state.jwt_token = data["access_token"]
                        
                        # Store user info
                        st.session_state.is_logged_in = True
                        st.session_state.user_email = data["user"]["email"]
                        st.session_state.user_name = data["user"]["name"]
                        st.session_state.user_age = data["user"]["age"]
                        st.session_state.language = data["user"]["preferred_language"]
                        
                        st.session_state.current_page = "dashboard"
                        st.success("✅ Login successful!")
                        st.rerun()
                    else:
                        try:
                            error_msg = response.json().get("detail", "Login failed")
                        except:
                            error_msg = f"Login failed (Status {response.status_code})"
                        st.error(f"⚠️ {error_msg}")
                except requests.exceptions.ConnectionError:
                    st.error("⚠️ Backend server is not running.")
                    
        # Put the links OUTSIDE the form so they don't trigger form validation
        if st.button(get_translation("create_account"), key="create_account_btn"):
            st.session_state.current_page = "register"
            st.rerun()
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True) # Spacer at the bottom        
