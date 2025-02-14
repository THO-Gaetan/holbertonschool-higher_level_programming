#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        # Open the CSV file and read its contents
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        # Serialize the data to JSON and write to data.json
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
