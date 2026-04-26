"""Skin Secure - AI Skin Disease Detection Landing Page."""
import streamlit as st
import pathlib
import base64
import os
import textwrap
from utils.helpers import init_session_state, get_translation, COLORS
from pages_logic import dashboard, detection, community, profile, login, register, results
from utils.styles import apply_index_styles

# Page config
st.set_page_config(
    page_title="Skin Secure - AI Skin Disease Detection",
    page_icon="🏥",
    layout="wide" ,
)

#load CSS
@st.cache_data
def load_css(file_path):
    with open(file_path) as f:
        return f.read()

#load external CSS

BASE_DIR = pathlib.Path(__file__).parent
css_path = BASE_DIR/"style.css"
st.markdown(f"""<style>{load_css(css_path)}</style>""", unsafe_allow_html=True)

# ------------------------
# Initialize Session State
# ------------------------

init_session_state()

# ------------------------
# Sidebar Navigation
# ------------------------

@st.cache_data
def get_logo():
    return f"{BASE_DIR}/assets/logo.PNG"

if st.session_state.is_logged_in:
    st.sidebar.image(get_logo(), width=150)
    st.sidebar.write(f"👤 {st.session_state.user_name}")
    st.sidebar.divider()

    if st.sidebar.button("🏠 Dashboard"):
        st.session_state.current_page = "dashboard"

    if st.sidebar.button("🔍 Detection"):
        st.session_state.current_page = "detection"

    if st.sidebar.button("👥 Community"):
        st.session_state.current_page = "community"

    if st.sidebar.button("👤 Profile"):
        st.session_state.current_page = "profile"
    if st.sidebar.button("About Us"):
        st.session_state.current_page = "Index"

    st.sidebar.divider()

    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.session_state.current_page = "login"
        st.rerun()

    # --- SIDEBAR LANGUAGE TOGGLE ---
    st.sidebar.divider()
    st.sidebar.markdown("**🌐 Language**")
    
    # Get current language to set the default radio selection
    current_lang = st.session_state.get("language", "en")
    default_index = 0 if current_lang == "en" else 1
    
    selected_lang = st.sidebar.radio(
        "Select Language", 
        options=["EN", "UR"], 
        index=default_index,
        horizontal=True,
        label_visibility="collapsed" # Hides the label to make it look cleaner
    )
    
    # Map the selection to the session state variable
    lang_map = {"EN": "en", "UR": "ur"}
    if lang_map[selected_lang] != current_lang:
        st.session_state.language = lang_map[selected_lang]
        st.rerun() # Refresh page immediately to apply language
    # -------------------------------
else:
    st.sidebar.image(get_logo(), width=150)
    st.sidebar.write("Your skin, Protected")
    st.sidebar.divider()
    if st.sidebar.button(" Sign In  ", key="login_btn"):
            st.session_state.current_page = "login"
            st.rerun()
    if st.sidebar.button("Register", key="register_btn"):
            st.session_state.current_page = "register"
            st.rerun()
            
    # --- SIDEBAR LANGUAGE TOGGLE ---
    st.sidebar.divider()
    st.sidebar.markdown("**🌐 Language**")
    
    # Get current language to set the default radio selection
    current_lang = st.session_state.get("language", "en")
    default_index = 0 if current_lang == "en" else 1
    
    selected_lang = st.sidebar.radio(
        "Select Language", 
        options=["EN", "UR"], 
        index=default_index,
        horizontal=True,
        label_visibility="collapsed" # Hides the label to make it look cleaner
    )
    
    # Map the selection to the session state variable
    lang_map = {"EN": "en", "UR": "ur"}
    if lang_map[selected_lang] != current_lang:
        st.session_state.language = lang_map[selected_lang]
        st.rerun() # Refresh page immediately to apply language
    # -------------------------------

# ------------------------
# Page Components
# ------------------------

@st.cache_data
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

