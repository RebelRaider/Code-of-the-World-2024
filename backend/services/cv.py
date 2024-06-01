import uuid

from fastapi import Depends

from models.cv import CV
from repositories.cv import CVRepository
from schemas.cvschema import CVSchema


class CVService:
    def __init__(self, repo: CVRepository = Depends(CVRepository)):
        self._repo = repo

    def create(self, data: CVSchema, user_id: uuid.UUID) -> CV:
        return self._repo.create(data, user_id)