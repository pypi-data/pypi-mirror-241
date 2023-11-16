class TaskParseError(Exception):
    """
    Represents an error when parsing a task.
    """

    def __init__(self, message):
        self.message = message

        super().__init__(message)

    def __str__(self):
        return self.message
