import streamlit as st
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="Skills - Jyoti Tiwari",
    page_icon="💻",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    with open('data/portfolio_data.json', 'r') as f:
        return json.load(f)

data = load_data()

st.title("💻 Skills & Experience")
st.markdown("Technical expertise and professional journey")

st.markdown("---")

# Skills Overview
st.markdown("## 🛠️ Technical Skills")

# Create tabs for different skill categories
tabs = st.tabs(["📊 Overview", "🐍 Programming", "🤖 ML/DL", "🚀 MLOps", "☁️ Cloud", "📝 NLP"])

# Tab 1: Overview - Radar Chart
with tabs[0]:
    # Combine all skills for overview
    all_skills = {}
    for category, skills in data['skills'].items():
        for skill, prof in skills.items():
            all_skills[skill] = prof
    
    # Top 10 skills
    top_skills = sorted(all_skills.items(), key=lambda x: x[1], reverse=True)[:10]
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Radar chart
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=[s[1] for s in top_skills],
            theta=[s[0] for s in top_skills],
            fill='toself',
            fillcolor='rgba(102, 126, 234, 0.3)',
            line=dict(color='rgb(102, 126, 234)', width=2),
            name='Proficiency'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    tickfont=dict(size=10)
                )
            ),
            showlegend=False,
            title="Top 10 Skills Proficiency",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🏆 Skill Highlights")
        
        for skill, prof in top_skills[:5]:
            st.markdown(f"**{skill}**")
            st.progress(prof / 100)
            st.markdown(f"{prof}% Proficiency")
            st.markdown("<br>", unsafe_allow_html=True)

