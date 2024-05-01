import json
import random

def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def generate_basic_stats():
    return {
        "Strength": random.randint(3, 18),
        "Dexterity": random.randint(3, 18),
        "Constitution": random.randint(3, 18),
        "Intelligence": random.randint(3, 18),
        "Wisdom": random.randint(3, 18),
        "Charisma": random.randint(3, 18)
    }

def lambda_handler(event, context):
    if event['path'] == "/dropdowns":
        data = load_json_data()
        return {
            'statusCode': 200,
            'body': json.dumps({'races': data['races'], 'classes': data['classes']})
        }
    elif event['path'] == "/stats":
        stats = generate_basic_stats()
        race_name = event['queryStringParameters']['race_name']
        class_name = event['queryStringParameters']['class_name']
        # Simulating race and class retrieval, normally you'd apply bonuses here
        return {
            'statusCode': 200,
            'body': json.dumps({'race': race_name, 'class': class_name, 'stats': stats})
        }

    return {'statusCode': 400, 'body': 'No valid path provided'}
