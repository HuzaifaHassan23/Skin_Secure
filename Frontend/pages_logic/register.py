import streamlit as st
import textwrap
from utils.helpers import get_translation
from utils.styles import apply_reg_styles

def show():
    apply_reg_styles()
    
    left, right = st.columns([1, 1.2]) 

    # LEFT SIDE
    with left:
        st.markdown("""
        <div class="card-left" style="height: 100%;">
            <div class="reg-left-title">Join Skin Secure</div>
            <div class="reg-left-sub">Get instant AI-powered skin disease detection</div>
            <div class="check-item">
                <div class="check-circle">✓</div>
                <div class="check-text">Free preliminary analysis</div>
            </div>
            <div class="check-item">
                <div class="check-circle">✓</div>
                <div class="check-text">85% accuracy rate</div>
            </div>
            <div class="check-item">
                <div class="check-circle">✓</div>
                <div class="check-text">Bilingual support (EN/UR)</div>
            </div>
            <div class="check-item">
                <div class="check-circle">✓</div>
                <div class="check-text">Community forum access</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # RIGHT SIDE
    with right:
        # ---------------------------------

        st.markdown(f"""
        <div class="reg-header">
            <h2>{get_translation('create_account')}</h2>
            <div class="reg-header-sub">{get_translation('subtitle')}</div>
        </div>
        """, unsafe_allow_html=True)

        with st.form("register_form", border=False):
            
            name = st.text_input(get_translation('full_name'), placeholder="Babar", key="reg_name")
            
            # CSS automatically shrinks this input via its key
            age = st.text_input(get_translation('age'), placeholder="18", key="reg_age")
            
            email = st.text_input(get_translation('email'), placeholder="SpongBobSquarePants@nick.com", key="reg_email")
            
            password = st.text_input(get_translation('password'), type="password", placeholder="At least 8 characters", key="reg_password")
            
            confirm_password = st.text_input(get_translation('confirm_password'), type="password", placeholder="Re-enter password", key="reg_confirm")
            
            language = st.selectbox(get_translation('preferred_language'), options=["English", "Urdu"], key="reg_language")

            submitted = st.form_submit_button(get_translation('sign_up'), key="reg_submit", use_container_width=True)

            if submitted:
                if name and email and password and password == confirm_password:
                    st.success("Account created successfully!")
                    st.session_state.user_name = name
                    st.session_state.user_email = email
                    st.session_state.user_password = password
                    st.session_state.current_page = "login"
                    st.rerun()
                elif password != confirm_password:
                    st.error("Passwords do not match!")
                else:
                    st.error("Please fill in all fields.")
        
        # Bottom text redirecting to Login
        st.markdown('<div class="login-link-container">Already have an account?</div>', unsafe_allow_html=True)
        if st.button(get_translation('sign_in'), key="login_redirect_btn", use_container_width=True):
            st.session_state.current_page = "login"
            st.rerun()