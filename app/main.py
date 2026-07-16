from fastapi import FastAPI
from app.schemes import TicketRequest, TicketResponse
from app.predict import predict_ticket

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "Hello World!"}

@app.post("/predict/")
async def predict_item(request: TicketRequest):
    category, confidence = predict_ticket(
        request.subcategory,
        request.description
    )

    return{
        "Category": category,
        "Confidence": confidence
    }
    