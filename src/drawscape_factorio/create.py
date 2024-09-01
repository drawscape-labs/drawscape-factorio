import svgwrite

from .themes.circles_theme import CirclesTheme
from .themes.default_theme import DefaultTheme

def create(data, settings={}):
    
    # Initialize the theme based on the template parameter
    theme_name = settings.get('theme_name', 'default')
    settings['show_layers'] = ['assets', 'belts', 'walls', 'rails']

    if theme_name == 'circles':
        theme = CirclesTheme(data, settings)
    else:  # default theme
        theme = DefaultTheme(data, settings)

    # Calculate the viewBox parameters
    bounds = theme.get_entity_bounds()    
    viewbox_width = bounds['max_x'] - bounds['min_x']
    viewbox_height = bounds['max_y'] - bounds['min_y']

    # Create the SVG drawing object optimized for screen
    dwg = svgwrite.Drawing(
        profile='full',
        size=('100%', '100%'),
        viewBox=f"0 0 {viewbox_width} {viewbox_height}"
    )

    # Do the rendering
    theme.render(dwg)

    # Get the SVG string
    svg_string = dwg.tostring()

    # Prepare the return dictionary
    result = {
        'svg_string': svg_string,
        'bounds': bounds,
        'viewbox': {
            'x': 0,
            'y': 0,
            'width': viewbox_width,
            'height': viewbox_height
        },
        'theme_name': theme_name,   
    }

    return result
