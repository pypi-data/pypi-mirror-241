import click

from todotree.Commands.AbstractCommand import AbstractCommand
from todotree.Errors.TodoFileNotFound import TodoFileNotFound


class Filter(AbstractCommand):

    def run(self, search_term=None):
        try:
            self.taskManager.import_tasks()
        except TodoFileNotFound as e:
            e.echo_and_exit(self.config)

        self.config.console.info(f"Todos for term '{search_term}'")
        self.taskManager.filter_by_string(search_term)
        click.echo(self.taskManager)
