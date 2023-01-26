from pydantic import BaseModel


class PhotoColorSchema(BaseModel):
    photo_id: int
    red: int
    green: int
    blue: int

    class Config:
        orm_mode = True
