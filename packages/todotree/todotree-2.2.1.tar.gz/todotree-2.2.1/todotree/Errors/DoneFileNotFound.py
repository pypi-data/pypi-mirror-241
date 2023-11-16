from todotree.Config.Config import Config


class DoneFileNotFound(BaseException):
    """
    Represents an error indicating that the done.txt file is not found.
    """

    def __init__(self, message):
        self.message = message

        super().__init__(message)

    def __str__(self):
        return self.message

    def echo_and_exit(self, config: Config):
        config.console.error("The done.txt could not be found.")
        config.console.error(f"It searched at the following location: {config.paths.done_file}")
        config.console.verbose(self)
        exit(1)
