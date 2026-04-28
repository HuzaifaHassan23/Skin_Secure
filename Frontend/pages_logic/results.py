import streamlit as st
import textwrap
import base64
from utils.styles import apply_results_styles
from utils.helpers import get_results_translation

def show():
    # Check if user has valid token
    if not st.session_state.get("jwt_token"):
        st.session_state.is_logged_in = False
        st.session_state.current_page = "login"
        st.rerun()

    apply_results_styles()
    t = get_results_translation

    # Fetch real data from session state
    result_data = st.session_state.get("latest_result")
    
    # If a user refreshes the page or comes here directly without analyzing, send them back
    if not result_data or "error" in result_data:
        st.warning("No recent analysis found. Please run a new scan.")
        st.session_state.current_page = "detection"
        st.rerun()

    # Page Header
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="color: #333; font-weight: 800; font-size: 28px; margin-bottom: 5px;">{t('page_title')}</h1>
        <p style="color: #666; font-size: 14px;">{t('page_desc')}</p>
        </div>""", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # TOP BANNER: DIAGNOSIS
    # ---------------------------------------------------------
    # Determine styles based on real risk level from AI
    if result_data["risk_level"] == "high":
        banner_class = "banner-high"
        icon = "fa-exclamation-triangle"
        severity_text = t("severity_high")
    elif result_data["risk_level"] == "med":
        banner_class = "banner-med"
        icon = "fa-exclamation-circle"
        severity_text = t("severity_med")
    else:
        banner_class = "banner-low"
        icon = "fa-check-circle"
        severity_text = t("severity_low")

    st.markdown(f"""
        <div class="result-banner {banner_class}">
        <div class="severity-badge"><i class="fas {icon}"></i> {severity_text}</div>
        <h1>{result_data['prediction']}</h1>
        <p style="margin:0; opacity: 0.9;">{t('confidence')}: {int(result_data['confidence'] * 100)}%</p>
        </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 2-COLUMN LAYOUT (Details vs Remedies)
    # ---------------------------------------------------------
    col1, col2 = st.columns([1, 1.2], gap="large")

    with col1:
        # Details & Top 3 Predictions Card
        st.markdown("""
            <div class="info-card">
            <div class="card-header"><i class="fas fa-microscope"></i> AI Confidence Breakdown</div>
            <p style="color:#666; font-size: 13px; margin-bottom: 10px;">The AI analyzed your image against 7 skin conditions. Here are the top 3 most likely matches:</p>
        """, unsafe_allow_html=True)
        
        # Dynamically loop through the top 3 predictions
        for pred in result_data.get("top_3", []):
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; margin-bottom: 5px; border-bottom: 1px solid #eee; padding-bottom: 5px;">
                <span style="color:#333; font-weight: 500;">{pred['name']}</span>
                <span style="color:#666;">{int(pred['confidence'] * 100)}%</span>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("</div>", unsafe_allow_html=True)

        # Heatmap Card
        st.markdown(f"""
            <div class="info-card">
            <div class="card-header"><i class="fas fa-layer-group"></i> {t('heatmap_title')}</div>
            <p style="color:#666; font-size: 13px; margin-bottom: 10px;">The red areas highlight exactly what the AI focused on to make its decision.</p>
        """, unsafe_allow_html=True)
        
        # Decode the Base64 image directly into Streamlit!
        if "heatmap_base64" in result_data:
            img_bytes = base64.b64decode(result_data["heatmap_base64"])
            st.image(img_bytes, use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        # Dynamic Remedies Card
        remedy = result_data.get("remedies", {})
        
        st.markdown(f"""
            <div class="info-card">
            <div class="card-header"><i class="fas fa-notes-medical"></i> {t('remedy_title')}</div>    
            
            <div class="remedy-item urgent">
                <h4><i class="fas fa-user-md"></i> {remedy.get('action', 'Seek Medical Advice')}</h4>
                <p>{remedy.get('description', 'Please consult a healthcare professional for an accurate diagnosis.')}</p>
            </div>
            
            <div class="remedy-item">
                <h4><i class="fas fa-leaf"></i> {t('home_care')}</h4>
                <p>{remedy.get('home_care', 'Keep the area clean, dry, and protected from the sun.')}</p>
            </div>
            
            </div>
        """, unsafe_allow_html=True)

        # Action Buttons
        b1, b2 = st.columns(2)
        with b1:
            if st.button(t('back_detect'), type="secondary", use_container_width=True):
                st.session_state.current_page = "detection"
                st.rerun()
        with b2:
            # Backend already saved this, so we can use this button to navigate elsewhere!
            if st.button("Share in Community", type="primary", use_container_width=True):
                st.session_state.current_page = "community"
                st.rerun()