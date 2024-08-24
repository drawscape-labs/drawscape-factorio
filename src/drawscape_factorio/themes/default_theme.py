class DefaultTheme:
    # Constants for directions
    NORTH = 0
    EAST = 2
    SOUTH = 4
    WEST = 6

    # Constant for stroke width
    STROKE_WIDTH = 0.4  # unsure if this really translates to millimetes, AI saying it's releative to the view box. 

    def __init__(self, resolution='HIGH'):
        self.resolution = resolution
        self.default_color = '#0000FF' # Blue
        self.belt_color = '#008000' # Green
        self.splitter_color = '#008000' # Green
        self.wall_color = '#FF0000' # Red
        self.asset_color = '#0000FF'  # Blue

    def render_default(self, dwg, entity, color=None):
        
        # This method renders a default entity as a filled in square
        # Inputs:
        #   dwg: The SVG drawing object
        #   entity: A dictionary containing entity properties including:
        #   color: Optional color parameter, defaults to self.default_color if not provided

        if color is None: 
            color = self.default_color

        # Calculate top-left corner from center point
        top_left_x = entity['x'] - entity['width'] / 2
        top_left_y = entity['y'] - entity['height'] / 2
        width = entity['width']
        height = entity['height']

        group = dwg.g()
        
        # Draw the rectangle
        stroke_offset = self.STROKE_WIDTH / 2
        group.add(dwg.rect(
            insert=(top_left_x + stroke_offset, top_left_y + stroke_offset),
            size=(width - self.STROKE_WIDTH, height - self.STROKE_WIDTH),
            fill='none',
            stroke=color,
            stroke_width=self.STROKE_WIDTH
        ))
        
        # If height is greater than or equal to 1, draw an X in the middle
        if height > 1 or width > 1:
            center_x = entity['x']
            center_y = entity['y']
            half_width = width / 2 - self.STROKE_WIDTH / 2
            half_height = height / 2 - self.STROKE_WIDTH / 2
            
            # Draw the X
            group.add(dwg.line(start=(center_x - half_width, center_y - half_height), 
                               end=(center_x + half_width, center_y + half_height), 
                               stroke=color, stroke_width=self.STROKE_WIDTH))
            group.add(dwg.line(start=(center_x - half_width, center_y + half_height), 
                               end=(center_x + half_width, center_y - half_height), 
                               stroke=color, stroke_width=self.STROKE_WIDTH))
            
        if height > 2 or width > 2:
            # Draw a cross that touches all sides of the rectangle
            center_x = entity['x']
            center_y = entity['y']
            half_width = width / 2 - self.STROKE_WIDTH / 2
            half_height = height / 2 - self.STROKE_WIDTH / 2

            # Vertical line of the cross
            group.add(dwg.line(start=(center_x, center_y - half_height),
                               end=(center_x, center_y + half_height),
                               stroke=color, stroke_width=self.STROKE_WIDTH))

            # Horizontal line of the cross
            group.add(dwg.line(start=(center_x - half_width, center_y),
                               end=(center_x + half_width, center_y),
                               stroke=color, stroke_width=self.STROKE_WIDTH))
        
        return group

    def render_asset(self, dwg, entity):
        group = self.render_default(dwg, entity, color=self.asset_color)        
        return group
    
    def render_wall(self, dwg, entity):
        group = self.render_default(dwg, entity, color=self.wall_color)        
        return group

    def render_splitter(self, dwg, entity):
        direction = entity.get('direction', self.NORTH)
        
        if direction == self.EAST:
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
        group.add(dwg.rect(insert=(x, y), size=(width, height), fill='none', stroke=self.splitter_color, stroke_width=self.STROKE_WIDTH))
        
        # Add a single line down the middle of the rectangle
        if direction == self.EAST:
            start = (x + width / 2, y)
            end = (x + width / 2, y + height)
        else:
            start = (x, y + height / 2)
            end = (x + width, y + height / 2)
        
        group.add(dwg.line(start=start, end=end, stroke=self.splitter_color, stroke_width=self.STROKE_WIDTH))
        
        return group

    def render_belt(self, dwg, entity):
        x = entity['x'] - entity['width'] / 2
        y = entity['y'] - entity['height'] / 2
        width = entity['width']
        height = entity['height']
        
        group = dwg.g()
        
        if 'direction' in entity:
            direction = entity['direction']
            
            if direction == self.NORTH or direction == self.SOUTH:  # North or South (vertical)
                start = (x + width * 0.5, y)
                end = (x + width * 0.5, y + height)
                
                group.add(dwg.line(start=start, end=end, stroke=self.belt_color, stroke_width=self.STROKE_WIDTH))
            
            elif direction == self.EAST or direction == self.WEST:  # East or West (horizontal)
                start = (x, y + height * 0.5)
                end = (x + width, y + height * 0.5)

                group.add(dwg.line(start=start, end=end, stroke=self.belt_color, stroke_width=self.STROKE_WIDTH))
        
        return group