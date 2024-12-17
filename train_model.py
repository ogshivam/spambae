import pandas as pd
from sklearn.naive_bayes import MultinomialNB
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the data
data = pd.read_csv('spam.csv', encoding='ISO-8859-1')
data = data.rename(columns={
    'v2': 'Text',  # Message content column
    'v1': 'Label'  # Label column (spam/ham)
})

# Convert labels to numeric
data['Label'] = (data['Label'] == 'spam').astype(int)

# Load the existing vectorizer
with open('spam_classification_model_vectorizer copy.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Transform the text data
X = vectorizer.transform(data['Text']).toarray()
y = data['Label']

# Train the model
model = MultinomialNB()
model.fit(X, y)

# Save the model
with open('spam_classification_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved successfully!")
