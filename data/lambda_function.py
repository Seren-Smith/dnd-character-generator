import json
import random

def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def generate_basic_stats():
    """Generates basic D&D stats randomly within standard rules."""
    return {
        "Strength": random.randint(1, 18),
        "Dexterity": random.randint(1, 18),
        "Constitution": random.randint(1, 18),
        "Intelligence": random.randint(1, 18),
        "Wisdom": random.randint(1, 18),
        "Charisma": random.randint(1, 18)
    }

def apply_race_bonuses(stats, bonuses):
    """Applies race bonuses to the generated stats."""
    for key, value in bonuses.items():
        stats[key] += value
    return stats

def lambda_handler(event, context):
    # Load data from JSON files
    races = load_json_data('data/races.json')['races']
    classes = load_json_data('data/classes.json')['classes']

    # Retrieve query parameters
    race_name = event['queryStringParameters'].get('race_name', '').lower()
    class_name = event['queryStringParameters'].get('class_name', '').lower()

    # Find requested race and class
    found_race = next((item for item in races if item['name'].lower() == race_name), None)
    found_class = next((item for item in classes if item['name'].lower() == class_name), None)

    # Generate basic stats
    stats = generate_basic_stats()

    # Apply race bonuses to stats
    if found_race:
        stats = apply_race_bonuses(stats, found_race['bonuses'])

    response = {
        'race': found_race['name'] if found_race else "Race not found",
        'class': found_class['name'] if found_class else "Class not found",
        'stats': stats
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response)
    }
