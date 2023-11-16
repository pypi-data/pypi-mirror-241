import typer

from . import dataset, image, job
from .fs import app

app.add_typer(dataset.app, name="dataset")
app.add_typer(image.app, name="image")
app.add_typer(job.app, name="job")
