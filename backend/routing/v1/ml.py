import json
import tempfile
import uuid

from fastapi import APIRouter, File, UploadFile, HTTPException, Depends

from ml.template_ml_for_api import template_for_upload_cv
from schemas.cvschema import CVSchema
from services.cv import CVService

router = APIRouter(prefix="/api/v1/cv", tags=["cv"])


@router.post(
    "/upload",
    summary="загрузить cv",
)
async def create_from_wb(
    user: uuid.UUID,
    cv: UploadFile = File(...),
    cv_service: CVService = Depends()
):
    with tempfile.NamedTemporaryFile() as temp_file:
        temp_file.write(cv.file.read())

        file_path = temp_file.name
        answer = template_for_upload_cv(file_path)

        try:
            answer = json.loads(answer)
        except Exception as e:
            raise HTTPException(status_code=500, detail="cannot parse your cv, try pls again")

        cv_schema = CVSchema(**answer)

        cv_service.create(cv_schema, user)

