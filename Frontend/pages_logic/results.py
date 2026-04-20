import streamlit as st
import textwrap
from utils.styles import apply_results_styles
from utils.helpers import get_results_translation

def show():
    if not st.session_state.get("is_logged_in", False):
        st.session_state.current_page = "login"
        st.rerun()

    apply_results_styles()
    t = get_results_translation

    # Fetch data from session state (or use dummy data if accessed directly)
    result_data = st.session_state.get("latest_result", {
        "prediction": "Melanoma",
        "confidence": 0.87,
        "risk_level": "high",  # 'high', 'med', 'low'
        "body_part": "Left Arm",
        "symptoms": ["Itching", "Dark Spots", "Changes in color/size"],
        "image": "assets/symptoms.png" # Placeholder
    })

    # Page Header
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="color: #333; font-weight: 800; font-size: 28px; margin-bottom: 5px;">{t('page_title')}</h1>
        <p style="color: #666; font-size: 14px;">{t('page_desc')}</p>
        </div>""", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # TOP BANNER: DIAGNOSIS
    # ---------------------------------------------------------
    # Determine styles based on risk level
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
        st.markdown(f"""
            <div class="info-card">
            <div class="card-header"><i class="fas fa-microscope"></i> {t('details_title')}</div>
            <p style="color:#333"><strong>{t('body_part')}:</strong> {result_data['body_part']}</p>
            <p style="color:#333"><strong>{t('symptoms')}:</strong> {", ".join(result_data['symptoms'])}</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div class="info-card">
            <div class="card-header"><i class="fas fa-layer-group"></i> {t('heatmap_title')}</div>
        """, unsafe_allow_html=True)
        # Use Streamlit's native image renderer for the heatmap
        st.image(result_data['image'], use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="info-card">
            <div class="card-header"><i class="fas fa-notes-medical"></i> {t('remedy_title')}</div>    
            <div class="remedy-item urgent">
            <h4><i class="fas fa-user-md"></i> {t('see_doctor')}</h4>
            <p>{t('see_doctor_desc')}</p>
            </div>
            <div class="remedy-item">
            <h4><i class="fas fa-leaf"></i> {t('home_care')}</h4>
            <p>• Avoid direct sunlight on the affected area.<br>
            • Do not scratch or pick at the skin.<br>
            • Keep the area clean and dry.</p>
            </div>
            <div class="remedy-item">
            <h4><i class="fas fa-pills"></i> Pharmacy Solutions</h4>
            <p>Over-the-counter hydrocortisone cream may provide temporary relief for itching, but <b>do not</b> apply if the skin is broken or bleeding.</p>
            </div>
            </div>
        """, unsafe_allow_html=True)

        # Action Buttons
        b1, b2 = st.columns(2)
        with b1:
            if st.button(t('back_detect'), type="secondary"):
                st.session_state.current_page = "detection"
                st.rerun()
        with b2:
            if st.button(t('save_history'), type="primary"):
                st.success("Saved to your database history!")