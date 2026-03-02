import streamlit as st
import json

st.set_page_config(
    page_title="Projects - Jyoti Tiwari",
    page_icon="🚀",
    layout="wide"
)




# Load data
@st.cache_data
def load_data():
    with open('data/portfolio_data.json', 'r') as f:
        return json.load(f)


data = load_data()

st.title("🚀 My Projects")
st.markdown("End-to-end machine learning projects with production deployment")

# Filters
col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    categories = ["All"] + sorted(list(set([p['category'] for p in data['projects']])))
    selected_category = st.selectbox("Filter by Category", categories)

with col2:
    tech_list = []
    for project in data['projects']:
        tech_list.extend(project['tech_stack'])
    unique_tech = ["All"] + sorted(list(set(tech_list)))
    selected_tech = st.selectbox("Filter by Technology", unique_tech)

with col3:
    sort_by = st.selectbox("Sort by", ["Latest", "Category", "Name"])

# Filter projects
filtered_projects = data['projects']

if selected_category != "All":
    filtered_projects = [p for p in filtered_projects if p['category'] == selected_category]

if selected_tech != "All":
    filtered_projects = [p for p in filtered_projects if selected_tech in p['tech_stack']]

# Sort projects
if sort_by == "Latest":
    filtered_projects = sorted(filtered_projects, key=lambda x: x['id'], reverse=True)
elif sort_by == "Category":
    filtered_projects = sorted(filtered_projects, key=lambda x: x['category'])
elif sort_by == "Name":
    filtered_projects = sorted(filtered_projects, key=lambda x: x['name'])

st.markdown(f"**Showing {len(filtered_projects)} of {len(data['projects'])} projects**")

st.markdown("---")

# Display projects
for project in filtered_projects:
    with st.container():
        # Project header
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"### {project['name']}")
            st.markdown(f"**{project['category']}** | {project['date']}")
        
        with col2:
            # Status badge
            status = project['metrics']['status']
            status_color = "🟢" if status == "Deployed" else "🟡"
            st.markdown(f"**Status:** {status_color} {status}")
        
        # Project description
        st.markdown(project['description'])
        
        # Expandable details
        with st.expander("📋 View Details", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("**Key Highlights:**")
                for highlight in project['highlights']:
                    st.markdown(f"✓ {highlight}")
                
                st.markdown(f"**Impact:** {project['impact']}")
            
            with col2:
                st.markdown("**Tech Stack:**")
                for tech in project['tech_stack']:
                    st.markdown(f"""
                    <span style="display: inline-block; background: #E3F2FD; 
                                 color: #1976D2; padding: 0.3rem 0.8rem; 
                                 border-radius: 15px; margin: 0.2rem; 
                                 font-size: 0.85rem;">{tech}</span>
                    """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                st.markdown("**Metrics:**")
                st.markdown(f"• Accuracy: {project['metrics']['accuracy']}")
                st.markdown(f"• Deployment: {project['metrics']['deployment']}")
        
        # Action buttons
        col1, col2, col3 = st.columns([1, 1, 3])
        
        with col1:
            st.link_button("📂 View Code", project['github'], use_container_width=True)
        
        with col2:
            if project['demo_url']:
                st.link_button("🌐 Live Demo", project['demo_url'], use_container_width=True)
        
        st.markdown("---")

# Summary section
st.markdown("## 📊 Projects Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Projects", len(data['projects']))

with col2:
    deployed = len([p for p in data['projects'] if 'Deployed' in p['metrics']['status']])
    st.metric("Deployed Projects", deployed)

with col3:
    categories = len(set([p['category'] for p in data['projects']]))
    st.metric("Categories", categories)

# Technology usage
st.markdown("### 🛠️ Technologies Used")

tech_counts = {}
for project in data['projects']:
    for tech in project['tech_stack']:
        tech_counts[tech] = tech_counts.get(tech, 0) + 1

sorted_tech = sorted(tech_counts.items(), key=lambda x: x[1], reverse=True)[:10]

cols = st.columns(5)
for i, (tech, count) in enumerate(sorted_tech):
    with cols[i % 5]:
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem; background: #f8f9fa; 
                    border-radius: 10px; margin: 0.5rem 0;">
            <strong>{tech}</strong><br>
            <span style="color: #667eea; font-size: 1.5rem;">{count}</span> projects
        </div>
        """, unsafe_allow_html=True)