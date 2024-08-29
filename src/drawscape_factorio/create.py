import svgwrite
from drawscape_factorio.themes.circles_theme import CirclesTheme
from drawscape_factorio.themes.default_theme import DefaultTheme

def create(data, template='default', add_grid=False):

    print(f"Creating SVG with template: {template}")
    
    # Initialize the theme based on the template parameter
    if template == 'circles':
        theme = CirclesTheme()
    else:  # default theme
        theme = DefaultTheme(resolution='LOW')

    # Calculate the bounds of all entities in the data
    bounds = get_entity_bounds(data)
    
    # Calculate the viewBox parameters
    viewbox_x = bounds['min_x']
    viewbox_y = bounds['min_y']
    viewbox_width = bounds['max_x'] - bounds['min_x']
    viewbox_height = bounds['max_y'] - bounds['min_y']

    # Create the SVG drawing object optimized for screen
    dwg = svgwrite.Drawing(
        profile='full',
        size=('100%', '100%'),
        viewBox=f"{viewbox_x} {viewbox_y} {viewbox_width} {viewbox_height}"
    )

    # Add the grid to the drawing if requested
    if add_grid:
        create_grid(dwg, viewbox_x, viewbox_y, viewbox_width, viewbox_height)

    # Define entity types and that will be rendered
    entity_types = {
        'belts': theme.render_belt,
        'walls': theme.render_wall,
        'splitters': theme.render_splitter,
        'asset': theme.render_asset,
        'spaceship': theme.render_spaceship,
        'rails': theme.render_rail,
        'electrical': theme.render_electrical
    }

    # Create and populate groups for each entity type
    for entity_type, render_method in entity_types.items():
        group = dwg.g(id=entity_type)
        entities = data.get(entity_type, [])
        for entity in entities:
            group.add(render_method(dwg, entity))
        if entities:  # Check if there are any entities for this type
            dwg.add(group)

    # Get the SVG string
    svg_string = dwg.tostring()

    # Prepare the return dictionary
    result = {
        'svg_string': svg_string,
        'bounds': bounds,
        'viewbox': {
            'x': viewbox_x,
            'y': viewbox_y,
            'width': viewbox_width,
            'height': viewbox_height
        },
        'size': {
            'width': 100,
            'height': 100,
            'unit': '%'
        },
        'template': template,
        'theme_resolution': theme.resolution,
    }

    return result

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

def create_grid(dwg, viewbox_x, viewbox_y, viewbox_width, viewbox_height):
    # Create a light gray grid for the whole drawing
    # really just for debugging theme layouts.

    grid_color = svgwrite.rgb(200, 200, 200)  # Light gray color
    grid_stroke_width = 0.05
        
    # Create a group for the grid
    grid_group = dwg.g(id="grid")
    
    # Vertical lines
    for x in range(int(viewbox_x), int(viewbox_x + viewbox_width) + 1):
        grid_group.add(dwg.line(
            start=(x, viewbox_y),
            end=(x, viewbox_y + viewbox_height),
            stroke=grid_color,
            stroke_width=grid_stroke_width
        ))
    
    # Horizontal lines
    for y in range(int(viewbox_y), int(viewbox_y + viewbox_height) + 1):
        grid_group.add(dwg.line(
            start=(viewbox_x, y),
            end=(viewbox_x + viewbox_width, y),
            stroke=grid_color,
            stroke_width=grid_stroke_width
        ))
    
    # Add the grid group to the drawing
    dwg.add(grid_group)