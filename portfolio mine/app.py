from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpeg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio| PRANSHU GUPTA"
PAGE_ICON = ":wave:"
NAME = "Pranshu Gupta"
DESCRIPTION = """
Blockchain Developer || FrontEnd Developer || Machine Learning || Competitive Programmer || Researcher
"""
EMAIL = "gpranshu482@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/pranshugupta01",
    "GitHub": "https://github.com/pranshugupta01",
    "Twitter": "https://twitter.com/pranshu_gupta01",
    "Instagram": "https://www.instagram.com/pranshu_gupta01"
}
PROJECTS = {
    "🏆 SecureProX - A browser extension which promptly alerts users if a site is potentially a phishing site": "https://github.com/nayan911/securehack",
    "🏆 BookWise - This is an innovative library management system tailored for an NGO": "https://github.com/ninadsonawane/libproject",
    "🏆 Etherscan Clone - An Ethereum blockchain explorer, providing a user-friendly interface for tracking transactions, blocks, and smart contracts on the Ethereum network.": "https://github.com/pranshugupta01/Ethereum-Blockchain-Explorer"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Hello, I am Pranshu Gupta, a versatile developer proficient in ReactJS, Python, Web3JS, Solidity, JavaScript, and smart contracts. My passion lies in the intersection of blockchain and machine learning, where I am actively expanding my expertise in NLP, deep learning, and data science. Through rigorous research, I strive to unlock the untapped potential of these technologies, revolutionizing industries with intelligent, decentralized solutions. Let's harness the power of blockchain and machine learning to shape a future of innovation and limitless possibilities.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Languages: C , C++ , Javascript, Solidity, Python
- 📊 Libraries/Framework: React.js, Web3.js, Numpy, Pandas, Matplotlib, TensorFlow, Scikit-learn, Flask
- 🗄️ Tools/Technologies: Linux, Git, Github, Jupyter Notebook, Bootstrap, Google Colab, Visual Studio Code, Pycharm
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Junior Blockchain Developer| Telusko**")
st.write("Nov 2022 - Jun 2023 | 8 months")
st.write(
    """
- ► I have worked on several Blockchain projects including the development of smart contracts and decentralized application. I have worked on several Frontend projects and I am also a part of content writing team
- ► Skills: React.js · JavaScript · Solidity · Front-End Development · Next.js · Node.js · web3.js · Smart Contracts · Web Content Writing · Problem Solving · Blockchain · Cascading Style Sheets (CSS) · HTML · Git · GitHub · Git BASH
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
