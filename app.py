from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

races = ["Halfling", "Gnome", "Faen"]

# Expanded data for classes
base_classes = [
    "Akashic", "Archivist", "Ardent", "Artificer", "Barbarian", "Bard", "Bardic Sage", "Battle Dancer",
    "Battle Sorcerer", "Beguiler", "Binder", "Blade Lord", "Chronoshifter", "Crusader", "Cleric",
    "Divine Mind", "Dragon Shaman", "Dread Necromancer", "Druid", "Duskblade", "Dragonfire Adept",
    "Eagle’s Eye", "Factotum", "Favored Soul", "Fighter", "Greenbond", "Healer", "Hexblade", "Hexblade, Variant",
    "Incarnate", "Jester", "Knight", "Lurk", "Marshal", "Monk", "Mountebank (Base Class)", "Mystic",
    "Naturalist Adept", "Ninja", "Paladin", "Prismatic Shadow", "Psion", "Psychic Warrior", "Ranger",
    "Ranger, Guardian", "Rogue", "Samurai", "Savant", "Scout", "Shadowcaster", "Sha’ir", "Shugenja",
    "Sorcerer", "Soulborn", "Soul Siphon", "Soulknife", "Spellcaster", "Spellthief", "Spirit Shaman",
    "Swashbuckler", "Swordsage", "Totemist", "Treader of Dawn and Twilight", "True Namer", "Unfettered",
    "Warblade", "Warlock", "Warmage", "Warmain", "Wilder", "Wizard", "Wu Jen"
]

