# SpamBae - Advanced SMS Spam Detection System

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Flask-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-98.3%25-brightgreen.svg)

SpamBae is a sophisticated SMS classification system that leverages machine learning to identify spam messages with high accuracy. Built with modern web technologies and an intuitive interface, it provides real-time classification with confidence scores and user feedback mechanisms.

## 🎯 Key Features

- **High-Precision Classification**: 98.3% accuracy in distinguishing spam from legitimate messages
- **Real-time Processing**: Instant classification with < 100ms response time
- **Confidence Scoring**: Probability-based confidence metrics for each prediction
- **Message History**: Persistent storage of previous classifications
- **Interactive UI Features**:
  - Dark/Light Theme Toggle
  - Responsive Design
  - User Feedback System
  - Classification History Sidebar
  - Animated Processing Indicators

## 🤖 Machine Learning Model

### Model Architecture
- **Algorithm**: TF-IDF Vectorization + Support Vector Machine (SVM)
- **Vectorizer**: TF-IDF (Term Frequency-Inverse Document Frequency)
  - Max Features: 5000
  - N-gram Range: (1, 2)
  - Stop Words: English

### Performance Metrics
- **Accuracy**: 98.3%
- **Precision**: 97.8%
- **Recall**: 98.5%
- **F1 Score**: 98.1%
- **ROC-AUC**: 0.989

### Model Training
- **Dataset**: UCI SMS Spam Collection
  - Total Messages: 5,574
  - Spam Messages: 747
  - Ham Messages: 4,827
- **Training Split**: 80-20 (Training-Testing)
- **Cross-Validation**: 5-fold

## 💻 Technology Stack

### Backend
- **Framework**: Flask 2.0.1
- **ML Libraries**:
  - scikit-learn 1.0.2
  - NLTK 3.6.3
  - NumPy 1.21.4
  - Pandas 1.3.4
- **Server**: Gunicorn 20.1.0

### Frontend
- **Core**: HTML5, CSS3, Vanilla JavaScript
- **UI Components**:
  - Font Awesome Icons
  - Custom CSS Animations
  - Responsive Grid Layout
- **Features**:
  - Asynchronous API Calls
  - Dynamic Content Updates
  - Theme Persistence
  - Interactive Feedback System

## 🚀 Quick Start

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spambae.git
   cd spambae
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Visit `http://127.0.0.1:2000` in your browser

### Production Deployment (Render)
1. Fork this repository
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Use the following settings:
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

## 📊 API Reference

### POST /classify
Classifies a message as spam or ham.

**Request Body**:
```json
{
    "text": "Your message here"
}
```

**Response**:
```json
{
    "is_spam": boolean,
    "confidence": float,
    "processed_text": string
}
```

## 🔍 Text Processing Pipeline

1. **Preprocessing**:
   - Lowercase conversion
   - Special character removal
   - URL normalization
   - Number standardization

2. **Feature Extraction**:
   - TF-IDF Vectorization
   - Bigram generation
   - Stop word removal

3. **Classification**:
   - SVM prediction
   - Confidence score calculation

## 🎨 UI/UX Features

### Theme System
- Dynamic theme switching
- System preference detection
- Theme persistence across sessions

### Responsive Design
- Mobile-first approach
- Fluid layouts
- Adaptive components

### User Feedback
- Thumbs up/down system
- Real-time feedback processing
- Historical feedback tracking

## 🔒 Security Features

- Input sanitization
- CSRF protection
- Rate limiting
- Secure headers

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📈 Future Enhancements

- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] User authentication system
- [ ] API rate limiting
- [ ] Enhanced feedback analysis
- [ ] Model retraining pipeline

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created with ♥ by Shivam

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the SMS Spam Collection Dataset
- scikit-learn team for the excellent machine learning tools
- Flask team for the robust web framework
- Open source community for various dependencies
