import streamlit as st
import json

# Page config
st.set_page_config(
    page_title="Jyoti Kumari Tiwari - ML/MLOps Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Load data
@st.cache_data
def load_data():
    with open('data/portfolio_data.json', 'r') as f:
        return json.load(f)


try:
    data = load_data()
except:
    st.error("Error loading portfolio data. Make sure portfolio_data.json exists in data/ folder")
    st.stop()

# Custom CSS
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Main container */
    .main {
        padding: 0rem 2rem;
    }
    
    /* Headers */
    h1, h2, h3 {
        font-weight: 800;
    }
    
    /* Gradient text */
    .gradient-text {
        background: linear-gradient(120deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Cards */
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
    }
    
    .card:hover {
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.15);
        transform: translateY(-5px);
        border-color: #667eea;
    }
    
    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.7rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 800;
    }
    
    /* Links */
    a {
        color: #667eea;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    
    a:hover {
        color: #764ba2;
    }
    
    /* Progress bars */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: #f8f9fa;
        border-radius: 10px;
        font-weight: 600;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 1rem 2rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Profile section with gradient background
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem 0;">
        <img src="https://github.com/Jyotitiwari24.png" 
             style="width: 150px; height: 150px; border-radius: 50%; 
             border: 5px solid white; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
        <h2 style="margin-top: 1rem; margin-bottom: 0.5rem;">{data['personal']['name']}</h2>
        <p style="font-size: 1.1rem; opacity: 0.9;">{data['personal']['title']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Contact info with icons
    st.markdown("### 📱 Connect")
    st.markdown(f"""
    📧 [{data['personal']['email']}](mailto:{data['personal']['email']})  
    📍 {data['personal']['location']}  
    💼 [LinkedIn]({data['personal']['linkedin']})  
    🐙 [GitHub]({data['personal']['github']})  
    """)
    
    st.markdown("---")
    
    # Quick stats
    st.markdown("### 📊 Quick Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Projects", "9+", delta="All Deployed")
    with col2:
        st.metric("GitHub", "150+", delta="Commits")
    
    st.markdown("---")
    
    # Availability badge
    st.markdown(f"""
    <div style="background: rgba(255,255,255,0.2); padding: 1rem; 
                border-radius: 10px; text-align: center;">
        <strong>🟢 Available for Work</strong><br>
        <small>{data['personal']['availability']}</small>
    </div>
    """, unsafe_allow_html=True)

# Main welcome message
st.markdown(f"""
<div style="text-align: center; padding: 2rem 0;">
    <h1 class="gradient-text" style="font-size: 3.5rem; margin-bottom: 1rem;">
        Welcome to My Portfolio
    </h1>
    <p style="font-size: 1.3rem; color: #666;">
        {data['personal']['tagline']}
    </p>
</div>
""", unsafe_allow_html=True)

# Navigation info
st.info("👈 Use the sidebar to navigate through different sections of my portfolio")

# Quick overview with cards
st.markdown("## 🎯 What I Do")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🚀 MLOps</h3>
        <p>Build production-ready ML pipelines with Docker, FastAPI, and CI/CD</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🤖 Machine Learning</h3>
        <p>Develop intelligent models for classification, regression, and NLP tasks</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>📊 Data Science</h3>
        <p>Extract insights from data with advanced analytics and visualization</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Featured projects preview
st.markdown("## ⭐ Featured Projects")

# Show top 3 projects
for project in data['projects'][:3]:
    with st.container():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"""
            <div class="card">
                <h3>{project['name']}</h3>
                <p>{project['description']}</p>
                <p><strong>Impact:</strong> {project['impact']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="card" style="text-align: center;">
                <p><strong>Category</strong></p>
                <p>{project['category']}</p>
                <p><strong>Accuracy</strong></p>
                <p>{project['metrics']['accuracy']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

# CTA Section
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h2>Let's Work Together!</h2>
        <p>Looking for ML/MLOps opportunities in Hyderabad</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📩 Get in Touch", use_container_width=True):
        st.switch_page("pages/5_📞_Contact.py")

# Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; padding: 2rem; color: #666;">
    <p>Built with ❤️ using Python & Streamlit</p>
    <p>© 2025 {data['personal']['name']} | All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)