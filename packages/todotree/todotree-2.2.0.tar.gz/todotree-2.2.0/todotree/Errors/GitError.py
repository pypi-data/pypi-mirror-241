from todotree.ConsolePrefixes import ConsolePrefixes


class GitError(Exception):
    """
    Represents an error indicating that something is wrong with the git repo.
    """
    def __init__(self, message):
        self.message = message

        super().__init__(message)

    def __str__(self):
        return self.message

    def warn_and_continue(self, console: ConsolePrefixes):
        console.warning("An error occurred while trying to git pull.")
        console.warning("If this was unexpected, try again with the --verbose flag.")


