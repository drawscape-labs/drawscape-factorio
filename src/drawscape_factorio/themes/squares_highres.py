from .squares import SquaresTheme

class SquaresHighResTheme(SquaresTheme):

    # Constants for theme attributes
    THEME_NAME = "Squares (High Res)"
    THEME_SLUG = "squares_highres"
    THEME_VERSION = "1.0"

    def render_asset(self, dwg, entity):
        """
        Default rendering for all square assets
        Handles rotation based on direction.
        """

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