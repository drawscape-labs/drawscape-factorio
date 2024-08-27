![image](https://github.com/user-attachments/assets/864cb82c-6635-427b-becb-f5e34a0d75ef)


# Drawing a Factorio Base with a Pen Plotter
CLI written in Python to create SVG images from Factorio base data that you can then draw on a pen plotter.

## Demo
In case you are wondering what pen plotting is, checkout this video: [Pen Plotting Video Demo](https://www.youtube.com/shorts/DEY43r4u00o)

## Installation

Clone this repository and then run:

```
pip3 install -e .
```

## Exporting Map Data out of Factorio
Currently using a Factorio MOD called `FUE5-Exporter` to export all entites on a map in JSON format. 

https://github.com/FUE5BASE/FUE5-Exporter

1) Install the MOD via the Factorio GUI. Search for `FUE5`
2) Use MOD to "select" area of the map you want to export. Try to "frame" your seletion to only export the area you want to render. 
3) Find the `exported-entities.json` file inside your Factorio Application Data
  - For OS X Steam install (`~/Library/Application Support/factorio/script-output`)
  - Maybe here as well (`%APPDATA%/Factorio/script-output`)
4) Copy/Paste they JSON file somewhere else so you can work with it. It will get overwritten if you leave it there. 

## Usage

```
drawscape-factorio create --json exported-entities.json
```

- `--optimize` will run `vpype` commands to prepare the SVG for efficient pen plotting. This will not work unless you already have `vpype` installed via the command line. https://github.com/abey79/vpype

## Themes
Goal being more themes can be implimented that will uniquely render each of the Entity Types. Most likely each theme will be dedicated to a specific pen type and paper size. 

## Notes
- I've only tested this on a Mac (OSX)
- For some reason the FUE5-Exporter mod isn't exporting roads. 

## TODO
- Implement Rendering for the Rail Systems. 

## Examples
<table>
  <tr>
    <td><a href="https://github.com/user-attachments/assets/dc106066-e577-492f-ab55-cf9106614c2b" target="_blank"><img src="https://github.com/user-attachments/assets/dc106066-e577-492f-ab55-cf9106614c2b" alt="IMG_6576" ></a></td>
    <td><a href="https://github.com/user-attachments/assets/531cc4e8-3f67-429a-ab2d-f6c93de927ec" target="_blank"><img src="https://github.com/user-attachments/assets/531cc4e8-3f67-429a-ab2d-f6c93de927ec" alt="IMG_6588" ></a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/user-attachments/assets/36f47d8d-ff88-45b0-9943-ecaa87a545a5" target="_blank"><img src="https://github.com/user-attachments/assets/36f47d8d-ff88-45b0-9943-ecaa87a545a5" alt="IMG_6620" ></a></td>
    <td><a href="https://github.com/user-attachments/assets/f2324abc-e2d2-4873-a882-350a80342469" target="_blank"><img src="https://github.com/user-attachments/assets/f2324abc-e2d2-4873-a882-350a80342469" alt="IMG_6635" ></a></td>
  </tr>
</table>
