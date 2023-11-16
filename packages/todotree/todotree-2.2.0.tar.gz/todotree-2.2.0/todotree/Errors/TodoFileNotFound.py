from todotree.Config.Config import Config


class TodoFileNotFound(Exception):
    """
    Represents an error indicating that the todo.txt file is not found.
    """
    def __init__(self, message):
        self.message = message

        super().__init__(message)

    def __str__(self):
        return self.message

    def echo_and_exit(self, config: Config):
        config.console.error("The todo.txt could not be found.")
        config.console.error(f"It searched at the following location: {config.paths.todo_file}")
        config.console.verbose(str(self))
        exit(1)
