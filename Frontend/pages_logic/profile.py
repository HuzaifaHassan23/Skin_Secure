import streamlit as st
import requests
from utils.styles import apply_profile_styles
from utils.helpers import get_profile_translation

def show():
    # Check if user has valid token
    if not st.session_state.get("jwt_token"):
        st.warning("Please login first.")
        st.session_state.is_logged_in = False
        st.session_state.current_page = "login"
        st.rerun()

    apply_profile_styles()
    t = get_profile_translation

    # Page Header Text
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 30px;">
            <h1 style="color: #333; font-weight: 800; font-size: 32px; margin-bottom: 5px;">
                <i class="fas fa-user-circle" style="color: #ff9966;"></i> {t('page_title')}
            </h1>
            <p style="color: #666; font-size: 15px;">{t('page_desc')}</p>
        </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # PROFILE HEADER CARD
    # ---------------------------------------------------------
    # Generate initials from name (e.g., "Ahmad Khan" -> "AK")
    name = st.session_state.get("user_name", "")
    initials = "".join([n[0] for n in name.split() if n])[:2].upper() if name else "US"
    email = st.session_state.get("user_email", "")

    st.markdown(f"""
        <div class="profile-header-card">
            <div class="profile-avatar-large">{initials}</div>
            <div class="profile-header-info">
                <h2>{name}</h2>
                <p><i class="fas fa-envelope"></i> {email}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # PERSONAL INFO FORM
    # ---------------------------------------------------------
    st.markdown(f"""
        <div class="profile-section-card">
            <div class="section-title"><i class="fas fa-id-card"></i> {t('personal_info')}</div>
    """, unsafe_allow_html=True)
    
    with st.form("personal_info_form", border=False):
        c1, c2 = st.columns(2)
        with c1:
            new_name = st.text_input(t('full_name'), value=name)
            new_age = st.text_input(t('age'), value=st.session_state.get("user_age", ""))
            
        with c2:
            new_email = st.text_input(t('email'), value=email)
            lang_index = 0 if st.session_state.get("language", "en") == "en" else 1
            new_lang = st.selectbox(t('language'), ["English", "Urdu"], index=lang_index)

        submit_info = st.form_submit_button(t('update_info_btn'), use_container_width=True)
        
        if submit_info:
            # Prepare API call with only changed fields
            update_payload = {}
            if new_name != name:
                update_payload["name"] = new_name
            if new_email != email:
                update_payload["email"] = new_email
            if new_age and new_age != st.session_state.get("user_age", ""):
                try:
                    update_payload["age"] = int(new_age)
                except ValueError:
                    st.error("Age must be a valid number")
            
            # Map language selection to database value (1=English, 2=Urdu)
            lang_value = 1 if new_lang == "English" else 2
            current_lang = st.session_state.get("language", "en")
            current_lang_value = 1 if current_lang == "en" else 2
            if lang_value != current_lang_value:
                update_payload["preferred_language"] = lang_value
            
            if not update_payload:
                st.info("No changes to save")
            else:
                try:
                    headers = {"Authorization": f"Bearer {st.session_state.jwt_token}"}
                    response = requests.put(
                        "https://skin-secure-api-ufhov.ondigitalocean.app/user/profile",
                        json=update_payload,
                        headers=headers
                    )
                    if response.status_code == 200:
                        data = response.json()
                        # Update session state with new values
                        st.session_state.user_name = data["name"]
                        st.session_state.user_email = data["email"]
                        st.session_state.user_age = str(data["age"]) if data["age"] else ""
                        st.session_state.language = "en" if data["preferred_language"] == 1 else "ur"
                        st.success(t('success_info'))
                        st.rerun()
                    else:
                        error_msg = response.json().get("detail", "Failed to update profile")
                        st.error(f"Error: {error_msg}")
                except requests.exceptions.ConnectionError:
                    st.error("Backend server is not running")
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    st.markdown("</div>", unsafe_allow_html=True) # Close info card

    # ---------------------------------------------------------
    # SECURITY & PASSWORD FORM
    # ---------------------------------------------------------
    st.markdown(f"""
        <div class="profile-section-card">
            <div class="section-title"><i class="fas fa-lock"></i> {t('security')}</div>
    """, unsafe_allow_html=True)

    with st.form("security_form", border=False):
        curr_pass = st.text_input(t('current_pass'), type="password")
        
        c3, c4 = st.columns(2)
        with c3:
            new_pass = st.text_input(t('new_pass'), type="password")
        with c4:
            conf_pass = st.text_input(t('confirm_pass'), type="password")
            
        submit_pass = st.form_submit_button(t('update_pass_btn'), use_container_width=True)
        
        if submit_pass:
            # Validation
            if not curr_pass:
                st.error("Current password is required")
            elif not new_pass:
                st.error("New password is required")
            elif new_pass != conf_pass:
                st.error(t('err_pass_match'))
            elif len(new_pass) < 6:
                st.error("New password must be at least 6 characters")
            else:
                # Send to backend for verification and update
                try:
                    headers = {"Authorization": f"Bearer {st.session_state.jwt_token}"}
                    payload = {
                        "current_password": curr_pass,
                        "new_password": new_pass
                    }
                    response = requests.put(
                        "https://skin-secure-api-ufhov.ondigitalocean.app/user/password",
                        json=payload,
                        headers=headers
                    )
                    if response.status_code == 200:
                        st.success(t('success_pass'))
                    else:
                        error_msg = response.json().get("detail", "Failed to change password")
                        st.error(f"Error: {error_msg}")
                except requests.exceptions.ConnectionError:
                    st.error("Backend server is not running")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
                
    st.markdown("</div>", unsafe_allow_html=True) # Close security card