from .parent import ParentTheme

class SquaresTheme(ParentTheme):  # Extend ParentTheme

    # Constants for theme attributes
    THEME_NAME = "Squares (Low Res)"
    THEME_SLUG = "squares"
    THEME_VERSION = "1.0"

    COLOR_SCHEMES = {
        'black': {
            'background': '#ffffff',
            'assets': '#000000',
            'belts': '#000000',
            'walls': '#000000',
            'spaceship': '#000000',
            'rails': '#000000',
            'electrical': '#000000', 
            'pipes': '#000000'
        },
        'algae': {
            'background': '#ffffff',  
            'assets': '#438ab7',
            'belts': '#9db669',
            'walls': '#438ab7',
            'spaceship': '#438ab7',
            'rails': '#000000',
            'electrical': '#438ab7',
            'pipes': '#438ab7'
        },
        'white': {
            'background': '#000000',
            'assets': '#FFFFFF',
            'belts': '#FFFFFF',
            'walls': '#FFFFFF',
            'spaceship': '#FFFFFF',
            'rails': '#FFFFFF',
            'electrical': '#FFFFFF',
            'pipes': '#FFFFFF'
        },
        'matrix': {
            'background': '#000000',
            'assets': '#00FF00',
            'belts': '#00FF20',
            'walls': '#00FF40',
            'spaceship': '#00FF60',
            'rails': '#00FF80',
            'electrical': '#00FFA0',
            'pipes': '#00FFC0'
        },
        'ocean': {
            'background': '#719db0',
            'assets': '#588aa0',
            'belts': '#ffffff',
            'walls': '#6091a7',
            'spaceship': '#6091a7',
            'rails': '#ffffff',
            'electrical': '#6091a7',
            'pipes': '#6091a7'
        },
        'blueprint': {
            'background': '#007ACC',
            'assets': '#DEE9EF',
            'belts': '#FFFFFF',
            'walls': '#FFFFFF',
            'spaceship': '#FFFFFF',
            'rails': '#FFFFFF',
            'electrical': '#FFFFFF',
            'pipes': '#FFFFFF'
        },
        'flat_blue': {
            'background': '#1E3A4C',
            'assets': '#FFA500',
            'belts': '#FFA500',
            'walls': '#FFA500',
            'spaceship': '#FFA500',
            'rails': '#FFA500',
            'electrical': '#FFA500',
            'pipes': '#FFA500'
        },
        'rails': {
            'background': '#000000',  
            'assets': '#FFFFFF',
            'belts': '#FFFFFF', 
            'walls': '#FFFFFF',
            'spaceship': '#FFFFFF',
            'rails': '#00FFFF',
            'electrical': '#FFFFFF',
            'pipes': '#FFFFFF'
        },
        'belts': {
            'background': '#000000',  
            'assets': '#FFFFFF',
            'belts': '#00FFFF', 
            'walls': '#FFFFFF',
            'spaceship': '#FFFFFF',
            'rails': '#FFFFFF',
            'electrical': '#FFFFFF',
            'pipes': '#FFFFFF'
        },
        'terracotta': {
            'background': '#B85042',  
            'assets': '#A7BEAE',
            'belts': '#E7E8D1', 
            'walls': '#A7BEAE',
            'spaceship': '#A7BEAE',
            'rails': '#E7E8D1',
            'electrical': '#A7BEAE',
            'pipes': '#A7BEAE'
        },
        'circuit': {
            'background': '#2E8B57',
            'assets': '#C0C0C0',
            'belts': '#B87333', 
            'walls': '#C0C0C0',
            'spaceship': '#C0C0C0',
            'rails': '#000000',
            'electrical': '#C0C0C0',
            'pipes': '#C0C0C0'
        },
        'asphalt': {
            'background': '#2c404b',
            'assets': '#8b969c',
            'belts': '#8b969c',
            'walls': '#8b969c',
            'spaceship': '#FFFFFF',
            'rails': '#fbfcfc',
            'electrical': '#8b969c',
            'pipes': '#8b969c'
        },
        'sky': {
            'background': '#D1DAE4',
            'assets': '#6C849C',
            'belts': '#8898A9',
            'walls': '#6C849C',
            'spaceship': '#6C849C',
            'rails': '#6C849C',
            'electrical': '#6C849C',
            'pipes': '#6C849C'
        },
        'earth': {
            'background': '#FDF5EC',
            'assets': '#DBDEC9',
            'belts': '#C2836A',
            'walls': '#ECDCC3',
            'spaceship': '#ECDCC3',
            'rails': '#C2836A',
            'electrical': '#ECDCC3',
            'pipes': '#ECDCC3'
        },
        'grey_scale': {
            'background': '#ffffff',
            'assets': '#dddddd',
            'belts': '#050505',
            'walls': '#dddddd',
            'spaceship': '#dddddd',
            'rails': '#050505',
            'electrical': '#dddddd',
            'pipes': '#dddddd'
        }
    }