import json
import random

def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def generate_basic_stats():
    """Generates basic D&D stats."""
    return {
        "Strength": random.randint(3, 18),
        "Dexterity": random.randint(3, 18),
        "Constitution": random.randint(3, 18),
        "Intelligence": random.randint(3, 18),
        "Wisdom": random.randint(3, 18),
        "Charisma": random.randint(3, 18)
    }

def lambda_handler(event, context):
    # Assuming JSON files are loaded correctly
    races = load_json_data('data/races.json')['races']
    classes = load_json_data('data/classes.json')['classes']

    # Parse query parameters
    race_name = event['queryStringParameters'].get('race_name', '').lower()
    class_name = event['queryStringParameters'].get('class_name', '').lower()

    # Find race and class
    found_race = next((r for r in races if r['name'].lower() == race_name), None)
    found_class = next((c for c in classes if c['name'].lower() == class_name), None)

    # Generate stats and apply any race bonuses
    stats = generate_basic_stats()
    if found_race and 'bonuses' in found_race:
        for stat, bonus in found_race['bonuses'].items():
            stats[stat] += bonus

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({
            'race': found_race['name'] if found_race else 'Race not found',
            'class': found_class['name'] if found_class else 'Class not found',
            'stats': stats
        })
    }
