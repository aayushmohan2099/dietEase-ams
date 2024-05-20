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
            <source src="" type="video/mp4">
            Your browser does not support HTML5 video.
        </video>
    </div>
    <div style="{}">
        <img src="https://i.ibb.co/GsdHf7D/about-me.png" alt="About_Me" style="width: 700px;">
    </div>
    """.format(video_container_css, video_css, content_css),
    unsafe_allow_html=True
)
