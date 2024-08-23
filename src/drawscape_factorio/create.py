import json
import svgwrite
from drawscape_factorio.import_json import parseJSON

def create(json_file_path):
    # Use parseJSON function to load and process the JSON file
    data = parseJSON(json_file_path)
    
    # Create an SVG drawing object
    output_svg = 'output.svg'
    dwg = svgwrite.Drawing(output_svg, profile='full')  # A4 size in millimeters
    
    # Create a main group for all entities
    main_group = dwg.g(id='entities', transform='scale(6)')
    
    # Create groups for each category (Color of Pens)
    belt_group = dwg.g(id='belts')
    rail_group = dwg.g(id='rails')
    wall_group = dwg.g(id='walls')
    splitter_group = dwg.g(id='splitters')
    asset_group = dwg.g(id='assets')
    
    for entity in data.get('belts', []):
        belt_group.add(create_belts(dwg, entity))
    
    # for entity in data.get('rails', []):
    #     x = entity['x'] - entity['width'] / 2
    #     y = entity['y'] - entity['height'] / 2
    #     width = entity['width']
    #     height = entity['height']
    #     rail_group.add(dwg.rect(insert=(x, y), size=(width, height), fill='grey', stroke='black', stroke_width=0.1))
    
    for entity in data.get('walls', []):
        x = entity['x'] - entity['width'] / 2
        y = entity['y'] - entity['height'] / 2
        width = entity['width']
        height = entity['height']
        wall_group.add(dwg.rect(insert=(x, y), size=(width, height), fill='none', stroke='black', stroke_width=0.1))
    
    for entity in data.get('splitters', []):
        splitter_group.add(create_splitter(dwg, entity))
    
    for entity in data.get('asset', []):
        if 'name' in entity:
            if 'assembling-machine' in entity['name']:
                asset_group.add(create_asset(dwg, entity))
            else:
                asset_group.add(create_asset(dwg, entity))
    
    # Add category groups to the main group
    if belt_group:
        main_group.add(belt_group)
    if rail_group:
        main_group.add(rail_group)
    if wall_group:
        main_group.add(wall_group)
    if splitter_group:
        main_group.add(splitter_group)
    if asset_group:
        main_group.add(asset_group)
    
    # Add the main group to the drawing
    dwg.add(main_group)
    
    # Save the SVG file
    dwg.save()


def create_asset(dwg, entity, color = 'blue'):
    x = entity['x'] - entity['width'] / 2
    y = entity['y'] - entity['height'] / 2
    width = entity['width']
    height = entity['height']
    
    group = dwg.g()
    group.add(dwg.rect(insert=(x, y), size=(width, height), fill='none', stroke=(color), stroke_width=0.1))
    
    # Add X in the middle of the rect
    group.add(dwg.line(start=(x, y), end=(x + width, y + height), stroke=(color), stroke_width=0.1))
    group.add(dwg.line(start=(x, y + height), end=(x + width, y), stroke=(color), stroke_width=0.1))
    
    return group



def create_belts(dwg, entity):
    color = '#8B8000' 
    
    x = entity['x'] - entity['width'] / 2
    y = entity['y'] - entity['height'] / 2
    width = entity['width']
    height = entity['height']
    
    group = dwg.g()
    
    # Add direction indicator (2 lines)
    if 'direction' in entity:
        direction = entity['direction']
        
        print(entity)
        if direction == 0 or direction == 4:  # North or South (vertical)
            # Left side line
            start_left = (x + width * 0.25, y)
            end_left = (x + width * 0.25, y + height)
            
            # Right side line
            start_right = (x + width * 0.75, y)
            end_right = (x + width * 0.75, y + height)
            
            # Add left and right side lines
            group.add(dwg.line(start=start_left, end=end_left, stroke=color, stroke_width=0.05))
            group.add(dwg.line(start=start_right, end=end_right, stroke=color, stroke_width=0.05))
            
        
        elif direction == 2 or direction == 6:  # East or West (horizontal)
            start_top = (x, y + height * 0.25)
            end_top = (x + width, y + height * 0.25)
            start_bottom = (x, y + height * 0.75)
            end_bottom = (x + width, y + height * 0.75)

            group.add(dwg.line(start=start_top, end=end_top, stroke=color, stroke_width=0.05))
            group.add(dwg.line(start=start_bottom, end=end_bottom, stroke=color, stroke_width=0.05))
    
    return group

def create_splitter(dwg, entity):
    
    color = '#8B8000'
    
    print(entity)
    direction = entity.get('direction', 0)
    
    if direction == 2:
        x = entity['x'] - entity['height'] / 2
        y = entity['y'] - entity['width'] / 2
        width = entity['height']
        height = entity['width']
    else:
        x = entity['x'] - entity['width'] / 2
        y = entity['y'] - entity['height'] / 2
        width = entity['width']
        height = entity['height']
    
    
    
    group = dwg.g()
    
    # Create rectangle
    group.add(dwg.rect(insert=(x, y), size=(width, height), fill='none', stroke=color, stroke_width=0.1))
    
    return group
