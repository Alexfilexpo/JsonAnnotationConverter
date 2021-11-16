from fastapi import FastAPI

from models import annotell, open_label

app = FastAPI()


@app.post("/")
def convert(annotation: annotell.AnnotellAnnotation):
    elements = {}
    relations = {}
    relation_counter = 0
    for shapeObjectName, shapeObjectProperty in annotation.shapeProperties.items():
        # Populate openlabel element objects
        elements[shapeObjectName] = open_label.ElementObject(
            name=shapeObjectName,
            type=shapeObjectProperty['@all'].class_
        )
        # Populate openlabel element relations
        rdf_subject_uid = None
        if shapeObjectProperty["@all"].PushingOrPulling is not None:
            if type(shapeObjectProperty["@all"].PushingOrPulling) == dict:
                rdf_subject_uid = shapeObjectProperty["@all"].PushingOrPulling["shape"]
            elif type(shapeObjectProperty["@all"].PushingOrPulling) == str:
                rdf_subject_uid = shapeObjectProperty["@all"].PushingOrPulling
            relations[str(relation_counter)] = open_label.ElementRelation(
                name=str(relation_counter),
                rdf_objects=[open_label.RdfData(
                    type="object",
                    uid=shapeObjectName
                )],
                rdf_subjects=[open_label.RdfData(
                    type="object",
                    uid=rdf_subject_uid
                )],
                type="PushingOrPulling"
            )
        relation_counter += 1

    return annotation


# @app.post("/")
# def convert(annotation: open_label.OpenLabelAnnotation):
#     return annotation

