from typing import Annotated

import typer
from rich import print
from rich.panel import Panel

import keks


app = typer.Typer(add_completion=False, no_args_is_help=True, rich_markup_mode='rich')


def version_callback(show: bool):
    if show:
        panel = Panel.fit(
            f'[bold][red]{keks.__title__}[/red] ─ [dodger_blue1]{keks.__version__}[/]',
            padding=(1, 4),
            border_style='grey42'
        )

        print(panel)
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            '--version',
            help='[bold red]Show[/] keks [bold]version[/] and exit.',
            is_eager=True,
            callback=version_callback
        )
    ] = False
):
    pass


if __name__ == '__main__':
    app()