import svgwrite
import subprocess
import tempfile
import os
import time


from .theme_helper import loadTheme

def create(data, settings={}):
    
    """
    Create an SVG image from the given data and settings.
    
    data: dict containing entities to render, you can pass an empty dict {}
    settings: dict containing settings for the theme
        - theme: The slug of the theme we want to use
        - color: The name of the color scheme to use.
        - layers: An array of layer names to show. If nothing set, all layers are shown. ['assets', 'belts', 'walls', 'spaceship', 'rails', 'electrical', 'pipes']
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
    theme.render_styles(dwg)
    svg_string = dwg.tostring()

    # start_time = time.time()
    # svg_string_optimized = optimize_svg(svg_string)
    # end_time = time.time()
    # optimization_time = end_time - start_time
    # print(f'Optimization completed in {optimization_time:.2f} seconds')

    # Prepare the return dictionary
    result = {
        'svg_string': svg_string,
        'size_mb': len(svg_string) / 1024 / 1024,
        'bounds': bounds,
        'viewbox': {
            'x': 0,
            'y': 0,
            'width': viewbox_width,
            'height': viewbox_height
        },
        'theme_name': theme_slug,   
    }

    return result


def optimize_svg(svg_data):
    # Create temporary input and output files
    with tempfile.NamedTemporaryFile(mode='w', suffix='.svg', delete=False) as temp_input_file, \
         tempfile.NamedTemporaryFile(mode='w', suffix='.svg', delete=False) as temp_output_file:
        temp_input_file.write(svg_data)
        temp_input_path = temp_input_file.name
        temp_output_path = temp_output_file.name

    # Construct the vpype command
    vpype_command = [
        "vpype",
        "read",
        temp_input_path,
        "linemerge",
        "linesort",
        "linesimplify",
        "write",
        temp_output_path
    ]

    print(vpype_command)

    # Execute the vpype command
    try:
        subprocess.run(vpype_command, check=True, capture_output=True, text=True)
        print(f"Optimized SVG data generated.")
        with open(temp_output_path, 'r') as optimized_file:
            optimized_svg = optimized_file.read()
    except subprocess.CalledProcessError as e:
        print(f"Error optimizing SVG: {e}")
        print(f"Command output: {e.output}")
        optimized_svg = None
    finally:
        # Clean up the temporary files
        os.unlink(temp_input_path)
        os.unlink(temp_output_path)

    return optimized_svg