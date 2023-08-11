import json
import jsonschema

# Read in json and schema files
with open("sets-definition.json") as f, open("sets-definition-schema.json") as sf:
    jsonfile = json.load(f)
    schemafile = json.load(sf)

    jsonschema.validate(jsonfile, schemafile)
