from datetime import datetime
from prompt_toolkit.validation import Validator
import typer
from typing import Annotated, Optional
from prompt_toolkit import prompt
import rich
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.console import Console
from inferless_cli.utils.helpers import (
    decrypt_tokens,
)

from inferless_cli.utils.services import (
    get_volumes_list,
)


app = typer.Typer(
    no_args_is_help=True,
)

processing = "processing..."
desc = "[progress.description]{task.description}"
no_volumes = "[red]No volumes found in your account[/red]"


@app.command(
    "list",
    help="List all volumes.",
)
def list():
    _, _, _, workspace_id, _ = decrypt_tokens()
    with Progress(
        SpinnerColumn(),
        TextColumn(desc),
        transient=True,
    ) as progress:
        task_id = progress.add_task(description=processing, total=None)

        volumes = get_volumes_list(workspace_id)

        progress.remove_task(task_id)

    if len(volumes) == 0:
        rich.print(no_volumes)
        raise typer.Exit(1)

    table = Table(
        title="Volumes List",
        box=rich.box.ROUNDED,
        title_style="bold Black underline on white",
    )
    table.add_column("ID", style="yellow")
    table.add_column(
        "Name",
    )

    for volume in volumes:
        table.add_row(
            volume["id"],
            volume["name"],
        )

    console = Console()
    console.print(table)
    console.print("\n")
