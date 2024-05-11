import streamlit as st

st.set_page_config(
    page_title="Menu",
    page_icon="👋",
    layout="wide",
)

# Define CSS styles for video container and content
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
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    text-align: center;
"""

st.markdown(
    """
    <h1 style='text-align: center; color: white;'>Welcome to DietEase! 👋</h1>
    <div style="{}">
        <video autoplay muted loop style="{}">
            <source src="https://cloudconvert-files.s3.eu-central-1.amazonaws.com/8b3b5ba3-0482-4ded-af9f-98c99dd96336/11323-229392548.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAI2WCZ54772T33JEQ%2F20240511%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20240511T144317Z&X-Amz-Expires=86400&X-Amz-Signature=2de4a93bef1bcb71a253675668987ce3dc06a52b636b389a7443903579cdcb33&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%2211323-229392548.mp4%22&response-content-type=video%2Fmp4&x-id=GetObject" type="video/mp4">
            Your browser does not support HTML5 video.
        </video>
    </div>
    <div style="{}">
        <h1 style='text-align: center; color: white;'>Welcome to DietEase! 👋</h1>
        <p>
            DietEase is a diet recommendation web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.
            You can find more details and the whole project on my <a href="https://github.com/aayushmohan2099/dietEase-ams.git" style="color: white;">repo</a>.
        </p>
    </div>
    """.format(video_container_css, video_css, content_css),
    unsafe_allow_html=True
)

# import streamlit as st

# st.set_page_config(
#     page_title="Menu",
#     page_icon="👋",
#     layout="wide",
# )

# video_container_css = """
#     position: relative;
#     width: 100%;
#     padding-bottom: 56.25%;
# """

# video_css = """
#     position: absolute;
#     top: 0;
#     left: 0;
#     width: 100%;
#     height: 100%;
# """

# content_css = """
#     position: absolute;
#     top: 50%;
#     left: 50%;
#     transform: translate(-50%, -50%);
#     color: white;
#     text-align: center;
# """

# st.markdown(
#     """
#     <div style="position: relative;">
#         <div style="{}">
#             <video autoplay muted loop style="{}">
#                 <source src="https://static.streamlit.io/examples/star.mp4" type="video/mp4">
#                 Your browser does not support HTML5 video.
#             </video>
#         </div>
#         <div style="{}">
#             <h1 style='text-align: center; color: white;'>Welcome to DietEase! 👋</h1>
#             <p>
#                 DietEase is a diet recommendation web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.
#                 You can find more details and the whole project on my <a href="https://github.com/aayushmohan2099/dietEase-ams.git" style="color: white;">repo</a>.
#             </p>
#         </div>
#     </div>
#     """.format(video_container_css, video_css, content_css),
#     unsafe_allow_html=True
# )
