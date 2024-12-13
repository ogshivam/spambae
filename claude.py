import re
import nltk
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

class SMSSpamClassifier:
    def __init__(self, model_path, training_data=None):
        """
        Initialize the SMS Spam Classifier
        
        :param model_path: Path to save/load the pickled machine learning model
        :param training_data: DataFrame containing 'Text' and target columns for initial setup
        """
        # Load or set up the model
        try:
            with open(model_path, 'rb') as model_file:
                self.model = pickle.load(model_file)
            self.is_trained = True
        except FileNotFoundError:
            self.model = None
            self.is_trained = False
        
        # Initialize lemmatizer and stop words
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words("english"))
        
        # TF-IDF Vectorizer
        self.tfidf = TfidfVectorizer()
        
        # If training data is provided, fit the vectorizer and train the model
        if training_data is not None:
            self.fit(training_data)
    
    def _preprocess_corpus(self, data):
        """
        Preprocess the entire corpus for vectorization
        
        :param data: DataFrame with 'Text' column
        :return: List of preprocessed texts
        """
        corpus = []
        for text in data["Text"]:
            # Full preprocessing pipeline
            cleaned_text = self._clean_text(text)
            tokenized_text = word_tokenize(cleaned_text)
            filtered_text = self._remove_stopwords(tokenized_text)
            lemmatized_text = self._lemmatize_words(filtered_text)
            processed_text = ' '.join(lemmatized_text)
            corpus.append(processed_text)
        
        return corpus
    
    def fit(self, data, target_column='Label', model_path=None):
        """
        Fit the TF-IDF vectorizer and train the model
        
        :param data: Training DataFrame
        :param target_column: Name of the column with target labels
        :param model_path: Path to save the trained model
        """
        # Preprocess the corpus
        corpus = self._preprocess_corpus(data)
        
        # Fit TF-IDF Vectorizer
        X = self.tfidf.fit_transform(corpus).toarray()
        y = data[target_column]
        
        # Train the model (you should replace this with your actual model)
        from sklearn.naive_bayes import MultinomialNB
        self.model = MultinomialNB()
        self.model.fit(X, y)
        self.is_trained = True
        
        # Save the model if path is provided
        if model_path:
            with open(model_path, 'wb') as model_file:
                pickle.dump(self.model, model_file)
            
            # Save the TF-IDF vectorizer
            tfidf_path = model_path.replace('.pkl', '_vectorizer.pkl')
            with open(tfidf_path, 'wb') as vectorizer_file:
                pickle.dump(self.tfidf, vectorizer_file)
    
    def preprocess_text(self, text):
        """
        Preprocess the input SMS text
        
        :param text: Input SMS text
        :return: Preprocessed text ready for prediction
        """
        # Cleaning
        cleaned_text = self._clean_text(text)
        
        # Tokenization
        tokenized_text = word_tokenize(cleaned_text)
        
        # Remove stopwords
        filtered_text = self._remove_stopwords(tokenized_text)
        
        # Lemmatization
        lemmatized_text = self._lemmatize_words(filtered_text)
        
        # Create corpus
        processed_text = ' '.join(lemmatized_text)
        
        # Vectorize
        vectorized_text = self.tfidf.transform([processed_text]).toarray()
        
        return vectorized_text
    
    def _clean_text(self, text):
        """
        Clean the input text
        
        :param text: Input text
        :return: Cleaned text
        """
        # Replace non-alphabetic characters with space
        sms = re.sub('[^a-zA-Z]', ' ', text)
        # Convert to lowercase
        sms = sms.lower()
        return sms
    
    def _remove_stopwords(self, text):
        """
        Remove stopwords from tokenized text
        
        :param text: Tokenized text
        :return: Text without stopwords
        """
        return [word for word in text if word not in self.stop_words]
    
    def _lemmatize_words(self, text):
        """
        Lemmatize words in the text
        
        :param text: List of words
        :return: Lemmatized words
        """
        return [self.lemmatizer.lemmatize(word, pos='v') for word in text]
    
    def predict(self, text):
        """
        Predict if an SMS is spam or ham
        
        :param text: Input SMS text
        :return: Prediction (0 for ham, 1 for spam)
        """
        if not self.is_trained:
            raise ValueError("Model is not trained. Please train the model first.")
        
        # Preprocess the text
        processed_text = self.preprocess_text(text)
        
        # Make prediction
        prediction = self.model.predict(processed_text)
        
        return int(prediction[0])
    
    def predict_proba(self, text):
        """
        Get probability of spam prediction
        
        :param text: Input SMS text
        :return: Probability of being spam
        """
        if not self.is_trained:
            raise ValueError("Model is not trained. Please train the model first.")
        
        # Preprocess the text
        processed_text = self.preprocess_text(text)
        
        # Get prediction probabilities
        proba = self.model.predict_proba(processed_text)
        
        return float(proba[0][1])  # Probability of spam class

def main():
    # Import pandas (assumed you're using pandas for data loading)
    import pandas as pd
    
    # Load your training data
    data = pd.read_csv('spam.csv', encoding='ISO-8859-1')
    
    # Print column names to verify what's available
    print("Available columns:", data.columns.tolist())
    
    # Rename columns to match expected format if needed
    # Assuming your spam.csv has columns like 'v1' (labels) and 'v2' (messages)
    data = data.rename(columns={
        'v2': 'Text',  # Message content column
        'v1': 'Label'  # Label column (spam/ham)
    })
    
    # Convert labels to numeric (assuming 'spam' = 1, 'ham' = 0)
    data['Label'] = (data['Label'] == 'spam').astype(int)
    
    # Initialize the classifier with training data and model save path
    MODEL_PATH = 'spam_classification_model.pkl'
    classifier = SMSSpamClassifier(MODEL_PATH, training_data=data)
    
    # Train and save the model
    classifier.fit(data, model_path=MODEL_PATH)
    
    # Example SMS messages
    sms_messages = [
        "Congratulations! You've won a free iPhone. Click here to claim!",
        "Hey, can we meet for coffee later today?"
    ]
    
    # Predict for each message
    for message in sms_messages:
        prediction = classifier.predict(message)
        probability = classifier.predict_proba(message)
        
        print(f"Message: {message}")
        print(f"Prediction: {'Spam' if prediction == 1 else 'Ham'}")
        print(f"Spam Probability: {probability:.2%}\n")

if __name__ == "__main__":
    main()