import json
import os

# Update the file paths if necessary:
input_file = r'C:\Users\maxda\PycharmProjects\pythonProject6\src\data\card_counters_with_elixir.json'
output_file = r'C:\Users\maxda\PycharmProjects\pythonProject6\src\data\card_counters_trade_evaluation.json'


def evaluate_elixir_trades():
    # Load the existing JSON data
    try:
        with open(input_file, 'r') as f:
            card_data = json.load(f)
        print('Successfully loaded card data with elixir costs from:', input_file)
    except FileNotFoundError:
        print('Error: file not found at ' + input_file)
        return

        # Evaluate elixir trade advantages for each card.
    # For each counter in the enemy card's counter list, the trade advantage is computed as:
    # enemy card's elixir cost - counter card's elixir cost.
    for card_name, details in card_data.items():
        enemy_elixir = details.get('elixir')
        if enemy_elixir is None:
            details['trade_advantages'] = 'elixir cost missing for enemy card'
            continue

        trade_dict = {}
        counters_list = details.get('counters', [])
        for counter in counters_list:
            counter_details = card_data.get(counter)
            if counter_details and isinstance(counter_details, dict):
                counter_elixir = counter_details.get('elixir')
                if counter_elixir is not None:
                    trade_advantage = enemy_elixir - counter_elixir
                    trade_dict[counter] = trade_advantage
                else:
                    trade_dict[counter] = 'counter elixir missing'
            else:
                trade_dict[counter] = 'counter not found'
        details['trade_advantages'] = trade_dict

        # Save the updated JSON data into a new file
    with open(output_file, 'w') as f:
        json.dump(card_data, f, indent=4)

    print('Trade evaluation completed. Updated data saved to ' + output_file)


if __name__ == '__main__':
    evaluate_elixir_trades()

print('Elixir Trade Evaluation Script Ready.')