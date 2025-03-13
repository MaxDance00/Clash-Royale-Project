import json
import os


def merge_elixir_costs():
    # Update the paths to point to the correct location
    counter_file_path = r'C:\Users\maxda\PycharmProjects\pythonProject6\src\data\card_counters.json'

    # Assuming the API data is also in the same directory
    api_file_path = r'C:\Users\maxda\PycharmProjects\pythonProject6\src\data\clash_royale_cards.json'

    print("Current working directory:", os.getcwd())
    print("Using counter card file at:", counter_file_path)
    print("Using API data file at:", api_file_path)

    # Load your current counter cards data
    try:
        with open(counter_file_path, 'r') as f:
            card_counters = json.load(f)
    except FileNotFoundError:
        print("Error: counter file not found at " + counter_file_path)
        return

        # Load the Clash Royale API data
    try:
        with open(api_file_path, 'r') as f:
            api_data = json.load(f)
        print("Successfully loaded API data")
    except FileNotFoundError:
        print("Error: API data file not found at " + api_file_path)
        return

        # Build a mapping of card names to elixir costs from the API data
    elixir_map = {}
    for card in api_data.get('items', []):
        name = card.get('name')
        elixir = card.get('elixirCost')  # The API uses "elixirCost"
        if name and elixir is not None:
            elixir_map[name] = elixir
    print("Found " + str(len(elixir_map)) + " cards with elixir costs in API data")

    # Merge the elixir cost into the counter card data
    updated_counters = {}
    missing_cards = []

    for card_name, counters in card_counters.items():
        # Check if the card exists in the API data
        if card_name in elixir_map:
            # If the current value is already a dict with counters, update it
            if isinstance(counters, dict) and 'counters' in counters:
                counters['elixir'] = elixir_map[card_name]
                updated_counters[card_name] = counters
                # If it's just a list of counters, create a new dict structure
            else:
                updated_counters[card_name] = {
                    'counters': counters,
                    'elixir': elixir_map[card_name]
                }
        else:
            missing_cards.append(card_name)
            # Keep the card but mark it as missing an elixir cost
            if isinstance(counters, dict) and 'counters' in counters:
                counters['elixir_missing'] = True
                updated_counters[card_name] = counters
            else:
                updated_counters[card_name] = {
                    'counters': counters,
                    'elixir_missing': True
                }

    if missing_cards:
        print("Warning: " + str(len(missing_cards)) + " cards not found in API data:")
        for card in missing_cards:
            print("  - " + card)

            # Save the updated card counters data to the same directory
    output_file = r'C:\Users\maxda\PycharmProjects\pythonProject6\src\data\card_counters_with_elixir.json'
    with open(output_file, 'w') as f:
        json.dump(updated_counters, f, indent=4)

    print("Updated data saved to " + output_file)


if __name__ == "__main__":
    merge_elixir_costs()