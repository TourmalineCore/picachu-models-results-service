from pydantic import BaseModel


class EmotionSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True
