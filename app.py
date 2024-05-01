from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Placeholder data for classes and races
classes = ['Warrior', 'Wizard', 'Rogue']
races = ['Human', 'Elf', 'Dwarf']

def generate_stats():
    return {stat: random.randint(1, 18) for stat in ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']}

@app.route('/')
def home():
    return render_template('index.html', classes=classes, races=races)

@app.route('/generate', methods=['POST'])
def generate_character():
    class_selected = request.json['class']
    race_selected = request.json['race']
    stats = generate_stats()
    return jsonify({'class': class_selected, 'race': race_selected, 'stats': stats})

if __name__ == "__main__":
    app.run(debug=True)
