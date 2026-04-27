import streamlit as st
import textwrap
from datetime import datetime
from utils.styles import apply_dashboard_styles
from utils.helpers import get_translation

def show():
    # Check if user has valid token
    if not st.session_state.get("jwt_token"):
        st.warning("Please login first.")
        st.session_state.is_logged_in = False
        st.session_state.current_page = "login"
        st.rerun()

    # Apply the beautiful new CSS
    apply_dashboard_styles()

    # Dynamic variables
    user_name = st.session_state.get("user_name", "User")
    current_date = datetime.now().strftime("%A, %B %d, %Y")

    # ========================= WELCOME SECTION =========================
    st.markdown(textwrap.dedent(f"""
        <div class="welcome-section">
            <div class="welcome-text">
                <h1>Welcome back, {user_name}! 👋</h1>
                <p>Here's your skin health overview</p>
            </div>
            <div class="welcome-date">
                <i class="fas fa-calendar"></i>
                <span>{current_date}</span>
            </div>
        </div>
    """), unsafe_allow_html=True)

    # ========================= STATS SECTION =========================
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown(textwrap.dedent("""
            <div class="stat-card">
                <div class="stat-icon blue"><i class="fas fa-chart-line"></i></div>
                <div class="stat-details">
                    <h3>5</h3>
                    <p>Total Scans</p>
                </div>
            </div>
        """), unsafe_allow_html=True)
    with s2:
        st.markdown(textwrap.dedent("""
            <div class="stat-card">
                <div class="stat-icon green"><i class="fas fa-bullseye"></i></div>
                <div class="stat-details">
                    <h3>87%</h3>
                    <p>Avg. Confidence</p>
                </div>
            </div>
        """), unsafe_allow_html=True)
    with s3:
        st.markdown(textwrap.dedent("""
            <div class="stat-card">
                <div class="stat-icon orange"><i class="fas fa-clock"></i></div>
                <div class="stat-details">
                    <h3>2 days</h3>
                    <p>Last Scan</p>
                </div>
            </div>
        """), unsafe_allow_html=True)
    with s4:
        st.markdown(textwrap.dedent("""
            <div class="stat-card">
                <div class="stat-icon purple"><i class="fas fa-comments"></i></div>
                <div class="stat-details">
                    <h3>12</h3>
                    <p>Community Posts</p>
                </div>
            </div>
        """), unsafe_allow_html=True)

    # ========================= QUICK ACTIONS =========================
    st.markdown("<h3 class='section-heading'>Quick Actions</h3>", unsafe_allow_html=True)
    q1, q2 = st.columns(2)
    with q1:
        st.markdown(textwrap.dedent("""
            <div class="action-card primary">
                <div class="action-icon"><i class="fas fa-microscope"></i></div>
                <div class="action-content">
                    <h3>Start New Analysis</h3>
                    <p>Upload image and get instant results</p>
                </div>
            </div>
        """), unsafe_allow_html=True)
        # Using Streamlit buttons right below the cards for pure functionality!
        if st.button("Go to Detection", key="btn_detect", use_container_width=True):
            st.session_state.current_page = "detection"
            st.rerun()
            
    with q2:
        st.markdown(textwrap.dedent("""
            <div class="action-card secondary">
                <div class="action-icon" style="background: linear-gradient(135deg, #a8a29e, #78716c);"><i class="fa-solid fa-building-columns"></i></div>
                <div class="action-content">
                    <h3>See History</h3>
                    <p>Check previous diagnoses and results</p>
                </div>
            </div>
        """), unsafe_allow_html=True)
        if st.button("Go to History", key="btn_history", use_container_width=True):
            st.session_state.current_page = "community"
            st.rerun()

    # ========================= PREDICTIONS SECTION =========================
    st.markdown("<h3 class='section-heading'>Recent Predictions</h3>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    
    with p1:
        st.markdown(textwrap.dedent("""
            <div class="prediction-card high-confidence">
                <div class="prediction-header">
                    <div class="prediction-badge high"><i class="fas fa-check-circle"></i> High Confidence</div>
                    <span class="prediction-date">Dec 5, 2024</span>
                </div>
                <div class="prediction-body">
                    <div class="prediction-info">
                        <h3>Melanoma</h3>
                        <p><i class="fas fa-map-marker-alt"></i> Left Arm</p>
                        <p><i class="fas fa-notes-medical"></i> Itching, Dark spot</p>
                    </div>
                </div>
            </div>
        """), unsafe_allow_html=True)
        if st.button(get_translation("view_details"), key="view_1", use_container_width=True):
            st.info("Navigating to details...") # Placeholder logic

    with p2:
        st.markdown(textwrap.dedent("""
            <div class="prediction-card medium-confidence">
                <div class="prediction-header">
                    <div class="prediction-badge medium"><i class="fas fa-exclamation-circle"></i> Medium Confidence</div>
                    <span class="prediction-date">Nov 28, 2024</span>
                </div>
                <div class="prediction-body">
                    <div class="prediction-info">
                        <h3>Acne Vulgaris</h3>
                        <p><i class="fas fa-map-marker-alt"></i> Face (Forehead)</p>
                        <p><i class="fas fa-notes-medical"></i> Redness, Inflammation</p>
                    </div>
                </div>
            </div>
        """), unsafe_allow_html=True)
        if st.button(get_translation("view_details"), key="view_2", use_container_width=True):
            st.info("Navigating to details...")

    with p3:
        st.markdown(textwrap.dedent("""
            <div class="prediction-card low-confidence">
                <div class="prediction-header">
                    <div class="prediction-badge low"><i class="fas fa-info-circle"></i> Low Confidence</div>
                    <span class="prediction-date">Nov 15, 2024</span>
                </div>
                <div class="prediction-body">
                    <div class="prediction-info">
                        <h3>Uncertain Analysis</h3>
                        <p><i class="fas fa-map-marker-alt"></i> Right Hand</p>
                        <p><i class="fas fa-notes-medical"></i> Dry skin, Mild redness</p>
                        <div class="remedy-tag"><i class="fas fa-leaf"></i> Home remedy suggested</div>
                    </div>
                </div>
            </div>
        """), unsafe_allow_html=True)
        if st.button(get_translation("view_details"), key="view_3", use_container_width=True):
            st.info("Navigating to details...")

    # ========================= HEALTH TIPS =========================
    st.markdown("""
                <h3 class='section-heading'><i class="fas fa-lightbulb" style="color: #ff9966;"></i> Health Tips</h3>
                """, unsafe_allow_html=True)
    t1, t2, t3 = st.columns(3)
    
    with t1:
        st.markdown(textwrap.dedent("""
            <div class="tip-card">
                <i class="fas fa-sun"></i>
                <h4>Sun Protection</h4>
                <p>Always use sunscreen with SPF 30+ when going outdoors</p>
            </div>
        """), unsafe_allow_html=True)
    with t2:
        st.markdown(textwrap.dedent("""
            <div class="tip-card">
                <i class="fas fa-tint"></i>
                <h4>Stay Hydrated</h4>
                <p>Drink 8 glasses of water daily for healthy skin</p>
            </div>
        """), unsafe_allow_html=True)
    with t3:
        st.markdown(textwrap.dedent("""
            <div class="tip-card">
                <i class="fas fa-heartbeat"></i>
                <h4>Regular Check-ups</h4>
                <p>Visit a dermatologist annually for skin screening</p>
            </div>
        """), unsafe_allow_html=True)