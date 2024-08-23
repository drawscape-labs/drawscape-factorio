#!/usr/bin/env python3

import argparse
from .import_json import parseJSON
from .create import create

def main():
    parser = argparse.ArgumentParser(description='Drawscape Factorio CLI toolbelt')
    parser.add_argument('action', choices=['import', 'create'], help='Action to perform')
    parser.add_argument('--json', help='Path to the JSON file for import or create action')
    args = parser.parse_args()

    try:
        if args.action == 'import':
            if not args.json:
                raise ValueError("--json argument is required for import action")
            parseJSON(args.json)
        elif args.action == 'create':
            if not args.json:
                raise ValueError("--json argument is required for create action")
            create(args.json)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()