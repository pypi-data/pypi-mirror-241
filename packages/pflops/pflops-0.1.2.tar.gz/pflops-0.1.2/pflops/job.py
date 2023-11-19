from typing import TypedDict
from urllib.parse import urljoin

import requests
import typer
from rich import print
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
    if r.status_code != 200:
        print("[red]Failed to reach Petaflops server.")
        return
    jobs = r.json()
    if not jobs:
        print("No jobs are running.")
    else:
        for job in jobs:
            # TODO
            print(job)


@app.command()
def submit(
    image: Annotated[
        str,
        typer.Option(
            help="Path to the image to run the job.",
        ),
    ],
    command: Annotated[
        str,
        typer.Option(
            help="Path to the executable to be submitted to a job queue.",
        ),
    ],
):
    """
    Submit a job to run.
    """
    r = requests.post(
        url=urljoin(config.BASE_URL, "/job/submit"),
        data={
            "image": image,
            "command": command,
        },
    )
    if r.status_code in [200, 201]:
        print(
            "[green]Job submitted. You can check your running jobs with `pflops job ls`."
        )
    else:
        print(f"[red]Job submission failed. Status code: {r.status_code}")
