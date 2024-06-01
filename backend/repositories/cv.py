import uuid

from fastapi import Depends
from loguru import logger
from sqlalchemy.orm import Session

from configs.Database import get_db_connection
from conventors.cv import convert_cv
from models.cv import CV
from schemas.cvschema import CVSchema


class CVRepository:
    def __init__(self, db: Session = Depends(get_db_connection)):
        self.db = db

    def create(self, cv: CVSchema, user_id: uuid.UUID) -> CV:
        cv = convert_cv(cv_schema=cv, user_id=user_id)

        logger.debug(f"model cv = {cv}")

        self.db.add(cv)
        self.db.commit()

        return cv
