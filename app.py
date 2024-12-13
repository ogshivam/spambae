from flask import Flask, render_template, request, jsonify
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
from datetime import datetime

app = Flask(__name__)

# Download necessary NLTK resources
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

# Load the model and vectorizer
model_path = 'spam_classification_model.pkl'
vectorizer_path = 'spam_classification_model_vectorizer copy.pkl'

with open(vectorizer_path, 'rb') as file:
    vectorizer = pickle.load(file)

with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Store message history in memory (you might want to use a database in production)
message_history = []

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords and lemmatize
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    
    # Join tokens back into text
    return ' '.join(tokens)

@app.route('/')
def home():
    return render_template('index.html', history=message_history)

@app.route('/classify', methods=['POST'])
def classify():
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Preprocess the text
    processed_text = preprocess_text(text)
    
    # Vectorize the text
    text_vectorized = vectorizer.transform([processed_text])
    
    # Make prediction
    prediction = model.predict(text_vectorized)[0]
    probability = model.predict_proba(text_vectorized)[0].tolist()
    
    result = {
        'is_spam': bool(prediction),
        'confidence': max(probability) * 100,
        'processed_text': processed_text
    }
    
    # Add to history
    message_history.append({
        'text': text[:50] + '...' if len(text) > 50 else text,
        'is_spam': result['is_spam'],
        'confidence': result['confidence'],
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    
    # Keep only the last 50 messages
    if len(message_history) > 50:
        message_history.pop(0)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=2000)
