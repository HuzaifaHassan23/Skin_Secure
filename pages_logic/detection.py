import streamlit as st
import time
from PIL import Image
from utils.styles import apply_detection_styles
from utils.helpers import get_detection_translation, get_translation

def show():
    if not st.session_state.get("is_logged_in", False):
        st.warning("Please login first.")
        st.session_state.current_page = "login"
        st.rerun()

    apply_detection_styles()

    # Define a quick helper function for translation inside this file
    t = get_detection_translation

    # Page Header
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 30px;">
            <h1 style="color: #333; font-weight: 800; font-size: 32px; margin-bottom: 5px;">
                <i class="fas fa-microscope" style="color: #ff9966;"></i> {t('page_title')}
            </h1>
            <p style="color: #666; font-size: 15px;">{t('page_desc')}</p>
        </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # STEP 1: IMAGE UPLOAD
    # ---------------------------------------------------------
    st.markdown(f"""
        <div class="step-container">
            <div class="step-circle">1</div>
            <div>
                <h2 class="step-title">{t('step1_title')}</h2>
                <p style="color: #666; font-size: 13px; margin: 0;">{t('step1_desc')}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose an image (JPG, PNG)", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

    # Guidelines Card
    st.markdown(f"""
        <div class="upload-guidelines">
            <h4><i class="fas fa-info-circle" style="color: #ff9966;"></i> {t('guide_title')}</h4>
            <ul>
                <li><i class="fas fa-check" style="color: #10b981;"></i> {t('guide1')}</li>
                <li><i class="fas fa-check" style="color: #10b981;"></i> {t('guide2')}</li>
                <li><i class="fas fa-check" style="color: #10b981;"></i> {t('guide3')}</li>
                <li><i class="fas fa-check" style="color: #10b981;"></i> {t('guide4')}</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.markdown("<br>", unsafe_allow_html=True)
        st.image(image, caption="Uploaded Image", width=250)

        # ---------------------------------------------------------
        # STEP 2 & 3: DETAILS
        # ---------------------------------------------------------
        st.markdown(f"""
            <div class="step-container" style="margin-top: 30px;">
                <div class="step-circle">2</div>
                <div>
                    <h2 class="step-title">{t('step2_title')} & {t('step3_title')}</h2>
                </div>
            </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        
        with col1:
            body_part = st.selectbox("Body Location", [
                t('body_part_placeholder'), "Face", "Neck", "Chest", "Back", 
                "Left Arm", "Right Arm", "Left Leg", "Right Leg", "Other"
            ], label_visibility="collapsed")
            
            # Logic for "Other" Body Part
            custom_body_part = ""
            if body_part == "Other":
                custom_body_part = st.text_input(t('custom_prompt'), key="custom_body")

        with col2:
            symptoms = st.multiselect("Symptoms", [
                "Itching", "Redness", "Swelling", "Pain", "Bleeding", 
                "Scaling/Peeling", "Changes in color/size", "Other"
            ], label_visibility="collapsed", placeholder=t('step3_desc'))
            
            # Logic for "Other" Symptom
            custom_symptom = ""
            if "Other" in symptoms:
                custom_symptom = st.text_input(t('custom_prompt'), key="custom_symp")

        # ---------------------------------------------------------
        # STEP 4: ANALYZE BUTTON & LOGIC
        # ---------------------------------------------------------
        if st.button(t('analyze_btn'), key="analyze_btn"):
            if body_part == t('body_part_placeholder'):
                st.error("Please select a body location before analyzing.")
            else:
                # --- NATIVE STREAMLIT LOADING OVERLAY ---
                with st.status("🤖 AI model processing...", expanded=True) as status:
                    st.write("✓ Image preprocessed")
                    time.sleep(1) # Simulating step 1
                    
                    st.write("⏳ Analyzing features...")
                    time.sleep(1.5) # Simulating step 2 (Drop AI model logic here)
                    
                    st.write("✓ Generating results and heatmap")
                    time.sleep(1)
                    
                    status.update(label="Analysis Complete!", state="complete", expanded=False)

                # DUMMY RESULTS
                prediction = "Melanoma (High Risk)"
                confidence = 0.87
                is_high_risk = True 

                # --- SHOW RESULTS UI ---
                st.markdown(f"""
                    <div class="step-container" style="margin-top: 40px;">
                        <div class="step-circle">3</div>
                        <h2 class="step-title">{t('results_title')}</h2>
                    </div>
                """, unsafe_allow_html=True)

                box_color = "#fee2e2" if is_high_risk else "#d1fae5" 
                text_color = "#991b1b" if is_high_risk else "#065f46" 
                icon = "⚠️" if is_high_risk else "✅"

                st.markdown(f"""
                    <div class="result-box" style="border-left: 6px solid {text_color}; background-color: {box_color};">
                        <h3 style="color: {text_color}; margin-top: 0; font-size: 18px;">{icon} Predicted Condition: <b>{prediction}</b></h3>
                        <p style="color: #555; margin-bottom: 5px; font-size: 14px;">AI Confidence Score:</p>
                    </div>
                """, unsafe_allow_html=True)
                
                st.progress(confidence, text=f"{int(confidence * 100)}% Match")

                if st.button(get_translation("view_details"), key="view_1", use_container_width=True):
                    st.info("Navigating to details...") # Placeholder logic
                st.markdown("<br><p style='font-weight: 600; color: #333; font-size: 14px;'>AI Focus Map (Grad-CAM):</p>", unsafe_allow_html=True)
                st.image(image, caption="Areas the AI focused on", width=300)

        # Disclaimer
        st.markdown(f"""
            <div class="medical-disclaimer">
                <i class="fas fa-exclamation-triangle" style="font-size: 20px;"></i>
                <div>
                    <strong>{t('disclaimer_title')}:</strong> {t('disclaimer_text')}
                </div>
            </div>
        """, unsafe_allow_html=True)