import json
import os
from collections import Counter


class CounterDeckBuilder:
    def __init__(self, counter_data_path="data/card_counters.json"):
        # Load the counter data
        try:
            with open(counter_data_path, "r") as f:
                self.counter_data = json.load(f)
        except FileNotFoundError:
            print(f"Counter data file not found at {counter_data_path}")
            self.counter_data = {}

            # Load the card data for additional information
        try:
            with open("data/clash_royale_cards.json", "r") as f:
                card_data = json.load(f)
                self.cards = {card["name"]: card for card in card_data.get("items", [])}
        except FileNotFoundError:
            print("Card data file not found.")
            self.cards = {}

    def get_counters(self, card_name):
        """Get the list of counters for a specific card."""
        return self.counter_data.get(card_name, [])

    def build_counter_deck(self, opponent_deck, max_deck_size=8):
        """
        Build a counter deck based on the opponent's deck.

        Args:
            opponent_deck (list): List of card names in the opponent's deck
            max_deck_size (int): Maximum number of cards in a deck (default: 8)

        Returns:
            list: Suggested counter deck
        """
        # Validate input
        if not isinstance(opponent_deck, list) or len(opponent_deck) == 0:
            return {"error": "Opponent deck must be a non-empty list of card names"}

            # Check if all cards in the opponent's deck exist in our data
        unknown_cards = [card for card in opponent_deck if card not in self.counter_data]
        if unknown_cards:
            print(f"Warning: The following cards are not in our database: {', '.join(unknown_cards)}")

            # Get all possible counters for the opponent's deck
        all_counters = []
        for card in opponent_deck:
            counters = self.get_counters(card)
            all_counters.extend(counters)

            # Count the frequency of each counter
        counter_freq = Counter(all_counters)

        # Sort counters by frequency (most effective counters first)
        sorted_counters = [card for card, _ in counter_freq.most_common()]

        # Remove duplicates and limit to max_deck_size
        counter_deck = []
        for card in sorted_counters:
            if card not in counter_deck and len(counter_deck) < max_deck_size:
                counter_deck.append(card)

                # If we don't have enough counters, add some placeholder cards
        if len(counter_deck) < max_deck_size:
            print("Warning: Not enough counters found. Adding placeholder cards.")
            placeholder_cards = ["Fireball", "Zap", "The Log", "Valkyrie", "Skeleton Army", "Inferno Tower"]
            for card in placeholder_cards:
                if card not in counter_deck and len(counter_deck) < max_deck_size:
                    counter_deck.append(card)

        return counter_deck

    def get_card_details(self, card_name):
        """Get details for a specific card."""
        return self.cards.get(card_name, {})

    def print_deck_details(self, deck):
        """Print details about a deck."""
        print("\nDeck Details:")
        print("-" * 50)

        total_elixir = 0
        count = 0

        for card_name in deck:
            card_details = self.get_card_details(card_name)
            elixir = card_details.get("elixirCost", "?")
            rarity = card_details.get("rarity", "?")

            if elixir != "?":
                total_elixir += elixir
                count += 1

            print(f"- {card_name} (Elixir: {elixir}, Rarity: {rarity})")

        print("-" * 50)

        if count > 0:
            avg_elixir = total_elixir / count
            print(f"Average Elixir Cost: {avg_elixir:.2f}")


def main():
    # Create an instance of the CounterDeckBuilder
    builder = CounterDeckBuilder()

    # Example opponent deck
    opponent_deck = [
        "Giant Skeleton",
        "Bomber",
        "Arrows",
        "Wizard",
        "Minion Hoard",
        "Prince",
        "Ice Spirit",
        "Skeletons"
    ]

    print(f"Opponent's Deck: {', '.join(opponent_deck)}")

    # Build a counter deck
    counter_deck = builder.build_counter_deck(opponent_deck)

    if isinstance(counter_deck, dict) and "error" in counter_deck:
        print(f"Error: {counter_deck['error']}")
    else:
        print(f"\nSuggested Counter Deck: {', '.join(counter_deck)}")
        builder.print_deck_details(counter_deck)


if __name__ == "__main__":
    main()