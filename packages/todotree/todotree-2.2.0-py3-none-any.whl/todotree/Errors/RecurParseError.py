class RecurParseError(Exception):
    """
    Represents an error when parsing a recur task.
    """

    def __init__(self, message):
        self.message = message

        super().__init__(message)

    def __str__(self):
        return self.message
