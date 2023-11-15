from urllib.parse import urljoin, urlsplit

import requests
import typer
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from rich import print
from rich.columns import Columns
from rich.progress import Progress
from typing_extensions import Annotated

from . import config
from .common import FileInfo

app = typer.Typer()


@app.command()
def ls():
    """
    List available images.
    """
    r = requests.get(url=urljoin(config.BASE_URL, "/image/list"))
    body: list[FileInfo] = r.json()
    filenames = [file["name"] for file in body]
    print(Columns(filenames, padding=(0, 6)))


@app.command()
def build():
    """
    TODO
    """
    print("TODO")
    pass
