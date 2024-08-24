class CirclesTheme:
    # Constants for directions
    NORTH = 0
    EAST = 2
    SOUTH = 4
    WEST = 6

    # Constant for stroke width
    STROKE_WIDTH = 0.3  # 0.3mm

    def __init__(self):
        self.belt_color = '#FFA500' # Orange
        self.splitter_color = '#FF0000' # Red
        self.wall_color = '#808080' # Grey
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
                start = (x + width / 2, y)
                end = (x + width / 2, y + height)
            
            elif direction == self.EAST or direction == self.WEST:  # East or West (horizontal)
                start = (x, y + height / 2)
                end = (x + width, y + height / 2)

            group.add(dwg.line(start=start, end=end, stroke=self.belt_color, stroke_width=self.STROKE_WIDTH))
        
        return group

    def build_wall(self, dwg, entity):
        x = entity['x']
        y = entity['y']
        diameter = min(entity['width'], entity['height'])
        radius = diameter / 2
        return dwg.circle(center=(x, y), r=radius, fill='none', stroke=self.wall_color, stroke_width=self.STROKE_WIDTH)

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
        x = entity['x']
        y = entity['y']
        width = entity['width']
        height = entity['height']
        
        group = dwg.g()
        
        if width == height:
            # If it's a square, draw a single circle
            radius = width / 2
            group.add(dwg.circle(center=(x, y), r=radius, fill='none', stroke=self.asset_color, stroke_width=self.STROKE_WIDTH))
            # If width and height are greater than or equal to 4, draw another smaller circle inside
            if width >= 3 and height >= 3:
                inner_radius = radius * 0.3  # 60% of the original radius
                group.add(dwg.circle(center=(x, y), r=inner_radius, fill='none', stroke=self.asset_color, stroke_width=self.STROKE_WIDTH))

        else:
            # If it's a rectangle, draw two circles
            radius = min(width, height) / 2
            if width > height:
                # Horizontal rectangle
                center1 = (x - width/4, y)
                center2 = (x + width/4, y)
            else:
                # Vertical rectangle
                center1 = (x, y - height/4)
                center2 = (x, y + height/4)
            
            group.add(dwg.circle(center=center1, r=radius, fill='none', stroke=self.asset_color, stroke_width=self.STROKE_WIDTH))
            group.add(dwg.circle(center=center2, r=radius, fill='none', stroke=self.asset_color, stroke_width=self.STROKE_WIDTH))
        
        return group
