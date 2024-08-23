class DefaultTheme:
    # Constants for directions
    NORTH = 0
    EAST = 2
    SOUTH = 4
    WEST = 6

    # Constant for stroke width
    STROKE_WIDTH = 0.15

    def __init__(self):
        self.belt_color = '#008000' # Green
        self.splitter_color = '#008000' # Green
        self.wall_color = '#FF0000' # Red
        self.asset_color = '#0000FF'  # Blue

    def build_belt(self, dwg, entity):
        x = entity['x'] - entity['width'] / 2
        y = entity['y'] - entity['height'] / 2
        width = entity['width']
        height = entity['height']
        
        group = dwg.g()
        
        if 'direction' in entity:
            direction = entity['direction']
            
            if direction == self.NORTH or direction == self.SOUTH:  # North or South (vertical)
                start_left = (x + width * 0.25, y)
                end_left = (x + width * 0.25, y + height)
                start_right = (x + width * 0.75, y)
                end_right = (x + width * 0.75, y + height)
                
                group.add(dwg.line(start=start_left, end=end_left, stroke=self.belt_color, stroke_width=self.STROKE_WIDTH))
                group.add(dwg.line(start=start_right, end=end_right, stroke=self.belt_color, stroke_width=self.STROKE_WIDTH))
            
            elif direction == self.EAST or direction == self.WEST:  # East or West (horizontal)
                start_top = (x, y + height * 0.25)
                end_top = (x + width, y + height * 0.25)
                start_bottom = (x, y + height * 0.75)
                end_bottom = (x + width, y + height * 0.75)

                group.add(dwg.line(start=start_top, end=end_top, stroke=self.belt_color, stroke_width=self.STROKE_WIDTH))
                group.add(dwg.line(start=start_bottom, end=end_bottom, stroke=self.belt_color, stroke_width=self.STROKE_WIDTH))
        
        return group

    def build_wall(self, dwg, entity):
        x = entity['x'] - entity['width'] / 2
        y = entity['y'] - entity['height'] / 2
        width = entity['width']
        height = entity['height']
        return dwg.rect(insert=(x, y), size=(width, height), fill='none', stroke=self.wall_color, stroke_width=self.STROKE_WIDTH * 2)

    def build_splitter(self, dwg, entity):
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

    def build_asset(self, dwg, entity):
        x = entity['x'] - entity['width'] / 2
        y = entity['y'] - entity['height'] / 2
        width = entity['width']
        height = entity['height']
        
        group = dwg.g()
        group.add(dwg.rect(insert=(x, y), size=(width, height), fill='none', stroke=self.asset_color, stroke_width=self.STROKE_WIDTH * 2))
        
        # Add X in the middle of the rect if asset is larger than 1x1
        if width > 1 and height > 1:
            group.add(dwg.line(start=(x, y), end=(x + width, y + height), stroke=self.asset_color, stroke_width=self.STROKE_WIDTH * 2))
            group.add(dwg.line(start=(x, y + height), end=(x + width, y), stroke=self.asset_color, stroke_width=self.STROKE_WIDTH * 2))
        
        return group
