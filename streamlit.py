import streamlit as st
from PIL import Image





# -------------------- PAGE SETUP --------------------
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon="😍",
    default=True
)

project_1_page = st.Page(
    page="views/project_1.py",
    title="Project_1",
    icon="📊"
)

project_2_page = st.Page(
    page="views/project_2.py",
    title="Project_2",
    icon="❤️"
)

# -------------------- NAVIGATION --------------------
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page]
    }
)




# -------------------- RUN APP --------------------
pg.run()