# Tab 2: Programming
with tabs[1]:
    st.markdown("### Programming Languages")
    
    skills_data = data['skills']['programming']
    
    # Create DataFrame
    df = pd.DataFrame(list(skills_data.items()), columns=['Language', 'Proficiency'])
    
    # Bar chart
    fig = px.bar(
        df,
        x='Proficiency',
        y='Language',
        orientation='h',
        color='Proficiency',
        color_continuous_scale='Viridis',
        text='Proficiency'
    )
    
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(
        showlegend=False,
        xaxis_title="Proficiency Level (%)",
        yaxis_title="",
        height=400,
        xaxis=dict(range=[0, 100])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Skill details
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🐍 Python")
        st.markdown("""
        - **Experience:** 3+ years
        - **Use Cases:** ML/DL, Data Science, Web APIs
        - **Libraries:** NumPy, Pandas, Scikit-learn, TensorFlow
        - **Projects:** All 9 projects use Python
        """)
    
    with col2:
        st.markdown("#### 🗄️ SQL")
        st.markdown("""
        - **Experience:** 2+ years
        - **Databases:** MySQL, PostgreSQL
        - **Skills:** Complex queries, Joins, Optimization
        - **Use Cases:** Data analysis, ETL pipelines
        """)

# Tab 3: ML/DL
with tabs[2]:
    st.markdown("### Machine Learning & Deep Learning")
    
    skills_data = data['skills']['ml_frameworks']
    df = pd.DataFrame(list(skills_data.items()), columns=['Framework', 'Proficiency'])
    
    fig = px.bar(
        df,
        x='Proficiency',
        y='Framework',
        orientation='h',
        color='Proficiency',
        color_continuous_scale='Blues',
        text='Proficiency'
    )
    
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(
        showlegend=False,
        xaxis_title="Proficiency Level (%)",
        yaxis_title="",
        height=400,
        xaxis=dict(range=[0, 100])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ML Expertise breakdown
    st.markdown("### 🎯 ML Expertise Areas")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Supervised Learning**
        - ✅ Classification
        - ✅ Regression
        - ✅ Ensemble Methods
        - ✅ SVM, Random Forest
        - ✅ XGBoost, LightGBM
        """)
    
    with col2:
        st.markdown("""
        **Unsupervised Learning**
        - ✅ Clustering (K-Means)
        - ✅ Dimensionality Reduction
        - ✅ PCA, t-SNE
        - ✅ Anomaly Detection
        """)
    
    with col3:
        st.markdown("""
        **Deep Learning**
        - ✅ Neural Networks
        - ✅ CNNs (Computer Vision)
        - ✅ RNNs, LSTMs
        - ✅ Transfer Learning
        - ✅ TensorFlow, Keras
        """)

# Tab 4: MLOps
with tabs[3]:
    st.markdown("### MLOps & DevOps")
    
    skills_data = data['skills']['mlops']
    df = pd.DataFrame(list(skills_data.items()), columns=['Tool', 'Proficiency'])
    
    fig = px.bar(
        df,
        x='Proficiency',
        y='Tool',
        orientation='h',
        color='Proficiency',
        color_continuous_scale='Purples',
        text='Proficiency'
    )
    
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(
        showlegend=False,
        xaxis_title="Proficiency Level (%)",
        yaxis_title="",
        height=400,
        xaxis=dict(range=[0, 100])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # MLOps Pipeline
    st.markdown("### 🔄 My MLOps Pipeline")
    
    st.markdown("""
                Data Collection → Preprocessing → Feature Engineering
        ↓
Model Training → Hyperparameter Tuning → Model Evaluation
        ↓
Model Registry (MLflow) → CI/CD Pipeline (GitHub Actions)
        ↓
Containerization (Docker) → Deployment (FastAPI)
        ↓
Monitoring (Prometheus/Grafana) → Auto-Retraining (Airflow)
                """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🐳 Docker")
        st.markdown("""
        - Containerize ML applications
        - Multi-stage builds for optimization
        - Docker Compose for multi-service apps
        - **9/9 projects** are Dockerized
        """)
    
    with col2:
        st.markdown("#### ⚡ FastAPI")
        st.markdown("""
        - RESTful API development
        - Automatic documentation (Swagger)
        - Input validation with Pydantic
        - Async support for high performance
        """)

# Tab 5: Cloud
with tabs[4]:
    st.markdown("### Cloud & Deployment")
    
    skills_data = data['skills']['cloud']
    df = pd.DataFrame(list(skills_data.items()), columns=['Service', 'Proficiency'])
    
    fig = px.bar(
        df,
        x='Proficiency',
        y='Service',
        orientation='h',
        color='Proficiency',
        color_continuous_scale='Oranges',
        text='Proficiency'
    )
    
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(
        showlegend=False,
        xaxis_title="Proficiency Level (%)",
        yaxis_title="",
        height=300,
        xaxis=dict(range=[0, 100])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("#### ☁️ AWS Services")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Compute**
        - EC2 (Virtual Servers)
        - Lambda (Serverless)
        - ECS (Containers)
        """)
    
    with col2:
        st.markdown("""
        **Storage**
        - S3 (Object Storage)
        - EBS (Block Storage)
        - RDS (Databases)
        """)
    
    with col3:
        st.markdown("""
        **ML Services**
        - SageMaker
        - ECR (Container Registry)
        - CloudWatch (Monitoring)
        """)

# Tab 6: NLP
with tabs[5]:
    st.markdown("### Natural Language Processing")
    
    skills_data = data['skills']['nlp']
    df = pd.DataFrame(list(skills_data.items()), columns=['Skill', 'Proficiency'])
    
    fig = px.bar(
        df,
        x='Proficiency',
        y='Skill',
        orientation='h',
        color='Proficiency',
        color_continuous_scale='Greens',
        text='Proficiency'
    )
    
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(
        showlegend=False,
        xaxis_title="Proficiency Level (%)",
        yaxis_title="",
        height=400,
        xaxis=dict(range=[0, 100])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("#### 📝 NLP Projects")
    
    nlp_projects = [p for p in data['projects'] if p['category'] in ['NLP', 'NLP/LLM']]
    
    for project in nlp_projects:
        st.markdown(f"""
        **{project['name']}**
        - {project['description']}
        - Accuracy: {project['metrics']['accuracy']}
        """)

st.markdown("---")

# Education Section
st.markdown("## 🎓 Education")

for edu in data['education']:
    with st.expander(f"**{edu['degree']}**", expanded=False):
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown(f"### {edu['degree']}")
            st.markdown(f"**{edu['institution']}**")
            st.markdown(f"📅 {edu['year']}")
            st.markdown(f"🏆 **Grade:** {edu['grade']}")
        
        with col2:
            st.markdown("**Key Highlights:**")
            for highlight in edu['highlights']:
                st.markdown(f"✓ {highlight}")

st.markdown("---")

# Certifications
st.markdown("## 🏅 Certifications")

for cert in data['certifications']:
    st.markdown(f"""
    <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; 
                margin: 0.5rem 0; border-left: 4px solid #667eea;">
        <strong>{cert['name']}</strong><br>
        <small>{cert['issuer']} | {cert['date']}</small>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Interests
st.markdown("## 🎯 Areas of Interest")

cols = st.columns(len(data['interests']))
for col, interest in zip(cols, data['interests']):
    with col:
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 15px; color: white;">
            {interest}
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Learning Journey
st.markdown("## 📚 Continuous Learning")

st.markdown("""
I believe in continuous learning and staying updated with the latest in ML/AI:

- **Currently Learning:** Advanced MLOps, Kubernetes, LLM Fine-tuning
- **Reading:** Latest research papers on arXiv
- **Practice:** Daily DSA problems on LeetCode
- **Building:** New projects integrating cutting-edge technologies

**Learning Resources I Use:**
- Coursera, Udemy for structured courses
- YouTube (StatQuest, Krish Naik, Abhishek Thakur)
- Medium, Towards Data Science for articles
- GitHub for open-source contributions
""")