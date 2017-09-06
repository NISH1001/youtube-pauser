#!/usr/bin/env python3

import json
import os


def load_config(filename="config.json"):
    filename_abs = os.path.abspath(os.path.expanduser(filename))
    data = {}
    try:
        with open(filename_abs, 'r') as f:
            jsonstr = f.read()
            data = json.loads(jsonstr)
    except FileNotFoundError as ferr:
        data = get_default_config()
    return data

def get_default_config():
    data = {}
    data['desktop_number'] = 0
    data['window_name'] = "YouTube"
    return data

def main():
    data = load_config("config.json")
    print(data)

if __name__ == "__main__":
    main()

