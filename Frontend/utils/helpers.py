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
            "view_details": "View Details",
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
            "view_details": "تفصیلات دیکھیں",
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
        
def get_detection_translation(key: str) -> str:
    """Specific translations for the Detection page."""
    translations = {
        "en": {
            "page_title": "Skin Disease Detection",
            "page_desc": "Upload an image and provide details for AI-powered preliminary analysis",
            "step1_title": "Upload Skin Image",
            "step1_desc": "Please upload a clear, well-lit photo of the affected area",
            "guide_title": "Photo Guidelines",
            "guide1": "Good lighting (avoid shadows)",
            "guide2": "Close-up of affected area",
            "guide3": "Clear and in-focus",
            "guide4": "Avoid filters or edits",
            "step2_title": "Select Affected Body Part",
            "step2_desc": "Indicate where the issue is located",
            "body_part_placeholder": "-- Select Body Part --",
            "step3_title": "Describe Your Symptoms",
            "step3_desc": "Select all symptoms that apply",
            "analyze_btn": "Analyze Skin Condition",
            "disclaimer_title": "Important Disclaimer",
            "disclaimer_text": "This is a preliminary AI-powered analysis and should not replace professional medical advice. Please consult a licensed dermatologist for accurate diagnosis and treatment.",
            "results_title": "Analysis Results",
            "custom_prompt": "Please specify:"
        },
        "ur": {
            "page_title": "جلد کی بیماری کی تشخیص",
            "page_desc": "AI سے ابتدائی تجزیہ کے لیے تصویر اپ لوڈ کریں اور تفصیلات فراہم کریں",
            "step1_title": "جلد کی تصویر اپ لوڈ کریں",
            "step1_desc": "براہ کرم متاثرہ علاقے کی واضح، اچھی روشنی والی تصویر اپ لوڈ کریں",
            "guide_title": "تصویر کی ہدایات",
            "guide1": "اچھی روشنی (سائے سے بچیں)",
            "guide2": "متاثرہ علاقے کا کلوز اپ",
            "guide3": "واضح اور فوکس میں",
            "guide4": "فلٹرز یا ترمیم سے بچیں",
            "step2_title": "متاثرہ جسم کا حصہ منتخب کریں",
            "step2_desc": "بتائیں کہ مسئلہ کہاں ہے",
            "body_part_placeholder": "-- جسم کا حصہ منتخب کریں --",
            "step3_title": "اپنی علامات بیان کریں",
            "step3_desc": "تمام لاگو علامات منتخب کریں",
            "analyze_btn": "جلد کی حالت کا تجزیہ کریں",
            "disclaimer_title": "اہم اعلان",
            "disclaimer_text": "یہ AI سے چلنے والا ابتدائی تجزیہ ہے اور پیشہ ورانہ طبی مشورے کی جگہ نہیں لے سکتا۔ درست تشخیص اور علاج کے لیے براہ کرم لائسنس یافتہ ماہر امراض جلد سے مشورہ کریں۔",
            "results_title": "تجزیہ کے نتائج",
            "custom_prompt": "براہ کرم وضاحت کریں:"
        }
    }
    lang = st.session_state.get("language", "en")
    return translations.get(lang, translations["en"]).get(key, key)

def get_community_translation(key: str) -> str:
    """Specific translations for the Community page."""
    translations = {
        "en": {
            "page_title": "Community Forum",
            "page_desc": "Connect, share experiences, and support each other in a safe space.",
            "create_btn": "✍️ Create a New Post",
            "post_title": "Post Title",
            "post_content": "Share your thoughts or experiences...",
            "post_anon": "Post Anonymously",
            "publish_btn": "Publish Post",
            "recent_posts": "Recent Discussions",
            "success_msg": "Your post has been published!",
            "empty_err": "Please fill out both the title and content."
        },
        "ur": {
            "page_title": "کمیونٹی فورم",
            "page_desc": "ایک محفوظ جگہ پر جڑیں، تجربات شیئر کریں اور ایک دوسرے کا ساتھ دیں۔",
            "create_btn": "✍️ نئی پوسٹ بنائیں",
            "post_title": "پوسٹ کا عنوان",
            "post_content": "اپنے خیالات یا تجربات شیئر کریں...",
            "post_anon": "گمنام طور پر پوسٹ کریں",
            "publish_btn": "پوسٹ شائع کریں",
            "recent_posts": "حالیہ مباحثے",
            "success_msg": "آپ کی پوسٹ شائع ہو گئی ہے!",
            "empty_err": "براہ کرم عنوان اور مواد دونوں کو پُر کریں۔"
        }
    }
    lang = st.session_state.get("language", "en")
    return translations.get(lang, translations["en"]).get(key, key)

def get_profile_translation(key: str) -> str:
    """Specific translations for the Profile page."""
    translations = {
        "en": {
            "page_title": "My Profile",
            "page_desc": "Manage your personal information and account settings.",
            "personal_info": "Personal Information",
            "update_info_btn": "Update Information",
            "full_name": "Full Name",
            "email": "Email Address",
            "age": "Age",
            "language": "Preferred Language",
            "security": "Security & Password",
            "current_pass": "Current Password",
            "new_pass": "New Password",
            "confirm_pass": "Confirm New Password",
            "update_pass_btn": "Update Password",
            "success_info": "Personal information updated successfully!",
            "success_pass": "Password updated successfully!",
            "err_pass_match": "New passwords do not match!",
            "err_pass_wrong": "Current password is incorrect."
        },
        "ur": {
            "page_title": "میری پروفائل",
            "page_desc": "اپنی ذاتی معلومات اور اکاؤنٹ کی ترتیبات کا نظم کریں۔",
            "personal_info": "ذاتی معلومات",
            "update_info_btn": "معلومات اپ ڈیٹ کریں",
            "full_name": "پورا نام",
            "email": "ای میل ایڈریس",
            "age": "عمر",
            "language": "ترجیحی زبان",
            "security": "سیکیورٹی اور پاس ورڈ",
            "current_pass": "موجودہ پاس ورڈ",
            "new_pass": "نیا پاس ورڈ",
            "confirm_pass": "نئے پاس ورڈ کی تصدیق کریں",
            "update_pass_btn": "پاس ورڈ اپ ڈیٹ کریں",
            "success_info": "ذاتی معلومات کامیابی سے اپ ڈیٹ ہو گئیں!",
            "success_pass": "پاس ورڈ کامیابی سے اپ ڈیٹ ہو گیا!",
            "err_pass_match": "نئے پاس ورڈ آپس میں نہیں ملتے!",
            "err_pass_wrong": "موجودہ پاس ورڈ غلط ہے۔"
        }
    }
    lang = st.session_state.get("language", "en")
    return translations.get(lang, translations["en"]).get(key, key)