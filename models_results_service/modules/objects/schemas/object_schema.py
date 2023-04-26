from pydantic import BaseModel


class ObjectSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True