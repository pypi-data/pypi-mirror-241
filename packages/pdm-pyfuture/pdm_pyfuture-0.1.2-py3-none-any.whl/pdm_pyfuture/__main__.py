import argparse
import readline
import subprocess

from pdm.cli.commands.base import BaseCommand
from pdm.cli.commands.build import Command as BuildCommand
from pdm.core import Core
from pdm.project import Project
from pdm.cli.options import Option, global_option, project_option, verbose_option


class MultiBuildCommand(BuildCommand):
    """
    Run a PDM script using tab completion
    """
    
    name = "multibuild"

    def handle(self, project: Project, options: argparse.Namespace) -> None:
        """The command handler function.

        :param project: the pdm project instance
        :param options: the parsed Namespace object
        """
        for k, v in project.config.items():
            project.core.ui.echo(repr((k, v)), err=True)
        project.core.ui.echo(repr(options), err=True)
        project.backend.root
        
        # try:
        #     subprocess.run(f"pdm {user_input}", shell=True)
        # except KeyboardInterrupt:
        #     project.core.ui.echo(message="Choice aborted by user.", err=True)


def plugin(core: Core) -> None:
    core.register_command(MultiBuildCommand)
