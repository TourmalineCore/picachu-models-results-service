from pydantic import BaseModel


class PhotoColorSchema(BaseModel):
    red: int
    green: int
    blue: int

    class Config:
        orm_mode = True
