from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load class data from a JSON file
def load_classes():
    with open('data/classes.json', 'r') as file:
        class_data = json.load(file)
    base_classes = [cls for cls in class_data['classes'] if cls['type'] == 'base']
    prestige_classes = [cls for cls in class_data['classes'] if cls['type'] == 'prestige']
    return base_classes, prestige_classes

# Home page route
@app.route('/')
def index():
    base_classes, prestige_classes = load_classes()
    return render_template('index.html', base_classes=base_classes, prestige_classes=prestige_classes)

# Character generation route
@app.route('/generate', methods=['POST'])
def generate_character():
    data = request.json
    base_class = data.get('class', 'None selected')
    prestige_class = data.get('prestige', 'None selected')
    stats = {
        "Strength": random.randint(3, 18),
        "Dexterity": random.randint(3, 18),
        "Constitution": random.randint(3, 18),
        "Intelligence": random.randint(3, 18),
        "Wisdom": random.randint(3, 18),
        "Charisma": random.randint(3, 18)
    }
    return jsonify({
        "base_class": base_class,
        "prestige_class": prestige_class,
        "stats": stats
    })

if __name__ == '__main__':
    app.run(debug=True)
