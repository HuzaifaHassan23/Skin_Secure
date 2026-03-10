import streamlit as st
from utils.styles import apply_profile_styles
from utils.helpers import get_profile_translation

def show():
    if not st.session_state.get("is_logged_in", False):
        st.warning("Please login first.")
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
    name = st.session_state.get("user_name", "User")
    initials = "".join([n[0] for n in name.split() if n])[:2].upper()
    email = st.session_state.get("user_email", "user@example.com")

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
            # Pre-filled with current data
            new_name = st.text_input(t('full_name'), value=name)
            # Defaulting age to empty string if not set, ready for DB implementation
            new_age = st.text_input(t('age'), value=st.session_state.get("user_age", "")) 
            
        with c2:
            new_email = st.text_input(t('email'), value=email)
            # Get current language index for default selection
            lang_index = 0 if st.session_state.get("language", "en") == "en" else 1
            new_lang = st.selectbox(t('language'), ["English", "Urdu"], index=lang_index)

        submit_info = st.form_submit_button(t('update_info_btn'), use_container_width=True)
        
        if submit_info:
            # TODO: BACKEND DB UPDATE HERE
            # db.execute("UPDATE users SET name=?, email=?, age=? WHERE id=?", ...)
            
            # Update Session State
            st.session_state.user_name = new_name
            st.session_state.user_email = new_email
            st.session_state.user_age = new_age
            st.session_state.language = "en" if new_lang == "English" else "ur"
            st.success(t('success_info'))
            st.rerun() # Refresh to update the UI immediately

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
            current_saved_pass = st.session_state.get("user_password", "")
            
            # TODO: Replace this with bcrypt check against Database
            if curr_pass != current_saved_pass and current_saved_pass != "":
                st.error(t('err_pass_wrong'))
            elif new_pass != conf_pass:
                st.error(t('err_pass_match'))
            elif len(new_pass) < 6:
                st.error("New password must be at least 6 characters.")
            else:
                # TODO: Hash new password and save to DB
                st.session_state.user_password = new_pass
                st.success(t('success_pass'))
                
    st.markdown("</div>", unsafe_allow_html=True) # Close security card