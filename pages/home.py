import streamlit as st
import json
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Home - Jyoti Tiwari",
    page_icon="🏠",
    layout="wide"
)




# Load data
@st.cache_data
def load_data():
    with open('data/portfolio_data.json', 'r') as f:
        return json.load(f)


data = load_data()

# Hero Section
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
    <h1 style="font-size: 3.5rem; margin-bottom: 0;">
        Hi, I'm <span style="background: linear-gradient(120deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        {data['personal']['name']}</span> 👋
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown(f"### {data['personal']['title']}")
    st.markdown(data['personal']['bio'])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # CTA Buttons
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    
    with col_btn1:
        st.link_button("📧 Email Me", f"mailto:{data['personal']['email']}", use_container_width=True)
    with col_btn2:
        st.link_button("💼 LinkedIn", data['personal']['linkedin'], use_container_width=True)
    with col_btn3:
        st.link_button("🐙 GitHub", data['personal']['github'], use_container_width=True)

with col2:
    # GitHub profile picture or placeholder
    st.image(f"https://github.com/Jyotitiwari24.png", width=350)

st.markdown("---")

# Stats Overview
st.markdown("## 📊 Portfolio Overview")

col1, col2, col3, col4 = st.columns(4)

stats = [
    ("🎯", len(data['projects']), "Projects Completed"),
    ("🚀", len([p for p in data['projects'] if p['metrics']['status'] == 'Deployed']), "Models Deployed"),
    ("⭐", "150+", "GitHub Commits"),
    ("🏆", len(data['certifications']), "Certifications")
]

for col, (icon, value, label) in zip([col1, col2, col3, col4], stats):
    with col:
        st.markdown(f"""
        <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 15px; color: white;">
            <div style="font-size: 2.5rem;">{icon}</div>
            <h2 style="margin: 0.5rem 0;">{value}</h2>
            <p style="margin: 0; opacity: 0.9;">{label}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Skills Overview
st.markdown("## 💻 Technical Expertise")

tab1, tab2, tab3 = st.tabs(["Programming", "ML/DL", "MLOps"])

with tab1:
    skills_data = data['skills']['programming']
    fig = px.bar(
        x=list(skills_data.values()),
        y=list(skills_data.keys()),
        orientation='h',
        title="Programming Languages Proficiency",
        color=list(skills_data.values()),
        color_continuous_scale='Viridis'
    )
    fig.update_layout(showlegend=False, xaxis_title="Proficiency %", yaxis_title="")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    skills_data = data['skills']['ml_frameworks']
    fig = px.bar(
        x=list(skills_data.values()),
        y=list(skills_data.keys()),
        orientation='h',
        title="ML/DL Frameworks Proficiency",
        color=list(skills_data.values()),
        color_continuous_scale='Blues'
    )
    fig.update_layout(showlegend=False, xaxis_title="Proficiency %", yaxis_title="")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    skills_data = data['skills']['mlops']
    fig = px.bar(
        x=list(skills_data.values()),
        y=list(skills_data.keys()),
        orientation='h',
        title="MLOps Tools Proficiency",
        color=list(skills_data.values()),
        color_continuous_scale='Purples'
    )
    fig.update_layout(showlegend=False, xaxis_title="Proficiency %", yaxis_title="")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Project Categories
st.markdown("## 🚀 Project Categories")

# Count projects by category
category_counts = {}
for project in data['projects']:
    cat = project['category']
    category_counts[cat] = category_counts.get(cat, 0) + 1

fig = px.pie(
    names=list(category_counts.keys()),
    values=list(category_counts.values()),
    title="Projects Distribution",
    hole=0.4,
    color_discrete_sequence=px.colors.sequential.Purples
)
st.plotly_chart(fig, use_container_width=True)

# Education
st.markdown("## 🎓 Education")

for edu in data['education']:
    with st.expander(f"**{edu['degree']}** - {edu['institution']}", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**Duration:** {edu['year']}")
            st.markdown(f"**Grade:** {edu['grade']}")
        
        with col2:
            st.markdown("**Key Areas:**")
            for highlight in edu['highlights']:
                st.markdown(f"• {highlight}")

# Call to Action
st.markdown("---")

st.markdown("""
<div style="text-align: center; padding: 3rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px; color: white;">
    <h2>Let's Build Something Amazing Together!</h2>
    <p style="font-size: 1.2rem;">I'm currently seeking ML/MLOps opportunities</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("📞 Contact Me", use_container_width=True):
        st.switch_page("pages/5_📞_Contact.py")