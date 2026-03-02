import requests
import streamlit as st


@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_github_stats(username):
    """
    Fetch GitHub statistics for a user
    """
    try:
        # User info
        user_url = f"https://api.github.com/users/{username}"
        user_response = requests.get(user_url, timeout=5)
        user_data = user_response.json()
        
        # Repositories
        repos_url = f"https://api.github.com/users/{username}/repos"
        repos_response = requests.get(repos_url, timeout=5)
        repos_data = repos_response.json()
        
        # Calculate stats
        total_stars = sum([repo.get('stargazers_count', 0) for repo in repos_data])
        total_forks = sum([repo.get('forks_count', 0) for repo in repos_data])
        
        # Language stats
        languages = {}
        for repo in repos_data:
            lang = repo.get('language')
            if lang:
                languages[lang] = languages.get(lang, 0) + 1
        
        stats = {
            'public_repos': user_data.get('public_repos', 0),
            'followers': user_data.get('followers', 0),
            'following': user_data.get('following', 0),
            'total_stars': total_stars,
            'total_forks': total_forks,
            'languages': languages,
            'top_repos': sorted(repos_data, key=lambda x: x.get('stargazers_count', 0), reverse=True)[:5]
        }
        
        return stats
    
    except Exception as e:
        st.error(f"Error fetching GitHub stats: {e}")
        return None

def display_github_stats(username):
    """
    Display GitHub statistics in Streamlit
    """
    stats = fetch_github_stats(username)
    
    if stats:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Public Repos", stats['public_repos'])
        with col2:
            st.metric("Total Stars", stats['total_stars'])
        with col3:
            st.metric("Followers", stats['followers'])
        with col4:
            st.metric("Total Forks", stats['total_forks'])
        
        # Top languages
        if stats['languages']:
            st.markdown("### 🔤 Top Languages")
            import plotly.express as px
            
            fig = px.pie(
                names=list(stats['languages'].keys()),
                values=list(stats['languages'].values()),
                hole=0.4
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Top repositories
        st.markdown("### ⭐ Top Repositories")
        for repo in stats['top_repos']:
            st.markdown(f"""
            **[{repo['name']}]({repo['html_url']})**
            - ⭐ {repo['stargazers_count']} | 🍴 {repo['forks_count']} | 📝 {repo.get('language', 'N/A')}
            - {repo.get('description', 'No description')}
            """)