"""Utility functions for Skin Secure app."""
import streamlit as st
from datetime import datetime

# Color scheme matching original design
COLORS = {
    "primary": "#2E6FD8",
    "accent": "#FF9966",
    "success": "#10b981",
    "background": "#FFF5ED",
    "surface": "#FFF9F3",
    "text": "#333333",
    "text_light": "#666666",
}

def init_session_state():
    """Initialize session state variables."""
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = False
    if "user_name" not in st.session_state:
        st.session_state.user_name = None
    if "user_email" not in st.session_state:
        st.session_state.user_email = None
    if "user_password" not in st.session_state:
        st.session_state.user_password = None
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Index"
    if "language" not in st.session_state:
        st.session_state.language = "en"

def get_translation(key, lang="en"):
    """Get translated text."""
    translations = {
        "en": {
            "app_title": "Skin Secure - AI Skin Disease Detection",
            "subtitle": "Start your skin health journey today",
            "features": "Why Choose Skin Secure?",
            "about": "About Skin Secure",
            "login": "Login",
            "get_started": "Get Started",
            "logout": "Logout",
            "dashboard": "Dashboard",
            "detection": "Detection",
            "community": "Community",
            "profile": "Profile",
            "welcome": "Welcome",
            "sign_in": "Sign in to Skin Secure",
            "email": "Email",
            "password": "Password",
            "confirm_password": "Confirm Password",
            "create_account": "Create Your Account",
            "full_name": "Full Name",
            "preferred_language": "Preferred Language",
            "sign_up": "Sign Up",
            "upload_image": "Upload Skin Image",
            "age": "Age",
            "body_location": "Body Location",
            "predict": "Analyze Image",
            "my_profile": "My Profile",
            "edit_profile": "Edit Profile",
            "account_settings": "Account Settings",
        },
        "ur": {
            "app_title": "اسکن سیکور - ایل جلد کی بیماری کی شناخت",
            "subtitle": "آج ہی اپنے جلد کی صحت کا سفر شروع کریں",
            "features": "اسکن سیکور کیوں منتخب کریں؟",
            "about": "اسکن سیکور کے بارے میں",
            "login": "لاگ ان",
            "get_started": "شروع کریں",
            "logout": "لاگ آؤٹ",
            "dashboard": "ڈیش بورڈ",
            "detection": "شناخت",
            "community": "کمیونٹی",
            "profile": "پروفائل",
            "welcome": "خوش آمدید",
            "sign_in": "اسکن سیکور میں سائن ان کریں",
            "email": "ای میل",
            "password": "پاس ورڈ",
            "confirm_password": "پاس ورڈ کی تصدیق کریں",
            "create_account": "اپنا اکاؤنٹ بنائیں",
            "full_name": "پورا نام",
            "preferred_language": "ترجیحی زبان",
            "sign_up": "سائن اپ",
            "upload_image": "جلد کی تصویر اپ لوڈ کریں",
            "age": "عمر",
            "body_location": "جسم کا مقام",
            "predict": "تصویر کا تجزیہ کریں",
            "my_profile": "میری پروفائل",
            "edit_profile": "پروفائل میں ترمیم کریں",
            "account_settings": "اکاؤنٹ سیٹنگز",
        }
    }
    lang_to_use = st.session_state.get("language", "en")
    result = translations.get(lang_to_use, {}).get(key, key)
    return str(result) if result else key

    
def display_header_logo():
    """Display header with logo and navigation context."""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write("🏥 **Skin Secure**")

def display_footer():
    """Display footer."""
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption("© 2025 Skin Secure")
    with col2:
        st.caption("All Rights Reserved")
    with col3:
        st.caption("Privacy • Contact • About")