prestige_classes = [
    "Abjurant Champion", "Acolyte of Ego", "Acolyte of the Skin", "Alienist", "Anarchic Initiate", "Anima Mage",
    "Animal Lord", "Arcane Archer", "Arcane Heirophant", "Arcane Trickster", "Archmage", "Argent Savant",
    "Ashworm Dragoon", "Assassin", "Avenging Executioner", "Battle Trickster", "Bear Warrior", "Beastmaster",
    "Bereft", "Blackflame Zealot", "Blackguard", "Bladesinger", "Blighter", "Blood Magus", "Bloodclaw Master",
    "Bloodhound", "Bloodstorm Blade", "Bonded Summoner", "Brimstone Speaker", "Cavalier", "Cave Stalker",
    "Cerebremancer", "Chameleon", "Champion of Corellon Larethian", "Child of the Night", "Church Inquisitor",
    "Cloaked Dancer", "Cloud Anchorite", "Combat Trapsmith", "Consecrated Harrier", "Contemplative",
    "Corrupt Avenger", "Cryokineticist", "Daggerspell Mage", "Daggerspell Shaper", "Dark Hunters",
    "Darkwood Stalker", "Death Delver", "Deepstone Sentinel", "Demon Binder", "Dervish", "Diamond Dragon",
    "Dirge Singer", "Disciple of the Eye", "Disciple of Thrym", "Disciple of the World", "Divine Crusader",
    "Divine Oracle", "Dracolexi", "Dragon Descendent", "Dragon Devotee", "Dragon Disciple", "Dragon Lord",
    "Dragon Samurai", "Dragonheart Mage", "Dread Fang of Lolth", "Dread Pirate", "Dread Witch",
    "Drunken Master", "Duelist", "Dungeon Delver", "Dwarven Defender", "Ebon Saint", "Ectopic Adept",
    "Effigy Master", "Eldritch Disciple", "Eldritch Knight", "Eldritch Theurge", "Elemental Savant",
    "Elocater", "Enlightened Fist", "Enlightened Spirit", "Entropomancer", "Ephemeral Exemplar",
    "Eternal Blade", "Evangelist", "Exemplar", "Exotic Weapons Master", "Eye of Gruumsh", "Eye of Lolth",
    "Fatespinner", "Fiend Blooded", "Fiendbinder", "Fist of the Forest", "Fist of Zouken (Psionic Fist)",
    "Fochlucan Lyrist", "Forest Reeve", "Fortune’s Friend", "Frenzied Berserker", "Frost Mage", "Frostrager",
    "Flayerspawn Psychic", "Geomancer", "Geometer", "Ghost-faced Killer", "Gnome Giant-Slayer", "Grayguard",
    "Greenstar Adept", "Halfling Outrider", "Hand of the Winged Masters", "Havoc Mage", "Hierophant",
    "Highland Stalker", "Holt Warden", "Holy Liberator", "Holy Scourge", "Horizon Walker", "Hospitaler",
    "Hulking Hurler", "Hunter of the Dead", "Illumine Soul", "Incandescent Champion", "Incarnum Blade",
    "Initiate of the Sevenfold Veil", "Insidious Corrupter", "Invisible Blade", "Ironsoul Forgemaster",
    "Ithilid Slayer (Slayer)", "Jade Phoenix Mage", "Justicar", "Kensai", "Kinslayer", "Knight of the Chalice",
    "Knight of the Iron Glacier", "Knight of the Pearl", "Knight of the Sacred Seal", "Knight Protector",
    "Legacy Champion", "Legendary Captain", "Leviathan Hunter", "Lord of the Tides", "Loredelver",
    "Loremaster", "Luck Stealer", "Lurking Terror", "Lyric Thaumaturgist", "Maester", "Mage of the Arcane Order",
    "Magical Trickster", "Malconvoker", "Master of Many Forms", "Master of Masks", "Master of Nine",
    "Master of Radiance", "Master of Shadow", "Master of Shrouds", "Master of the Unseen Hand",
    "Master Specialist", "Master Thrower", "Master Transmogrifist", "Master Vampire", "Menacing Brute",
    "Metamind", "Mindbender", "Mindculler", "Mindspy", "Mountebank", "Mystic Theurge", "Mythic Exemplar",
    "Nature’s Warrior", "Necrocarnate", "Nightmare Spinner", "Nightsong Enforcer", "Nightsong Infiltrator",
    "Noctumancer", "Occult Slayer", "Ollam", "Ordained Champion", "Order of the Bow Initiate", "Outcast Champion",
    "Pact-bound Adept", "Pale Master", "Paragnostic Apostle", "Paragnostic Initiate", "Pious Templar",
    "Primeval", "Psibond Agent", "Psion Uncarnate", "Purifier of the Hallowed Doctrine", "Purple Dragon Knight",
    "Pyrokineticist", "Radiant Servant of Pelor", "Rainbow Servant", "Ravager", "Reaping Mauler", "Rimefire Witch",
    "Ronin", "Ruathar", "Ruby Knight Vindicator", "Sacred Exorcist", "Sacred Fist", "Sacred Purifier", "Sanctified One",
    "Sand Shaper", "Sapphire Hierarch", "Scar Enforcer", "Scion of Tem-Et-Nu", "Scarlet Corsair", "Scion of Dantalion",
    "Scorpion Heritor", "Sea Witch", "Seeker of the Misty Isle", "Seeker of the Song", "Shadow of the Hydra",
    "Shadow Sentinel", "Shadow Sun Ninja", "Shadowbane Inquisitor", "Shadowbane Stalker", "Shadowblade",
    "Shadowdancer", "Shadowmind", "Shadowsmith", "Shadowspy", "Shadowstriker", "Shining Blade of Heironeous",
    "Singer of Concordance", "Skullclan Hunter", "Skypledged", "Soulbow", "Soulcaster", "Spellsword",
    "Spellwarp Sniper", "Spinemeld Warrior", "Spymaster", "Squire of Legend", "Stonelord", "Storm Disciple",
    "Stormcaster", "Stormlord", "Stormsinger", "Stormtalon", "Streetfighter", "Sublime Chord", "Suel Arcanamach",
    "Swift Wing", "Tactical Soldier", "Tainted Scholar", "Tattooed Monk", "Tempest", "Temple Raider of Olidammara",
    "Tenebrous Apostate", "Thaumaturgist", "Thayan Knight", "Thief-Acrobat", "Thrallherd", "Toxicant Demagogue",
    "Tomb Warden", "Totem Rager", "True Necromancer", "Ultimate Magus", "Umbral Disciple", "Uncanny Trickster",
    "Unseen Seer", "Ur-Priest", "Urban Soul", "Vigilante", "Virtuoso", "Void Disciple", "Walker in the Waste",
    "War Hulk", "War Mind", "Warchanter", "Warpriest", "Warchief", "Warshaper", "Wavekeeper", "Wayfarer Guide",
    "Whisper Knife", "Wild Mage", "Wild Plains Outrider", "Wild Soul", "Wildrunner", "Winterhaunt of Iborighu",
    "Witch Slayer", "Witchborn Binder", "Wyrm Mage", "Zerth Cenobite"
]

@app.route('/')
def index():
    return render_template('index.html', base_classes=base_classes, prestige_classes=prestige_classes)

@app.route('/generate', methods=['POST'])
def generate_character():
    data = request.json
    base_class = data.get('class', 'None')
    prestige_class = data.get('prestige', 'None')
    multi_class = data.get('multi_class', 'None')
    # Simulating character stats generation
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
        "multi_class": multi_class,
        "stats": stats
    })

if __name__ == '__main__':
    app.run(debug=True)
