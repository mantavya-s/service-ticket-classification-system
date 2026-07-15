from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
import pandas as pd
from pathlib import Path
import joblib

DATA_FILE = Path("data/combined_ticket.csv")
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_FILE, dtype=str).fillna("")
df["Text"] = df["Subcategory"] + ' ' + df["Description"]

train_df = df[df["Source"] == "Public"]
test_df = df[df["Source"] == "Synthetic"]

X_train = train_df["Text"]
X_test = test_df["Text"]
y_train = train_df["Category"]
y_test = test_df["Category"]

category_classifier = Pipeline([
    ('vectorizer', TfidfVectorizer(
        sublinear_tf=True, 
        max_df = 0.9, 
        min_df = 2,
        ngram_range=(1, 2)
    )),
    ('model', LogisticRegression(max_iter=1000))
])

category_classifier.fit(X_train, y_train)
predictions = category_classifier.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, predictions)}")
print(classification_report(y_test, predictions))

new_texts = ["VPN Connection Issue user cannot connect to VPN even after changing their password and updating the application"]
new_predictions = category_classifier.predict(new_texts)
print("predictions for new text: ", new_predictions)

joblib.dump(category_classifier, MODEL_DIR / "ticket_classifier_unsplit_v1.joblib")

