import svgwrite
import psutil

from .theme_helper import loadTheme

def create(data, settings={}):

    process = psutil.Process()
    memory_usage = process.memory_info().rss  # in bytes
    print(f"--Memory Module Start: {memory_usage / 1024 ** 2} MB")    
    
    """
    Create an SVG image from the given data and settings.
    
    data: dict containing entities to render, you can pass an empty dict {}
    settings: dict containing settings for the theme
        - theme: The slug of the theme we want to use
        - color: The name of the color scheme to use.
        - layers: An array of layer names to show. If nothing set, all layers are shown. ['assets', 'belts', 'walls', 'spaceship', 'rails', 'electrical']
        - add_grid: Add a grid to the SVG for debugging (default: False)
    TODO: move all SVGWRITE stuff into parent theme class.
    """
    
    theme_slug = settings.get('theme', 'squares') or 'squares'
    color_scheme = settings.get('color', 'black') or 'black'

    # Load the theme
    try:
        ThemeClass = loadTheme(theme_slug)
        theme = ThemeClass(data, settings)
    except ValueError as e:
        print(f"Error: {e}. Falling back to 'squares' theme.")
        ThemeClass = loadTheme('squares')
        theme = ThemeClass(data, settings)

    # Check if the color scheme passed in settings is available in the theme
    if color_scheme not in theme.COLOR_SCHEMES:
        raise ValueError(f"Color scheme '{color_scheme}' is not available in the theme.")        

    # Calculate the viewBox parameters
    bounds = theme.get_entity_bounds()    
    viewbox_width = bounds['max_x']
    viewbox_height = bounds['max_y']

    
    # Create the SVG drawing object optimized for screen
    dwg = svgwrite.Drawing(
        profile='full',
        size=('100%', '100%'),
        viewBox=f"0 0 {viewbox_width} {viewbox_height}"
    )

    # Do the rendering
    theme.render(dwg) 
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
        'theme_name': theme_slug,   
    }


    memory_usage = process.memory_info().rss  # in bytes
    print(f"---Memory Module END: {memory_usage / 1024 ** 2} MB")    

    return result
