"""
Parent theme is the base class for all themes.
This will be extended by child themes added to this theme folder

Theme Requirements:
    - Must define a THEME_NAME, THEME_SLUG, and THEME_VERSION
    - Must define a COLOR_SCHEMES dictionary with a 'main' key.    

TODO:
    - Remove reliance on svgwrite library and allow users to override with other SVG libraries.
"""

class ParentTheme:
    
    # Theme Attributes
    THEME_NAME = "Parent Theme"
    THEME_SLUG = "parent-theme"
    THEME_VERSION = "1.0"

    # Constants for directions
    NORTH = 0
    EAST = 2
    SOUTH = 4
    WEST = 6

    # Constant for stroke width
    STROKE_WIDTH = 0.2

    # Layers are meant to group like entities to hide/show as desired.
    # Each Layer Definitions is an array of entity names that we can use for fuzzy matching
    # Intent is this can be overridden at child theme level.
    LAYER_DEFINITIONS = {
        'belts': ['belt', 'splitter'],
        'walls': ['wall', 'gate'],
        'rails': ['rail'],
        'electrical': ['electric-pole'],
        'pipes': ['pipe'],
        'spaceship': ['spaceship'],
        'assets': [] ## This should be empty as a catch all. 
    }

    # Settings
    DEFAULT_SETTINGS = {
        'color': 'main',
        'layers': ['assets', 'belts', 'walls', 'rails', 'electrical', 'spaceship'], # what are we showing
        'add_grid': False
    }

    # Colors should be a background + each key in LAYER_DEFINITION
    # Colors are really meant to be built out at child theme level. This is just a fallback.
    # Structure: COLOR_SCHEMES[color_scheme_name] = {layer_name: color_value}
    # When defining colors in a child theme, always include a "main" color scheme as the fallback if nothing is defined.
    COLOR_SCHEMES = {
        'main': {
            'bg': None,
            'assets': '#000000',
            'belts': '#000000',
            'walls': '#000000',
            'spaceship': '#000000',
            'rails': '#000000',
            'pipes': '#000000',
            'electrical': '#000000'
        }
    }

    def __init__(self, data, settings={}):
        """
        Initialize the ParentTheme with data and settings.
        :param data: The entity data to be rendered
        :param settings: User-defined settings to override defaults
        """

        # Will be populated by the organize_layers method.
        # needs to be reset on init to not compound data from previous runs.
        self.LAYERS = {
            'belts': [],
            'walls': [],
            'rails': [],
            'electrical': [],
            'spaceship': [],
            'pipes': [],
            'assets': []
        }

        # Set the settings
        # Use default settings if user is passing bad settings
        self.settings = self.DEFAULT_SETTINGS.copy()
        for key, value in settings.items():
            if value is not None and value != []:
                self.settings[key] = value


        if data:
            self.organize_layers(data)
            self.bounds = self.get_entity_bounds()

    
    def get_color(self, layer_name):
        color_scheme = self.settings['color']
        return self.COLOR_SCHEMES[color_scheme].get(layer_name, self.COLOR_SCHEMES[color_scheme]['assets'])
    
    def list_colors(self):
        """
        Returns the COLOR_SCHEMES dictionary.
        """
        return self.COLOR_SCHEMES

       
    def organize_layers(self, data):
        """
        Build the LAYERS dictionary from the LAYER_DEFINITIONS.
        Intention is this is NOT overridden by child themes.
        """
        for entity in data.get('entities', []):
            if any(belt in entity['name'] for belt in self.LAYER_DEFINITIONS['belts']):
                self.LAYERS['belts'].append(entity)
            elif any(wall in entity['name'] for wall in self.LAYER_DEFINITIONS['walls']):
                self.LAYERS['walls'].append(entity)
            elif any(rail in entity['name'] for rail in self.LAYER_DEFINITIONS['rails']):
                self.LAYERS['rails'].append(entity)
            elif any(electrical in entity['name'] for electrical in self.LAYER_DEFINITIONS['electrical']):
                self.LAYERS['electrical'].append(entity)
            elif any(pipe in entity['name'] for pipe in self.LAYER_DEFINITIONS['pipes']):
                self.LAYERS['pipes'].append(entity)
            elif any(spaceship in entity['name'] for spaceship in self.LAYER_DEFINITIONS['spaceship']):
                self.LAYERS['spaceship'].append(entity)
            else:
                self.LAYERS['assets'].append(entity)

    
    def render(self, dwg):
        """
        Iterates through each layer and renders the entities in that LAYER.
        Each LAYER is a group of entities that are the same color and stroke width.
        Inside of each LAYER we have a switch case that determines the rendering for specific entity types.
        This is NOT intended to be overridden by child themes unless advanced logic is needed.
        """

        # Add the background to a group with id = 'background'
        # TODO: Will this be pen plotted if there is no stroke? 
        color_scheme = self.settings['color']
        if self.COLOR_SCHEMES[color_scheme]['bg']:
            background_group = dwg.g(id='background')
            background_group.add(dwg.rect(insert=(0, 0), size=(self.bounds['max_x'], self.bounds['max_y']), fill=self.COLOR_SCHEMES[color_scheme]['bg']))
            dwg.add(background_group)

        if self.settings['add_grid']:
            create_grid(dwg, 0, 0, self.bounds['max_x'] - self.bounds['min_x'], self.bounds['max_y'] - self.bounds['min_y'])

        # Add the layers
        for layer_name, entities in self.LAYERS.items():
            if layer_name in self.settings['layers']:
                group = dwg.g(id=layer_name)
                group['stroke'] = self.get_color(layer_name)
                group['stroke-width'] = self.STROKE_WIDTH
                if layer_name == 'rails':
                    group['stroke-width'] = 0.4
                group['fill'] = 'none'
                for entity in entities:
                    
                    # Switch case logic for rendering each entity based on its name
                    # This ensures that we can have unique rendering per entity within a LAYER group.
                    # Example: splitters and belts need different renderings, but are the same color and layer.
                    # TODO: keep adding render_<entity_name> methods as we add more entity types and see what needs custom rendering logic
                    if any(definition in entity['name'] for definition in ['belt']):
                        rendered_element = self.render_belt(dwg, entity)
                    elif any(definition in entity['name'] for definition in ['gate']):
                        rendered_element = self.render_gate(dwg, entity)
                    elif any(definition in entity['name'] for definition in ['wall']):
                        rendered_element = self.render_wall(dwg, entity)
                    elif any(definition in entity['name'] for definition in ['rail']):
                        rendered_element = self.render_rail(dwg, entity)
                    elif any(definition in entity['name'] for definition in ['splitter']):
                        rendered_element = self.render_splitter(dwg, entity)
                    elif any(definition in entity['name'] for definition in ['electric-pole']):
                        rendered_element = self.render_electric_pole(dwg, entity)
                    elif any(definition in entity['name'] for definition in ['pipe']):
                        rendered_element = self.render_pipe(dwg, entity)
                    else:
                        rendered_element = self.render_asset(dwg, entity)
                    if rendered_element:
                        group.add(rendered_element)
                if group.elements:
                    dwg.add(group)
        return None

    def get_entity_bounds(self):
        """
        Calculates the bounds of all entities in the data.
        This is used to set the viewbox for the SVG.
        Looking for max x,y coordinates for all entities.   
        TODO: have this consider which layers are being shown and only calculate bounds for those layers.
        """
        # If there are no entities, return None
        if not self.LAYERS:
            return None
                
        min_x = max_x = 0
        min_y = max_y = 0
        
        # Iterate through all entities to find the minimum and maximum x and y coordinates
        for entities in self.LAYERS.values():
            for entity in entities:
                min_x = min(min_x, entity['x'])
                max_x = max(max_x, entity['x'])
                min_y = min(min_y, entity['y'])
                max_y = max(max_y, entity['y'])
        
        # Return a dictionary with the calculated bounds
        return {
            'min_x': min_x,
            'max_x': max_x,
            'min_y': min_y,
            'max_y': max_y
        }
    
    def render_asset(self, dwg, entity):
        """
        Default rendering for all square assets
        Handles rotation based on direction.
        """

        """
        IMPORTANT: By default we are not rendering "small" assets.
        This can be overridden in a child themes if desired.
        But this is a big performance issue when rendering large maps.
        """
        if entity.get('height') <= 1 or entity.get('width') <=1:
            return None
        
        if entity.get('direction') in [self.EAST, self.WEST]:
            x = entity['x'] - entity['height'] / 2 + self.STROKE_WIDTH / 2
            y = entity['y'] - entity['width'] / 2 + self.STROKE_WIDTH / 2
            # handle rotation
            width = entity['height'] - self.STROKE_WIDTH
            height = entity['width'] - self.STROKE_WIDTH
        else:
            x = entity['x'] - entity['width'] / 2 + self.STROKE_WIDTH / 2
            y = entity['y'] - entity['height'] / 2 + self.STROKE_WIDTH / 2
            # no rotation
            width = entity['width'] - self.STROKE_WIDTH
            height = entity['height'] - self.STROKE_WIDTH
        
        return dwg.rect(insert=(x, y), size=(width, height))       


    def render_belt(self, dwg, entity):
        
        x = entity['x'] - entity['width'] / 2
        y = entity['y'] - entity['height'] / 2
        width = entity['width']
        height = entity['height']
        direction = entity['direction']
        center = (x + width / 2, y + height / 2)
        
        if entity.get('variant') == 'I':
            if direction in [self.NORTH, self.SOUTH]:  # Vertical
                start = (x + width * 0.5, y)
                end = (x + width * 0.5, y + height)
            elif direction in [self.EAST, self.WEST]:  # Horizontal
                start = (x, y + height * 0.5)
                end = (x + width, y + height * 0.5)
            else:
                return dwg.g()
            
            return dwg.line(start=start, end=end)
        
        if entity.get('variant') in ['L', 'R']:
            
            belt_group = dwg.g()
            
            # Create the L-shaped belt
            start_v = (x + width * 0.5, y)
            end_v = (x + width * 0.5, y + height * 0.5)
            
            start_h = (x + width * 0.5, y + height * 0.5)
            end_h = (x + width, y + height * 0.5)
            
            # Create a group for the L-shaped belt
            belt_group.add(dwg.line(start=start_v, end=end_v))
            belt_group.add(dwg.line(start=start_h, end=end_h))

            # Rotate the belt group based on the direction for L-shaped belts
            if entity.get('variant') == 'L':
                if direction == self.NORTH:
                    belt_group.rotate(270, center)
                elif direction == self.SOUTH:
                    belt_group.rotate(90, center)
                elif direction == self.EAST:
                    belt_group.rotate(0, center)
                elif direction == self.WEST:
                    belt_group.rotate(180, center)
            
            # Rotate the belt group based on the direction for R-shaped belts
            if entity.get('variant') == 'R':
                if direction == self.NORTH:
                    belt_group.rotate(0, center)
                elif direction == self.SOUTH:
                    belt_group.rotate(180, center)
                elif direction == self.EAST:
                    belt_group.rotate(90, center)
                elif direction == self.WEST:
                    belt_group.rotate(270, center)

            return belt_group;                
            
        return dwg.g()    

    def render_rail(self, dwg, entity):
        
        # center point of the entity
        x = entity.get('x')
        y = entity.get('y')

        direction = entity.get('direction')
        width = entity.get('width')
        group = dwg.g()

        if entity['name'] == 'straight-rail' and entity.get('variant') == "I":
            length = 2  # unsure why height width data doesn't seem to connect the lines. harcoding for now.

            # Draw a vertical line first
            half_length = length / 2
            start = (x, y - half_length)
            end = (x, y + half_length)
            
            line = dwg.line(start=start, end=end)
            
            # Create a group for the line
            rail_group = dwg.g()
            rail_group.add(line)

            if direction == self.EAST: rail_group.rotate(90, center=(x, y))
            
            group.add(rail_group)
        
        elif entity['name'] == 'straight-rail' and entity.get('variant') == "/":
            

            length = width
            # Draw a vertical line first
            half_length = length / 2
            start = (x, y - half_length)
            end = (x, y + half_length)
            
            line = dwg.line(start=start, end=end)
            
            # Create a group for the line
            rail_group = dwg.g()
            rail_group.add(line)
            
            # Rotate the group based on direction
            if direction == self.NORTH:
                rail_group.rotate(-45, center=(x, y))
            if direction == self.SOUTH:
                rail_group.rotate(-45, center=(x, y))

            # Rotate the group based on direction
            if direction == self.EAST:
                rail_group.rotate(45, center=(x, y))
            if direction == self.WEST:
                rail_group.rotate(45, center=(x, y))

            # Add the rotated group to the main group
            group.add(rail_group)

        elif entity['name'] == 'curved-rail':

            # Create two lines for curved rail
            width, height = entity['width'], entity['height']
            
            # Rotate the belt group based on the direction for L-shaped belts
            if entity.get('variant') == 'L':
                if direction == self.NORTH:
                    short_x = x - 2
                    short_y = y - 3
                    long_x = x + 1
                    long_y = y + 4

                elif direction == self.SOUTH:
                    short_x = x + 2 
                    short_y = y + 3
                    long_x = x - 1
                    long_y = y - 4

                elif direction == self.EAST:
                    short_x = x + 3
                    short_y = y - 2
                    long_x = x - 4
                    long_y = y + 1

                elif direction == self.WEST:
                    short_x = x + 4
                    short_y = y - 1
                    long_x = x - 3
                    long_y = y + 2

            
            # Rotate the belt group based on the direction for R-shaped belts
            if entity.get('variant') == 'R':
                if direction == self.NORTH:
                    short_x = x + 2
                    short_y = y - 3
                    long_x = x - 1
                    long_y = y + 4
                elif direction == self.SOUTH:
                    short_x = x - 2
                    short_y = y + 3
                    long_x = x + 1
                    long_y = y - 4

                elif direction == self.EAST:
                    short_x = x + 3
                    short_y = y + 2
                    long_x = x - 4
                    long_y = y - 1

                elif direction == self.WEST:
                    short_x = x - 3
                    short_y = y - 2
                    long_x = x + 4
                    long_y = y + 1


            # Draw the short line
            short_line = dwg.line(start=(x, y), end=(short_x, short_y))
            group.add(short_line)

            # Draw the long line
            long_line = dwg.line(start=(x, y), end=(long_x, long_y))
            group.add(long_line)

        return group


    def render_gate(self, dwg, entity):
        return self.render_asset(dwg, entity)

    def render_wall(self, dwg, entity):
        return self.render_asset(dwg, entity)

    def render_splitter(self, dwg, entity):
        return self.render_asset(dwg, entity)

    def render_electric_pole(self, dwg, entity):
        return self.render_asset(dwg, entity)

    def render_pipe(self, dwg, entity):
        return self.render_asset(dwg, entity)
    


def create_grid(dwg, viewbox_x, viewbox_y, viewbox_width, viewbox_height):
    """
    Creates a light gray grid for the whole drawing
    Really just for debugging theme layouts and placement.
    """

    grid_color = "#C8C8C8"  # Light gray color
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