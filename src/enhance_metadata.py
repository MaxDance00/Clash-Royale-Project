import csv
import os

# File paths
input_csv_file = r'C:\Users\maxda\PycharmProjects\pythonProject6\src\data\card_metadata.csv'
output_csv_file = r'C:\Users\maxda\PycharmProjects\pythonProject6\src\data\card_metadata_enhanced.csv'

# Define card type lists
BUILDINGS = [
    "Cannon", "Tesla", "Inferno Tower", "Bomb Tower", "Goblin Cage",
    "Tombstone", "Furnace", "Goblin Hut", "Barbarian Hut", "Elixir Collector",
    "X-Bow", "Mortar"
]

SPELLS = [
    "Fireball", "Zap", "The Log", "Arrows", "Poison", "Lightning",
    "Rocket", "Tornado", "Snowball", "Earthquake", "Barbarian Barrel",
    "Giant Snowball", "Rage", "Freeze", "Clone", "Mirror", "Heal Spirit",
    "Fire Spirit", "Ice Spirit", "Electro Spirit", "Void"
]


def enhance_metadata():
    # Read existing metadata
    cards = []
    with open(input_csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cards.append(row)

    print(f"Read {len(cards)} cards from existing metadata file")

    # Define new fields to add
    new_fields = [
        "Rarity",
        "Speed",
        "Hit Speed",
        "Deploy Time",
        "Range Classification",
        "Archetype Affinity",
        "Defensive Value",
        "Offensive Value",
        "Crowd Control",
        "Splash Radius",
        "Spawner",
        "Troop Count",
        "Lifetime",
        "Counter Type",
        "Meta Relevance",
        "Skill Floor",
        "Synergy Tags",
        "Vulnerability Tags"
    ]

    # Add new fields to each card
    for card in cards:
        for field in new_fields:
            card[field] = ""  # Initialize with empty string

        # Pre-fill some values based on existing data
        # Example: Set Spawner based on card name
        if any(spawner in card['Card Name'] for spawner in ['Hut', 'Furnace', 'Tombstone']):
            card['Spawner'] = "Yes"
        else:
            card['Spawner'] = "No"

            # Example: Set Troop Count based on card name
        if any(multi in card['Card Name'] for multi in ['Army', 'Gang', 'Horde']):
            card['Troop Count'] = "Horde"
        elif "Minions" == card['Card Name']:
            card['Troop Count'] = "Trio"
        elif any(pair in card['Card Name'] for pair in ['Archers', 'Rascals']):
            card['Troop Count'] = "Pair"
        elif any(building in card['Card Name'] for building in BUILDINGS):
            card['Troop Count'] = "Building"
        elif any(spell in card['Card Name'] for spell in SPELLS):
            card['Troop Count'] = "Spell"
        else:
            card['Troop Count'] = "Single"

            # Write enhanced metadata to new CSV
    fieldnames = list(cards[0].keys())
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for card in cards:
            writer.writerow(card)

    print(f"Enhanced metadata saved to: {output_csv_file}")
    print("Please review and fill in the new fields manually for accuracy.")


if __name__ == "__main__":
    enhance_metadata()