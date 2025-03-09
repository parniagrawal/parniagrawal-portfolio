import streamlit as st
import webbrowser
from streamlit_lottie import st_lottie
import requests
# Page Config
st.set_page_config(page_title="My Data Science Portfolio", layout="wide")
# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation (example: AI/ML animation)
lottie_ai = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_1pxqjqps.json")

# Display the animation
st_lottie(lottie_ai, height=250, key="ai")

# Sidebar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Projects", "Work Experience","Education","Certifications", "Achievements","Contact"])

# Home Page
if selection == "Home":
    st.title("Welcome to My Portfolio")
    st.write('''Hi, I am Parni Agarwal, a Data Analyst passionate about Artificial Intelligence and Machine Learning. 
    Proficient in Python, SQL, and DBMS, with a proven track record in developing data-driven solutions and managing 
    collaborative projects. Experienced in leading teams and received the “Best Paper” Award at NCICIS 2025 for my 
    NeuroVision Brain Tumor Research Paper. Currently working as an **AI/ML Research Intern at NIT Trichy**. 
    Passionate about leveraging analytics and technology to solve real-world problems and drive innovation in data science.''')
    
    st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .fade-in {
        animation: fadeIn 2s ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)
    st.image("Profile.jpg", width=200)

    st.markdown("---")
    st.header("📌 Portfolio Summary")

    # Summary of Work Experience
    st.subheader("💼 Work Experience")
    st.write("""
    - **AI/ML Research Intern at NIT Trichy** (Feb 2025 - Present)  
      Conducting research on **Disease Detection in Infants** using Machine Learning.  
    - **AWS Internship at AICTE** (Feb 2025 - Present)  
      Working with AWS tools to deploy ML models.  
    """)

    # Summary of Projects
    st.subheader("🚀 Projects")
    st.write("""
    - **Loan Approval Prediction** – Achieved **98.5% accuracy** using XGBoost.  
    - **NeuroVision Brain Tumor Classification** – Developed a CNN model with **96.8% accuracy**.  
    - **Customer Churn Prediction** – Improved retention rates by **30%**.  
    """)

    # Summary of Education
    st.subheader("🎓 Education")
    st.write("""
    - **B.Tech in Computer Science Engineering with Big Data Analytics** | SRM IST (2022 - 2026)  
      CGPA: **8.82**  
    """)

    # Summary of Certifications
    st.subheader("📜 Certifications")
    st.write("""
    - **Python for Data Science and AI** – IBM (Coursera)  
    - **Oracle Certified Foundations Associate** – Oracle  
    - **AWS Academy Machine Learning** – Amazon Web Services  
    """)

    # Summary of Achievements
    st.subheader("🏆 Achievements")
    st.write("""
    - **Best Paper Award** at NCICIS 2025 for **NeuroVision Brain Tumor Detection**.  
    - **Secured 6th position in SRM Hackathon 8.0** among 75 teams.  
    - **Academic Excellence Award** for 92.6% in 12th Boards.  
    """)

    # Summary of Contact Information
    st.subheader("📩 Contact Information")
    st.write("""
    - 📍 **Location:** Chennai, Tamil Nadu  
    - 📧 **Email:** agrawalparni@gmail.com  
    - 🔗 **[GitHub](https://github.com/parniagrawal)**  
    - 💼 **[LinkedIn](https://www.linkedin.com/in/parni-agrawal)**  
    """)

    st.markdown("---")
    st.write("🔗 **Explore the sections in the sidebar to view detailed information!**")

