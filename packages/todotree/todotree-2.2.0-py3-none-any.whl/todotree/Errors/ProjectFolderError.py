class ProjectFolderError(Exception):
    """
    Represents an error when parsing the project folder.
    """
    def __init__(self, message):
        self.message = message

        super().__init__(message)

    def __str__(self):
        return self.message
