import json
import os


def generate_counters_template():
    # Load the card data to extract card names
    try:
        with open("data/clash_royale_cards.json", "r") as f:
            card_data = json.load(f)
            cards = card_data.get("items", [])
    except FileNotFoundError:
        print("Card data file not found. Run card_data.py first.")
        return

        # Create a dictionary with every card's name mapped to an empty list
    counter_template = {}
    for card in cards:
        name = card.get("name")
        if name:
            counter_template[name] = []  # Placeholder for counter cards

    # Save the template to a JSON file
    os.makedirs("data", exist_ok=True)
    with open("data/card_counters_template.json", "w") as f:
        json.dump(counter_template, f, indent=2)

    print("Counter template generated with", len(counter_template), "cards.")
    print("Saved to 'data/card_counters_template.json'")


if __name__ == "__main__":
    generate_counters_template()