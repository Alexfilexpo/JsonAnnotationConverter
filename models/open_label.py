from pydantic import BaseModel

from typing import Dict, List, Optional, Union


class ElementObject(BaseModel):
    name: str
    type: str


class RdfData(BaseModel):
    type: str
    uid: str


class ElementRelation(BaseModel):
    name: str
    rdf_objects: List[RdfData]
    rdf_subjects: List[RdfData]
    type: str


class OpenLabelElement(BaseModel):
    objects: Dict[str, ElementObject]
    relations: Dict[str, ElementRelation]


class FrameObjectBbox(BaseModel):
    name: str
    stream: str
    val: list


class FrameObjectBooleanOrText(BaseModel):
    name: str
    val: Optional[Union[str, bool]]


class FrameObjectData(BaseModel):
    bbox: List[FrameObjectBbox]
    boolean: Optional[List[FrameObjectBooleanOrText]]
    text: Optional[List[FrameObjectBooleanOrText]]


class FrameObject(BaseModel):
    object_data: FrameObjectData


class OpenLabelFrame(BaseModel):
    objects: Dict[str, FrameObject]
    relations: dict


class OpenLabelWrapper(BaseModel):
    elements: OpenLabelElement
    frames: Dict[str, OpenLabelFrame]


class OpenLabelAnnotation(BaseModel):
    data: Dict[str, OpenLabelWrapper]

