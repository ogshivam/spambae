import pickle

with open('spam_classification_model_vectorizer copy.pkl', 'rb') as file:
    data = pickle.load(file)
    print("Type of loaded data:", type(data))
    print("Contents:", data)
