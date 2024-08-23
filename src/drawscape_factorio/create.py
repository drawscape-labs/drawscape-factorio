import json
import svgwrite
import os
from drawscape_factorio.import_json import parseJSON
from drawscape_factorio.themes.default_theme import DefaultTheme
from drawscape_factorio.optimize_svg import optimize_svg

def create(json_file_path, optimize=False):
    # Use parseJSON function to load and process the JSON file
    data = parseJSON(json_file_path)
    
    # Create an SVG drawing object
    output_svg = 'output.svg'
    dwg = svgwrite.Drawing(output_svg, profile='full')
    
    # Create groups for each category (Color of Pens)
    belt_group = dwg.g(id='belts')
    rail_group = dwg.g(id='rails')
    wall_group = dwg.g(id='walls')
    splitter_group = dwg.g(id='splitters')
    asset_group = dwg.g(id='assets')
    
    # Initialize the default theme
    theme = DefaultTheme()
    
    for entity in data.get('belts', []):
        belt_group.add(theme.build_belt(dwg, entity))
    
    ## TODO: Add rails
    # for entity in data.get('rails', []):
    #     rail_group.add(theme.build_rail(dwg, entity))
    
    for entity in data.get('walls', []):
        wall_group.add(theme.build_wall(dwg, entity))
    
    for entity in data.get('splitters', []):
        splitter_group.add(theme.build_splitter(dwg, entity))
    
    for entity in data.get('asset', []):
        asset_group.add(theme.build_asset(dwg, entity))
    
    # Add category groups directly to the drawing
    if belt_group:
        dwg.add(belt_group)
    if rail_group:
        dwg.add(rail_group)
    if wall_group:
        dwg.add(wall_group)
    if splitter_group:
        dwg.add(splitter_group)
    if asset_group:
        dwg.add(asset_group)
    
    # Save the SVG file
    dwg.save()

    if optimize:
        # Optimize the SVG file
        optimized_svg = optimize_svg(output_svg)
        
        if optimized_svg:
            # Remove the original unoptimized SVG file
            os.remove(output_svg)
            print(f"Original SVG file {output_svg} has been deleted.")
        else:
            print("SVG optimization failed. Original file retained.")
    else:
        print(f"SVG file saved as {output_svg}")
