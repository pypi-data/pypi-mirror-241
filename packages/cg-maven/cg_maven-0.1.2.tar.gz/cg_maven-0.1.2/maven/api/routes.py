from fastapi import APIRouter, Depends, status

from maven.crud import create
from maven.maven_db.maven_adapter import MavenAdapter, get_maven_adapter
from maven.models.case import Case

router = APIRouter()


@router.post(
    "/",
    response_description="Create a new case document",
    status_code=status.HTTP_201_CREATED,
    response_model=Case,
)
def create_case(case_json: dict, maven_adapter: MavenAdapter = Depends(get_maven_adapter)) -> Case:
    """Create a case document in the database."""
    case: Case = Case.model_validate(case_json)
    create.create_case(case=case, maven_adapter=maven_adapter)
    return case
