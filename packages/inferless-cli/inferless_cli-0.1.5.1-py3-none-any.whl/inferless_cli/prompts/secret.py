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
    get_models,
    get_by_keys,
    key_bindings,
)

from inferless_cli.utils.services import (
    activate_model,
    deactivate_model,
    delete_model,
    get_workspace_models,
    rebuild_model,
    get_model_code,
    get_user_secrets,
    get_model_details,
)
from inferless_cli.utils.validators import validate_models


app = typer.Typer(
    no_args_is_help=True,
)

processing = "processing..."
desc = "[progress.description]{task.description}"
no_secrets = "[red]No secrets found in your account[/red]"


@app.command(
    "list",
    help="List all secrets.",
)
def list():
    with Progress(
        SpinnerColumn(),
        TextColumn(desc),
        transient=True,
    ) as progress:
        task_id = progress.add_task(description=processing, total=None)

        secrets = get_user_secrets()

        progress.remove_task(task_id)

    if len(secrets) == 0:
        rich.print(no_secrets)
        raise typer.Exit(1)

    table = Table(
        title="Secrets List",
        box=rich.box.ROUNDED,
        title_style="bold Black underline on white",
    )
    table.add_column("ID", style="yellow")
    table.add_column(
        "Name",
    )
    table.add_column("Created At")
    table.add_column("Last used on")

    for secret in secrets:
        created_at = datetime.fromisoformat(secret["created_at"]).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        updated_at = datetime.fromisoformat(
            secret["last_used_in_model_import"]
        ).strftime("%Y-%m-%d %H:%M:%S")
        table.add_row(
            secret["id"],
            secret["name"],
            created_at,
            updated_at,
        )

    console = Console()
    console.print(table)
    console.print("\n")
