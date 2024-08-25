# Detect-AI-Generated-Text

## Overview

This project aims to build a machine learning model that can differentiate between AI-generated text and human-written text. The model is trained on a dataset containing labeled examples of both types of text and uses a vectorization technique to convert text into numerical features. The classifier can then predict whether a given text was written by a human or generated by an AI.

## Project Structure

- Model/data/: Contains the dataset used for training and testing the model.
- Model/Jupyter files/: Jupyter notebooks used for data exploration, model training, and evaluation.
- Model/Jupyter files/models/: Saved models and vectorizers for future use.
- pages/: Pages for the other sections.
- login.py: Entry point of the project.
- README.md: Project documentation.
- requirements.txt: List of dependencies required to run the project.

## Dataset

The dataset used in this project is a CSV file with the following columns:

- id: Unique identifier for each record.
- prompt_id: Identifier for the prompt associated with the text.
- text: The actual text to be classified.
- generated: Label indicating whether the text was AI-generated (1) or human-written (0).

## Installation

> Clone the repository:

```
git clone https://github.com/your-username/ai-vs-human-text-classifier.git
cd ai-vs-human-text-classifier
```

> Create a virtual environment and install dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> Install Jupyter Notebook (if not installed):

```
pip install notebook
```

## Usage

### Training the Model

Open the Jupyter notebook in the notebooks/ directory to train the model.

```
jupyter notebook notebooks/train_model.ipynb
```

Follow the steps in the notebook to load the data, preprocess it, and train the model.

Save the trained model and vectorizer:

python
Copy code
import joblib
joblib.dump(model, 'models/ai_text_detector.pkl')
joblib.dump(vectorizer, 'models/vectorizer.pkl')

## Making Predictions

Load the saved model and vectorizer:

```model = joblib.load('models/ai_text_detector.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')
```

Use the predict_text_type function to classify new text:

```def predict_text_type(text):
text_vectorized = vectorizer.transform([text])
prediction = model.predict(text_vectorized)
```

return 'AI-generated' if prediction[0] == 1 else 'Human-written'

Test the model with sample text:

```
sample_text = "This is a sample text to test the model."
result = predict_text_type(sample_text)
print(f"Prediction: {result}")
```

## Integration

The model is integrated into a web-based application using Streamlit. Streamlit allows for easy creation of interactive web apps directly from Python scripts.

To run the Streamlit app, follow these steps:

Run the Streamlit app:

```
streamlit run login.py
```

Access the web app:

After running the above command, the app will be accessible in your web browser at http://localhost:8501.
Use the app to input text and see whether the model predicts it as AI-generated or human-written.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Please ensure that your code follows the existing coding style and that all tests pass before submitting.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

The project was inspired by the need to differentiate between AI-generated content and human-written content.
Special thanks to the open-source community for providing valuable resources and tools.
