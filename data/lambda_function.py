import json

def load_json_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def lambda_handler(event, context):
    # Load data from JSON files
    races = load_json_data('data/races.json')['races']
    classes = load_json_data('data/classes.json')['classes']

    # Construct a list of race names and class names
    race_names = [race['name'] for race in races]
    class_names = [cls['name'] for cls in classes]

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'races': race_names, 'classes': class_names})
    }
