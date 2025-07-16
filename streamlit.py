import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# -------------------- FUNCTION: Convert image to base64 --------------------
def logo_to_base64(image):
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

# -------------------- LOAD THE LOGO IMAGE --------------------
try:
    logo_img = Image.open("F:/STREAMLIT/assets/Krish_Logo_Transparent (1).png")
    logo_base64 = logo_to_base64(logo_img)

    st.markdown(
        f"""
        <style>
            .fixed-logo {{
                position: fixed;
                top: 10px;
                left: 10px;
                width: 50px;
                z-index: 1000;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            }}
        </style>
        <img src="data:image/png;base64,{logo_base64}" class="fixed-logo">
        """,
        unsafe_allow_html=True
    )
except Exception as e:
    st.error(f"⚠️ Could not load logo: {e}")

# -------------------- PAGE NAVIGATION --------------------
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon="😍",
    default=True
)

project_1_page = st.Page(
    page="views/project_1.py",
    title="Project 1",
    icon="📊"
)

project_2_page = st.Page(
    page="views/project_2.py",
    title="Project 2",
    icon="❤️"
)

pg = st.navigation({
    "Info": [about_page],
    "Projects": [project_1_page, project_2_page]
})

# -------------------- RUN APP --------------------
pg.run()
