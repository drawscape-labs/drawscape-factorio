# Pen Plotting a Factorio Base Layout
CLI written in Python to create SVG images from Factorio base data that you can then draw on a pen plotter.

## Demo
In case you are wondering what pen plotting is, checkout this video: 

[Pen Plotting Video Demo](https://www.youtube.com/shorts/DEY43r4u00o)

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


## Themes
Goal being more themes can be implimented that will uniquely render each of the Entity Types. Most likely each theme will be dedicated to a specific pen type and paper size. 

## Usage

```
drawscape-factorio create --json exported-entities.json
```

- `--optimize` will run `vpype` commands to prepare the SVG for efficient pen plotting. This will not work unless you already have `vpype` installed via the command line. https://github.com/abey79/vpype

## Notes
- I've only tested this on a Mac (OSX)
- For some reason the FUE5-Exporter mod isn't exporting roads. 

## TODO
- Implement Rendering for the Rail Systems. 
