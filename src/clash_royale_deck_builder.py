import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Set page title and configuration
st.set_page_config(page_title="Clash Royale Deck Builder", layout="wide")
st.title("Clash Royale Deck Builder")


# Load data
@st.cache_data
def load_data():
    # Load the card metadata from CSV
    # Use a relative path that works both locally and on Streamlit Cloud
    current_dir = os.path.dirname(__file__)
    cards_df = pd.read_csv(os.path.join(current_dir, 'data', 'card_metadata_enhanced_final.csv'))

    # Load the counter cards JSON
    with open(r'C:\Users\maxda\PycharmProjects\pythonProject6\src\data\card_counters.json', 'r') as f:
        counter_data = json.load(f)

    return cards_df, counter_data


cards_df, counter_data = load_data()

# Sidebar for card selection
st.sidebar.header("Build Your Deck")
st.sidebar.write("Select up to 8 cards for your deck")

# Create multiselect for card selection
selected_cards = st.sidebar.multiselect(
    "Select Cards:",
    options=cards_df['Card Name'].tolist(),
    max_selections=8
)

# Main content area
if selected_cards:
    st.header("Your Selected Deck")

    # Display selected cards in a grid
    cols = st.columns(min(len(selected_cards), 4))
    for i, card_name in enumerate(selected_cards):
        card_info = cards_df[cards_df['Card Name'] == card_name].iloc[0]
        with cols[i % 4]:
            st.subheader(card_name)
            st.write(f"**Elixir Cost:** {card_info['Elixir']}")
            st.write(f"**Role:** {card_info['Role']}")
            st.write(f"**Special Ability:** {card_info['Special Abilities']}")

            # Display deck stats
    st.header("Deck Analysis")

    # Calculate average elixir cost
    avg_elixir = cards_df[cards_df['Card Name'].isin(selected_cards)]['Elixir'].mean()
    st.write(f"**Average Elixir Cost:** {avg_elixir:.2f}")

    # Show counters for selected cards
    st.header("Potential Counters to Watch For")
    for card in selected_cards:
        if card in counter_data:
            st.subheader(f"Counters to {card}:")
            st.write(", ".join(counter_data[card]))

            # Show synergies and vulnerabilities
    if len(selected_cards) > 0:
        st.header("Card Synergies and Vulnerabilities")
        for card in selected_cards:
            card_info = cards_df[cards_df['Card Name'] == card].iloc[0]
            st.subheader(card)
            st.write(f"**Synergies:** {card_info['Synergy Tags']}")
            st.write(f"**Vulnerabilities:** {card_info['Vulnerability Tags']}")
else:
    st.info("Select cards from the sidebar to build your deck")

    # Footer
st.sidebar.markdown("---")
st.sidebar.info("Data from Clash Royale card metadata")