import importlib
import os
import inspect

from .themes.parent import ParentTheme

# Utility function to access themes in the /themes directory
# 1) List all Themes
# 2) Get theme details
# 3) Load a specific theme

def listThemes():
    themes = []
    themes_dir = os.path.join(os.path.dirname(__file__), 'themes')
    
    for filename in os.listdir(themes_dir):
        if filename.endswith('.py') and filename != 'parent.py' and filename != '__init__.py':
            module_name = f'drawscape_factorio.themes.{filename[:-3]}'
            module = importlib.import_module(module_name)
            
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, ParentTheme) and obj != ParentTheme and obj.__module__ == module_name:
                    # Initialize the theme with empty data and empty settings
                    theme = obj({})
                    themes.append({
                        'name': theme.THEME_NAME,
                        'slug': theme.THEME_SLUG,
                        'version': theme.THEME_VERSION,
                        'colors': theme.COLOR_SCHEMES,
                        'file_name': filename  # Add the theme file name
                    })
    return themes




def loadTheme(slug):
    """
    Load a theme by its slug.
    Allows us to just keep adding themes to the directory and not worry about updating the code.
    """
    themes_dir = os.path.join(os.path.dirname(__file__), 'themes')
    
    for filename in os.listdir(themes_dir):
        if filename.endswith('.py') and filename != 'parent.py' and filename != '__init__.py':
            module_name = f'drawscape_factorio.themes.{filename[:-3]}'
            module = importlib.import_module(module_name)
            
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, ParentTheme) and obj != ParentTheme and obj.__module__ == module_name:
                    if obj.THEME_SLUG == slug:
                        return obj
    
    raise ValueError(f"Theme with slug '{slug}' not found.")