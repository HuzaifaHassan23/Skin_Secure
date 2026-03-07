import streamlit as st

def apply_index_styles():
    """Apply custom CSS styling exclusively for the Index landing page."""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif !important;
    }
    
    /* FIX: Protect Streamlit's Material Icons from the font override */
    [data-testid="stIconMaterial"] {
        font-family: 'Material Symbols Rounded' !important;
    }
    
    /* 1. App Background matching your image */
    .stApp {
        background-color: #fcebe0;
    }
    /* Hide Streamlit's massive default padding for the landing page */
    [data-testid="stMain"] .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 1200px !important;
    }

    /* Hero Section Buttons */
    .st-key-hero_start button {
        background-color: #2E6FD8 !important;
        color: white !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 0.6rem !important;
        border: none !important;
    }
    .st-key-hero_start button:hover {
        background-color: #1A54B3 !important;
    }

    .st-key-hero_demo button {
        background-color: transparent !important;
        color: #2E6FD8 !important;
        border: 2px solid #2E6FD8 !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 0.6rem !important;
    }
    .st-key-hero_demo button:hover {
        background-color: #f0f5ff !important;
    }

    /* Feature Cards (Why Choose Us) */
    .feature-card {
        background: #FFF9F3;
        padding: 30px;
        border-radius: 18px;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
        height: 100%;
    }
    .feature-card:hover {
        transform: translateY(-8px);
    }

    /* Step Cards (About Section) */
    .step-card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.05);
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .step-number {
        width: 45px;
        height: 45px;
        background: #2E6FD8;
        color: white;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: 700;
        font-size: 18px;
        margin: -22px auto 15px auto;
        border: 4px solid white;
    }
    </style>
    """, unsafe_allow_html=True)

def login_styles():
    """Apply custom CSS styling to match original design."""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif !important;
    }
    
    /* FIX: Protect Streamlit's Material Icons from the font override */
    [data-testid="stIconMaterial"] {
        font-family: 'Material Symbols Rounded' !important;
    }
    
    /* 1. App Background matching your image */
    .stApp {
        background-color: #fcebe0;
    }

    /* 2. Center ONLY the main page, not sidebar */
    /* 2. Fix the Layout, Empty Space & Footer Issue */
    [data-testid="stMain"] .block-container {
        display: flex;
        flex-direction: column; /* Stacks items vertically so footers go at the bottom */
        justify-content: center;
        align-items: center;
        min-height: 85vh; /* Reduced from 100vh to prevent overflow/cutoff */
        padding-top: 3rem;
        padding-bottom: 2rem;
    }

    /* 3. The Login Card Container */
    [data-testid="stMain"] [data-testid="stHorizontalBlock"]:first-of-type {
        background: white;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05);
        max-width: 900px;
        overflow: hidden; /* Clips the background colors to the border radius */
        gap: 0 !important; /* Removes gap between streamlit columns */
    }

    /* 4. Left Column (Peach Background) */
    [data-testid="stMain"] [data-testid="stColumn"]:nth-child(1) {
        background-color: #ffddbe;
        padding: 80px 50px !important;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    /* Left Side Typography */
    .card-left h1 {
        color: #333333;
        font-size: 42px !important;
        font-weight: 800;
        margin-bottom: 10px;
    }
    .card-left-sub {
        font-size: 18px;
        color: #444;
        margin-bottom: 15px;
    }
    .card-left-footer {
        font-size: 13px;
        color: #666;
    }

    /* 5. Right Column (White Background & Form) */
    [data-testid="stMain"] [data-testid="stColumn"]:nth-child(2) {
        padding: 60px 50px !important;
        background: white;
    }

    /* Target the wrapper around your H2 */
    .login-header h2 span {
        font-size: 24px !important;
        color: #333333 !important;
        font-weight: 700;
        padding-bottom: 0px;
        width: 100%;
    }
    
    h2#sign-in-to-skin-secure{
    font-size:2px !important;
    color:#333333 !important;
    font-weight: 700;
    padding-bottom: 0px;
    width: 100%;
    }
    
    h1 span {
        font-size: 36px !important;
        color: #333333 !important;
        font-weight: 700;
        padding-bottom: 0px;
        width: 100%;
    }
    
    h1#skin-secure{
    font-size:36px !important;
    color:#333333 !important;
    font-weight: 700;
    padding-bottom: 0px;
    width: 100%;
    }

    /* FIX: Target ONLY input labels to change their color */
    [data-testid="stWidgetLabel"] p {
        color: #4a4a4a !important; /* Dark gray for labels */
        font-weight: 600;
        font-size: 14px;
    }
    
    /* 1. Change the color of the TYPED text inside the input box */
    [data-testid="stTextInputRootElement"] input {
        color: #4a4a4a !important; /* Change this hex code to whatever color you want */
        font-weight: 500; /* Optional: makes the typed text a bit bolder */
    }

    /* 2. Change the color of the PLACEHOLDER text (e.g., "e.g. user@example.com") */
    [data-testid="stTextInputRootElement"] input::placeholder {
        color: #a0a0a0 !important; /* Usually a lighter gray looks best */
        opacity: 1 !important; /* Ensures the browser doesn't fade it further */
    }

    /* 6. Form & Button Styling */
    [data-testid="stForm"] {
        border: none !important; /* Remove streamlit's default form border */
        padding: 0 !important;
    }

    .st-key-login_email input, .st-key-login_password input {
        width: 100%;
        background-color: #f9f9f9;
        border: 1px solid #ddd;
    }

    .st-key-login_submit button {
        background-color: #fc9466;
        color: white;
        border: none;
        width: 100%;
        padding: 0.6rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 16px;
        margin-top: 10px;
    }
    
    .st-key-login_submit button:hover {
        background-color: #f08354;
        color: white;
    }

    /* Links at bottom */
    .st-key-create_account_btn button {
    background: none;
    border: none;
    color: #2E6FD8;
    text-decoration: underline;
    cursor: pointer;
    padding: 0;
    font: inherit;
    }
    .st-key-create_account_btn button:hover{
    background: none;
    border: none;
    color: #1210a0; 
    text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

def apply_reg_styles():
    """Apply custom CSS styling for the registration page."""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif !important;
    }
    
    /* Protect Material Icons */
    [data-testid="stIconMaterial"] {
        font-family: 'Material Symbols Rounded' !important;
    }
    
    .stApp {
        background-color: #fcebe0;
    }

    /* Container & Layout */
    [data-testid="stMain"] .block-container {
        display: flex;
        flex-direction: column; 
        justify-content: center;
        align-items: center;
        padding-top: 2rem !important; /* Overrides Streamlit's massive default top padding */
        padding-bottom: 1rem !important; /* Overrides Streamlit's massive default bottom padding */
        min-height: 100vh; /* Let it center naturally within the full viewport */
    }

    /* The Card Container */
    [data-testid="stMain"] [data-testid="stHorizontalBlock"]:first-of-type {
        background: white;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05);
        max-width: 950px; /* Slightly wider to accommodate form */
        width: 100%;
        overflow: hidden; 
        gap: 0 !important; 
    }

    /* Left Column (Peach) */
    [data-testid="stMain"] [data-testid="stColumn"]:nth-child(1) {
        background-color: #ffddbe;
        padding: 60px 40px !important;
        display: flex;
        flex-direction: column;
        justify-content: flex-start; /* Aligns content near the top */
    }

    .reg-left-title {
        color: #333333;
        font-size: 38px !important;
        font-weight: 800;
        margin-bottom: 5px;
        line-height: 1.2;
    }
    
    .reg-left-sub {
        font-size: 16px;
        color: #555;
        margin-bottom: 30px;
    }

    /* Custom Checkmarks */
    .check-item {
        display: flex;
        align-items: center;
        margin-bottom: 18px;
    }
    .check-circle {
        background-color: #fc9466;
        color: white;
        border-radius: 50%;
        width: 24px;
        height: 24px;
        min-width: 24px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-right: 12px;
        font-size: 12px;
        font-weight: bold;
    }
    .check-text {
        color: #444;
        font-size: 15px;
    }

    /* Right Column (White) - Added Scrollbar */
    [data-testid="stMain"] [data-testid="stColumn"]:nth-child(2) {
        padding: 40px 50px !important;
        background: white;
        max-height: 650px; /* Forces the internal scrollbar seen in mockup */
        overflow-y: auto;
    }
    
    /* Style the custom scrollbar */
    [data-testid="stMain"] [data-testid="stColumn"]:nth-child(2)::-webkit-scrollbar {
        width: 8px;
    }
    [data-testid="stMain"] [data-testid="stColumn"]:nth-child(2)::-webkit-scrollbar-track {
        background: #f1f1f1; 
        border-radius: 10px;
    }
    [data-testid="stMain"] [data-testid="stColumn"]:nth-child(2)::-webkit-scrollbar-thumb {
        background: #ccc; 
        border-radius: 10px;
    }

    .reg-header h2 {
        font-size: 28px !important;
        color: #333333 !important;
        font-weight: 700;
        margin-bottom: 0px;
        padding-bottom: 5px;
    }
    .reg-header-sub {
        font-size: 14px;
        color: #666;
        margin-bottom: 25px;
    }

    /* Inputs & Labels */
    [data-testid="stWidgetLabel"] p {
        color: #4a4a4a !important; 
        font-weight: 600;
        font-size: 13px;
    }
    
    [data-testid="stTextInputRootElement"] input, 
    [data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        color: #4a4a4a !important; 
        font-weight: 500; 
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 8px;
    }

    [data-testid="stTextInputRootElement"] input::placeholder {
        color: #b3b3b3 !important; 
        opacity: 1 !important; 
    }

    [data-testid="stForm"] {
        border: none !important; 
        padding: 0 !important;
    }

    /* Shrink the Age Input to match mockup */
    .st-key-reg_age {
        width: 80px !important;
    }

    /* Submit Button */
    .st-key-reg_submit button {
        background-color: #fc9466;
        color: white;
        border: none;
        width: 100%;
        padding: 0.6rem;
        border-radius: 8px;
        font-weight: 600;
        font-size: 16px;
        margin-top: 15px;
    }
    
    .st-key-reg_submit button:hover {
        background-color: #f08354;
        color: white;
    }

    /* Login Link Button */
    .login-link-container {
        text-align: center;
        margin-top: 20px;
        font-size: 14px;
        color: #333;
    }
    .st-key-login_redirect_btn button {
        background: none;
        border: none;
        color: #fc9466;
        text-decoration: underline;
        cursor: pointer;
        padding: 0;
        font-weight: 600;
        display: inline;
    }
    .st-key-login_redirect_btn button:hover {
        color: #e07545;
    }
    </style>
    """, unsafe_allow_html=True)