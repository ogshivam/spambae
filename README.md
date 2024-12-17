# SpamBae - Smart SMS Classification

SpamBae is an intelligent SMS classification web application that helps users identify spam and legitimate (ham) messages with high accuracy. Built with Python Flask and modern web technologies, it provides a sleek, user-friendly interface for real-time message classification.

## Features

- **Real-time Classification**: Instantly classify messages as spam or ham
- **High Accuracy**: Powered by a machine learning model trained on a large dataset
- **Confidence Scores**: View classification confidence levels for each prediction
- **Message History**: Keep track of previously classified messages
- **Dark/Light Theme**: Toggle between dark and light modes for comfortable viewing
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **User Feedback**: Provide feedback on classification results with thumbs up/down

## Technology Stack

- **Backend**:
  - Python 3.x
  - Flask (Web Framework)
  - Scikit-learn (Machine Learning)
  - Pickle (Model Serialization)

- **Frontend**:
  - HTML5
  - CSS3
  - JavaScript (Vanilla)
  - Font Awesome Icons

## Project Structure

```
spambae/
├── app.py                 # Main Flask application
├── train_model.py         # Model training script
├── requirements.txt       # Python dependencies
├── spam_classification_model.pkl  # Trained ML model
├── static/
│   ├── styles.css        # Application styles
│   └── logo.svg          # Application logo
└── templates/
    └── index.html        # Main application template
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spambae.git
   cd spambae
   ```

2. Create a virtual environment (recommended):
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

5. Open your browser and navigate to `http://127.0.0.1:5000`

## Usage

1. Enter or paste the message you want to classify in the input box
2. Click "Classify Message" or press Enter
3. View the classification result with confidence score
4. Provide feedback using the thumbs up/down buttons
5. Access previous classifications in the history sidebar

## Model Training

The spam classification model is trained using Scikit-learn on a curated dataset of spam and ham messages. To retrain the model:

```bash
python train_model.py
```

This will generate a new `spam_classification_model.pkl` file.

## UI Components

- **Navbar**: Contains logo, navigation icons, and theme toggle
- **Sidebar**: Displays message history with classification results
- **Main Content**: 
  - Message input area
  - Classification result card
  - Confidence indicator
  - Feedback buttons

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created with ♥ by Shivam

## Acknowledgments

- Font Awesome for the icons
- Flask community for the excellent web framework
- Scikit-learn team for the machine learning tools