# Projects Page
elif selection == "Projects":
    st.title("My Projects")
    st.write("### 1. Loan Approval Prediction")
    st.write('''• Developed a machine learning model to predict loan approval status based on applicant financial data.
\n• Achieved 98.5% accuracy using XGBoost, optimizing features and performing hyperparameter tuning.
\n• Deployed a Streamlit web app for real-time predictions, making it accessible via a web interface.
\n• Tools & Technologies: Python (Pandas, NumPy, Scikit-learn, XGBoost), Streamlit, GitHub, VS Code.''')
    st.link_button("View Loan Approval Prediction", "https://github.com/parniagrawal/loan-approval-predictor.git")
    st.link_button("Run App", "https://loan-approval-predictor-efec8javuptkd6ywaj3p6k.streamlit.app/")
    st.write(" ")
    st.write("### 2. Data Science and Machine Learning Portfolio")
    st.write('''• Developed an interactive portfolio website showcasing ML projects using Streamlit and Flask.
\n• Integrated dynamic project visualizations, live model demos, and research insights.
\n• Hosted on Render with seamless deployment from GitHub.
\n• Designed a responsive UI for a user-friendly experience.
\n• Tools & Technologies: Python (Streamlit, Flask, Pandas, NumPy, Scikit-learn), Jupyter Notebook, VS Code, GitHub.''')
    st.link_button("View Portfolio", "https://github.com/parniagrawal/parniagrawal-portfolio.git")
    st.link_button("Run App", "https://parniagrawal-portfolio-h7ajplxztjsqjf22xpbtdm.streamlit.app/")
    st.write("### 3. NeuroVision Brain Tumor Classification Model")
    st.write('''• Developed a deep learning model for MRI-based brain tumor classification using CNN architecture.
\n• Utilized VGG16 for feature extraction, integrated Feature Pyramid Network (FPN) and attention mechanisms to enhance accuracy.
\n• Achieved high classification performance using image preprocessing (normalization, augmentation).
\n• Evaluated using accuracy, F1-score, confusion matrix and achieved an accuracy of 96.8%.''')
    st.write(" ")
    st.write("### 4. Price Prediction Machine Learning Model")
    st.write('''•Developed a machine learning model to predict house prices using python and regression algorithms
\n•Achieved 92% accuracy in predicting prices by analysing historical data and optimizing features.
\n•Tools & Technologies: Python (Pandas, NumPy, Scikit-learn), Jupyter Notebook, VS Code.''')
    st.write(" ")
    st.write("### 5. Customer Churn Prediction")
    st.write('''• Built a churn prediction model using **Random Forest & XGBoost** to analyze customer retention trends.  
\n• Improved customer retention by **30%** through feature engineering and hyperparameter tuning.  
\n• **Tools & Technologies:** Python (*Scikit-learn, Matplotlib, Seaborn*), Jupyter Notebook, Streamlit.''')

# Work Experience
elif selection == "Work Experience":
    st.header("💼 Work Experience")
    st.subheader("1. AI/ML Research Intern | National Institute of Technology (NIT) Trichy (Feb 2025 - Present)")
    st.write("""
- Conducting research in **machine learning and predictive analytics**  
- Developing Classification Model for **Disease Detection in Infants**
""")
    st.subheader("2. AWS Internship | All India Council Technical Education (AICTE) | (Feb 2025 - Present)")
    st.subheader("3. Research and Developement (R&D) Director | Society of Women Engineers - SRM IST | (Feb 2025 - Present)")
    st.subheader("4. Committe Head | Aaruush, SRM University | (Sep 2022 - Oct 2024)")
    st.write("""
\n• Managed a team of 25 to organize over 10 large-scale technical events with 5,000+ attendees. Part-Time
\n• Increased participant engagement by 15% through innovative event formats and marketing strategies.
\n• Coordinated with sponsors and stakeholders, raising funds for the successful execution of the fest.
""")

# Education
elif selection == "Education":
    st.header("🎓 Education")
    st.subheader("B.Tech in Computer Science Engineering with Big Data Analytics | SRM Institute of Science and Technology, KTR (Sep 2022 -  Apr 2026)")
    st.write(" - CGPA: **8.82**")
    st.subheader("Academic Excellence Award Isuued by AISSCE | CBSE Board  | Father Agnel School (Mar 2021 - Mar 2022)")
    st.write("""
- Coursework: **Physics, Chemistry, Maths and Informatics Practices**.  
- CGPA: **92.6%**
""")

# Certifications
elif selection == "Certifications":
    st.header("📜 Certifications")
    st.write('''
- 🏅 **Python for Data Science and AI** - IBM (Coursera)''')
    st.linl_button("View Certification", "https://coursera.org/share/32532091f6b1a801b443580adca136b0")
    st.write('''
- 🏅 **Oracle Certified Foundations Associate** - Oracle''')
    st.link_button("View Certification", https://brm-certview.oracle.com/ords/certview/ecertificate?ssn=OC5625741&trackId=OCI2024FNDCFA&key=d47a67f93e5642a7b69b195c6ba9a734af9c7b95" )
    st.write('''
- 🏅 **Networking basics** - Cisco''')
    st.link_button("View Certification", "https://www.netacad.com/certificates?issuanceId=5ba5c36e-ed28-4f9a-afc0-7abc39c81b19")
    st.write('''
- 🏅 **AWS Academy Machine Learning** - Amazon Web Services(AWS)''')
    st.link_button("View Certification", "https://www.credly.com/go/1wcQFMC9")


# Achievements
elif selection == "Achievements":
    st.header("🏆 Achievements")
    st.write("""
- 🏆 **Best Paper Award** at NCICIS 2025 for **NeuroVision** (Brain Tumor Detection).  
- 🏆 **Recieved Academic Excellence Award for Securing 92.6% in 12th Boards ** 
- 🏆 **Got funding and Secured 6th position in SRM Hackathon 8.0 among 75 teams**.  
""")

# Contact Page
elif selection == "Contact":
    st.title("Contact Me")
    st.write("📍Location: Chennai, Tamil Nadu")
    st.write("📧 Email: agrawalparni@gmail.com")
    st.write("🔗 [GitHub](https://github.com/parniagrawal)")
    st.write("💼 [LinkedIn](https://www.linkedin.com/in/parni-agrawal)")
    
