#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save to file."""
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Load and deserialize data from JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)
