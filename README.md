![image](https://github.com/user-attachments/assets/864cb82c-6635-427b-becb-f5e34a0d75ef)

# Drawing a Factorio Base with a Pen Plotter
CLI written in Python to create SVG images from Factorio base data that you can then draw on a pen plotter.

## Demos
- [Live Demo](https://build.drawscape.io/factorio)
- [Pen Plotting Video](https://www.youtube.com/shorts/DEY43r4u00o)

## Installation

```
pip3 install drawscape-factorio
```

- Requires python 3.8+
- I'm using with python 3.12 in development and production

## CLI Usage

```
drawscape-factorio create --json exported-entities.json
```

Additional Params
```
--theme [default]
--color [main, black, blueprint, matrix, easter]
--debug-grid (helpful for theme development)
```

## Code Usage

Include the modules
```python
from drawscape_factorio import create as createFactorio
from drawscape_factorio import importFUE5
```

You are responsible for parsing the input file and then saving the output as an SVG file. 
```python
# Load the JSON file coming from the FUE5 MOD
with open('/path/to/exported-entities.json, 'r') as file:
    json_data = json.load(file)

# Parse the JSON data
data = importFUE5(json_data)

# Call the create function with the parsed data and settings
result = create(data, {
    'theme_name': 'default',
    'color_scheme': 'main',
    'show_layers': ['assets', 'belts', 'walls', 'rails', 'electrical', 'spaceship']
})

# Save the SVG file
with open(output_file_name, 'w') as f:
    f.write(result['svg_string'])
```

## Exporting Map Data (exported-entities.json)
Currently using a Factorio MOD called `FUE5-Exporter` to export all entites on a map in JSON format. 

https://github.com/FUE5BASE/FUE5-Exporter

1) Install the MOD via the Factorio GUI. Search for `FUE5`
2) Use MOD to "select" area of the map you want to export. Try to "frame" your seletion to only export the area you want to render. 
3) Find the `exported-entities.json` file inside your Factorio Application Data:
  - Mac (`~/Library/Application Support/factorio/script-output`)
  - Windows (`%APPDATA%/Factorio/script-output`)
4) Copy/Paste they JSON file somewhere else so you can work with it. It will get overwritten if you leave it there. 


## Themes
The `drawscape-factorio` CLI supports different themes for rendering the Factorio base. Each theme is a Python class that extends the `ParentTheme` class. The `ParentTheme` class provides the basic structure and functionality for rendering the base, while the child themes (e.g., `DefaultTheme`) define the specific colors and styles for each entity in the base.

A child theme can extend and of the `render_` function to create new shapes and designs.

Theme Requirements:
  - Must define a THEME_NAME, THEME_SLUG, and THEME_VERSION
  - Must define a COLOR_SCHEMES dictionary with a 'main' key

Easiest way to get started it to clone the `default_theme.py` and start making your edits.  


## Examples
<table>
  <tr>
    <td><a href="https://github.com/user-attachments/assets/531cc4e8-3f67-429a-ab2d-f6c93de927ec" target="_blank">
      <img src="https://github.com/user-attachments/assets/531cc4e8-3f67-429a-ab2d-f6c93de927ec" alt="IMG_6588" ></a></td>
    <td><a href="https://github.com/user-attachments/assets/36f47d8d-ff88-45b0-9943-ecaa87a545a5" target="_blank">
      <img src="https://github.com/user-attachments/assets/36f47d8d-ff88-45b0-9943-ecaa87a545a5" alt="IMG_6620" ></a></td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/user-attachments/assets/f2324abc-e2d2-4873-a882-350a80342469" target="_blank">
        <img src="https://github.com/user-attachments/assets/f2324abc-e2d2-4873-a882-350a80342469" alt="IMG_6635" >
       </a></td>
    <td>
      <a href="https://github.com/user-attachments/assets/dc106066-e577-492f-ab55-cf9106614c2b" target="_blank">
        <img src="https://github.com/user-attachments/assets/dc106066-e577-492f-ab55-cf9106614c2b" alt="IMG_6576" >
      </a>
    </td> 
  </tr>
  <tr>
    <td><a href="https://github.com/user-attachments/assets/c6d03728-bf6f-4136-8b73-c5dd40bbfd58" target="_blank">
      <img src="https://github.com/user-attachments/assets/c6d03728-bf6f-4136-8b73-c5dd40bbfd58" alt="IMG_6635" ></a>
    </td>
    <td><a href="https://github.com/user-attachments/assets/7775d327-aca9-47a2-a217-86d0da47bf09" target="_blank">
      <img src="https://github.com/user-attachments/assets/7775d327-aca9-47a2-a217-86d0da47bf09" alt="IMG_6635" ></a>
    </td>    
  </tr>
</table>



### Development
```
conda env update --file environment.yml --prune  
conda activate drawscape_factorio
```

Install for live local dev
```
pip3 install -e .
```


### Distribution Cheat Sheet

PyPi API saved in ~/.pypirc for auto-authentication

```
python setup.py clean --all
rm -rf dist/*
python setup.py sdist bdist_wheel
twine upload dist/*
```
