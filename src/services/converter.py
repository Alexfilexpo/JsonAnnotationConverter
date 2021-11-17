import random
import string

# Allow script to be run inside api; allow relative imports
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models import annotell, open_label
from utils import calculations


def converter(data: dict):
    annotation = annotell.AnnotellAnnotation.parse_obj(data)

    # Populate openlabel elements
    objects = {}
    relations = {}
    relation_counter = 0
    for shapeObjectName, shapeObjectProperty in annotation.shapeProperties.items():
        # Populate openlabel element objects
        objects[shapeObjectName] = open_label.ElementObject(
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
    elements = open_label.OpenLabelElement(
        objects=objects,
        relations=relations
    )
    # Populate openlabel frames
    frame_objects = {}
    for shape in annotation.shapes["CAM"].features:
        # Populate openlabel frames objects
        frame_objects[shape.id] = open_label.FrameObject(
            object_data=open_label.FrameObjectData(
                bbox=[open_label.FrameObjectBbox(
                    name="bbox-" + "".join(random.choices(string.ascii_lowercase + string.digits, k=8)),
                    stream="CAM",
                    val=[
                        # Calculating midpoint of shape
                        *calculations.calculate_midpoint(*shape.geometry.coordinates.minX.coordinates,
                                                         *shape.geometry.coordinates.maxX.coordinates),
                        # Calculating width
                        calculations.calculate_points_segment(*shape.geometry.coordinates.minX.coordinates,
                                                              *shape.geometry.coordinates.maxX.coordinates),
                        # Calculating height
                        calculations.calculate_points_segment(*shape.geometry.coordinates.minY.coordinates,
                                                              *shape.geometry.coordinates.maxY.coordinates),
                    ]
                )]
            )
        )
        if annotation.shapeProperties[shape.id]["@all"].Unclear is not None:
            frame_objects[shape.id].object_data.boolean = [open_label.FrameObjectBooleanOrText(
                        name="Unclear",
                        val=annotation.shapeProperties[shape.id]["@all"].Unclear
                    )]
        if annotation.shapeProperties[shape.id]["@all"].ObjectType is not None:
            frame_objects[shape.id].object_data.text = [open_label.FrameObjectBooleanOrText(
                name="ObjectType",
                val=annotation.shapeProperties[shape.id]["@all"].ObjectType
            )]
    frame_relations = {}
    for relation_id in relations.keys():
        frame_relations[relation_id] = {}
    open_label_frame = open_label.OpenLabelFrame(
        objects=frame_objects,
        relations=frame_relations
    )
    frames = {
        "": open_label_frame
    }
    open_label_wrapper = open_label.OpenLabelWrapper(
        elements=elements,
        frames=frames
    )
    open_label_data = {
        'openlabel': open_label_wrapper
    }
    open_label_annotation = open_label.OpenLabelAnnotation(data=open_label_data)
    return open_label_annotation.json()
