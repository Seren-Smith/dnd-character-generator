import json
import os

def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def lambda_handler(event, context):
    # Load data from JSON files
    races = load_json_data('data/races.json')['races']
    classes = load_json_data('data/classes.json')['classes']

    # Retrieve query parameters
    query_params = event['queryStringParameters']
    race_name = query_params.get('race_name', '').lower()
    class_name = query_params.get('class_name', '').lower()

    # Find requested race and class
    found_race = next((item for item in races if item['name'].lower() == race_name), None)
    found_class = next((item for item in classes if item['name'].lower() == class_name), None)

    # Construct response
    response = {}
    if found_race:
        response['race'] = found_race
    if found_class:
        response['class'] = found_class

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response)
    }

