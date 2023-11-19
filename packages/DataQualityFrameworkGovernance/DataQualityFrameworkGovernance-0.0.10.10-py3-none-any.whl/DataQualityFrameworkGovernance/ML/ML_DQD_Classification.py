import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Sample labeled dataset (replace this with your actual dataset)
data = {
    'text': ['accurate', 'complete', 'invalid', 'consistent', 'unique', 'timely', 'inaccurate', 'incomplete', 'valid', 'inconsistent', 'non-unique', 'untimely'],
    'label': ['accuracy', 'completeness', 'validity', 'consistency', 'uniqueness', 'timeliness', 'accuracy', 'completeness', 'validity', 'consistency', 'uniqueness', 'timeliness']
}

df = pd.DataFrame(data)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Convert text data to numerical features using CountVectorizer
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)

# Make predictions on the test set
predictions = classifier.predict(X_test_vectorized)

# Evaluate the classifier
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(report)
