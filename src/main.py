from fastapi import FastAPI

from models import annotell
from services.converter import converter

app = FastAPI()


@app.post("/")
def processing_annotation(annotation: annotell.AnnotellAnnotation):
    return converter(annotation)


