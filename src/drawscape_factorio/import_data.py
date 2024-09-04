
# Do not include these items in the JSON file
BLACKLIST = ['fish', 'salmon', 'tree', 'ghost', 'cliff', 'biter', 'sand', 'worm', 'rock', 'spitter', 'item-on-ground', 'locomotive', 'wagon']

"""
This JSON data is coming from the Factorio FUE5 MOD
https://github.com/FUE5BASE/FUE5-Exporter
"""
def importFUE5(json_data):
    entities = []

    for entity in json_data.get('entities', []):
        if not any(blacklisted in entity['name'].lower() for blacklisted in BLACKLIST):
            entities.append(entity)

    # Sort entities by their x, y coordinates
    entities.sort(key=lambda e: (e['x'], e['y']))

    return {'entities': entities}

## TODO: Implement blueprint importer
def importBlueprint(data):
    return None