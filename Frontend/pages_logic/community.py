import streamlit as st
import textwrap
from utils.styles import apply_community_styles
from utils.helpers import get_community_translation

def show():
    if not st.session_state.get("is_logged_in", False):
        st.warning("Please login first.")
        st.session_state.current_page = "login"
        st.rerun()

    apply_community_styles()
    t = get_community_translation

    # Page Header
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 30px;">
            <h1 style="color: #333; font-weight: 800; font-size: 32px; margin-bottom: 5px;">
                <i class="fas fa-users" style="color: #ff9966;"></i> {t('page_title')}
            </h1>
            <p style="color: #666; font-size: 15px;">{t('page_desc')}</p>
        </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # CREATE NEW POST SECTION
    # ---------------------------------------------------------
    with st.expander(t('create_btn'), expanded=False):
        with st.form("new_post_form", border=False):
            title = st.text_input(t('post_title'), placeholder="e.g. My experience with early detection")
            content = st.text_area(t('post_content'), height=150)
            
            col1, col2 = st.columns([3, 1])
            with col1:
                is_anonymous = st.checkbox(t('post_anon'))
            with col2:
                submitted = st.form_submit_button(t('publish_btn'), key="submit_post")
                
            if submitted:
                if title and content:
                    # TODO: BACKEND LOGIC HERE
                    # e.g., db.add(Post(title=title, content=content, author=st.session_state.user_id))
                    # db.commit()
                    st.success(t('success_msg'))
                else:
                    st.error(t('empty_err'))

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # COMMUNITY FEED SECTION (Ready for Database!)
    # ---------------------------------------------------------
    st.markdown(f"<h3 style='color: #333; font-weight: 700; margin-bottom: 20px;'>{t('recent_posts')}</h3>", unsafe_allow_html=True)

    # MOCK DATABASE DATA (Replace this with actual DB query later)
    mock_posts = [
        {
            "id": 1,
            "author": "Sarah M.",
            "initials": "SM",
            "date": "2 hours ago",
            "tag": "Story",
            "title": "Don't ignore the small changes!",
            "content": "I noticed a strange mole last month and decided to use this app. It flagged it as medium risk. I finally went to the dermatologist yesterday, and they caught it just in time! Always listen to your body and get checked.",
            "likes": 24,
            "comments": 5
        },
        {
            "id": 2,
            "author": "Anonymous",
            "initials": "AN",
            "date": "5 hours ago",
            "tag": "Question",
            "title": "How accurate is the Grad-CAM heatmap?",
            "content": "I just did a scan and the heatmap highlights an area slightly off from my actual redness. Has anyone else experienced this? Should I retake the photo in better lighting?",
            "likes": 8,
            "comments": 12
        },
        {
            "id": 3,
            "author": "Dr. Ahmed (Verified)",
            "initials": "DA",
            "date": "1 day ago",
            "tag": "Advice",
            "title": "A quick tip about photo lighting",
            "content": "Just a friendly reminder to the community: when taking photos for the AI, make sure you are in natural daylight if possible. Yellow indoor bulbs can sometimes mess with the color detection of redness and rashes.",
            "likes": 156,
            "comments": 18
        }
    ]

    # Render the Feed
    for post in mock_posts:
        st.markdown(textwrap.dedent(f"""
            <div class="post-card">
                <div class="post-header">
                    <div class="post-avatar">{post['initials']}</div>
                    <div>
                        <p class="post-author">{post['author']}</p>
                        <p class="post-date">{post['date']}</p>
                    </div>
                    <div class="post-tag">{post['tag']}</div>
                </div>
                <h3 class="post-title">{post['title']}</h3>
                <p class="post-content">{post['content']}</p>
                <div class="post-footer">
                    <div><i class="fas fa-heart"></i> {post['likes']} Likes</div>
                    <div><i class="fas fa-comment"></i> {post['comments']} Comments</div>
                </div>
            </div>
        """), unsafe_allow_html=True)