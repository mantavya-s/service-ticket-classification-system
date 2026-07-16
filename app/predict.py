import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "ticket_classifier_split_v1.joblib"

classifier = joblib.load(MODEL_PATH)

def predict_ticket(subcategory:str, description: str):
    text  = f"{subcategory} {description}"

    probabilities = classifier.predict_proba([text])[0]
    classes = classifier.classes_
    best_index = probabilities.argmax()

    prediction = classifier.predict([text])
    confidence = probabilities[best_index]

    return str(prediction), float(confidence)