import argparse

from hacktegic._internal.commands.auth.login import LoginCommand
from hacktegic._internal.commands.auth.register import RegisterCommand
from hacktegic._internal.commands.auth.logout import LogoutCommand
from hacktegic._internal.commands.projects.create import ProjectsCreateCommand
from hacktegic._internal.commands.projects.delete import ProjectsDeleteCommand
from hacktegic._internal.commands.projects.describe import ProjectsDescribeCommand
from hacktegic._internal.commands.projects.list import ProjectsListCommand
from hacktegic._internal.commands.projects.update import ProjectsUpdateCommand


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, **kwargs):
        super(ArgumentParser, self).__init__(**kwargs)

    def add_arguments(self):
        subparsers = self.add_subparsers()

        auth_parser = subparsers.add_parser("auth", help="authentication commands")
        auth_subparsers = auth_parser.add_subparsers(help="auth sub-command help")

        projects_parser = subparsers.add_parser("projects", help="project commands")
        projects_subparsers = projects_parser.add_subparsers(
            help="project sub-command help"
        )

        login_parser = auth_subparsers.add_parser("login", help="login help")
        login_parser.set_defaults(func=LoginCommand.run)

        logout_parser = auth_subparsers.add_parser("logout", help="logout help")
        logout_parser.set_defaults(func=LogoutCommand.run)

        register_parser = auth_subparsers.add_parser("register", help="register help")
        register_parser.set_defaults(func=RegisterCommand.run)

        create_project_parser = projects_subparsers.add_parser(
            "create", help="Create a new project"
        )
        create_project_parser.set_defaults(func=ProjectsCreateCommand.run)
        create_project_parser.add_argument("project_name", type=str)

        describe_project_parser = projects_subparsers.add_parser(
            "describe", help="Describe project"
        )
        describe_project_parser.set_defaults(func=ProjectsDescribeCommand.run)
        describe_project_parser.add_argument("project_id", type=str)

        list_projects_parser = projects_subparsers.add_parser(
            "list", help="Get list of projects"
        )
        list_projects_parser.set_defaults(func=ProjectsListCommand.run)

        update_project_parser = projects_subparsers.add_parser(
            "update", help="Update a project"
        )
        update_project_parser.set_defaults(func=ProjectsUpdateCommand.run)
        update_project_parser.add_argument("project_id", type=str)
        update_project_parser.add_argument(
            "--name", type=str, help="New name to be set"
        )

        delete_project_parser = projects_subparsers.add_parser(
            "delete", help="Delete a project"
        )
        delete_project_parser.set_defaults(func=ProjectsDeleteCommand.run)
        delete_project_parser.add_argument("project_id", type=str)
