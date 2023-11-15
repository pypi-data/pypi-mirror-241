import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import make_pipeline


def train_and_classify(input_csv_file_path, result_csv_file_path, new_feedback):
    # Load data from the CSV file
    data = pd.read_csv(input_csv_file_path, encoding='latin-1')

    # Split the data into features and labels
    X = data['DQ Log']
    y = data['DQ Dimension']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=36)

    # Create a text classifier pipeline using Naive Bayes
    classifier = make_pipeline(TfidfVectorizer(), MultinomialNB())

    # Train the classifier
    classifier.fit(X_train, y_train)

    # Predict the test set
    predicted = classifier.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, predicted)
    print(f"Accuracy: {accuracy:.2f}")

    # Classification report
    print("Classification Report:")
    print(classification_report(y_test, predicted))

    # Predict sentiments of new feedback
    predicted_sentiments = classifier.predict(new_feedback)

    # Store results in a DataFrame
    new_results = pd.DataFrame({'DQ Log': new_feedback, 'DQ Dimension': predicted_sentiments})

    # Save the updated DataFrame to a CSV file
    new_results.to_csv(result_csv_file_path, index=False)

    return new_results


# Usage example:
input_path = '/Users/rajithprabhakaran/Documents/Python/Python Package/Files/Sample_DQ_Log_for_ML.csv'
result_path = '/Users/rajithprabhakaran/Documents/Python/Python Package/Files/Result_Feedback_in_text.csv'

new_feedback_to_classify = [
    "Start and end date is inconsistent",
    "Missing data",
    "ID is not unique",
    "Incorrect DOB",
    "Format entering full name",
    "A product's price is not same in system A and B",
    "An order is processed twice.",
    "A financial transaction is recorded twice in the accounting system"
]

train_and_classify(input_path, result_path, new_feedback_to_classify)
