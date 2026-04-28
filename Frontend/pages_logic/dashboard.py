import streamlit as st
import textwrap
import requests
from datetime import datetime, timezone
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

    # ========================= FETCH REAL DATA =========================
    headers = {"Authorization": f"Bearer {st.session_state.jwt_token}"}
    API_URL = "http://127.0.0.1:8000"

    scans = []
    total_posts = 0

    try:
        # Fetch User's Scan History
        res_scans = requests.get(f"{API_URL}/analyze/history", headers=headers)
        if res_scans.status_code == 200:
            scans = res_scans.json()
            
        # Fetch Community Posts (to show total platform activity)
        res_posts = requests.get(f"{API_URL}/community/posts", headers=headers)
        if res_posts.status_code == 200:
            total_posts = len(res_posts.json())
    except requests.exceptions.ConnectionError:
        st.error("⚠️ Backend server is offline. Showing cached/empty data.")

    # ========================= CALCULATE STATS =========================
    total_scans = len(scans)
    avg_confidence = int(sum(s['confidence'] for s in scans) / total_scans * 100) if total_scans > 0 else 0
    
    last_scan_text = "No scans yet"
    if total_scans > 0:
        # Safely parse UTC time from database
        last_dt_str = scans[0]['created_at']
        if last_dt_str.endswith('Z'):
            last_dt_str = last_dt_str[:-1] + '+00:00'
        last_dt = datetime.fromisoformat(last_dt_str)
        if last_dt.tzinfo is None:
            last_dt = last_dt.replace(tzinfo=timezone.utc)
            
        # Calculate time difference
        diff = datetime.now(timezone.utc) - last_dt
        if diff.days > 0:
            last_scan_text = f"{diff.days} days ago"
        elif diff.seconds >= 3600:
            last_scan_text = f"{diff.seconds // 3600} hrs ago"
        elif diff.seconds >= 60:
            last_scan_text = f"{diff.seconds // 60} mins ago"
        else:
            last_scan_text = "Just now"

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
        st.markdown(textwrap.dedent(f"""
            <div class="stat-card">
                <div class="stat-icon blue"><i class="fas fa-chart-line"></i></div>
                <div class="stat-details">
                    <h3>{total_scans}</h3>
                    <p>Total Scans</p>
                </div>
            </div>
        """), unsafe_allow_html=True)
    with s2:
        st.markdown(textwrap.dedent(f"""
            <div class="stat-card">
                <div class="stat-icon green"><i class="fas fa-bullseye"></i></div>
                <div class="stat-details">
                    <h3>{avg_confidence}%</h3>
                    <p>Avg. Confidence</p>
                </div>
            </div>
        """), unsafe_allow_html=True)
    with s3:
        st.markdown(textwrap.dedent(f"""
            <div class="stat-card">
                <div class="stat-icon orange"><i class="fas fa-clock"></i></div>
                <div class="stat-details">
                    <h3 style="font-size: 1.2rem; margin-top: 5px;">{last_scan_text}</h3>
                    <p>Last Scan</p>
                </div>
            </div>
        """), unsafe_allow_html=True)
    with s4:
        st.markdown(textwrap.dedent(f"""
            <div class="stat-card">
                <div class="stat-icon purple"><i class="fas fa-comments"></i></div>
                <div class="stat-details">
                    <h3>{total_posts}</h3>
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
        # Fixed: Now routes to history instead of community!
        if st.button("Go to History", key="btn_history", use_container_width=True):
            st.session_state.current_page = "history"
            st.rerun()

    # ========================= PREDICTIONS SECTION =========================
    st.markdown("<h3 class='section-heading'>Recent Predictions</h3>", unsafe_allow_html=True)
    
    if total_scans == 0:
        st.info("You haven't run any AI scans yet. Head over to the Detection page to get started!")
    else:
        # Create up to 3 columns
        recent_3 = scans[:3]
        cols = st.columns(3)
        
        for i, scan in enumerate(recent_3):
            with cols[i]:
                # Determine styling based on AI confidence
                conf = scan['confidence']
                if conf >= 0.8:
                    conf_class = "high-confidence"
                    badge_class = "high"
                    icon = "fa-check-circle"
                    text = "High Confidence"
                elif conf >= 0.5:
                    conf_class = "medium-confidence"
                    badge_class = "medium"
                    icon = "fa-exclamation-circle"
                    text = "Medium Confidence"
                else:
                    conf_class = "low-confidence"
                    badge_class = "low"
                    icon = "fa-info-circle"
                    text = "Low Confidence"

                # Parse date nicely
                dt_str = scan['created_at'].replace('Z', '+00:00')
                dt = datetime.fromisoformat(dt_str)
                display_date = dt.strftime("%b %d, %Y")

                st.markdown(textwrap.dedent(f"""
                    <div class="prediction-card {conf_class}">
                        <div class="prediction-header">
                            <div class="prediction-badge {badge_class}"><i class="fas {icon}"></i> {text}</div>
                            <span class="prediction-date">{display_date}</span>
                        </div>
                        <div class="prediction-body">
                            <div class="prediction-info">
                                <h3>{scan['primary_prediction']}</h3>
                                <p><i class="fas fa-map-marker-alt"></i> {scan['body_part']}</p>
                                <p><i class="fas fa-notes-medical"></i> {scan['symptoms'][:25]}...</p>
                            </div>
                        </div>
                    </div>
                """), unsafe_allow_html=True)
                
                # Dynamic key prevents Streamlit duplicate key errors
                if st.button("View Image", key=f"view_{scan['id']}", use_container_width=True):
                    # We can navigate them straight to the history page where all images are visible!
                    st.session_state.current_page = "history"
                    st.rerun()

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