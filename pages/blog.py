import streamlit as st
import json
from datetime import datetime

st.set_page_config(
    page_title="Blog - Jyoti Tiwari",
    page_icon="📝",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    with open('data/portfolio_data.json', 'r') as f:
        return json.load(f)

data = load_data()

st.title("📝 Technical Blog & Articles")
st.markdown("Sharing my learning journey, insights, and technical deep-dives")

st.markdown("---")

# Blog categories
categories = st.multiselect(
    "Filter by Category",
    ["All", "MLOps", "Machine Learning", "Deep Learning", "NLP", "Tutorial", "Project Walkthrough"],
    default=["All"]
)

st.markdown("---")

# Blog posts (You can expand this with actual blog posts)
blog_posts = [
    {
        "title": "Building Production-Ready ML Systems: My MLOps Journey",
        "date": "January 2025",
        "category": "MLOps",
        "read_time": "8 min read",
        "summary": "A comprehensive guide on deploying machine learning models to production, covering Docker, FastAPI, monitoring, and CI/CD pipelines.",
        "tags": ["MLOps", "Docker", "FastAPI", "Production ML"],
        "content": """
## Introduction

After deploying 9+ machine learning models to production, I've learned valuable lessons about what it takes to build reliable ML systems. This article shares my journey and best practices.

### Key Takeaways

1. **Containerization is Essential**
   - Docker ensures consistency across environments
   - Makes deployment reproducible
   - Simplifies dependency management

2. **API Design Matters**
   - FastAPI for automatic documentation
   - Proper input validation with Pydantic
   - Error handling and logging

3. **Monitoring is Non-Negotiable**
   - Track model performance over time
   - Detect data drift early
   - Set up alerting for failures

4. **CI/CD Automation**
   - Automated testing on every commit
   - Continuous deployment for faster iterations
   - Version control for models and data

### Real-World Example: Fraud Detection System

My fraud detection MLOps system includes:
- **Training Pipeline:** Automated with Airflow
- **Model Registry:** MLflow for version control
- **Deployment:** Docker + FastAPI
- **Monitoring:** Prometheus + Grafana
- **Alerting:** Slack notifications for anomalies

### Lessons Learned

**1. Start Simple:** Don't over-engineer initially. Get a basic pipeline working first.

**2. Test Everything:** Unit tests for code, integration tests for APIs, performance tests for latency.

**3. Document Thoroughly:** Future you will thank present you.

**4. Monitor Proactively:** Don't wait for users to report issues.

### Tools I Recommend

- **Docker:** Containerization
- **FastAPI:** API framework
- **MLflow:** Experiment tracking
- **Prometheus + Grafana:** Monitoring
- **GitHub Actions:** CI/CD

### Conclusion

MLOps is not just about deploying models—it's about building reliable, scalable systems that deliver value consistently. Start small, iterate fast, and always monitor.

**Connect with me** if you have questions or want to discuss MLOps!
        """
    },
    {
        "title": "From Jupyter Notebook to Production API: A Complete Guide",
        "date": "December 2024",
        "category": "Tutorial",
        "read_time": "10 min read",
        "summary": "Step-by-step tutorial on taking a machine learning model from experimentation in Jupyter to a production-ready API deployed with Docker.",
        "tags": ["Tutorial", "FastAPI", "Docker", "Deployment"],
        "content": """
## From Notebook to Production

Many data scientists can train models in Jupyter notebooks, but struggle with deployment. This guide bridges that gap.

### Step 1: Clean Your Notebook Code
```pythonBad: Everything in one cell
Good: Organized functionsdef load_data():
# Data loading logic
passdef preprocess(df):
# Preprocessing logic
passdef train_model(X, y):
# Training logic
pass

### Step 2: Create a Training Script

Convert notebook to `train.py`:
```pythonimport pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblibdef train_pipeline():
# Load data
df = pd.read_csv('data.csv')# Preprocess
X, y = preprocess(df)# Train
model = RandomForestClassifier()
model.fit(X, y)# Save
joblib.dump(model, 'model.pkl')if name == "main":
train_pipeline()

### Step 3: Build FastAPI Endpoint

Create `app.py`:
```pythonfrom fastapi import FastAPI
from pydantic import BaseModel
import joblibapp = FastAPI()
model = joblib.load('model.pkl')class PredictionInput(BaseModel):
feature1: float
feature2: float
# ... other features@app.post("/predict")
def predict(data: PredictionInput):
prediction = model.predict([[data.feature1, data.feature2]])
return {"prediction": int(prediction[0])}

### Step 4: Dockerize

Create `Dockerfile`:
```dockerfileFROM python:3.9-slimWORKDIR /appCOPY requirements.txt .
RUN pip install -r requirements.txtCOPY . .CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

### Step 5: Deploy
```bashdocker build -t ml-api .
docker run -p 8000:8000 ml-api

Your API is now running at `http://localhost:8000`!

### Testing
```bashcurl -X POST http://localhost:8000/predict 
-H "Content-Type: application/json" 
-d '{"feature1": 1.0, "feature2": 2.0}'
### Best Practices

1. **Validate inputs** with Pydantic
2. **Add health check** endpoint
3. **Log predictions** for monitoring
4. **Version your model** 
5. **Write tests**

### Conclusion

Deployment doesn't have to be scary. Follow these steps and you'll have a production-ready API in no time!
        """
    },
    {
        "title": "Handling Imbalanced Datasets: Techniques That Actually Work",
        "date": "November 2024",
        "category": "Machine Learning",
        "read_time": "7 min read",
        "summary": "Practical techniques for dealing with imbalanced datasets in real-world ML projects, with code examples and performance comparisons.",
        "tags": ["Machine Learning", "Data Science", "Imbalanced Data"],
        "content": """
## The Imbalanced Data Problem

In my fraud detection project, only 1% of transactions were fraudulent. This is a classic imbalanced dataset problem.

### Why It's a Problem

If you train a model that always predicts "not fraud," you get 99% accuracy—but catch zero fraud cases!

### Techniques That Work

#### 1. Resampling

**Oversampling (SMOTE):**
```pythonfrom imblearn.over_sampling import SMOTEsmote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

**Undersampling:**
```pythonfrom imblearn.under_sampling import RandomUnderSamplerrus = RandomUnderSampler(random_state=42)
X_resampled, y_resampled = rus.fit_resample(X, y)

#### 2. Class Weights
```pythonfrom sklearn.ensemble import RandomForestClassifiermodel = RandomForestClassifier(class_weight='balanced')
model.fit(X_train, y_train)

#### 3. Ensemble Methods

Use algorithms that handle imbalance well:
- XGBoost with `scale_pos_weight`
- Random Forest with `class_weight`

#### 4. Evaluation Metrics

**Don't use accuracy!**

Use instead:
- **Precision:** Of predicted positives, how many are correct?
- **Recall:** Of actual positives, how many did we catch?
- **F1-Score:** Harmonic mean of precision and recall
- **ROC-AUC:** Area under ROC curve
```pythonfrom sklearn.metrics import classification_report, roc_auc_scoreprint(classification_report(y_test, y_pred))
print(f"ROC-AUC: {roc_auc_score(y_test, y_pred_proba)}")

### My Results

| Method | Accuracy | Precision | Recall | F1 |
|--------|----------|-----------|--------|-----|
| Baseline | 99% | 0% | 0% | 0% |
| SMOTE | 85% | 72% | 68% | 0.70 |
| Class Weights | 87% | 75% | 70% | 0.72 |
| XGBoost | 89% | 78% | 75% | **0.76** |

### Recommendation

1. **Start with class weights** - easiest to implement
2. **Try SMOTE** if that doesn't work
3. **Use XGBoost** for best results
4. **Always evaluate with F1/ROC-AUC**, not accuracy

### Conclusion

Imbalanced datasets are common in real-world ML. Don't let high accuracy fool you—use proper techniques and metrics!
        """
    },
    {
        "title": "5 Mistakes I Made Deploying My First ML Model",
        "date": "October 2024",
        "category": "Project Walkthrough",
        "read_time": "6 min read",
        "summary": "Lessons learned from my first ML deployment experience—mistakes to avoid and best practices to follow.",
        "tags": ["Deployment", "Lessons Learned", "Best Practices"],
        "content": """
## My First Deployment Journey

When I deployed my first ML model, I made every mistake in the book. Here's what I learned.

### Mistake 1: Not Saving Preprocessing Steps

**What I did wrong:**
```pythonTrained model
model.fit(X_scaled, y)
joblib.dump(model, 'model.pkl')

**The problem:** At prediction time, I forgot how I scaled the data!

**The fix:**
```pythonSave scaler too!
from sklearn.pipeline import Pipelinepipeline = Pipeline([
('scaler', StandardScaler()),
('model', RandomForestClassifier())
])pipeline.fit(X, y)
joblib.dump(pipeline, 'pipeline.pkl')

### Mistake 2: No Input Validation

**What I did wrong:**
```python@app.post("/predict")
def predict(data: dict):
prediction = model.predict([list(data.values())])
return {"prediction": prediction}

**The problem:** Any garbage input would crash the API!

**The fix:**
```pythonfrom pydantic import BaseModel, validatorclass PredictionInput(BaseModel):
age: int
income: float@validator('age')
def age_valid(cls, v):
    if v < 0 or v > 120:
        raise ValueError('Invalid age')
    return v

### Mistake 3: Not Handling Errors

**What I did wrong:**
Let exceptions crash the API

**The fix:**
```pythonfrom fastapi import HTTPException@app.post("/predict")
def predict(data: PredictionInput):
try:
prediction = model.predict([data.dict().values()])
return {"prediction": int(prediction[0])}
except Exception as e:
raise HTTPException(status_code=500, detail=str(e))

### Mistake 4: No Logging

**What I did wrong:**
No idea what was happening in production

**The fix:**
```pythonimport logginglogging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name)@app.post("/predict")
def predict(data: PredictionInput):
logger.info(f"Received prediction request: {data}")
prediction = model.predict([data.dict().values()])
logger.info(f"Prediction: {prediction}")
return {"prediction": int(prediction[0])}

### Mistake 5: Not Monitoring Performance

**What I did wrong:**
Deployed and forgot about it

**The fix:**
- Track prediction latency
- Log all predictions
- Monitor accuracy over time
- Set up alerts for anomalies

### Key Takeaways

1. **Save everything:** Model, scaler, preprocessing steps
2. **Validate inputs:** Use Pydantic models
3. **Handle errors gracefully:** Don't crash on bad input
4. **Log everything:** You'll thank yourself later
5. **Monitor continuously:** Models degrade over time

### Conclusion

Deployment is a learning process. Make mistakes, learn from them, and improve. These lessons saved me countless hours of debugging!
        """
    }
]

# Display blog posts
for i, post in enumerate(blog_posts):
    # Check category filter
    if "All" not in categories and post["category"] not in categories:
        continue
    
    with st.container():
        # Post header
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"## {post['title']}")
            st.markdown(f"📅 {post['date']} | ⏱️ {post['read_time']} | 📂 {post['category']}")
        
        with col2:
            st.markdown(f"""
            <div style="text-align: right;">
                <span style="background: #E3F2FD; color: #1976D2; 
                            padding: 0.5rem 1rem; border-radius: 20px;">
                    {post['category']}
                </span>
            </div>
            """, unsafe_allow_html=True)
        
        # Summary
        st.markdown(post['summary'])
        
        # Tags
        tags_html = " ".join([
            f'<span style="background: #f0f0f0; padding: 0.3rem 0.8rem; '
            f'border-radius: 15px; margin: 0.2rem; font-size: 0.85rem;">{tag}</span>'
            for tag in post['tags']
        ])
        st.markdown(tags_html, unsafe_allow_html=True)
        
        # Read more button
        with st.expander("📖 Read Full Article"):
            st.markdown(post['content'])
        
        st.markdown("---")

# Call to Action
st.markdown("""
<div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px; color: white; margin-top: 2rem;">
    <h3>Want to Discuss ML/MLOps?</h3>
    <p>I'm always happy to connect with fellow ML enthusiasts!</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("💬 Let's Connect", use_container_width=True):
        st.switch_page("pages/5_📞_Contact.py")
