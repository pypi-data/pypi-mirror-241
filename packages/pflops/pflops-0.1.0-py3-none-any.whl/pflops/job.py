import time
from typing import TypedDict
from urllib.parse import urljoin, urlsplit

import requests
import typer
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from rich import print
from rich.progress import Progress
from rich.columns import Columns
from typing_extensions import Annotated

from . import config

app = typer.Typer()


class FileInfo(TypedDict):
    name: str
    size: int


@app.command()
def ls():
    """
    List currently running jobs.
    """
    r = requests.get(url=urljoin(config.BASE_URL, "/job/list"))
    # TODO


@app.command()
def submit(
    command: Annotated[
        str,
        typer.Argument(
            help="Path to the executable to be submitted to a job queue.",
        ),
    ],
):
    """
    Submit a job to run.
    """
    r = requests.get(url=urljoin(config.BASE_URL, f"/job/submit?{command}"))
    if r.status_code in [200, 201]:
        print(
            "[green]Job submitted. You can check your running jobs with `pflops job ls`."
        )
    else:
        print(f"[red]Job submission failed. Status code: {r.status_code}")
