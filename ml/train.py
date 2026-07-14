from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from pathlib import Path
import pandas as pd

DATA_FILE = Path("data/combined_ticket.csv")

df = pd.read_csv(DATA_FILE, dtype=str).fillna("")
X = df['Subcategory'] + ' ' + df['Description']
y = df['Category']

X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.2, 
    random_state=42, 
    stratify=y
)

vectorizer = TfidfVectorizer(
    sublinear_tf=True, 
    max_df = 0.9, 
    min_df = 2, 
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

predictions = model.predict(X_test_tfidf)
print(f"Accuracy: {accuracy_score(y_test, predictions)}")
print(classification_report(y_test, predictions))

new_texts = ["VPN Connection Issue user cannot connect to VPN even after changing their password and updating the application"]
new_text_tfidf = vectorizer.transform(new_texts)
new_predictions = model.predict(new_text_tfidf)
print("predictions for new text: ", new_predictions)