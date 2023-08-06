import typer

from fibery.console.commands.auth import auth


main = typer.Typer()
main.add_typer(auth, name="auth")
