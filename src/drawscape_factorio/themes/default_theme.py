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
        self.default_color = '#0000FF' # Blue
        self.belt_color = '#008000' # Green
        self.splitter_color = '#008000' # Green
        self.wall_color = '#FF0000' # Red
        self.asset_color = '#0000FF'  # Blue
        self.spaceship_color = '#FFD700' # Gold
        self.rail_color = '#808080'  # Gray

    def render_default(self, dwg, entity, color=None):

        if color is None: 
            color = self.default_color

        if self.resolution == 'LOW':
            return self.render_default_low(dwg, entity, color)
        else:
            return self.render_default_high(dwg, entity, color)

    # Low resultion rendering for really large maps
    def render_default_low(self, dwg, entity, color=None):

        if entity.get('direction') in [self.EAST, self.WEST]:
            # Rotate 90 degrees for east or west direction
            top_left_x = entity['x'] - entity['height'] / 2
            top_left_y = entity['y'] - entity['width'] / 2
            width = entity['height']
            height = entity['width']
        else:
            # Default orientation for north, south, or no direction
            top_left_x = entity['x'] - entity['width'] / 2
            top_left_y = entity['y'] - entity['height'] / 2
            width = entity['width']
            height = entity['height']

        group = dwg.g()
        
        # draw containing rectangle
        if width >= 2 or height >= 2:
            stroke_offset = self.STROKE_WIDTH / 2
            group.add(dwg.rect(
                insert=(top_left_x + stroke_offset, top_left_y + stroke_offset),
                size=(width - self.STROKE_WIDTH, height - self.STROKE_WIDTH),
                fill='none',
                stroke=color,
                stroke_width=self.STROKE_WIDTH
            ))

        # if height > 4 or width > 4:
        #     center_x = entity['x']
        #     center_y = entity['y']
            
        #     # Draw an X in the middle
        #     half_width = width * 0.25  # Increased from 0.15 to make X larger
        #     half_height = height * 0.25  # Increased from 0.15 to make X larger
        #     group.add(dwg.line(start=(center_x - half_width, center_y - half_height),
        #                        end=(center_x + half_width, center_y + half_height),
        #                        stroke=color,
        #                        stroke_width=self.STROKE_WIDTH))
        #     group.add(dwg.line(start=(center_x - half_width, center_y + half_height),
        #                        end=(center_x + half_width, center_y - half_height),
        #                        stroke=color,
        #                        stroke_width=self.STROKE_WIDTH))
            
        return group
    
    def render_default_high(self, dwg, entity, color=None):
        if color is None: 
            color = self.default_color

        top_left_x = entity['x'] - entity['width'] / 2
        top_left_y = entity['y'] - entity['height'] / 2
        width = entity['width']
        height = entity['height']

        group = dwg.g()
        
        stroke_offset = self.STROKE_WIDTH / 2
        group.add(dwg.rect(
            insert=(top_left_x + stroke_offset, top_left_y + stroke_offset),
            size=(width - self.STROKE_WIDTH, height - self.STROKE_WIDTH),
            fill='none',
            stroke=color,
            stroke_width=self.STROKE_WIDTH
        ))
        
        if height > 2 or width > 2:
            center_x = entity['x']
            center_y = entity['y']
            half_width = width / 2 - self.STROKE_WIDTH / 2
            half_height = height / 2 - self.STROKE_WIDTH / 2
            
            group.add(dwg.line(start=(center_x - half_width, center_y - half_height), 
                               end=(center_x + half_width, center_y + half_height), 
                               stroke=color, stroke_width=self.STROKE_WIDTH))
            group.add(dwg.line(start=(center_x - half_width, center_y + half_height), 
                               end=(center_x + half_width, center_y - half_height), 
                               stroke=color, stroke_width=self.STROKE_WIDTH))
        
        return group


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
            
            line = dwg.line(start=start, end=end, stroke=self.rail_color, stroke_width=self.STROKE_WIDTH)
            
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
            
            line = dwg.line(start=start, end=end, stroke=self.rail_color, stroke_width=self.STROKE_WIDTH)
            
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
            short_line = dwg.line(start=(x, y), end=(short_x, short_y),
                                stroke=self.rail_color, stroke_width=self.STROKE_WIDTH)
            group.add(short_line)

            # Draw the long line
            long_line = dwg.line(start=(x, y), end=(long_x, long_y),
                                stroke=self.rail_color, stroke_width=self.STROKE_WIDTH)
            group.add(long_line)

        return group


    def render_asset(self, dwg, entity):
        group = self.render_default(dwg, entity, color=self.asset_color)        
        return group
    
    def render_wall(self, dwg, entity):
        group = self.render_default(dwg, entity, color=self.wall_color)        
        return group
    
    def render_spaceship(self, dwg, entity):
        group = self.render_default(dwg, entity, color=self.spaceship_color)        
        return group

    def render_electrical(self, dwg, entity):
        group = self.render_default(dwg, entity, color=self.asset_color)        
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
                
        return group

    def render_belt(self, dwg, entity):
        
        x = entity['x'] - entity['width'] / 2
        y = entity['y'] - entity['height'] / 2
        width = entity['width']
        height = entity['height']
        direction = entity['direction']
        center = (x + width / 2, y + height / 2)
        
        group = dwg.g()
        
        
        if entity.get('variant') == 'I':
            if direction in [self.NORTH, self.SOUTH]:  # Vertical
                start = (x + width * 0.5, y)
                end = (x + width * 0.5, y + height)
            elif direction in [self.EAST, self.WEST]:  # Horizontal
                start = (x, y + height * 0.5)
                end = (x + width, y + height * 0.5)
            else:
                return group  # Return empty group for invalid direction
            
            group.add(dwg.line(start=start, end=end, stroke=self.belt_color, stroke_width=self.STROKE_WIDTH))
        
        if entity.get('variant') in ['L', 'R']:
            
            belt_group = dwg.g()
            
            # Create the L-shaped belt
            start_v = (x + width * 0.5, y)
            end_v = (x + width * 0.5, y + height * 0.5)
            
            start_h = (x + width * 0.5, y + height * 0.5)
            end_h = (x + width, y + height * 0.5)
            
            # Create a group for the L-shaped belt
            belt_group.add(dwg.line(start=start_v, end=end_v, stroke=self.belt_color, stroke_width=self.STROKE_WIDTH))
            belt_group.add(dwg.line(start=start_h, end=end_h, stroke=self.belt_color, stroke_width=self.STROKE_WIDTH))

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

            group.add(belt_group)                
            
        return group