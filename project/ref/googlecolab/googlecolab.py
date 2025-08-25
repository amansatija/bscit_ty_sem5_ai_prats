import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')


# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment_vader(text):
    sentiment_scores = sia.polarity_scores(str(text))  # Convert to string to avoid errors
    compound_score = sentiment_scores['compound']
    print(f'compound_score : {compound_score}')
    # Assign sentiment labels
    if compound_score >= 0.05:
        sentiment_label = "Positive 😊"
    elif compound_score <= -0.05:
        sentiment_label = "Negative 😡"
    else:
        sentiment_label = "Neutral 😐"

    return sentiment_label

sentiment = analyze_sentiment_vader("i love this movie")
print(f'sentiment : {sentiment}')
