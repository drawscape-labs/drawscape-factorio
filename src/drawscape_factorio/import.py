import json

# Do not include these items in the JSON file
BLACKLIST = ['fish', 'tree', 'ghost', 'cliff', 'biter', 'sand', 'worm', 'rock', 'spitter', 'item-on-ground', 'locomotive', 'wagon', 'pipe-to-ground']

# Group entities into logical groups, anyting not in these groups is an ASSET
BELT = ['belt']
RAILS = ['rail']
WALLS = ['wall', 'gate']
SPLITTERS = ['splitter']
SPACESHIP = ['spaceship']
ELECTRIC_POLES = ['electric-pole']

approved_entities = {key: [] for key in ['belts', 'splitters', 'rails', 'walls', 'asset', 'spaceship', 'electrical']}

# JSON file should be coming from FUE5-Exporter MOD inside of Factorio
# https://github.com/FUE5BASE/FUE5-Exporter?tab=readme-ov-file

def parseJSON(json_file_path, save_file=False):
  return