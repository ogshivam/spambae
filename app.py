from flask import Flask, render_template, request, jsonify
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Join tokens back into text
    return ' '.join(tokens)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_spam():
    data = request.get_json()
    message = data.get('message', '')
    
    # Preprocess the text
    processed_text = preprocess_text(message)
    
    # TODO: Add your spam detection model here
    # For now, we'll use a simple rule-based approach
    spam_keywords = ['buy', 'free', 'win', 'winner', 'prize', 'offer', 'urgent', 
                    'limited', 'click', 'deal', 'discount', 'cash', 'money']
    
    # Count spam keywords
    spam_count = sum(1 for word in processed_text.split() if word in spam_keywords)
    
    # Simple rule: if more than 2 spam keywords are present, classify as spam
    result = 'spam' if spam_count > 2 else 'ham'
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
