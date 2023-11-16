# import argparse
# import readline
# import subprocess

# from pdm.cli.commands.base import BaseCommand
# from pdm.cli.commands.publish import Command as PublishCommand
# from pdm.core import Core
# from pdm.project import Project
# from pdm.cli.options import Option, global_option, project_option, verbose_option


# class MuiliPublishCommand(BaseCommand):
#     """
#     Run a PDM script using tab completion
#     """
    
#     name = "publish"
#     arguments = []

#     @staticmethod
#     def setup_tab_completion(scripts: list[str]) -> None:
#         def complete(text: str, state: int):
#             matches = []
#             for item in scripts:
#                 if item.startswith(text):
#                     matches.append(item)

#             if state < len(matches):
#                 return matches[state]
#             else:
#                 return None

#         readline.set_completer(complete)
#         readline.parse_and_bind("tab: complete")

#     def handle(self, project: Project, options: argparse.Namespace) -> None:
#         """The command handler function.

#         :param project: the pdm project instance
#         :param options: the parsed Namespace object
#         """

#         scripts = [str(script) for script in project.scripts]
#         if not scripts:
#             return project.core.ui.echo(message="No scripts found!", err=True)

#         self.setup_tab_completion(scripts)

#         try:
#             user_input = input(f"Choose script (<TAB> for list): ")
#             subprocess.run(f"pdm {user_input}", shell=True)
#         except KeyboardInterrupt:
#             project.core.ui.echo(message="Choice aborted by user.", err=True)


# def plugin(core: Core) -> None:
#     core.register_command(MuiliPublishCommand)

from pdm.cli.commands.base import BaseCommand
from pdm.cli.commands.publish import Command as PublishCommand
from pdm.core import Core
from pdm.backend.base import Context


class MypycBuildHook:
    def pdm_build_hook_enabled(self, context: Context):
        return context.target == "wheel"

    def pdm_build_initialize(self, context: Context):
        context.ensure_build_dir()
        print("pdm_build_initialize")