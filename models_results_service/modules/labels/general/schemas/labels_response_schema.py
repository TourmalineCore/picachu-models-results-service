from pydantic import BaseModel
from typing import List


class LabelsResponseSchema(BaseModel):
    photo_id: int
    tags: List[str]
