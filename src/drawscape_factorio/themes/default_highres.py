from .parent import ParentTheme

class DefaultHighResTheme(ParentTheme):  # Extend ParentTheme

    # Constants for theme attributes
    THEME_NAME = "Default (High Res)"
    THEME_SLUG = "default_highres"
    THEME_VERSION = "1.0"

    COLOR_SCHEMES = {
        'main': {
            'bg': None,
            'assets': '#000000',  # Black
            'belts': '#000000',  # Black
            'walls': '#000000',  # Black
            'spaceship': '#000000',  # Black
            'rails': '#000000',  # Black
            'electrical': '#000000'  # Black
        },
        'rainbow': {
            'bg': '#FF0000',  # Red
            'assets': '#FFA500',  # Orange
            'belts': '#FFFF00',  # Yellow
            'walls': '#008000',  # Green
            'spaceship': '#0000FF',  # Blue
            'rails': '#4B0082',  # Navy Blue
            'electrical': '#EE82EE'  # Violet
        },
        'black': {
            'bg': '#000000',  # Black
            'assets': '#FFFFFF',  # White
            'belts': '#FFFFFF',  # White
            'walls': '#FFFFFF',  # White
            'spaceship': '#FFFFFF',  # White
            'rails': '#FFFFFF',  # White
            'electrical': '#FFFFFF'  # White
        },
        'matrix': {
            'bg': '#000000',  # Black
            'assets': '#00FF00',  # Lime Green
            'belts': '#00FF20',  # Slightly darker Lime Green
            'walls': '#00FF40',  # Slightly lighter Lime Green
            'spaceship': '#00FF60',  # Lighter Lime Green
            'rails': '#00FF80',  # Lighter Lime Green
            'electrical': '#00FFA0'  # Lightest Lime Green
        },
        'easter': {
            'bg': '#FFFFFF',  # White
            'assets': '#FF69B4',  # Pastel Pink
            'belts': '#FFD700',  # Golden Yellow
            'walls': '#008080',  # Teal
            'spaceship': '#00FF00',  # Lime Green
            'rails': '#FFA07A',  # Light Coral
            'electrical': '#FF00FF'  # Magenta
        },
        'blueprint': {
            'bg': '#007ACC',  # Blue background
            'assets': '#FFFFFF',  # White
            'belts': '#FFFFFF',  # White
            'walls': '#FFFFFF',  # White
            'spaceship': '#FFFFFF',  # White
            'rails': '#FFFFFF',  # White
            'electrical': '#FFFFFF'  # White
        },
        'flat_blue': {
            'bg': '#1E3A4C',  # Dark Blue
            'assets': '#FFA500',  # Orange
            'belts': '#FFA500',  # Orange
            'walls': '#FFA500',  # Orange
            'spaceship': '#FFA500',  # Orange
            'rails': '#FFA500',  # Orange
            'electrical': '#FFA500'  # Orange
        }
    }

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