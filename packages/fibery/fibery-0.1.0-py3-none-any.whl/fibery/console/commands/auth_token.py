import typer
import asyncio

from tabulate import tabulate
from fibery.console.commands import pyppeteer_actions as action


token = typer.Typer()


def run(coroutine):
    asyncio.get_event_loop().run_until_complete(coroutine)


@token.command(name="create")
def token_create(email: str = typer.Option(...),
                 workspace: str = typer.Option(...),
                 login_url: str = "https://fibery.io/login"):

    # Get password securely
    password = typer.prompt("Type your password", hide_input=True)

    async def login_and_create_token():
        async with action.login(email, password, workspace, login_url) as page:
            result = await action.do_create_token(page)
            typer.echo(f"Token created: {result}")

    run(login_and_create_token())


@token.command(name="list")
def token_list(email: str = typer.Option(...),
               workspace: str = typer.Option(...),
               login_url: str = "https://fibery.io/login"):

    # Get password securely
    password = typer.prompt("Type your password", hide_input=True)

    async def login_and_list_tokens():
        async with action.login(email, password, workspace, login_url) as page:
            result = await action.do_list_tokens(page)
            typer.echo(tabulate(result, headers="keys"))

    run(login_and_list_tokens())


@token.command(name="delete")
def token_delete(email: str = typer.Option(...),
                 workspace: str = typer.Option(...),
                 token_id: str = typer.Option(...),
                 login_url: str = "https://fibery.io/login"):

    # Get password securely
    password = typer.prompt("Type your password", hide_input=True)

    async def login_and_delete_token():
        async with action.login(email, password, workspace, login_url) as page:
            result = await action.do_delete_token(page, token_id)
            typer.echo(result)

    run(login_and_delete_token())
