from fastapi import FastAPI
from agents.mind_map import MindMapAgent
from agents.retrieval import RetrievalAgent
from agents.computation import ComputationAgent

app = FastAPI()

mind_map = MindMapAgent()
retrieval = RetrievalAgent()
computation = ComputationAgent()

@app.get("/")
async def root():
    return {"message": "Oil and Gas Reasoning Agent API"}

@app.post("/query/")
async def query_model(question: str):
    # Step 1: Retrieve knowledge from vector DB
    context = retrieval.search_documents(question)
    
    # Step 2: Use Mind Map to refine reasoning
    structured_context = mind_map.process(question, context)
    
    # Step 3: Run engineering calculations if needed
    result = computation.calculate(question, structured_context)

    return {"answer": result}
