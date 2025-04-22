import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier

# Zbiór danych https://www.kaggle.com/datasets/marslinoedward/sms-spam-dataset
df = pd.read_csv('SI/spam.csv', encoding='latin-1')
df.columns = ['id','label', 'message']
df.head()

X = df['message']
y = df['label'].map({'ham': 0, 'spam': 1})

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
nb_preds = nb_model.predict(X_test)

print("Naiwny Bayes - Accuracy:", accuracy_score(y_test, nb_preds))
print(classification_report(y_test, nb_preds))

tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)
tree_preds = tree_model.predict(X_test)

print("Drzewo decyzyjne - Accuracy:", accuracy_score(y_test, tree_preds))
print(classification_report(y_test, tree_preds))
