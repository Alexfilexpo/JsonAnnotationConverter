from fastapi import FastAPI
from starlette.responses import RedirectResponse

from models import annotell
from services.converter import converter

app = FastAPI()


@app.get("/")
def redirect_to_client():
    response = RedirectResponse(url='/docs')
    return response


@app.post("/")
def processing_annotation(annotation: annotell.AnnotellAnnotation):
    return converter(annotation)


