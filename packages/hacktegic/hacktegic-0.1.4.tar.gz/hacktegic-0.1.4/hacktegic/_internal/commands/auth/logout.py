from argparse import Namespace

from asyncio import TaskGroup

from rich.console import Console
from rich.text import Text


from hacktegic._internal.base_command import BaseCommand
from hacktegic._internal.credentials import Credentials

class LogoutCommand(BaseCommand):
    @staticmethod
    async def run(tg: TaskGroup, args: Namespace) -> None:

        console = Console()

        creds = Credentials()
        await creds.load()

        if not await creds.authenticated():
            console.print("You seem already logged out.")

        else:
            remove = await creds.remove()
            if remove:
                console.print("You are now logged out!")

            else:
                console.print("Something went wrong!. Please try again.")


