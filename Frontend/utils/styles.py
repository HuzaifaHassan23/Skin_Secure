import streamlit as st

@st.cache_data
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

@st.cache_data
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
    
@st.cache_data
def apply_dashboard_styles():
    """Apply custom CSS styling exclusively for the Dashboard page."""
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    * {
        font-family: 'Poppins', sans-serif !important;
    }
    /* Protect Material Icons */
    [data-testid="stIconMaterial"] {
        font-family: 'Material Symbols Rounded' !important;
    }
    /* Protect FontAwesome Icons from the global font override */
    .fas, .fa-solid, .fa, .fab {
        font-family: "Font Awesome 6 Free" !important;
        font-weight: 900 !important;
    }
    /* Fix container padding */
    [data-testid="stMain"] .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1200px !important;
    }
    /* App Background */
    .stApp {
        background-color: #fcebe0;
    }
    .section-heading {
        font-size: 22px !important;
        color: #333 !important;
        margin-top: 35px !important;
        margin-bottom: 15px !important;
        font-weight: 700 !important;
    }
    /* Welcome Section */
    .welcome-section {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: white;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
        margin-bottom: 20px;
    }
    .welcome-text h1 {
        font-size: 28px !important;
        color: #333 !important;
        margin-bottom: 5px !important;
        font-weight: 700 !important;
        padding-bottom: 0 !important;
    }
    .welcome-text p {
        font-size: 15px !important;
        color: #666 !important;
        margin: 0 !important;
    }
    .welcome-date {
        display: flex;
        align-items: center;
        gap: 8px;
        color: #999;
        font-size: 14px;
        font-weight: 500;
    }
    /* Stats Cards */
    .stat-card {
        background: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
        display: flex;
        align-items: center;
        gap: 15px;
        transition: all 0.3s;
    }
    .stat-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }
    .stat-icon {
        width: 50px;
        height: 50px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        color: white;
        flex-shrink: 0;
    }
    .stat-icon.blue { background: linear-gradient(135deg, #3b82f6, #2563eb); }
    .stat-icon.green { background: linear-gradient(135deg, #10b981, #059669); }
    .stat-icon.orange { background: linear-gradient(135deg, #f59e0b, #d97706); }
    .stat-icon.purple { background: linear-gradient(135deg, #8b5cf6, #7c3aed); }
    .stat-details h3 {
        font-size: 24px !important;
        color: #333 !important;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1.2 !important;
        font-weight: 700 !important;
    }
    .stat-details p {
        font-size: 13px !important;
        color: #999 !important;
        font-weight: 500 !important;
        margin: 0 !important;
    }
    /* Quick Actions */
    .action-card {
        background: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 10px;
        border: 2px solid transparent;
    }
    .action-card.primary { border-color: #ffddbe; }
    .action-card.secondary { border-color: #e5e7eb; }
    .action-icon {
        width: 50px;
        height: 50px;
        border-radius: 12px;
        background: linear-gradient(135deg, #ff9966, #ff7a33);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        color: white;
        flex-shrink: 0;
    }
    .action-content h3 {
        font-size: 16px !important;
        color: #333 !important;
        margin: 0 0 4px 0 !important;
        padding: 0 !important;
        font-weight: 600 !important;
    }
    .action-content p {
        font-size: 13px !important;
        color: #666 !important;
        margin: 0 !important;
    }
    /* Predictions */
    .prediction-card {
        background: white;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
        border-left: 4px solid #ddd;
        height: 100%;
        margin-bottom: 10px;
    }
    .prediction-card.high-confidence { border-left-color: #10b981; }
    .prediction-card.medium-confidence { border-left-color: #f59e0b; }
    .prediction-card.low-confidence { border-left-color: #ef4444; }
    .prediction-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 16px;
        background: #f9fafb;
    }
    .prediction-badge {
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
    }
    .prediction-badge.high { background: #d1fae5; color: #065f46; }
    .prediction-badge.medium { background: #fef3c7; color: #92400e; }
    .prediction-badge.low { background: #fee2e2; color: #991b1b; }
    .prediction-date { font-size: 12px; color: #999; }
    .prediction-body {
        padding: 16px;
    }
    .prediction-info h3 {
        font-size: 17px !important;
        color: #333 !important;
        margin: 0 0 10px 0 !important;
        font-weight: 700 !important;
    }
    .prediction-info p {
        font-size: 13px !important;
        color: #666 !important;
        margin: 0 0 6px 0 !important;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .prediction-info i {
        color: #999;
        width: 14px;
        text-align: center;
    }
    .remedy-tag {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #d1fae5;
        color: #065f46;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 11px;
        font-weight: 600;
        margin-top: 8px;
    }
    /* Tips */
    .tip-card {
        background: white;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
        text-align: center;
        height: 100%;
        transition: all 0.3s;
    }
    .tip-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }
    .tip-card i {
        font-size: 32px;
        color: #ff9966;
        margin-bottom: 12px;
    }
    .tip-card h4 {
        font-size: 16px !important;
        color: #333 !important;
        margin: 0 0 8px 0 !important;
        font-weight: 600 !important;
    }
    .tip-card p {
        font-size: 13px !important;
        color: #666 !important;
        margin: 0 !important;
        line-height: 1.5 !important;
    }
    /* Streamlit Button Overrides */
    div[data-testid="stButton"] button {
        background-color: white !important;
        color: #fc9466 !important;
        border: 1px solid #fc9466 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stButton"] button:hover {
        background-color: #fc9466 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def apply_detection_styles():
    """Apply custom CSS styling exclusively for the Detection page."""
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    * {
        font-family: 'Poppins', sans-serif !important;
    }
    /* Protect Material Icons */
    [data-testid="stIconMaterial"] {
        font-family: 'Material Symbols Rounded' !important;
    }
    /* Protect FontAwesome Icons */
    .fas, .fa-solid, .fa, .fab {
        font-family: "Font Awesome 6 Free" !important;
        font-weight: 900 !important;
    }
    /* Centered Narrow Container for the Form */
    [data-testid="stMain"] .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 850px !important; 
    }
    .stApp {
        background-color: #fcebe0;
    }
    /* Step Header Styling */
    .step-container {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-top: 10px;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 1px solid #eee;
    }
    .step-circle {
        width: 36px;
        height: 36px;
        background: linear-gradient(135deg, #2E6FD8, #1A54B3);
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 16px;
        flex-shrink: 0;
    }
    .step-title {
        font-size: 20px !important;
        color: #333 !important;
        font-weight: 700 !important;
        margin: 0 !important;
    }
    /* Upload Guidelines Box */
    .upload-guidelines {
        background: #f9fafb;
        border-radius: 12px;
        padding: 20px;
        border-left: 4px solid #ff9966;
        margin-top: 15px;
    }
    .upload-guidelines h4 {
        font-size: 15px !important;
        color: #333 !important;
        margin-bottom: 12px !important;
        font-weight: 600 !important;
    }
    .upload-guidelines ul {
        list-style: none;
        padding-left: 0;
        margin: 0;
    }
    .upload-guidelines li {
        font-size: 13px;
        color: #555;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    /* Medical Disclaimer Box */
    .medical-disclaimer {
        background: #fff3cd;
        color: #856404;
        padding: 15px 20px;
        border-radius: 12px;
        border-left: 5px solid #ffc107;
        font-size: 13px;
        margin-top: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    /* Result Box (Dynamically colored via Streamlit logic later) */
    .result-box {
        background: white;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-top: 20px;
        border: 2px solid #eee;
    }
    /* Streamlit Uploader & Input Overrides */
    [data-testid="stFileUploadDropzone"] {
        background-color: #f8fafc !important;
        border: 2px dashed #cbd5e1 !important;
        border-radius: 16px !important;
        padding: 30px !important;
    }
    [data-testid="stFileUploadDropzone"]:hover {
        border-color: #2E6FD8 !important;
        background-color: #f0f5ff !important;
    }
    /* Analyze Button */
    .st-key-analyze_btn button {
        background-color: #fc9466 !important;
        color: white !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 0.8rem !important;
        border: none !important;
        width: 100%;
        font-size: 16px !important;
        margin-top: 20px !important;
    }
    .st-key-analyze_btn button:hover {
        background-color: #e07a50 !important;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def apply_community_styles():
    """Apply custom CSS styling exclusively for the Community page."""
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    * {
        font-family: 'Poppins', sans-serif !important;
    }
    /* Protect Material Icons */
    [data-testid="stIconMaterial"] {
        font-family: 'Material Symbols Rounded' !important;
    }
    .fas, .fa-solid, .fa, .fab {
        font-family: "Font Awesome 6 Free" !important;
        font-weight: 900 !important;
    }
    /* Centered Narrow Container */
    [data-testid="stMain"] .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 900px !important; 
    }
    .stApp {
        background-color: #fcebe0;
    }
    /* For text */
    p, .stMarkdown p, .stText p {
        color: #4b5563 !important; 
    }
    /* Post Card Styling */
    .post-card {
        background: white;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        border-left: 4px solid #ff9966;
        transition: transform 0.2s ease;
    }
    .post-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    }
    .post-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 15px;
    }
    .post-avatar {
        width: 42px;
        height: 42px;
        border-radius: 50%;
        background: linear-gradient(135deg, #ffddbe, #ffc7a3);
        color: #d95a1c;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 16px;
    }
    .post-author {
        font-weight: 600;
        color: #333;
        font-size: 15px;
        margin: 0;
        line-height: 1.2;
    }
    .post-date {
        color: #999;
        font-size: 12px;
        margin: 0;
    }
    .post-tag {
        background: #f3f4f6;
        color: #4b5563;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 11px;
        font-weight: 600;
        margin-left: auto;
    }
    
    .post-title {
        font-size: 18px !important;
        font-weight: 700 !important;
        color: #333 !important;
        margin: 0 0 10px 0 !important;
    }
    .post-content {
        color: #555 !important;
        font-size: 14px !important;
        line-height: 1.6 !important;
        margin-bottom: 0 !important;
    }
    .post-footer {
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px solid #f0f0f0;
        display: flex;
        gap: 20px;
        color: #666;
        font-size: 13px;
        font-weight: 500;
    }
    .post-footer i {
        color: #ff9966;
        margin-right: 5px;
    }
    /* Submit Button Override */
    .st-key-submit_post button {
        background-color: #fc9466 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.5rem !important;
        border: none !important;
        width: 100%;
    }
    .st-key-submit_post button:hover {
        background-color: #e07a50 !important;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def apply_profile_styles():
    """Apply custom CSS styling exclusively for the Profile page."""
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    * {
        font-family: 'Poppins', sans-serif !important;
    }
    /* Protect Material Icons */
    [data-testid="stIconMaterial"] {
        font-family: 'Material Symbols Rounded' !important;
    }
    .fas, .fa-solid, .fa, .fab {
        font-family: "Font Awesome 6 Free" !important;
        font-weight: 900 !important;
    }
    /* Centered Narrow Container */
    [data-testid="stMain"] .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 850px !important; 
    }
    .stApp {
        background-color: #fcebe0;
    }
    /* For text */
    p, .stMarkdown p, .stText p {
        color: #4b5563 !important; 
    }
    /* Profile Header Card */
    .profile-header-card {
        background: white;
        border-radius: 16px;
        padding: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 30px;
        border-left: 4px solid #2E6FD8;
    }
    .profile-avatar-large {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: linear-gradient(135deg, #2E6FD8, #1A54B3);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 32px;
        box-shadow: 0 4px 10px rgba(46, 111, 216, 0.3);
    }
    .profile-header-info h2 {
        margin: 0 !important;
        color: #333 !important;
        font-weight: 700 !important;
        font-size: 24px !important;
    }
    .profile-header-info p {
        margin: 5px 0 0 0 !important;
        color: #666 !important;
        font-size: 15px !important;
    }
    /* Section Cards */
    .profile-section-card {
        background: white;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 18px !important;
        font-weight: 600 !important;
        color: #333 !important;
        margin-bottom: 20px !important;
        display: flex;
        align-items: center;
        gap: 10px;
        border-bottom: 2px solid #f0f0f0;
        padding-bottom: 10px;
    }
    .section-title i {
        color: #ff9966;
    }
    /* Form Buttons */
    div[data-testid="stFormSubmitButton"] button {
        background-color: #fc9466 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.6rem !important;
        border: none !important;
        width: 100%;
        margin-top: 10px;
    }
    div[data-testid="stFormSubmitButton"] button:hover {
        background-color: #e07a50 !important;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def apply_results_styles():
    """Apply custom CSS styling exclusively for the Results page."""
    st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * { font-family: 'Poppins', sans-serif !important; }
    .fas, .fa-solid, .fa, .fab { font-family: "Font Awesome 6 Free" !important; font-weight: 900 !important; }
    
    [data-testid="stMain"] .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1000px !important; 
    }
    .stApp { background-color: #fcebe0; }
    /* Main Result Banner */
    .result-banner {
        border-radius: 16px;
        padding: 30px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .banner-high { background: linear-gradient(135deg, #ef4444, #dc2626); }
    .banner-med { background: linear-gradient(135deg, #f59e0b, #d97706); }
    .banner-low { background: linear-gradient(135deg, #10b981, #059669); }
    .result-banner h1 { font-size: 32px !important; margin: 10px 0 !important; color: white !important; font-weight: 800 !important; }
    .severity-badge {
        background: rgba(255,255,255,0.2);
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 14px;
        display: inline-block;
    }
    /* Content Cards */
    .info-card {
        background: white;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        margin-bottom: 20px;
        height: 100%;
    }
    .card-header {
        font-size: 18px !important;
        font-weight: 700 !important;
        color: #333 !important;
        margin-bottom: 20px !important;
        display: flex;
        align-items: center;
        gap: 10px;
        border-bottom: 2px solid #f0f0f0;
        padding-bottom: 10px;
    }
    .card-header i { color: #ff9966; }
    /* Remedy List */
    .remedy-item {
        background: #f9fafb;
        border-left: 4px solid #2E6FD8;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .remedy-item.urgent { border-left-color: #ef4444; background: #fef2f2; }
    .remedy-item h4 { margin: 0 0 5px 0 !important; color: #333 !important; font-size: 15px !important; font-weight: 600 !important;}
    .remedy-item p { margin: 0 !important; color: #666 !important; font-size: 13px !important; }
    /* Buttons */
    div[data-testid="stButton"] button {
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.6rem !important;
        width: 100%;
    }</style>""", unsafe_allow_html=True)