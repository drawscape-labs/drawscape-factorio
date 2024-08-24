import svgwrite
import os
from drawscape_factorio.import_json import parseJSON
from drawscape_factorio.themes.default_theme import DefaultTheme
from drawscape_factorio.optimize_svg import optimize_svg

# Constants for filenames
DEFAULT_OUTPUT_SVG = 'output.svg'

def create(json_file_path, optimize=False):
    
    # Use parseJSON function to load and process the JSON file
    data = parseJSON(json_file_path)
    
    # Get the bounds of all entities
    bounds = get_entity_bounds(data)
    
    # Define A4 paper size in mm with 10mm padding
    svg_width_mm = 210
    svg_height_mm = 297
    padding_mm = 10
    content_width_mm = svg_width_mm - 2 * padding_mm
    content_height_mm = svg_height_mm - 2 * padding_mm
    
    # Calculate the dimensions and scale
    width = bounds['max_x'] - bounds['min_x']
    height = bounds['max_y'] - bounds['min_y']
    scale = min(content_width_mm / width, content_height_mm / height)
    
    # Calculate the scaled dimensions
    scaled_width = width * scale
    scaled_height = height * scale
    
    # Calculate offsets to center the drawing horizontally and vertically with padding
    y_offset = (svg_height_mm - scaled_height) / 2
    
    # Calculate the viewBox parameters to center the content horizontally
    viewbox_width = svg_width_mm / scale
    viewbox_height = svg_height_mm / scale
    viewbox_x = (bounds['min_x'] + bounds['max_x']) / 2 - viewbox_width / 2
    viewbox_y = bounds['min_y'] - (y_offset - padding_mm) / scale
    
    # Create the SVG drawing object with forced A4 size and centered content
    dwg = svgwrite.Drawing(
        filename=DEFAULT_OUTPUT_SVG,
        profile='full',
        size=(f'{svg_width_mm}mm', f'{svg_height_mm}mm'),
        viewBox=f"{viewbox_x} {viewbox_y} {viewbox_width} {viewbox_height}"
    )
        
    # Initialize the default theme
    theme = DefaultTheme()

    # Define entity types and their corresponding build methods
    entity_types = {
        'belts': theme.build_belt,
        'walls': theme.build_wall,
        'splitters': theme.build_splitter,
        'asset': theme.build_asset,
        # 'rails': theme.build_rail,  # TODO: Uncomment when rail building is implemented
    }

    # Create and populate groups for each entity type
    for entity_type, build_method in entity_types.items():
        group = dwg.g(id=entity_type)
        entities = data.get(entity_type, [])
        for entity in entities:
            group.add(build_method(dwg, entity))
        if entities:  # Check if there are any entities for this type
            dwg.add(group)

    # Save the SVG file
    dwg.save()

    # Print information about the SVG drawing
    print(f"Created SVG drawing:")
    print(f"  Output file: {DEFAULT_OUTPUT_SVG}")
    print(f"  Size: {svg_width_mm}mm x {svg_height_mm}mm (A4)")
    print(f"  ViewBox: {viewbox_x} {viewbox_y} {viewbox_width} {viewbox_height}")

    if optimize:
        # Optimize the SVG file
        optimized_svg = optimize_svg(DEFAULT_OUTPUT_SVG)
        
        if optimized_svg:
            # Remove the original unoptimized SVG file
            os.remove(DEFAULT_OUTPUT_SVG)
            print(f"Original SVG file {DEFAULT_OUTPUT_SVG} has been deleted.")
        else:
            print("SVG optimization failed. Original file retained.")
    else:
        print(f"SVG file saved as {DEFAULT_OUTPUT_SVG}")


# Function to calculate the bounds of all entities in the data
def get_entity_bounds(data):
    # Flatten all entities into a single list
    all_entities = [entity for category in data.values() for entity in category]
    
    # If there are no entities, return None
    if not all_entities:
        return None
    
    # Calculate the minimum and maximum x and y coordinates
    min_x = min(entity['x'] for entity in all_entities)
    max_x = max(entity['x'] for entity in all_entities)
    min_y = min(entity['y'] for entity in all_entities)
    max_y = max(entity['y'] for entity in all_entities)
    
    # Return a dictionary with the calculated bounds
    return {
        'min_x': min_x,
        'max_x': max_x,
        'min_y': min_y,
        'max_y': max_y
    }