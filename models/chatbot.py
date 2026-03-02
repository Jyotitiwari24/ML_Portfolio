import streamlit as st
import json


def load_resume_data():
    """
    Load resume/portfolio data for chatbot
    """
    with open('data/portfolio_data.json', 'r') as f:
        return json.load(f)


def simple_chatbot_response(question, data):
    """
    Simple rule-based chatbot
    For production, replace with actual NLP model
    """
    question_lower = question.lower()
    
    # Skills questions
    if any(word in question_lower for word in ['skill', 'technology', 'tech stack', 'programming']):
        skills_list = []
        for category, skills in data['skills'].items():
            for skill, prof in skills.items():
                if prof >= 75:
                    skills_list.append(f"{skill} ({prof}%)")
        
        return f"I have expertise in: {', '.join(skills_list[:10])}. My strongest skills are Python, ML frameworks (scikit-learn, TensorFlow, XGBoost), and MLOps tools (Docker, FastAPI)."
    
    # Projects questions
    elif any(word in question_lower for word in ['project', 'work', 'built', 'created']):
        project_count = len(data['projects'])
        top_projects = [p['name'] for p in data['projects'][:3]]
        return f"I've completed {project_count}+ production-ready ML projects. Some highlights: {', '.join(top_projects)}. All projects are deployed with Docker and FastAPI."
    
    # Experience questions
    elif any(word in question_lower for word in ['experience', 'background', 'qualification']):
        edu = data['education'][0]
        return f"I hold an {edu['degree']} from {edu['institution']} with {edu['grade']} grade. I specialize in MLOps and have deployed 9+ ML models to production."
    
    # MLOps questions
    elif 'mlops' in question_lower:
        return "I specialize in MLOps with hands-on experience in Docker containerization, FastAPI deployment, CI/CD pipelines with GitHub Actions, model monitoring with Prometheus/Grafana, and cloud deployment on AWS."
    
    # Contact questions
    elif any(word in question_lower for word in ['contact', 'email', 'reach', 'hire']):
        return f"You can reach me at {data['personal']['email']} or connect on LinkedIn: {data['personal']['linkedin']}. I'm available for immediate joining!"
    
    # Location/availability
    elif any(word in question_lower for word in ['location', 'available', 'join', 'start']):
        return f"I'm based in {data['personal']['location']} and available for {data['personal']['availability']}. Open to remote work and relocation."
    
    # Salary/compensation
    elif any(word in question_lower for word in ['salary', 'compensation', 'ctc', 'package']):
        return "I'm looking for competitive compensation based on industry standards for ML/MLOps roles. I'm flexible and open to discussing based on the role and responsibilities."
    
    # Default response
    else:
        return f"I'm an ML/MLOps Engineer with {len(data['projects'])}+ deployed projects. I specialize in building production-ready ML systems using Python, Docker, FastAPI, and cloud technologies. How can I help you learn more about my background?"


def display_chatbot():
    """
    Display chatbot interface in Streamlit
    """
    st.markdown("### 🤖 Ask Me Anything!")
    st.markdown("Chat with my AI assistant to learn about my background, skills, and projects.")
    
    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
        data = load_resume_data()
        st.session_state.chat_history.append({
            'role': 'assistant',
            'content': f"Hi! I'm Jyoti's AI assistant. I can answer questions about her skills, projects, and experience. What would you like to know?"
        })
    
    # Display chat history
    for message in st.session_state.chat_history:
        if message['role'] == 'user':
            st.markdown(f"""
            <div style="background: #E3F2FD; padding: 1rem; border-radius: 10px; 
                        margin: 0.5rem 0; text-align: right;">
                👤 <strong>You:</strong> {message['content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="background: #F3E5F5; padding: 1rem; border-radius: 10px; 
                        margin: 0.5rem 0;">
                🤖 <strong>Assistant:</strong> {message['content']}
            </div>
            """, unsafe_allow_html=True)
    
    # Suggested questions
    st.markdown("**💡 Try asking:**")
    cols = st.columns(3)
    
    suggestions = [
        "What are your technical skills?",
        "Tell me about your projects",
        "What's your experience?",
        "How can I contact you?",
        "What is your availability?",
        "Tell me about your MLOps skills"
    ]
    
    for i, suggestion in enumerate(suggestions):
        with cols[i % 3]:
            if st.button(suggestion, key=f"suggest_{i}"):
                st.session_state.pending_question = suggestion
    
    # Check for pending question from button
    if 'pending_question' in st.session_state:
        user_input = st.session_state.pending_question
        del st.session_state.pending_question
    else:
        # User input
        user_input = st.chat_input("Type your question here...")
    
    # Process input
    if user_input:
        # Add user message
        st.session_state.chat_history.append({
            'role': 'user',
            'content': user_input
        })
        
        # Generate response
        data = load_resume_data()
        response = simple_chatbot_response(user_input, data)
        
        # Add assistant response
        st.session_state.chat_history.append({
            'role': 'assistant',
            'content': response
        })
        
        # Rerun to display new messages
        st.rerun()
    
    # Clear chat button
    if len(st.session_state.chat_history) > 1:
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = [{
                'role': 'assistant',
                'content': "Hi! I'm Jyoti's AI assistant. What would you like to know?"
            }]
            st.rerun()


