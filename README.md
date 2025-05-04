🛡️ Malicious Script Detection System
This project focuses on identifying potentially harmful scripts using a range of machine learning and deep learning models. It processes code snippets and classifies them as either malicious or non-malicious, enabling early detection of security threats in web applications or user inputs.

📄 Dataset
The dataset is a collection of script samples labeled as malicious or not. After loading and cleaning the data, it is prepared for model training by removing duplicates and resetting the index.

🔍 Feature Extraction
Character-level tokenization and vectorization techniques such as TF-IDF and custom regex-based tokenization are used to extract meaningful patterns from script content. These representations are essential for training various models effectively.

🧠 Models Used
Logistic Regression: A baseline linear classifier using character-level TF-IDF features.
Random Forest: Utilizes a custom tokenizer to detect more complex malicious patterns based on keywords and syntax.
LSTM (Long Short-Term Memory): A deep learning model trained on character sequences to capture contextual dependencies in script behavior.
SVM (Support Vector Machine): A linear kernel model trained on TF-IDF features and exported for use in the FastAPI service.
XGBoost: A powerful tree-based model capable of handling diverse patterns in textual input.
Multinomial Naive Bayes: A probabilistic model trained using TF-IDF vectors to capture frequency-based malicious indicators.

🌐 FastAPI Service
A lightweight API is provided for real-time script classification. It loads a trained model and exposes a REST endpoint to check whether a script is malicious. This allows easy integration with web applications or security tools.

▶️ How to Run
Train your preferred model using the provided scripts, ensure the model is saved, then launch the FastAPI server. You can send scripts to the API and receive a prediction response indicating whether the script is malicious.

📌 Highlights
Supports multiple ML/DL models for experimentation and comparison.
Uses a character-based approach to catch obfuscated or encoded attacks.
Offers real-time detection through an API endpoint.
Easily extendable with other models or tokenization strategies.