def show():
    apply_index_styles()
    
    cap_img = get_base64(f"{BASE_DIR}/assets/capture.png")
    sym_img = get_base64(f"{BASE_DIR}/assets/symptoms.png")
    res_img = get_base64(f"{BASE_DIR}/assets/result.png")
    demo_webp_b64 = get_base64(f"{BASE_DIR}/assets/demo.webp")
        

    # ========================= HERO SECTION =========================
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1.2], gap="large")
    
    with col1:
        st.markdown("""
            <div style="padding-top: 50px;">
                <h1 style="font-size: 54px; font-weight: 800; color: #333; margin-bottom: 0px; line-height: 1.1;">Skin Secure</h1>
                <h2 style="font-size: 20px; font-weight: 600; color: #555; margin-top: 15px; margin-bottom: 30px;">AI-Powered Skin Disease Detection</h2>
            </div>
        """, unsafe_allow_html=True)
        
        b1, b2, _ = st.columns([1, 1, 0.5])
        with b1:
            if st.button("🔍 Start Free Analysis", key="hero_start", use_container_width=True):
                st.session_state.current_page = "login"
                st.rerun()
        with b2:
            st.button("▶️ Watch Demo", key="hero_demo", use_container_width=True)
            
    with col2:
        
        st.markdown(f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                <img src="data:image/webp;base64,{demo_webp_b64}" 
                    style="width: 100%; max-width: 550px; border-radius: 20px; box-shadow: 0 20px 40px rgba(46, 111, 216, 0.15);" 
                    alt="Skin Secure App Demo">
            </div>
        """, unsafe_allow_html=True)
        
    # ========================= FEATURES SECTION =========================
    st.markdown("<h2 style='text-align: center; margin-top: 90px; margin-bottom: 40px; color: #333; font-weight: 700;'>Why Choose Skin Secure?</h2>", unsafe_allow_html=True)
    f1, f2, f3 = st.columns(3, gap="large")
    
    with f1:
        st.markdown(textwrap.dedent("""
            <div class="feature-card">
                <div style="font-size: 45px; text-align: center; margin-bottom: 10px;">🤖</div>
                <h3 style="text-align: center; color: #333; font-size: 20px; margin-bottom: 5px;">AI Diagnosis</h3>
                <p style="text-align: center; color: #666; font-size: 14px;">Deep learning powered classification trained on HAM10000 dataset.</p>
            </div>
        """), unsafe_allow_html=True)
    
    with f2:
        st.markdown(textwrap.dedent("""
            <div class="feature-card">
                <div style="font-size: 45px; text-align: center; margin-bottom: 10px;">🌐</div>
                <h3 style="text-align: center; color: #333; font-size: 20px; margin-bottom: 5px;">Bilingual</h3>
                <p style="text-align: center; color: #666; font-size: 14px;">Supports both English & Urdu for wider accessibility.</p>
            </div>
        """), unsafe_allow_html=True)
    
    with f3:
        st.markdown(textwrap.dedent("""
            <div class="feature-card">
                <div style="font-size: 45px; text-align: center; margin-bottom: 10px;">👥</div>
                <h3 style="text-align: center; color: #333; font-size: 20px; margin-bottom: 5px;">Community Forum</h3>
                <p style="text-align: center; color: #666; font-size: 14px;">Connect with people, share symptoms, and engage safely.</p>
            </div>
        """), unsafe_allow_html=True)
    
    # ========================= ABOUT SECTION =========================
    st.markdown("<h2 style='text-align: center; margin-top: 100px; color: #333; font-weight: 700;'>About Skin Secure</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="max-width: 850px; margin: 0 auto 50px auto; color: #555; font-size: 15px; line-height: 1.6;">
        <p style="text-align: center;">
            Skin Secure is a web-based, AI-powered digital health platform designed 
            to provide preliminary diagnosis for skin diseases. It is specifically tailored 
            for the Pakistani context, aiming to bridge the gap between 
            patients and limited dermatological resources.
        </p>
        <ul style="margin-top: 15px;">
            <li><b>Core Goal:</b> To accurately classify skin diseases from user-uploaded images and provide "explainable" results.</li>
            <li><b>Key Differentiator:</b> Unlike standard black-box AI, your system builds trust by using Grad-CAM heatmaps to visually show where the AI is looking on the skin.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    s1, s2, s3 = st.columns(3, gap="large")
    
    with s1:
        st.markdown(textwrap.dedent(f"""
            <div class="step-card">
                <img src="data:image/png;base64,{cap_img}" style="width: 100%; border-radius: 12px; object-fit: cover; height: 180px;">
                <div class="step-number">1</div>
                <h3 style="text-align: center; color: #2E6FD8; font-size: 18px; margin-top: 5px; margin-bottom: 5px;">Upload Image</h3>
                <p style="text-align: center; color: #666; font-size: 14px;">Capture or upload an image of the affected skin area.</p>
            </div>
        """), unsafe_allow_html=True)
    
    with s2:
        st.markdown(textwrap.dedent(f"""
            <div class="step-card">
                <img src="data:image/png;base64,{sym_img}" style="width: 100%; border-radius: 12px; object-fit: cover; height: 180px;">
                <div class="step-number">2</div>
                <h3 style="text-align: center; color: #2E6FD8; font-size: 18px; margin-top: 5px; margin-bottom: 5px;">Select Symptoms</h3>
                <p style="text-align: center; color: #666; font-size: 14px;">Choose signs like redness, itching, or swelling.</p>
            </div>
        """), unsafe_allow_html=True)
    
    with s3:
        st.markdown(textwrap.dedent(f"""
            <div class="step-card">
                <img src="data:image/png;base64,{res_img}" style="width: 100%; border-radius: 12px; object-fit: cover; height: 180px;">
                <div class="step-number">3</div>
                <h3 style="text-align: center; color: #2E6FD8; font-size: 18px; margin-top: 5px; margin-bottom: 5px;">AI Analyze</h3>
                <p style="text-align: center; color: #666; font-size: 14px;">Get disease prediction with heatmap visualization.</p>
            </div>
        """), unsafe_allow_html=True)
    
    # ========================= STATS SECTION =========================
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FFE5D0 0%, #FFD5B8 100%); padding: 50px 0; margin-top: 100px; margin-bottom: 50px; border-radius: 20px; box-shadow: 0 10px 30px rgba(255, 153, 102, 0.15);">
        <div style="display: flex; justify-content: space-around; text-align: center;">
            <div>
                <div style="font-size: 54px; font-weight: 800; color: #2E6FD8; line-height: 1;">500</div>
                <div style="color: #444; font-weight: 600; font-size: 16px; margin-top: 5px;">Users Trust Us</div>
            </div>
            <div>
                <div style="font-size: 54px; font-weight: 800; color: #2E6FD8; line-height: 1;">85</div>
                <div style="color: #444; font-weight: 600; font-size: 16px; margin-top: 5px;">Accuracy (%)</div>
            </div>
            <div>
                <div style="font-size: 54px; font-weight: 800; color: #2E6FD8; line-height: 1;">7</div>
                <div style="color: #444; font-weight: 600; font-size: 16px; margin-top: 5px;">Diseases Covered</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------------
# Page Router
# ------------------------

if st.session_state.current_page == "login":
    login.show()

elif st.session_state.current_page == "register":
    register.show()

elif st.session_state.current_page == "dashboard":
    dashboard.show()

elif st.session_state.current_page == "detection":
    detection.show()

elif st.session_state.current_page == "community":
    community.show()

elif st.session_state.current_page == "profile":
    profile.show()

elif st.session_state.current_page == "results": 
    results.show()

elif st.session_state.current_page == "Index":
    show()
    
st.divider()
# Footer
st.markdown("""
<div class="footer">
© 2025 Skin Secure | All Rights Reserved | <span> Privacy • Contact • About </span>
</div>
""", unsafe_allow_html=True)
