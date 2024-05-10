import streamlit as st

st.set_page_config(
    page_title="Menu",
    page_icon="👋",
)

st.write("# Welcome to DietEase! 👋")

st.sidebar.success("Select a recommendation app.")

st.markdown(
    """
    DietEase is a diet recommendation web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.
    You can find more details and the whole project on my [repo]().
    """
)
