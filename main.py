from fastapi import FastAPI

from models import annotell, open_label

app = FastAPI()


@app.post("/")
def convert(annotation: annotell.AnnotellAnnotation):
    return annotation


# @app.post("/")
# def convert(annotation: open_label.OpenLabelAnnotation):
#     return annotation

