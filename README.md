# Pen Plotting a Factorio Bases Design
CLI written in Python to create SVG images from Factorio base data that you can then draw on a pen plotter.

## Installation

Clone this repository and then run:

```
pip3 install -e .
```

## Exporting Map Data out of Factorio
Currently using a Factorio MOD called `FUE5-Exporter` to export all entites on a map in JSON format. 

https://github.com/FUE5BASE/FUE5-Exporter

1) Install the MOD via the Factorio GUI. Search for `FUE5`
2) Use MOD to "select" area of the map you want to export.
3) Find the `exported-entities.json` file inside your Factorio Application Data
  - For OS X Steam install (`~/Library/Application Support/factorio/script-output`)
  - Maybe here as well (`%APPDATA%/Factorio/script-output`)
4) Copy/Paste they JSON file somewhere else so you can work with it. It will get overwritten if you leave it there. 


## Themes
Goal is that more themes can be implimented that will unique render each of the Entity Types. Most likely each theme will be dedicated to a specific pen type and paper size. 

## Usage

```
drawscape-factorio create --json exported-entities.json
```

- `--optimize` will run `vpype` commands to prepare the SVG for efficient pen plotting

## Notes
- I've only tested this on a Mac (OSX)
- For some reason the FUE5-Exporter mod isn't exporting roads. 

## TODO
- Implement Rendering for the Rail Systems. 