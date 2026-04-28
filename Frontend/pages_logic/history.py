import streamlit as st
import requests
from datetime import datetime

def show():
    if not st.session_state.get("is_logged_in", False):
        st.warning("Please login first.")
        st.session_state.current_page = "login"
        st.rerun()

    st.markdown("<h2 style='text-align: center; color: #333;'>My Scan History</h2>", unsafe_allow_html=True)
    
    headers = {"Authorization": f"Bearer {st.session_state.jwt_token}"}
    
    try:
        response = requests.get("http://127.0.0.1:8000/analyze/history", headers=headers)
        if response.status_code == 200:
            scans = response.json()
            
            if not scans:
                st.info("You haven't performed any skin analyses yet.")
                if st.button("Run your first scan"):
                    st.session_state.current_page = "detection"
                    st.rerun()
                return

            for scan in scans:
                with st.container(border=True):
                    c1, c2 = st.columns([1, 3])
                    with c1:
                        # Fetch the image directly from FastAPI!
                        st.image(f"http://127.0.0.1:8000/{scan['heatmap_path']}", use_container_width=True)
                    with c2:
                        dt = datetime.fromisoformat(scan['created_at'].replace('Z', '+00:00'))
                        st.write(f"**Date:** {dt.strftime('%B %d, %Y - %I:%M %p')}")
                        st.write(f"**Prediction:** {scan['primary_prediction']} ({int(scan['confidence']*100)}%)")
                        st.write(f"**Location:** {scan['body_part']} | **Symptoms:** {scan['symptoms']}")
                        
                        risk_color = "red" if scan['risk_level'] == "high" else "orange" if scan['risk_level'] == "med" else "green"
                        st.markdown(f"**Risk Level:** <span style='color:{risk_color}; font-weight:bold;'>{scan['risk_level'].upper()}</span>", unsafe_allow_html=True)
        else:
            st.error("Failed to fetch history.")
    except Exception as e:
        st.error("Cannot connect to server.")