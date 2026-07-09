from pydantic import BaseModel, ConfigDict


# INPUT SCHEMA (CREATE / UPDATE)
class TaskCreate(BaseModel):
    title: str


# OUTPUT SCHEMA (RESPONSE)
class TaskResponse(BaseModel):
    id: int
    title: str

    # Pydantic v2 fix (replaces class Config)
    model_config = ConfigDict(from_attributes=True)