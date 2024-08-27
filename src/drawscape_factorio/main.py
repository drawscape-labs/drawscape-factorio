#!/usr/bin/env python3

import argparse
import os
from .import_json import parseJSON
from .create import create
from .split import split_svg  # Add this import

def main():
    parser = argparse.ArgumentParser(description='Drawscape Factorio CLI toolbelt')
    parser.add_argument('action', choices=['import', 'create', 'split'], help='Action to perform')  # Add 'split' to choices
    parser.add_argument('--json', help='Path to the JSON file for import or create action')
    parser.add_argument('--svg', help='Path to the SVG file for split action')  # Add this argument
    parser.add_argument('--optimize', action='store_true', help='Optimize the SVG output', default=False)
    parser.add_argument('--template', help='Template to use for create action', default='default')
    parser.add_argument('--output', help='Name of the output file (for create action)')
    parser.add_argument('--landscape', action='store_true', help='Render the SVG in landscape mode', default=False)
    parser.add_argument('--size', help='Paper size for SVG (e.g., A4, A3). Default is optimized for screen.', default=None)
    args = parser.parse_args()

    try:
        if args.action == 'import':
            if not args.json:
                raise ValueError("--json argument is required for import action")
            parseJSON(args.json)
        elif args.action == 'create':
            if not args.json:
                raise ValueError("--json argument is required for create action")
            create_args = {
                'json_file_path': args.json,
                'optimize': args.optimize,
                'template': args.template,
                'landscape': args.landscape,
                'size': args.size
            }
            if args.output:
                create_args['output_file_name'] = args.output
            create(**create_args)
        elif args.action == 'split':  # Add this new elif block
            if not args.svg:
                raise ValueError("--svg argument is required for split action")
            split_svg(args.svg)
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
        print("This error might be due to a mismatch in function arguments.")
        print("Please check if the 'create' function in create.py accepts the provided arguments.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()