#!/usr/bin/python3
"""Module to convert CSV data to JSON."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and save as data.json.

    Args:
        csv_filename (str): The input CSV filename.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except (FileNotFoundError, IOError, csv.Error):
        return False
