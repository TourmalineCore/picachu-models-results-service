from pydantic import BaseModel


class AssociationSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True
