import streamlit as st
import json

st.set_page_config(
    page_title="Contact - Jyoti Tiwari",
    page_icon="📞",
    layout="wide"
)


# Load data
@st.cache_data
def load_data():
    with open('data/portfolio_data.json', 'r') as f:
        return json.load(f)


data = load_data()

st.title("📞 Let's Connect!")
st.markdown("I'm actively seeking ML/MLOps opportunities and always happy to discuss AI/ML projects")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## 💼 Looking For Opportunities")
    
    st.markdown(f"""
    I'm currently seeking **{', '.join(data['personal']['job_preferences'])}** roles in:
    - **Location:** {data['personal']['preferred_location']}
    - **Availability:** {data['personal']['availability']}
    - **Notice Period:** Immediate Joiner
    
    ### What I Bring to the Table:
    
    ✅ **9+ Production-Ready ML Projects** with complete deployment  
    ✅ **Strong MLOps Skills** (Docker, FastAPI, CI/CD, Monitoring)  
    ✅ **End-to-End ML Pipeline Experience** from data to deployment  
    ✅ **Proven Track Record** in Healthcare, Finance, NLP domains  
    ✅ **Fast Learner** with passion for solving real-world problems  
    
    ### Industries I'm Interested In:
    
    - Technology & SaaS
    - Healthcare & Pharmaceuticals
    - Finance & Banking
    - E-commerce & Retail
    - Consulting (Service-based companies)
    
    **Target Companies:** Deloitte, Accenture, HCLTech, Wipro, TCS, and similar service-based companies
    """)
    
    st.markdown("---")
    
    # Contact Form
    st.markdown("## ✉️ Send Me a Message")
    
    with st.form("contact_form", clear_on_submit=True):
        col_form1, col_form2 = st.columns(2)
        
        with col_form1:
            name = st.text_input("Your Name *")
            email = st.text_input("Your Email *")
        
        with col_form2:
            company = st.text_input("Company (Optional)")
            subject = st.selectbox(
                "Subject *",
                ["Job Opportunity", "Collaboration", "Project Discussion", "General Inquiry", "Other"]
            )
        
        message = st.text_area("Message *", height=150)
        
        submitted = st.form_submit_button("📨 Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message:
                st.success("✅ Thank you for reaching out! I'll get back to you within 24 hours.")
                st.balloons()
                
                # You can add email sending logic here
                # For now, just display confirmation
                st.info(f"""
                **Message Preview:**
                - From: {name} ({email})
                - Company: {company if company else 'N/A'}
                - Subject: {subject}
                - Message: {message[:100]}{'...' if len(message) > 100 else ''}
                """)
            else:
                st.error("⚠️ Please fill in all required fields (marked with *)")

with col2:
    st.markdown("## 📱 Direct Contact")
    
    # Contact cards
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 1.5rem; border-radius: 15px; color: white; margin-bottom: 1rem;">
        <h4 style="margin: 0;">📧 Email</h4>
        <a href="mailto:{data['personal']['email']}" 
           style="color: white; text-decoration: none; font-size: 1.1rem;">
            {data['personal']['email']}
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background: #0077B5; padding: 1.5rem; border-radius: 15px; 
                color: white; margin-bottom: 1rem;">
        <h4 style="margin: 0;">💼 LinkedIn</h4>
        <a href="{data['personal']['linkedin']}" target="_blank"
           style="color: white; text-decoration: none; font-size: 1.1rem;">
            Connect with me
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background: #333; padding: 1.5rem; border-radius: 15px; 
                color: white; margin-bottom: 1rem;">
        <h4 style="margin: 0;">🐙 GitHub</h4>
        <a href="{data['personal']['github']}" target="_blank"
           style="color: white; text-decoration: none; font-size: 1.1rem;">
            View my code
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background: #28a745; padding: 1.5rem; border-radius: 15px; 
                color: white;">
        <h4 style="margin: 0;">📍 Location</h4>
        <p style="margin: 0; font-size: 1.1rem;">{data['personal']['location']}</p>
        <small>Open to Remote & Relocation</small>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Resume download
    st.markdown("### 📄 Resume")
    st.download_button(
        label="📥 Download Resume (PDF)",
        data="C:\Users\tjyot\Videos\projects\project\cv_projects\My_Portfolio\data\jyoti_tiwari_cv.docx",  
        file_name="C:\Users\tjyot\Videos\projects\project\cv_projects\My_Portfolio\data\jyoti_tiwari_cv.docx",
        mime="application/pdf",
        use_container_width=True
    )

st.markdown("---")

# FAQ Section
st.markdown("## ❓ Frequently Asked Questions")

with st.expander("What kind of roles are you looking for?"):
    st.markdown("""
    I'm primarily looking for:
    - **ML Engineer** positions
    - **MLOps Engineer** roles
    - **Data Scientist** positions with ML focus
    
    Preferably in service-based companies (Deloitte, Accenture, HCLTech, Wipro) 
    or product companies with strong ML infrastructure.
    """)

with st.expander("What's your tech stack?"):
    st.markdown("""
    **Core Skills:**
    - Python, SQL, Bash
    - scikit-learn, TensorFlow, XGBoost
    - Docker, FastAPI, Flask
    - Git, CI/CD, MLflow
    - AWS (EC2, S3, SageMaker)
    
    **Specializations:**
    - End-to-end ML pipelines
    - Model deployment & monitoring
    - NLP & Text Analytics
    - Production ML systems
    """)

with st.expander("Can you start immediately?"):
    st.markdown(f"""
    **Yes!** I'm available to start immediately ({data['personal']['availability']}).
    
    No notice period required.
    """)

with st.expander("Are you open to remote work?"):
    st.markdown("""
    **Absolutely!** I'm open to:
    - Remote positions
    - Hybrid roles
    - On-site in Hyderabad
    - Willing to relocate for the right opportunity
    """)

with st.expander("What makes you different?"):
    st.markdown("""
    **Practical Experience:**
    - 9+ deployed ML projects (not just notebooks)
    - Complete MLOps pipelines with monitoring
    - Production-ready code with Docker & CI/CD
    
    **Fast Learner:**
    - Completed M.Tech in AI/ML
    - Self-taught MLOps stack
    - Constantly learning new technologies
    
    **Problem Solver:**
    - Built projects across multiple domains
    - Focus on business impact, not just accuracy
    - Can explain technical concepts clearly
    """)

st.markdown("---")

# Social proof
st.markdown("## 🌟 Why Work With Me?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 15px;">
        <h2 style="color: #667eea; margin: 0;">9+</h2>
        <p>Production ML Projects</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 15px;">
        <h2 style="color: #667eea; margin: 0;">100%</h2>
        <p>Deployment Success Rate</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 15px;">
        <h2 style="color: #667eea; margin: 0;">85%+</h2>
        <p>Average Model Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Call to action
st.markdown("""
<div style="text-align: center; padding: 3rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px; color: white;">
    <h2>Ready to Hire?</h2>
    <p style="font-size: 1.2rem;">Let's discuss how I can contribute to your team!</p>
</div>
""", unsafe_allow_html=True)