import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def create_skill_radar(skills_dict):
    """
    Create a radar chart for skills
    """
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=list(skills_dict.values()),
        theta=list(skills_dict.keys()),
        fill='toself',
        fillcolor='rgba(102, 126, 234, 0.3)',
        line=dict(color='rgb(102, 126, 234)', width=2)
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False
    )
    
    return fig


def create_project_timeline(projects):
    """
    Create a timeline visualization for projects
    """
    # Convert project dates to timeline format
    df = pd.DataFrame(projects)
    df['start_date'] = pd.to_datetime(df['date'], format='%B %Y')
    
    fig = px.timeline(
        df,
        x_start='start_date',
        y='name',
        color='category',
        title="Project Timeline"
    )
    
    return fig


def create_tech_stack_sunburst(projects):
    """
    Create sunburst chart showing technology usage
    """
    # Flatten tech stack
    tech_data = []
    for project in projects:
        for tech in project['tech_stack']:
            tech_data.append({
                'project': project['name'],
                'category': project['category'],
                'tech': tech
            })
    
    df = pd.DataFrame(tech_data)
    
    fig = px.sunburst(
        df,
        path=['category', 'tech'],
        title="Technology Stack Distribution"
    )
    
    return fig


def create_accuracy_chart(projects):
    """
    Create bar chart comparing project accuracies
    """
    # Extract accuracy values
    data = []
    for project in projects:
        accuracy_str = project['metrics']['accuracy']
        if accuracy_str != 'N/A':
            # Parse accuracy (handle different formats)
            try:
                if '%' in accuracy_str:
                    accuracy = float(accuracy_str.replace('%', ''))
                elif 'R²' in accuracy_str:
                    accuracy = float(accuracy_str.split('=')[1].strip()) * 100
                else:
                    accuracy = float(accuracy_str)
                
                data.append({
                    'name': project['name'],
                    'accuracy': accuracy,
                    'category': project['category']
                })
            except:
                pass
    
    df = pd.DataFrame(data)
    
    fig = px.bar(
        df,
        x='accuracy',
        y='name',
        orientation='h',
        color='category',
        title="Project Performance Comparison",
        labels={'accuracy': 'Accuracy (%)', 'name': 'Project'}
    )
    
    return fig