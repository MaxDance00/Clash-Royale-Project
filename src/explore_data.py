import json
import os


def explore_card_data():
    # Load the card data from the JSON file
    try:
        with open("data/clash_royale_cards.json", "r") as f:
            card_data = json.load(f)
    except FileNotFoundError:
        print("Card data file not found. Run card_data.py first.")
        return

        # Print basic information about the data
    print(f"Data structure type: {type(card_data)}")

    if isinstance(card_data, dict):
        print("\nKeys in the data:")
        for key in card_data.keys():
            print(f"- {key}")

            # Check if 'items' exists in the data (common structure for API responses)
    if isinstance(card_data, dict) and 'items' in card_data:
        items = card_data['items']
        print(f"\nNumber of cards: {len(items)}")

        # Print information about the first card as an example
        if len(items) > 0:
            first_card = items[0]
            print("\nExample card structure:")
            for key, value in first_card.items():
                print(f"- {key}: {type(value)}")

            print("\nFirst card details:")
            print(json.dumps(first_card, indent=2))


if __name__ == "__main__":
    explore_card_data()