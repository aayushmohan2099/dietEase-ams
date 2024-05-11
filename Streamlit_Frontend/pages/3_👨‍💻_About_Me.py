import streamlit as st

st.set_page_config(page_title="About DietEase", page_icon="👨‍💻",layout="wide",initial_sidebar_state="collapsed")

video_container_css = """
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
"""

video_css = """
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
"""

content_css = """
    overflow-y: auto;
    height: 100vh; 
    width: 100vw; 
    top: 10%;
    left: 0;
    position: fixed;
    justify-content: center;
    align-items: center;
    text-align: center;
"""

st.markdown(
    """
    <div style="{}">
        <video autoplay muted loop style="{}">
            <source src="https://cloudconvert-files.s3.eu-central-1.amazonaws.com/a584e468-9ee6-47e5-b184-be1ecd7ebd0d/bggbgbgb%20%281%29.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAI2WCZ54772T33JEQ%2F20240511%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20240511T160555Z&X-Amz-Expires=86400&X-Amz-Signature=2c8964a52d3cc816200021130ba6392be9774053c9ffa2886000d5822298b8c1&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%22bggbgbgb%20%281%29.mp4%22&response-content-type=video%2Fmp4&x-id=GetObject" type="video/mp4">
            Your browser does not support HTML5 video.
        </video>
    </div>
    <div style="{}">
        <img src="https://cloudconvert-files.s3.eu-central-1.amazonaws.com/0cc20a9d-0046-4002-b444-b4665c53481c/about_me.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAI2WCZ54772T33JEQ%2F20240511%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20240511T222010Z&X-Amz-Expires=86400&X-Amz-Signature=530675f224cecf51184dbcff8b3f1c377bf097f1852a3fc334dac535e728ef4d&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%22about_me.png%22&response-content-type=image%2Fpng&x-id=GetObject" alt="About_Me" style="width: 800px;">
    </div>
    """.format(video_container_css, video_css, content_css),
    unsafe_allow_html=True
)
