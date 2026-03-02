import streamlit as st
import json

# Page config
st.set_page_config(
    page_title="Jyoti Kumari Tiwari - ML/MLOps Engineer",
    page_icon="🌸",
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

# STUNNING PINK THEME CSS
st.markdown("""
<style>
    /* Import beautiful fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&family=Playfair+Display:wght@700;900&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main background with gradient */
    .main {
        background: linear-gradient(135deg, #FFF5F7 0%, #FFE5EC 50%, #FFF0F5 100%);
        padding: 0;
    }
    
    /* Animated gradient background */
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    
    /* Headers with gradient */
    h1 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #FF69B4, #FFB6C1, #FF1493, #C71585);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradient 8s ease infinite;
        text-shadow: 0 4px 12px rgba(255, 105, 180, 0.3);
    }
    
    h2 {
        font-family: 'Playfair Display', serif !important;
        color: #C71585 !important;
        font-weight: 800 !important;
    }
    
    h3 {
        color: #FF69B4 !important;
        font-weight: 700 !important;
    }
    
    /* Beautiful glass-morphism cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 182, 193, 0.3);
        border-radius: 25px;
        padding: 2rem;
        box-shadow: 
            0 8px 32px 0 rgba(255, 105, 180, 0.2),
            inset 0 1px 0 0 rgba(255, 255, 255, 0.8);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .glass-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 182, 193, 0.3), transparent);
        transition: left 0.5s;
    }
    
    .glass-card:hover::before {
        left: 100%;
    }
    
    .glass-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 
            0 16px 48px 0 rgba(255, 105, 180, 0.3),
            inset 0 1px 0 0 rgba(255, 255, 255, 0.9);
        border-color: rgba(255, 105, 180, 0.5);
    }
    
    /* Floating animation */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    .float {
        animation: float 6s ease-in-out infinite;
    }
    
    /* Glowing buttons */
    .stButton button {
        background: linear-gradient(135deg, #FF69B4, #FF1493, #C71585);
        background-size: 200% 200%;
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 2.5rem;
        font-weight: 700;
        font-size: 1.1rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        box-shadow: 
            0 8px 24px rgba(255, 105, 180, 0.4),
            0 0 0 0 rgba(255, 105, 180, 0.5);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .stButton button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton button:hover {
        transform: scale(1.1);
        box-shadow: 
            0 12px 36px rgba(255, 105, 180, 0.6),
            0 0 0 8px rgba(255, 105, 180, 0.2);
        animation: gradient 2s ease infinite;
    }
    
    /* Gradient sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, 
            #FF69B4 0%, 
            #FF1493 25%,
            #C71585 50%,
            #FF1493 75%,
            #FF69B4 100%);
        background-size: 100% 400%;
        animation: gradient 15s ease infinite;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown a {
        color: white !important;
        background: rgba(255, 255, 255, 0.2);
        padding: 0.5rem 1rem;
        border-radius: 15px;
        display: inline-block;
        margin: 0.2rem 0;
        transition: all 0.3s ease;
        text-decoration: none;
    }
    
    [data-testid="stSidebar"] .stMarkdown a:hover {
        background: rgba(255, 255, 255, 0.4);
        transform: translateX(5px);
    }
    
    /* Beautiful metrics */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #FF69B4, #FF1493);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    [data-testid="stMetricLabel"] {
        color: #C71585 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    
    /* Glowing metric cards */
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 20px;
        border: 2px solid rgba(255, 105, 180, 0.3);
        box-shadow: 
            0 8px 24px rgba(255, 105, 180, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.8);
        transition: all 0.3s ease;
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 
            0 12px 36px rgba(255, 105, 180, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 1);
        border-color: #FF69B4;
    }
    
    /* Sparkle effect */
    @keyframes sparkle {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.3; }
    }
    
    .sparkle {
        animation: sparkle 2s ease-in-out infinite;
    }
    
    /* Beautiful links */
    a {
        color: #FF1493 !important;
        text-decoration: none;
        font-weight: 600;
        position: relative;
        transition: all 0.3s ease;
    }
    
    a::after {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 0;
        height: 2px;
        background: linear-gradient(90deg, #FF69B4, #FF1493);
        transition: width 0.3s ease;
    }
    
    a:hover::after {
        width: 100%;
    }
    
    a:hover {
        color: #C71585 !important;
        transform: translateY(-2px);
    }
    
    /* Progress bars with gradient */
    .stProgress > div > div {
        background: linear-gradient(90deg, #FF69B4, #FF1493, #C71585);
        background-size: 200% 200%;
        animation: gradient 3s ease infinite;
        border-radius: 10px;
        height: 12px;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: rgba(255, 255, 255, 0.6);
        padding: 1rem;
        border-radius: 20px;
        backdrop-filter: blur(10px);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 15px;
        padding: 1rem 2rem;
        font-weight: 600;
        color: #C71585;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FF69B4, #FF1493);
        color: white !important;
        box-shadow: 0 4px 12px rgba(255, 105, 180, 0.4);
    }
    
    /* Input fields */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        border-radius: 15px !important;
        border: 2px solid rgba(255, 105, 180, 0.3) !important;
        background: rgba(255, 255, 255, 0.8) !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #FF69B4 !important;
        box-shadow: 0 0 0 3px rgba(255, 105, 180, 0.2) !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.7) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 15px !important;
        border: 2px solid rgba(255, 105, 180, 0.3) !important;
        font-weight: 600 !important;
        color: #C71585 !important;
        transition: all 0.3s ease !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(255, 182, 193, 0.3) !important;
        border-color: #FF69B4 !important;
        transform: translateX(5px);
    }
    
    /* Info, success, warning boxes */
    .stAlert {
        border-radius: 20px !important;
        backdrop-filter: blur(10px) !important;
        border: none !important;
    }
    
    /* Pulse animation for important elements */
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    .pulse {
        animation: pulse 2s ease-in-out infinite;
    }
    
    /* Hide scrollbar but keep functionality */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 182, 193, 0.1);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #FF69B4, #FF1493);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #FF1493, #C71585);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with profile
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <div class="float">
            <img src="https://github.com/Jyotitiwari24.png" 
                 style="width: 180px; height: 180px; border-radius: 50%; 
                 border: 5px solid white; 
                 box-shadow: 0 8px 32px rgba(255, 105, 180, 0.5);
                 transition: all 0.3s ease;">
        </div>
        <h2 style="margin-top: 1.5rem; margin-bottom: 0.5rem; color: white !important;">
            ✨ {name} ✨
        </h2>
        <p style="font-size: 1.2rem; opacity: 0.95; font-weight: 600;">
            {title}
        </p>
    </div>
    """.format(
        name=data['personal']['name'],
        title=data['personal']['title']
    ), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Contact with icons
    st.markdown("### 💌 Connect With Me")
    st.markdown(f"""
    <div style="line-height: 2.5;">
        ✉️ <a href="mailto:{data['personal']['email']}">{data['personal']['email']}</a><br>
        📍 {data['personal']['location']}<br>
        💼 <a href="{data['personal']['linkedin']}" target="_blank">LinkedIn Profile</a><br>
        🌸 <a href="{data['personal']['github']}" target="_blank">GitHub Portfolio</a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Animated stats
    st.markdown("### 📊 Portfolio Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Projects", "9+", delta="✨", delta_color="off")
    with col2:
        st.metric("Deployed", "9", delta="🚀", delta_color="off")
    
    st.markdown("---")
    
    # Availability badge with glow
    st.markdown(f"""
    <div style="background: rgba(255, 255, 255, 0.25); 
                padding: 1.5rem; 
                border-radius: 20px; 
                text-align: center;
                backdrop-filter: blur(10px);
                border: 2px solid rgba(255, 255, 255, 0.3);
                box-shadow: 0 8px 24px rgba(255, 255, 255, 0.2);">
        <div style="font-size: 2rem; margin-bottom: 0.5rem;">💖</div>
        <strong style="font-size: 1.1rem;">Open to Opportunities</strong><br>
        <small style="opacity: 0.9;">{data['personal']['availability']}</small>
    </div>
    """, unsafe_allow_html=True)

# Main hero section with sparkles
st.markdown(f"""
<div style="text-align: center; padding: 4rem 2rem 2rem 2rem;">
    <div class="sparkle" style="font-size: 4rem; margin-bottom: 1rem;">
        ✨ 🌸 ✨
    </div>
    <h1 style="font-size: 4rem; margin-bottom: 1rem; line-height: 1.2;">
        Welcome to My<br>Creative Portfolio
    </h1>
    <p style="font-size: 1.5rem; color: #C71585; font-weight: 600; max-width: 800px; margin: 0 auto;">
        {data['personal']['tagline']}
    </p>
    <div style="margin-top: 2rem; font-size: 2rem;">
        💖 🚀 🎯 💻 🌟
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation cards
st.info("💝 Explore my portfolio using the beautiful sections below! Each card is clickable and interactive.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="glass-card" style="text-align: center; min-height: 200px;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🚀</div>
        <h3>My Projects</h3>
        <p>9+ production-ready ML systems with complete deployment pipelines</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card" style="text-align: center; min-height: 200px;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">💻</div>
        <h3>Technical Skills</h3>
        <p>Expert in Python, MLOps, Docker, FastAPI, and Cloud Technologies</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="glass-card" style="text-align: center; min-height: 200px;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
        <h3>Live Demos</h3>
        <p>Interactive ML models you can try right now in your browser</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Stats with glowing cards
st.markdown("## ✨ Portfolio at a Glance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Projects Completed",
        value="9+",
        delta="All Deployed 🚀"
    )

with col2:
    st.metric(
        label="Model Accuracy",
        value="85%+",
        delta="Average ⭐"
    )

with col3:
    st.metric(
        label="Technologies",
        value="15+",
        delta="Mastered 💪"
    )

with col4:
    st.metric(
        label="GitHub Repos",
        value="9",
        delta="Public 🌸"
    )

st.markdown("<br><br>", unsafe_allow_html=True)

# Featured projects with beautiful cards
st.markdown("## 🌟 Featured Projects")

for i, project in enumerate(data['projects'][:3]):
    with st.container():
        st.markdown(f"""
        <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <h3 style="margin: 0;">{project['name']}</h3>
                <span style="background: linear-gradient(135deg, #FF69B4, #FF1493); 
                             color: white; padding: 0.5rem 1rem; border-radius: 20px;
                             font-weight: 600; font-size: 0.9rem;">
                    {project['category']}
                </span>
            </div>
            <p style="font-size: 1.1rem; color: #666; margin-bottom: 1rem;">
                {project['description']}
            </p>
            <p style="color: #FF1493; font-weight: 600;">
                💖 Impact: {project['impact']}
            </p>
            <div style="margin-top: 1rem;">
                <strong style="color: #C71585;">Accuracy:</strong> 
                <span style="font-size: 1.2rem; font-weight: 700; color: #FF69B4;">
                    {project['metrics']['accuracy']}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

# Call to action with gradient
st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div style="text-align: center; 
                padding: 3rem; 
                background: linear-gradient(135deg, #FF69B4, #FF1493, #C71585);
                border-radius: 30px;
                box-shadow: 0 12px 48px rgba(255, 105, 180, 0.5);
                color: white;">
        <h2 style="color: white !important; margin-bottom: 1rem;">
            💝 Let's Create Something Amazing!
        </h2>
        <p style="font-size: 1.2rem; opacity: 0.95; margin-bottom: 2rem;">
            I'm actively seeking ML/MLOps opportunities in Hyderabad
        </p>
        <div style="font-size: 2rem;">✨ 🚀 💖 ✨</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("💌 Get in Touch", use_container_width=True):
        st.switch_page("pages/5_📞_Contact.py")

# Footer with hearts
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; padding: 2rem; color: #C71585;">
    <p style="font-size: 1.1rem; margin-bottom: 0.5rem;">
        Built with 💖 using Python & Streamlit
    </p>
    <p style="font-weight: 600;">
        © 2025 {data['personal']['name']} | All Rights Reserved
    </p>
    <div style="margin-top: 1rem; font-size: 1.5rem;">
        ✨ 🌸 💖 🌸 ✨
    </div>
</div>
""", unsafe_allow_html=True)