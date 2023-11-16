from fastapi import APIRouter, status

from maven.models.case import Case
from maven.mongodb.crud import CrudHandler

router = APIRouter()


@router.post(
    "/",
    response_description="Create a new case document",
    status_code=status.HTTP_201_CREATED,
    response_model=None,
)
def create_case(case_json: dict) -> None:
    """Create a case document in the database."""
    case: Case = Case.model_validate(case_json)
    crud: CrudHandler = CrudHandler()
    crud.create_case(case=case)
