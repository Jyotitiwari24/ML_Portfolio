import streamlit as st
import re
from textblob import TextBlob


def preprocess_text(text):
    """
    Simple text preprocessing
    """
    # Convert to lowercase
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text


def analyze_sentiment(text):
    """
    Analyze sentiment using TextBlob (simple implementation)
    For production, replace with trained model
    """
    # Preprocess
    clean_text = preprocess_text(text)
    
    # Analyze
    blob = TextBlob(clean_text)
    polarity = blob.sentiment.polarity
    
    # Classify
    if polarity > 0.1:
        sentiment = "Positive"
        emoji = "😊"
        color = "green"
    elif polarity < -0.1:
        sentiment = "Negative"
        emoji = "😞"
        color = "red"
    else:
        sentiment = "Neutral"
        emoji = "😐"
        color = "gray"
    
    confidence = abs(polarity) * 100
    
    return {
        'sentiment': sentiment,
        'emoji': emoji,
        'color': color,
        'confidence': min(confidence, 95),  # Cap at 95%
        'polarity': polarity
    }


def display_sentiment_demo():
    """
    Display sentiment analysis demo in Streamlit
    """
    st.markdown("### 🎭 Live Sentiment Analysis Demo")
    st.markdown("Try analyzing the sentiment of any text!")
    
    # Sample texts
    samples = {
        "Positive": "This product is amazing! I absolutely love it. Highly recommended!",
        "Negative": "Terrible experience. Very disappointed. Would not recommend.",
        "Neutral": "The product arrived on time. It works as described."
    }
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Try Positive Example"):
            st.session_state.sample_text = samples["Positive"]
    with col2:
        if st.button("Try Negative Example"):
            st.session_state.sample_text = samples["Negative"]
    with col3:
        if st.button("Try Neutral Example"):
            st.session_state.sample_text = samples["Neutral"]
    
    # Text input
    default_text = st.session_state.get('sample_text', '')
    user_input = st.text_area(
        "Enter text to analyze:",
        value=default_text,
        height=100,
        placeholder="Type or paste your text here..."
    )
    
    if st.button("🔍 Analyze Sentiment", type="primary"):
        if user_input.strip():
            with st.spinner("Analyzing..."):
                result = analyze_sentiment(user_input)
                
                # Display result
                st.markdown(f"""
                <div style="text-align: center; padding: 2rem; 
                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            border-radius: 15px; color: white; margin: 1rem 0;">
                    <div style="font-size: 4rem;">{result['emoji']}</div>
                    <h2 style="margin: 1rem 0;">{result['sentiment']}</h2>
                    <p style="font-size: 1.2rem;">Confidence: {result['confidence']:.1f}%</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Detailed analysis
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Sentiment Score", f"{result['polarity']:.2f}")
                    st.caption("Range: -1 (Very Negative) to +1 (Very Positive)")
                
                with col2:
                    st.metric("Confidence", f"{result['confidence']:.1f}%")
                    st.caption("How confident the model is")
                
                # Word count
                word_count = len(user_input.split())
                char_count = len(user_input)
                
                st.markdown("---")
                st.markdown("### 📊 Text Statistics")
                col1, col2, col3 = st.columns(3)
                col1.metric("Words", word_count)
                col2.metric("Characters", char_count)
                col3.metric("Sentences", user_input.count('.') + user_input.count('!') + user_input.count('?'))
        
        else:
            st.warning("⚠️ Please enter some text to analyze")
    
    # Information
    with st.expander("ℹ️ About this demo"):
        st.markdown("""
        **How it works:**
        - Uses NLP techniques to analyze text sentiment
        - Classifies text as Positive, Negative, or Neutral
        - Provides confidence score for the prediction
        
        **Technologies:**
        - Python
        - TextBlob / NLTK
        - Machine Learning
        
        **Note:** This is a simplified demo. Production models use more sophisticated techniques 
        including deep learning, transformers, and domain-specific training.
        """)