class MavenAPIError(Exception):
    def __init__(self, message: str = ""):
        super(MavenAPIError, self).__init__()
        self.message = message


class DatabaseConnectionError(MavenAPIError):
    """Raises an error in case of a database connection error."""
