import json

# Do not include these items in the JSON file
BLACKLIST = ['fish', 'tree', 'ghost', 'cliff', 'biter', 'sand', 'worm', 'rock', 'spitter', 'item-on-ground', 'locomotive', 'wagon', 'pipe-to-ground']

# Group entities into logical groups, anything not in these groups is an ASSET
BELT = ['belt']
RAILS = ['rail']
WALLS = ['wall', 'gate']
SPLITTERS = ['splitter']
SPACESHIP = ['spaceship']
ELECTRIC_POLES = ['electric-pole']

approved_entities = {key: [] for key in ['belts', 'splitters', 'rails', 'walls', 'asset', 'spaceship', 'electrical']}

# JSON file should be coming from FUE5-Exporter MOD inside of Factorio
# https://github.com/FUE5BASE/FUE5-Exporter?tab=readme-ov-file

def parseFUE5(json_data):
    approved_entities = {key: [] for key in ['belts', 'splitters', 'rails', 'walls', 'asset', 'spaceship', 'electrical']}

    for entity in json_data.get('entities', []):
        if not any(blacklisted in entity['name'].lower() for blacklisted in BLACKLIST):
            if any(belt in entity['name'] for belt in BELT):
                approved_entities['belts'].append(entity)
            elif any(rail in entity['name'] for rail in RAILS):
                approved_entities['rails'].append(entity)
            elif any(wall in entity['name'] for wall in WALLS):
                approved_entities['walls'].append(entity)
            elif any(splitter in entity['name'] for splitter in SPLITTERS):
                approved_entities['splitters'].append(entity)
            elif any(spaceship in entity['name'] for spaceship in SPACESHIP):
                approved_entities['spaceship'].append(entity)
            elif any(electric_pole in entity['name'] for electric_pole in ELECTRIC_POLES):
                approved_entities['electrical'].append(entity)
            else:
                approved_entities['asset'].append(entity)

    # Sort each category of approved entities by their x, y coordinates
    for category in approved_entities:
        approved_entities[category].sort(key=lambda e: (e['x'], e['y']))

    return approved_entities
