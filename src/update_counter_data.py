import json
import os


def update_counter_data():
    # Load the existing counter data to preserve previous updates
    try:
        with open("data/card_counters.json", "r") as f:
            counter_data = json.load(f)
    except FileNotFoundError:
        # If not found, load the template
        try:
            with open("data/card_counters_template.json", "r") as f:
                counter_data = json.load(f)
        except FileNotFoundError:
            print("Counter template file not found. Run generate_counters_template.py first.")
            return

            # Further refined counter relationships
    counter_updates = {
        "Mighty Miner": ["Inferno Tower", "Electro Wizard", "P.E.K.K.A", "Skeleton Army"],
        "Skeleton King": ["Valkyrie", "Baby Dragon", "Fireball", "Wizard"],
        "Archer Queen": ["Lightning", "Rocket", "Fireball", "Electro Giant"],
        "Golden Knight": ["P.E.K.K.A", "Electro Wizard", "Valkyrie", "Skeleton Army"],
        "Monk": ["P.E.K.K.A", "Inferno Tower", "Electro Wizard", "Valkyrie"],
        "Skeleton Dragons": ["Musketeer", "Electro Wizard", "Fireball", "Mega Minion"],
        "Phoenix": ["Electro Wizard", "Musketeer", "Mega Minion", "Fireball"],
        "Little Prince": ["Valkyrie", "Knight", "Mini P.E.K.K.A", "Skeleton Army"],
        "Goblin Demolisher": ["Inferno Tower", "P.E.K.K.A", "Rocket", "Electro Wizard"],
        "Goblin Machine": ["Inferno Tower", "P.E.K.K.A", "Electro Wizard", "Rocket"],
        "Suspicious Bush": ["Fireball", "Arrows", "Baby Dragon", "Valkyrie"],
        "Goblinstein": ["P.E.K.K.A", "Inferno Tower", "Rocket", "Electro Wizard"],
        "Rune Giant": ["Inferno Tower", "P.E.K.K.A", "Inferno Dragon", "Skeleton Army"],
        "Berserker": ["Inferno Tower", "P.E.K.K.A", "Skeleton Army", "Electro Wizard"],
        "Barbarian Hut": ["Earthquake", "Lightning", "Rocket", "Poison"],
        "Elixir Collector": ["Earthquake", "Lightning", "Rocket", "Miner"],
        "Goblin Drill": ["Valkyrie", "Bomber", "Tornado", "Arrows"],
        "Arrows": ["Minion Horde", "Princess", "Goblin Barrel", "Skeleton Army"],
        "Rage": ["Inferno Tower", "Tornado", "Ice Wizard", "Freeze"],
        "Freeze": ["Skeleton Army", "Inferno Tower", "Valkyrie", "Tornado"],
        "Mirror": ["Tornado", "Valkyrie", "Inferno Tower", "Electro Wizard"],
        "The Log": ["Princess", "Dart Goblin", "Goblin Barrel", "Skeleton Army"],
        "Clone": ["Arrows", "Zap", "Tornado", "Baby Dragon"],
        "Heal Spirit": ["Arrows", "The Log", "Zap", "Knight"],
        "Void": ["Valkyrie", "Baby Dragon", "Wizard", "Tornado"],
        "Goblin Curse": ["Valkyrie", "Baby Dragon", "Wizard", "Arrows"]
    }

    # Update the counter data with the new relationships
    for card, counters in counter_updates.items():
        if card in counter_data:
            counter_data[card] = counters
        else:
            print("Warning: Card '" + card + "' not found in the template.")

            # Save the updated counter data
    with open("data/card_counters.json", "w") as f:
        json.dump(counter_data, f, indent=2)

    print("Refined counter data updated with " + str(len(counter_updates)) + " cards.")
    print("Saved to 'data/card_counters.json'")


if __name__ == "__main__":
    update_counter_data()