#!/usr/bin/env python3

import argparse
from .import_json import parseJSON
from .create import create

def main():
    parser = argparse.ArgumentParser(description='Drawscape Factorio CLI toolbelt')
    parser.add_argument('action', choices=['import', 'create'], help='Action to perform')
    parser.add_argument('--json', help='Path to the JSON file for import or create action')
    parser.add_argument('--optimize', action='store_true', help='Optimize the SVG output', default=False)
    parser.add_argument('--template', help='Template to use for create action', default='default')
    parser.add_argument('--output', help='Name of the output file')
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
            }
            if args.optimize:
                create_args['optimize'] = args.optimize
            if args.template != 'default':
                create_args['template'] = args.template
            if args.output:
                create_args['output_file_name'] = args.output
            create(**create_args)
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