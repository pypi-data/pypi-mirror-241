import typer

from . import dataset
from . import image
from . import job

app = typer.Typer()

app.add_typer(dataset.app, name="dataset")
app.add_typer(image.app, name="image")
app.add_typer(job.app, name="job")
