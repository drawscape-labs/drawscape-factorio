import numpy as np
import math

class DefaultTheme:
    # Constants for directions
    NORTH = 0
    EAST = 2
    SOUTH = 4
    WEST = 6

    # Constant for stroke width
    STROKE_WIDTH = 0.3  # unsure if this really translates to millimetes, doubtful

    def __init__(self, resolution='HIGH'):
        self.resolution = resolution.upper()
        self.colors = {
            'default': '#0000FF',  # Blue
            'belts': '#008000',    # Green
            'splitters': '#008000', # Green
            'walls': '#FF0000',    # Red
            'asset': '#0000FF',    # Blue
            'spaceship': '#FFD700', # Gold
            'rails': '#808080',    # Gray
            'electrical': '#0000FF' # Blue
        }

    def get_color(self, entity_type):
        return self.colors.get(entity_type, self.colors['default'])

    def render_default(self, dwg, entity):
        if self.resolution == 'LOW':
            return self.render_default_low(dwg, entity)
        else:
            return self.render_default_high(dwg, entity)

    # Low resultion rendering for really large maps
    def render_default_low(self, dwg, entity):

        element = None # default render nothing

        if entity.get('direction') in [self.EAST, self.WEST]:
            top_left_x = entity['x'] - entity['height'] / 2
            top_left_y = entity['y'] - entity['width'] / 2
        else:
            top_left_x = entity['x'] - entity['width'] / 2
            top_left_y = entity['y'] - entity['height'] / 2
        
        if entity['width'] >= 2 or entity['height'] >= 2:
            element = dwg.rect(insert=(top_left_x, top_left_y), size=(entity['width'], entity['height']))

        return element
    
    def render_default_high(self, dwg, entity):

        if entity.get('direction') in [self.EAST, self.WEST]:
            top_left_x = entity['x'] - entity['height'] / 2
            top_left_y = entity['y'] - entity['width'] / 2
        else:
            top_left_x = entity['x'] - entity['width'] / 2
            top_left_y = entity['y'] - entity['height'] / 2
        
        return dwg.rect(insert=(top_left_x, top_left_y), size=(entity['width'], entity['height']))


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


    def render_asset(self, dwg, entity):
        group = self.render_default(dwg, entity)        
        return group
    
    def render_wall(self, dwg, entity):
        group = self.render_default(dwg, entity)        
        return group
    
    def render_spaceship(self, dwg, entity):
        group = self.render_default(dwg, entity)        
        return group

    def render_electrical(self, dwg, entity):
        group = self.render_default(dwg, entity)        
        return group

    def render_splitter(self, dwg, entity):
        direction = entity.get('direction', self.NORTH)
        width = entity['height']
        height = entity['width']
        
        if direction == self.EAST:
            x = entity['x'] - entity['height'] / 2
            y = entity['y'] - entity['width'] / 2
        else:
            x = entity['x'] - entity['width'] / 2
            y = entity['y'] - entity['height'] / 2
        
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