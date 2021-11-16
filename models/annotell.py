from enum import Enum
from typing import Dict, List, Optional, Union

from pydantic import BaseModel


# Base Annotell models
class Certainty(str, Enum):
    SURE = 'sure'
    UNSURE = 'unsure'


class InternalProperty(BaseModel):
    active: Optional[int]
    created: int

    # Creating aliases
    class Config:
        fields = {
            'active': '@active',
            'created': '@created'
        }


# Shape property models
class ShapeProperty(BaseModel):
    ObjectType: Optional[str]
    PushingOrPulling: Optional[Union[dict, str]]
    Unclear: Optional[bool]
    class_: str

    # Creating aliases
    class Config:
        fields = {'class_': 'class'}


# Shapes models
class CoordProperty(BaseModel):
    coordinates: list
    visible: bool


class GeometryCoords(BaseModel):
    maxX: CoordProperty
    maxY: CoordProperty
    minX: CoordProperty
    minY: CoordProperty


class ShapeGeometry(BaseModel):
    coordinates: GeometryCoords
    type: str


class Shape(BaseModel):
    geometry: ShapeGeometry
    id: str
    properties: dict
    type: str


class ShapesWrapper(BaseModel):
    type: str
    features: List[Shape]


class AnnotellAnnotation(BaseModel):
    certainty: Certainty
    internalProperties: Dict[str, InternalProperty]
    properties: dict
    shapeProperties: Dict[str, Dict[str, ShapeProperty]]
    shapes: Dict[str, ShapesWrapper]


