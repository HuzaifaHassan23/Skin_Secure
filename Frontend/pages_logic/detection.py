import streamlit as st
import time
from PIL import Image
from utils.styles import apply_detection_styles
from utils.helpers import get_detection_translation, get_translation
import requests 


def show():
    # Check if user has valid token
    if not st.session_state.get("jwt_token"):
        st.warning("Please login first.")
        st.session_state.is_logged_in = False
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
        submit_btn = st.button(t('analyze_btn'), key="analyze_btn", use_container_width=True)

        if submit_btn:
            # 1. Validate that they uploaded an image
            if not uploaded_file:
                st.error("⚠️ Please upload an image first.")
            elif body_part == t('body_part_placeholder'):
                st.error("⚠️ Please select a body location before analyzing.")
            else:
                with st.spinner("🤖 AI is analyzing your skin... Please wait..."):
                    try:
                        # 2. Prepare the data to send to FastAPI
                        headers = {"Authorization": f"Bearer {st.session_state.jwt_token}"}
                        
                        # Files go in the 'files' parameter for requests
                        files = {
                            "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
                        }
                        
                        # Form data goes in the 'data' parameter
                        payload = {
                            "body_part": body_part,
                            "symptoms": ", ".join(symptoms) if symptoms else "None"
                        }
                        
                        # 3. Make the API Call to your new endpoint
                        response = requests.post(
                            "https://skin-secure-api-ufhov.ondigitalocean.app/analyze", 
                            files=files, 
                            data=payload, 
                            headers=headers
                        )
                        
                        # 4. Handle the Response
                        if response.status_code == 200:
                            # Save the entire JSON response into session state so Results page can see it
                            st.session_state.latest_result = response.json()
                            
                            st.success("Analysis Complete!")
                            
                            # Automatically redirect the user to the Results page
                            st.session_state.current_page = "results"
                            st.rerun()
                        else:
                            # If the backend crashed or returned an error
                            error_msg = response.json().get("detail", "Analysis failed.")
                            st.error(f"⚠️ Server Error: {error_msg}")
                            
                    except requests.exceptions.ConnectionError:
                        st.error("⚠️ Backend server is offline. Please start FastAPI.")
                    except Exception as e:
                        st.error(f"⚠️ An unexpected error occurred: {str(e)}")

        # Disclaimer
        st.markdown(f"""
            <div class="medical-disclaimer">
                <i class="fas fa-exclamation-triangle" style="font-size: 20px;"></i>
                <div>
                    <strong>{t('disclaimer_title')}:</strong> {t('disclaimer_text')}
                </div>
            </div>
        """, unsafe_allow_html=True)