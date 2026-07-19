from fastapi import FastAPI
from app.schemes import TicketRequest, TicketResponse, RetrieveRequest
from app.predict import predict_ticket
from rag.retrieve import retrieve as similarity_search

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

@app.post("/retrieve/")
async def retrieve(request: RetrieveRequest):
    results = similarity_search(request.text, request.limit)

    return{
        "query": request.text,
        "results": results
    }
    