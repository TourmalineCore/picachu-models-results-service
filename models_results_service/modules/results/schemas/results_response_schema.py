from pydantic import BaseModel
from typing import List


class ResultsResponseSchema(BaseModel):
    photo_id: int
    tags: List[str]
