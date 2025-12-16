from pydantic import BaseModel


class MathRequest(BaseModel):
    """Request model for math operations."""
    a: float
    b: float


class MathResponse(BaseModel):
    """Response model for math operations."""
    result: float

