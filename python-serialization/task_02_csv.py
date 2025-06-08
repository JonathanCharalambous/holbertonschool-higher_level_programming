#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_file):
    try:    
        data = []
        with open(csv_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception as e:
        print("Unable to convert CSV to JSON: {}".format(e))
        return False
