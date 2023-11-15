import webbrowser
from argparse import Namespace
from asyncio import TaskGroup

from rich.console import Console
from rich.text import Text

from hacktegic._internal.base_command import BaseCommand
from hacktegic._internal.credentials import Credentials



class RegisterCommand(BaseCommand):
    @staticmethod
    async def run(tg: TaskGroup, args: Namespace) -> None:
        console = Console()

        try:
            creds = Credentials()
            await creds.load()

            if await creds.authenticated():
                console.print("You seem to already have an account.")
                console.print("If you want to register again, log out first using using 'hacktegic auth logout'.")

            else:
                webbrowser.open("https://cloud.hacktegic.com/register")
                console.print("Use the web browser to register.")
                console.print("If it did not open for you, navigate to https://cloud.hacktegic.com/register .")

        except:
            text = Text("Something went wrong!")
            text.stylize("bold red")
            console.print(text)
