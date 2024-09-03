from .parent import ParentTheme

class SquaresTheme(ParentTheme):  # Extend ParentTheme

    # Constants for theme attributes
    THEME_NAME = "Squares (Low Res)"
    THEME_SLUG = "squares"
    THEME_VERSION = "1.0"

    COLOR_SCHEMES = {
        'black': {
            'bg': None,
            'assets': '#000000',  # Black
            'belts': '#000000',  # Black
            'walls': '#000000',  # Black
            'spaceship': '#000000',  # Black
            'rails': '#000000',  # Black
            'electrical': '#000000'  # Black
        },
        'algae': {
            'bg': None,  
            'assets': '#438ab7',  # Blue
            'belts': '#9db669',  # Green
            'walls': '#438ab7',  # Blue
            'spaceship': '#438ab7',  # Blue
            'rails': '#000000',  # Black
            'electrical': '#438ab7'  # Blue
        },
        'white': {
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
        },
        'rails': {
            'bg': '#000000',  
            'assets': '#FFFFFF',
            'belts': '#FFFFFF', 
            'walls': '#FFFFFF',
            'spaceship': '#FFFFFF',
            'rails': '#00FFFF',
            'electrical': '#FFFFFF'
        },
        'belts': {
            'bg': '#000000',  
            'assets': '#FFFFFF',
            'belts': '#00FFFF', 
            'walls': '#FFFFFF',
            'spaceship': '#FFFFFF',
            'rails': '#FFFFFF',
            'electrical': '#FFFFFF'
        },
        'terracotta': {
            'bg': '#B85042',  
            'assets': '#A7BEAE',
            'belts': '#E7E8D1', 
            'walls': '#A7BEAE',
            'spaceship': '#A7BEAE',
            'rails': '#E7E8D1',
            'electrical': '#A7BEAE'
        },
        'circuit': {
            'bg': '#2E8B57',  # Sea Green (darker than Medium Sea Green)
            'assets': '#C0C0C0',
            'belts': '#B87333', 
            'walls': '#C0C0C0',
            'spaceship': '#C0C0C0',
            'rails': '#000000',
            'electrical': '#C0C0C0'
        }

    }