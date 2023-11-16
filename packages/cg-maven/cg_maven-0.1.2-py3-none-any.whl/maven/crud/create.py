from maven.maven_db.maven_adapter import MavenAdapter
from maven.models import Case


def create_case(case: Case, maven_adapter: MavenAdapter):
    """Create a case document in the database."""
    case_json: dict = case.model_dump()
    maven_adapter.maven_db.case.insert_one(document=case_json)
