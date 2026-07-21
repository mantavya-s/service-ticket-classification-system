from fastapi import FastAPI
from app.schemas import TicketRequest, Priority
from app.predict import predict_ticket
from app.insert_user_data import insert_data
from rag.retrieve import retrieve as similarity_search

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "Hello World!"}

@app.post("/analyze-ticket/")
def analyze_ticket(request: TicketRequest):
    category, confidence = predict_ticket(
        request.subcategory,
        request.description
    )
    text = f"{request.subcategory}. {request.description or ''}"
    similar = similarity_search(text)

    insert_data(
        ticket_id=request.ticket_id,
        subcategory=request.subcategory,
        priority=request.priority.value,
        description=request.description,
        predicted_category=str(category),
        predicted_confidence=float(confidence)
    )

    return {
        "query": text,
        "Category": category,
        "Confidence": confidence,
        "Similar Docs": similar
    }
    