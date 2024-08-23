# Factorio CLI
Python CLI library to create Pen Plotter SVG files from Factorio data

## Installation

To install Drawscape Fractorio CLI, clone this repository and run:

```
pip3 install -e .
```

## Exporting Map Data
Currently using a Factorio MOD to export the JSON data of all entites on the map. 

https://github.com/FUE5BASE/FUE5-Exporter

1) Install the MOD via the Factorio GUI. Search for `FUE5`
2) Use MOD to "select" area of the map you want to export.
3) Find the `exported-entities.json` file inside your Factorio Application Data
  - For OS X Steam install (`~/Library/Application Support/factorio/script-output`)
  - Maybe here as well (`%APPDATA%/Factorio/script-output`)
4) Copy/Paste they JSON file somewhere else so you can work with it. It will get overwritten if you leave it there. 


## Usage

```
drawscape-factorio create --json exported-entities.json --optimize
```

- `--optimize` will run vpype commands to prepare for efficient pen plotting

## Notes
- I've only tested this on a Mac (OSX)

