#!/usr/bin/env python3

import argparse
import json
from .parse import parseFUE5
from .create import create

if __name__ == "__main__":
    main()

def main():
    parser = argparse.ArgumentParser(description='Drawscape Factorio CLI toolbelt')
    parser.add_argument('action', choices=['import', 'create'], help='Action to perform')
    parser.add_argument('--json', help='Path to the JSON file for import or create action')
    parser.add_argument('--optimize', action='store_true', help='Optimize the SVG output', default=False)
    parser.add_argument('--template', help='Template to use for create action', default='default')
    parser.add_argument('--output', help='Name of the output file (for create action)')
    parser.add_argument('--add-grid', action='store_true', help='Add a grid to the SVG (for debugging)', default=False)
    args = parser.parse_args()

    try:
        if args.action == 'import':
            if not args.json:
                raise ValueError("--json argument is required for import action")
            with open(args.json, 'r') as file:
                json_data = json.load(file)
            parsed_data = parseJSON(json_data)
            print(f"Parsed data: {json.dumps(parsed_data, indent=2)}")
        elif args.action == 'create':
            if not args.json:
                raise ValueError("--json argument is required for create action")
            create_args = {
                'json_file_path': args.json,
                'optimize': args.optimize,
                'template': args.template,
                'add_grid': args.add_grid
            }
            if args.output:
                create_args['output_file_name'] = args.output
            createWrapper(**create_args)
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
        print("This error might be due to a mismatch in function arguments.")
        print("Please check if the 'createWrapper' function accepts the provided arguments.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Function to handle the creation of SVG from JSON data
# Parameters:
#   json_file_path (str): Path to the input JSON file
#   optimize (bool): Flag to optimize the SVG output (currently disabled)
#   template (str): Template to use for creating the SVG (default: 'default')
#   output_file_name (str): Name of the output SVG file (default: 'output.svg')
#   add_grid (bool): Flag to add a grid to the SVG for debugging (default: False)
# Returns:
#   dict: Result containing SVG string and metadata

def createWrapper(json_file_path, optimize=False, template='default', output_file_name='output.svg', add_grid=False):
    # Load the JSON file
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
    
    # Parse the JSON data
    data = parseFUE5(json_data)
    
    # Call the create function with the parsed data
    result = create(data, template, add_grid)
    
    # Save the SVG file
    with open(output_file_name, 'w') as f:
        f.write(result['svg_string'])
    
    # Print information about the SVG drawing
    print(f"Created SVG drawing:")
    print(f"  Output file: {output_file_name}")
    print(f"  Size: 100% x 100% (optimized for screen)")
    print(f"  ViewBox: {result['viewbox']['x']} {result['viewbox']['y']} {result['viewbox']['width']} {result['viewbox']['height']}")
    print(f"  Template: {result['template']}")
    print(f"  Theme resolution: {result['theme_resolution']}")
    print(f"  Grid added: {'Yes' if add_grid else 'No'}")
    
    # Print bounding box information
    bounds = result['bounds']
    print(f"  Bounding Box:")
    print(f"    Min X: {bounds['min_x']:.2f}")
    print(f"    Max X: {bounds['max_x']:.2f}")
    print(f"    Min Y: {bounds['min_y']:.2f}")
    print(f"    Max Y: {bounds['max_y']:.2f}")
    print(f"    Width: {bounds['max_x'] - bounds['min_x']:.2f}")
    print(f"    Height: {bounds['max_y'] - bounds['min_y']:.2f}")

    print(f"SVG file saved as {output_file_name}")
    if optimize:
        print("Optimization is currently disabled.")

    return result
