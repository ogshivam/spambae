import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load the pickled model (using the optimized Naive Bayes model)
with open("naive_bayes_model.pkl", "rb") as f:
    model = pickle.load(f)

def clean_text(text):
    # Remove non-alphabetic characters
    text = re.sub('[^a-zA-Z]', ' ', text)
    # Convert to lowercase
    text = text.lower()
    # Split and join to remove extra spaces
    text = ' '.join(text.split())
    return text

def preprocess_text(text):
    # Clean the text
    cleaned_text = clean_text(text)
    
    # Tokenize
    tokens = nltk.word_tokenize(cleaned_text)
    
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word, pos='v') for word in tokens]
    
    # Join tokens back into text
    processed_text = ' '.join(tokens)
    
    return processed_text

def predict(input_text):
    """
    Make predictions on input text.
    Args:
        input_text (str): The SMS text to classify
    Returns:
        dict: Dictionary containing the prediction (0 for ham, 1 for spam) and the processed text
    """
    try:
        # Preprocess the input text
        processed_text = preprocess_text(input_text)
        
        # Make prediction
        prediction = model.predict([processed_text])[0]
        
        # Convert prediction to label
        label = "spam" if prediction == 1 else "ham"
        
        return {
            "success": True,
            "prediction": label,
            "processed_text": processed_text
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# Example usage:
if __name__ == "__main__":
    # Test message
    test_message = "WINNER!! As a valued network customer you have been selected to receivea £900 prize reward! To claim call 09061701461. Claim code KL341. Valid 12 hours only."
    result = predict(test_message)
    print(f"Input text: {test_message}")
    print(f"Prediction result: {result}")