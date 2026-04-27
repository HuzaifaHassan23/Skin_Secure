import streamlit as st
import requests
from datetime import datetime
from utils.styles import apply_community_styles
from utils.helpers import get_community_translation, format_time_ago

def show():
    # Check if user has valid token
    if not st.session_state.get("jwt_token"):
        st.warning("Please login first.")
        st.session_state.is_logged_in = False
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
        if st.session_state.pop("clear_new_post_form", False):
            st.session_state.new_post_title = ""
            st.session_state.new_post_content = ""
            st.session_state.new_post_type = "Story"
            st.session_state.new_post_anonymous = False

        if "new_post_title" not in st.session_state:
            st.session_state.new_post_title = ""
        if "new_post_content" not in st.session_state:
            st.session_state.new_post_content = ""
        if "new_post_type" not in st.session_state:
            st.session_state.new_post_type = "Story"
        if "new_post_anonymous" not in st.session_state:
            st.session_state.new_post_anonymous = False

        with st.form("new_post_form", border=False):
            title = st.text_input(
                t('post_title'),
                placeholder="e.g. My experience with early detection",
                key="new_post_title"
            )
            content = st.text_area(
                t('post_content'),
                height=150,
                key="new_post_content"
            )
            
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                post_type = st.selectbox(
                    "Post Type",
                    ["Story", "Question", "Advice"],
                    label_visibility="collapsed",
                    key="new_post_type"
                )
            with col2:
                is_anonymous = st.checkbox(t('post_anon'), key="new_post_anonymous")
            with col3:
                submitted = st.form_submit_button(t('publish_btn'), key="submit_post", use_container_width=True)
                
            if submitted:
                if title and content:
                    try:
                        headers = {"Authorization": f"Bearer {st.session_state.jwt_token}"}
                        payload = {
                            "post_title": title,
                            "body": content,
                            "type_of_post": post_type,
                            "is_anonymous": is_anonymous
                        }
                        response = requests.post(
                            "http://127.0.0.1:8000/posts",
                            json=payload,
                            headers=headers
                        )
                        if response.status_code == 200:
                            st.success(t('success_msg'))
                            # Clear form fields on the next render before widgets are instantiated
                            st.session_state.clear_new_post_form = True
                            # Trigger posts refresh
                            st.session_state.community_refresh = True
                            st.rerun()
                        else:
                            error_msg = response.json().get("detail", "Failed to create post")
                            st.error(f"Error: {error_msg}")
                    except requests.exceptions.ConnectionError:
                        st.error("Backend server is not running")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
                else:
                    st.error(t('empty_err'))

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # COMMUNITY FEED SECTION
    # ---------------------------------------------------------
    st.markdown(f"<h3 style='color: #333; font-weight: 700; margin-bottom: 20px;'>{t('recent_posts')}</h3>", unsafe_allow_html=True)

    # Initialize or refresh posts cache
    if "posts" not in st.session_state or st.session_state.get("community_refresh", False):
        try:
            response = requests.get("http://127.0.0.1:8000/posts")
            if response.status_code == 200:
                posts_data = response.json()
                st.session_state.posts = posts_data
                st.session_state.community_refresh = False
            else:
                st.error("Failed to load posts")
                st.session_state.posts = []
        except requests.exceptions.ConnectionError:
            st.error("Backend server is not running")
            st.session_state.posts = []
        except Exception as e:
            st.error(f"Error loading posts: {str(e)}")
            st.session_state.posts = []

    # Render the Feed
    if st.session_state.posts:
        for post in st.session_state.posts:
            # Generate initials from author name
            author_name = "Anonymous" if post.get('is_anonymous') else post.get('author_name', 'User')
            author_initials = "".join([n[0] for n in author_name.split() if n])[:2].upper() or "U"
            
            # Format timestamp
            created_at = datetime.fromisoformat(post['created_at'].replace('Z', '+00:00'))
            time_ago = format_time_ago(created_at)
            
            # Post card
            st.markdown(f"""
                <div class="post-card">
                    <div class="post-header">
                        <div class="post-avatar">{author_initials}</div>
                        <div>
                            <p class="post-author">{author_name}</p>
                            <p class="post-date">{time_ago}</p>
                        </div>
                        <div class="post-tag">{post['type_of_post']}</div>
                    </div>
                    <h3 class="post-title">{post['post_title']}</h3>
                    <p class="post-content">{post['body']}</p>
                    <div class="post-footer">
                        <div><i class="fas fa-heart"></i> {post['likes']} Likes</div>
                        <div><i class="fas fa-comment"></i> {post['comment_count']} Comments</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Interactive buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"👍 Like ({post['likes']})", key=f"like_{post['id']}"):
                    try:
                        headers = {"Authorization": f"Bearer {st.session_state.jwt_token}"}
                        response = requests.post(
                            f"http://127.0.0.1:8000/posts/{post['id']}/like",
                            headers=headers
                        )
                        if response.status_code == 200:
                            # Update posts cache
                            st.session_state.community_refresh = True
                            st.rerun()
                    except Exception as e:
                        st.error(f"Error liking post: {str(e)}")
            
            with col2:
                if st.button(f"💬 Comments ({post['comment_count']})", key=f"comments_{post['id']}"):
                    st.session_state.expanded_post_id = post['id']
            
            # Show comments section if expanded
            if st.session_state.get("expanded_post_id") == post['id']:
                st.markdown("---")
                st.subheader("Comments")
                
                # Fetch full post with comments
                try:
                    response = requests.get(f"http://127.0.0.1:8000/posts/{post['id']}")
                    if response.status_code == 200:
                        post_detail = response.json()
                        
                        # Display existing comments
                        if post_detail['comments']:
                            for comment in post_detail['comments']:
                                comment_time = datetime.fromisoformat(comment['created_at'].replace('Z', '+00:00'))
                                comment_author_name = comment.get('author_name', 'Unknown')
                                st.write(f"**{comment_author_name}** • {format_time_ago(comment_time)}")
                                st.write(comment['body'])
                                st.divider()
                        else:
                            st.info("No comments yet. Be the first to comment!")
                        
                        # Comment form
                        with st.form(f"comment_form_{post['id']}", border=False):
                            comment_text = st.text_area("Add a comment", height=80, key=f"comment_input_{post['id']}")
                            submit_comment = st.form_submit_button("Post Comment", key=f"submit_comment_{post['id']}")
                            
                            if submit_comment:
                                if comment_text:
                                    try:
                                        headers = {"Authorization": f"Bearer {st.session_state.jwt_token}"}
                                        payload = {"body": comment_text}
                                        response = requests.post(
                                            f"http://127.0.0.1:8000/posts/{post['id']}/comments",
                                            json=payload,
                                            headers=headers
                                        )
                                        if response.status_code == 200:
                                            st.success("Comment posted!")
                                            st.session_state.community_refresh = True
                                            st.rerun()
                                        else:
                                            st.error("Failed to post comment")
                                    except Exception as e:
                                        st.error(f"Error posting comment: {str(e)}")
                                else:
                                    st.error("Comment cannot be empty")
                except Exception as e:
                    st.error(f"Error loading comments: {str(e)}")
                
                st.markdown("---")
                if st.button("Close Comments", key=f"close_comments_{post['id']}"):
                    st.session_state.expanded_post_id = None
                    st.rerun()
    else:
        st.info("No posts yet. Be the first to share your story!")