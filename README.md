# 🤖 Jyoti Kumari Tiwari - ML/MLOps Portfolio

Interactive portfolio showcasing 9+ production-ready machine learning projects with complete MLOps deployment.

## 🌟 Features

- **Live Project Demos** - Interactive ML model demonstrations
- **Comprehensive Project Showcase** - Detailed view of all 9 deployed projects
- **Skills Visualization** - Interactive charts showing technical proficiency
- **Technical Blog** - Articles on ML/MLOps best practices
- **AI Chatbot** - Ask questions about my background and skills
- **GitHub Integration** - Live stats from GitHub profile
- **Contact Form** - Direct communication channel
- **Mobile Responsive** - Works seamlessly on all devices

## 🛠️ Tech Stack

- **Frontend:** Python + Streamlit
- **Data Visualization:** Plotly, Pandas
- **APIs:** GitHub API
- **NLP:** TextBlob (for sentiment demo)
- **Deployment:** Streamlit Cloud (FREE)

## 📦 Installation
```bash
# Clone repository
git clone https://github.com/Jyotitiwari24/ml-portfolio.git
cd ml-portfolio

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Run Locally
```bash
streamlit run app.py
```

Visit: `http://localhost:8501`

## 📂 Project Structure
```
ml-portfolio/
├── app.py                      # Main entry point
├── pages/
│   ├── 1_🏠_Home.py           # Home page
│   ├── 2_🚀_Projects.py       # Projects showcase
│   ├── 3_💻_Skills.py         # Skills & experience
│   ├── 4_📝_Blog.py           # Technical blog
│   └── 5_📞_Contact.py        # Contact page
├── utils/
│   ├── github_stats.py        # GitHub API integration
│   └── data_viz.py            # Visualization utilities
├── models/
│   ├── sentiment_model.py     # Sentiment analysis demo
│   └── chatbot.py             # AI chatbot
├── data/
│   └── portfolio_data.json    # Portfolio data
├── assets/
│   └── (images)
├── requirements.txt
├── .streamlit/
│   └── config.toml
└── README.md
```

## 🚀 Deployment

### Deploy to Streamlit Cloud (FREE)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub repository
4. Select `app.py` as main file
5. Deploy!

**Your portfolio will be live at:** `https://yourname.streamlit.app`

## 🎨 Customization

### Update Personal Information

Edit `data/portfolio_data.json`:
```json
{
  "personal": {
    "name": "Your Name",
    "email": "your.email@example.com",
    ...
  }
}
```

### Add New Projects

Add to `projects` array in `portfolio_data.json`:
```json
{
  "name": "Project Name",
  "description": "Description",
  "tech_stack": ["Python", "Docker"],
  ...
}
```

### Modify Styling

Edit colors in `.streamlit/config.toml`:
```toml
[theme]
primaryColor="#667eea"
backgroundColor="#FFFFFF"
...
```

## 📊 Features Breakdown

### Home Page
- Professional hero section
- Quick stats overview
- Skills radar chart
- Featured projects preview

### Projects Page
- Filterable project gallery
- Detailed project information
- Technology stack visualization
- GitHub links

### Skills Page
- Interactive skill charts
- Technology proficiency breakdown
- Education timeline
- Certifications

### Blog Page
- Technical articles
- ML/MLOps tutorials
- Project walkthroughs
- Best practices

### Contact Page
- Contact form
- Direct contact information
- FAQ section
- Resume download

## 🤖 Interactive Features

### Sentiment Analysis Demo
- Live text sentiment analysis
- Confidence scoring
- Text statistics

### AI Chatbot
- Answer questions about background
- Skills and project information
- Natural language interaction

### GitHub Stats
- Live repository statistics
- Language distribution
- Top repositories

## 📱 Mobile Responsive

Portfolio is fully responsive and works on:
- Desktop (1920px+)
- Laptop (1366px)
- Tablet (768px)
- Mobile (375px)

## 🔒 Privacy & Security

- No user data collected
- No tracking or analytics
- Open source code
- Self-hosted on Streamlit Cloud

## 📄 License

MIT License - Feel free to use this template for your own portfolio!

## 👤 Author

**Jyoti Kumari Tiwari**
- Email: jyoti81tiwari@gmail.com
- LinkedIn: [linkedin.com/in/Jyotitiwari24](https://linkedin.com/in/Jyotitiwari24)
- GitHub: [github.com/Jyotitiwari24](https://github.com/Jyotitiwari24)

## 🙏 Acknowledgments

- Streamlit for amazing framework
- Plotly for beautiful visualizations
- Open source community

## 📝 Updates

**v1.0.0** (March 2025)
- Initial release
- 9 projects showcase
- Interactive demos
- AI chatbot
- Blog section

---

**⭐ If you find this portfolio template helpful, please star this repository!**

Built with ❤️ using Python & Streamlit
```

---

## **FILE 15: .gitignore**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Streamlit
.streamlit/secrets.toml

# Logs
*.log

# Data
*.csv
*.xlsx
*.pkl
!models/*.pkl

# Environment variables
.env