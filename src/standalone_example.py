from services.converter import converter
import json


with open('annotell_1.json') as file:
    annotell_json = json.loads(file.read())
    print(converter(annotell_json))

