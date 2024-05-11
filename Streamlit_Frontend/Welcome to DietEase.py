import streamlit as st

st.set_page_config(
    page_title="Menu",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="collapsed"
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
            <source src="https://cloudconvert-files.s3.eu-central-1.amazonaws.com/a584e468-9ee6-47e5-b184-be1ecd7ebd0d/bggbgbgb%20%281%29.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAI2WCZ54772T33JEQ%2F20240511%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20240511T160555Z&X-Amz-Expires=86400&X-Amz-Signature=2c8964a52d3cc816200021130ba6392be9774053c9ffa2886000d5822298b8c1&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%22bggbgbgb%20%281%29.mp4%22&response-content-type=video%2Fmp4&x-id=GetObject" type="video/mp4">
            Your browser does not support HTML5 video.
        </video>
    </div>
    <div style="{}">
        <img src="https://cloudconvert-files.s3.eu-central-1.amazonaws.com/52eac1cf-1a2f-464d-9ab8-2c58eab42d8d/HomeScreen%20Logo.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAI2WCZ54772T33JEQ%2F20240511%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20240511T164848Z&X-Amz-Expires=86400&X-Amz-Signature=d715b0868e14d5803048a5a1e829475dcf105b5d411af130f9efb58ed07a8cfa&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%22HomeScreen%20Logo.png%22&response-content-type=image%2Fpng&x-id=GetObject" alt="Logo" style="width: 1000px;"><br><img src="https://cloudconvert-files.s3.eu-central-1.amazonaws.com/537832bc-67e0-4d79-9c62-fc344d34ccec/HomeScreen%20description.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAI2WCZ54772T33JEQ%2F20240511%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20240511T180226Z&X-Amz-Expires=86400&X-Amz-Signature=00463f5d327ca3bb73cb91564972843caf9c8c1eb555c991adc825e5865ee561&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%22HomeScreen%20description.png%22&response-content-type=image%2Fpng&x-id=GetObject" alt="Logo_Description" style="width: 600px;">
        <br>
        <br>
        <br>
        <br>
        <br><br><br><br><br><br><img src="https://cloudconvert-files.s3.eu-central-1.amazonaws.com/88a16fe6-284f-4e71-b1d0-1f4d96a59ebe/HomeScreen%20Diag.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAI2WCZ54772T33JEQ%2F20240511%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20240511T194414Z&X-Amz-Expires=86400&X-Amz-Signature=51b740fcee92dcb2ee2ee2c6ddff2f986a8e97f52b1fedb2a125fd6d2029a999&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%22HomeScreen%20Diag.png%22&response-content-type=image%2Fpng&x-id=GetObject" alt="Homepage_Diagram" style="display: block; margin: 0 auto; width: 800px;">
        <br>
        <br>
        <img src="https://cloudconvert-files.s3.eu-central-1.amazonaws.com/4753edd1-0eec-45d5-aac0-c2dbd4b6c45f/sidebar_sign.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAI2WCZ54772T33JEQ%2F20240511%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20240511T213614Z&X-Amz-Expires=86400&X-Amz-Signature=7e3c072947b007c059aa0adf8617ccf985920af26ae4e601ec315e8958aa3aac&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%22sidebar_sign.png%22&response-content-type=image%2Fpng&x-id=GetObject" alt="Sidebar_Sign" style="display: block; margin: 0 auto; width: 800px;">
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <img src="https://cloudconvert-files.s3.eu-central-1.amazonaws.com/ba1dc492-2dd5-4bf5-a536-c958f17a3aed/Sign.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAI2WCZ54772T33JEQ%2F20240511%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20240511T194539Z&X-Amz-Expires=86400&X-Amz-Signature=6c88c64b071648fe9e7f47c18f736724a0bd558d6908f6638f8a7d27975981a9&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%22Sign.png%22&response-content-type=image%2Fpng&x-id=GetObject" alt="Signature" style="display: block; margin: 0 auto; width: 300px;">
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
