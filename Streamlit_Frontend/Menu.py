import streamlit as st

st.set_page_config(
    page_title="Menu",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
    top: 0;
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
        <img src="https://i.ibb.co/6cQKMKx/Home-Screen-Logo.png" alt="Logo" style="width: 800px;">
        <br>
        <br>
        <br>
        <br>    
        <img src="https://i.ibb.co/bFMSFnT/Home-Screen-description.png" alt="Logo_Description" style="width: 600px;">
        <br>
        <br>
        <br>
        <br>
        <br><br><br><br><br><br><img src="https://i.ibb.co/Mp2H7Kx/Home-Screen-Diag.png" alt="Homepage_Diagram" style="display: block; margin: 0 auto; width: 800px;">
        <br>
        <br>
        <img src="https://i.ibb.co/wJ8wZqg/sidebar-sign.png" alt="Sidebar_Sign" style="display: block; margin: 0 auto; width: 800px;">
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <img src="https://i.ibb.co/hDTGxhm/Sign.png" alt="Signature" style="display: block; margin: 0 auto; width: 300px;">
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
