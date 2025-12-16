from fastapi import FastAPI
from app.models import MathRequest, MathResponse

app = FastAPI(title="Math Operations API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/add", response_model=MathResponse)
def add(request: MathRequest) -> MathResponse:
    """Add two numbers."""
    result = request.a + request.b
    return MathResponse(result=result)


@app.post("/subtract", response_model=MathResponse)
def subtract(request: MathRequest) -> MathResponse:
    """Subtract two numbers."""
    result = request.a - request.b
    return MathResponse(result=result)


@app.post("/multiply", response_model=MathResponse)
def multiply(request: MathRequest) -> MathResponse:
    """Multiply two numbers."""
    result = request.a * request.b
    return MathResponse(result=result)

