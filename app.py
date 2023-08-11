
from pathlib import Path

import streamlit as st
from PIL import Image

    
# --- PATH SETTINGS ---
current_dir = Path.cwd() / "styles"
css_file = current_dir / "main.css"
resume_file = current_dir.parent / "assets" / "CV.pdf"
profile_pic = current_dir.parent / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Zakaria TEMOUCH"
PAGE_ICON = ":wave:"
NAME = "ZAKARIA TEMOUCH"
DESCRIPTION = """
MSc Student - Renewable Energy Engineering & Energy Efficiency \n
Thermal Processes & Energy Valorization
"""
EMAIL = "zakariatemouch@gmail.com"
PHONE = "+212 696 79 16 27"

SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/zakariatemouch",
    "Digital CV - French Version": "https://zakaria-temouch-fr.onrender.com",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide", initial_sidebar_state="expanded",)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
st.markdown("""
    <style>
    .stColumn {
        margin-right: 5px; 
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.image(profile_pic, width=260)

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
    st.write("☎", PHONE)
    st.write('\n')
    st.write('\n')
    

# --- SOCIAL LINKS ---
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

    
# --- EDUCATION ---



def display_bio():
    st.header("SUMMARY")
    st.write('\n')
    st.write("Currently pursuing a Master's in Renewable Energy Engineering and Energy Efficiency, specializing in Thermal Processes and Energy Valorization. My experience includes internships where I gained expertise in sizing and installing photovoltaic systems and thermal equipment maintenance. I excel in energy system modeling, CFD analysis, thermal audits, renewables projects management, and programming with Python and Java Script. Academic projects honed my understanding of heat transfer and PV system sizing and energy audits.")

def display_education():

    st.header("EDUCATION")
    st.write('\n')
    st.subheader("Master of Science -  Renewable Energy Engineering & Energy Efficiency")
    st.write("October 2022 - Present")
  
    st.write(
"""
 \n
Option: Thermal Processes & Energy Valorization\n
Polydisciplinary Faculty - Sultan Moulay Slimane University - Beni Mellal, Morocco\n
"""
)
    st.subheader("Professional Bachelor -  Renewable Energies & Energy Efficiency")
    st.write("October 2021 - June 2022") 
    st.write("Higher School of Technology - Moulay Ismail University - Meknès, Morocco")

    st.subheader("University Diploma of Technology -  Thermal & Energy Engineering")
    st.write("September 2018 - June 2020")
    st.write("Higher School of Technology - Moulay Ismail University - Meknès, Morocco")    

def display_work_experience():
    st.header("WORK EXPERIENCE")
    st.write('\n')
    st.subheader("Internship - RANYACHAMS SOLAIRE S.A.R.L")
    st.write("April 2022 - June 2022")
    st.write(
        """
Sizing and installation of photovoltaic systems: \n
• Solar pumping \n
• On-grid\n
• Remote sites\n
• Solar lighting\n
"""
)
    st.write('\n')

    st.subheader("Internship - Agro Juice Processing")
   
    st.write("July 2019 - August 2019")
    st.write(
"""

• Maintenance of boilers and heat exchangers\n
• Supervision and monitoring of HVAC systems
"""
)
    
def display_skills():
    st.header("SKILLS")
    st.write("\n")
    st.write("• Modeling & Sizing of Energetic Systems")
    st.write("• CFD Analysis of Heat Transfer Phenomena")
    st.write("• Energy Audits for New & Existing Buildings")
    st.write("• Programming: Python, HTML, Java Script, C++")
   

def display_projects():
    st.header("PROJECTS")
    st.write("• Analytical & Numerical study of Heat Transfer Phenomena in a bi-dimensional Fin")
    st.write("• CFD Analysis of turbulent forced convection over a cylinder")
    st.write("• Sizing of a photovoltaic Pumping System - Peak Power: 12.2 kWp")
    st.write("• Energy Audit of an Existing Building in Meknès, Morocco")
   

def display_softwares():

    st.header("SOFTWARES")
    st.write("• MATLAB")
    st.write("• COMSOL")
    st.write("• ANSYS")
    st.write("• TRNSYS")
    st.write("• SOLIDWORKS")
    st.write("• AUTOCAD")
    st.write("• PVSYST")
    st.write("• RETSCREEN")


def display_languages():

    st.header("LANGUAGES")
    st.write("• English: Professional Working Proficiency")
    st.write("• French: Full Professional Proficiency")
    st.write("• Arabic: Native or Bilingual Proficiency")        


def display_interests():

    st.header("INTERSETS")
    st.write("• Astronomy")
    st.write("• Chess")
    st.write("• Basketball")    

def main():
    display_bio()
    st.markdown("---")
    display_education()
    st.markdown("---")
    display_work_experience()
    st.markdown("---")
    display_skills()
    st.markdown("---")
    display_projects()
    st.markdown("---")
    display_softwares()
    st.markdown("---")
    display_languages()
    st.markdown("---")
    display_interests()

if __name__ == "__main__":
    main()
