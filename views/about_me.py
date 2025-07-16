import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Krish Portfolio", layout="wide")

# ---------- HERO SECTION ----------
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;   /* 🟢 Reduced top padding */
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1], gap="small")

# -- Left: Profile Image --
with col1:
    st.image(r"F:\STREAMLIT\assets\converted_image.png", use_container_width=True)


# -- Middle: Name, Tagline, Contact, Logos --
with col2:
    st.markdown("<h1 style='margin-bottom:0;'>Krishna Kanta Maiti</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: grey; margin-top: 0;'>**Transforming Data into Deployed Intelligence**</h4>", unsafe_allow_html=True)

    st.markdown("<h5 style='margin-top: 15px;'>📬 Contact Me</h5>", unsafe_allow_html=True)

    st.markdown(
    """
    <style>
    .icon-container a {
        display: inline-block;
        transition: transform 0.2s ease-in-out;
    }
    .icon-container a:hover {
        transform: scale(1.2); /* Hover zoom effect */
    }
    .icon-container img {
        border-radius: 50%;        /* Make icons circular */
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);  /* Add soft shadow */
    }
    </style>

    <div class="icon-container" style='display: flex; gap: 25px; align-items: center; justify-content: flex-start;'>
        <a href="https://www.linkedin.com/in/krishna-kanta-maiti-658605320?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank" title="LinkedIn">
            <img src="https://cdn-icons-png.flaticon.com/512/145/145807.png" width="40"/>
        </a>
        <a href="https://github.com/code-with-krish" target="_blank" title="GitHub">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" width="40"/>
        </a>
        <a href="mailto:krishnakantamaiti7337@gmail.com" title="Email">
            <img src="https://cdn-icons-png.flaticon.com/512/5968/5968534.png" width="40"/>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)




# ---------- ABOUT ME ----------
st.markdown("---")
st.subheader("👋 About Me")

st.markdown("""
Hi, I'm Krishna Kanta Maiti — a passionate Data Science enthusiast with a strong foundation in Machine Learning, Deep Learning, and NLP.  
I enjoy building end-to-end AI solutions, from data preprocessing and modeling to deploying real-time applications using Flask and Streamlit.  
Always curious and committed to learning, I'm driven to solve real-world problems through data and innovation.
""")

# ---------- EXPERIENCE ----------
st.subheader("📌 Experience")

st.markdown("""
**🔐 Ethical Hacking Intern**  
*Dataspace Academy — 1 Month*  
Worked with **Kali Linux** and gained hands-on experience with cybersecurity tools and basic penetration testing practices.
""")

# ---------- SKILLS ----------
st.subheader("🧠 Technical Proficiencies")

st.markdown("""
**💡 Core Specializations**  
• Machine Learning (Supervised & Unsupervised)  
• Deep Learning (CNNs, RNNs, Feedforward Networks)  
• Natural Language Processing (Text Classification, Embeddings, Transformers)  
• Model Deployment (Flask, Streamlit)

**🛠 Programming & Libraries**  
• Python • scikit-learn • TensorFlow • Pandas • NumPy

**📊 Data Analysis & Visualization**  
• Exploratory Data Analysis (EDA) • Feature Engineering • PCA  
• Seaborn • Matplotlib

**🗄 Databases & Backend**  
• PostgreSQL • REST APIs

**🌐 Web Technologies**  
• HTML • CSS  
""")
