# Imports
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the API token from environment variables
token = os.getenv("API_TOKEN")

# Step 1: Fetch all teams and players from the API
all_teams_epl_data_url = f"https://api.sportmonks.com/v3/football/teams/seasons/23614?api_token={token}"
response = requests.get(all_teams_epl_data_url)
data = response.json()  # Parse the response as JSON

# Initialize a list to store all squads
all_squads = []

# Check if the data retrieval is successful
if response.status_code == 200:
    # Extract team IDs and names from the response
    teams_data = [{'id': team['id'], 'name': team['name']} for team in data['data']]

    # Base URLs for squad and player data requests
    squad_base_url = f"https://api.sportmonks.com/v3/football/squads/teams/{{ID}}?api_token={token}"
    player_base_url = f"https://api.sportmonks.com/v3/football/players/{{ID}}?api_token={token}"

    # Fetch squad data for each team
    for team in teams_data:
        team_id = team['id']
        team_name = team['name']

        # Format the squad URL with the team ID
        formatted_squad_url = squad_base_url.replace("{ID}", str(team_id))

        # Fetch squad data for the current team
        squad_response = requests.get(formatted_squad_url)
        if squad_response.status_code == 200:
            squad_data = squad_response.json()  # Parse the squad data
            # Extract players data
            players = squad_data['data']  # Adjust this if the structure is different
            all_squads.append({'team': team_name, 'players': players})
            print(f"Successfully fetched squad for {team_name}")
        else:
            print(f"Failed to fetch squad for {team_name}: {squad_response.status_code}")
else:
    print(f"Error fetching teams data: {response.status_code}, {response.text}")

# Initialize a list to store player information
player_list = []

# Step 2: Loop through each player in all squads to fetch player names and teams
for squad in all_squads:
    team_name = squad['team']
    players = squad['players']  # This assumes 'players' is a direct list of player dictionaries

    for player in players:
        player_id = player['player_id']  # Ensure 'player_id' is correctly referenced
        formatted_player_url = player_base_url.replace("{ID}", str(player_id))

        # Fetch player details
        player_response = requests.get(formatted_player_url)
        if player_response.status_code == 200:
            player_data = player_response.json()
            player_name = player_data['data']['name']  # Adjust based on the actual JSON structure
            # Append the player name and team name to the list
            player_list.append({'Player': player_name, 'Team': team_name})
        else:
            print(f"Failed to fetch data for player ID {player_id}: {player_response.status_code}")

# Convert the list of players into a pandas DataFrame
player_df = pd.DataFrame(player_list)

# Step 3: Scrape market values from each club page and match with player data
def scrape_transfermarkt():
    # Base URL of the Premier League start page on Transfermarkt
    base_url = "https://www.transfermarkt.us/premier-league/startseite/wettbewerb/GB1"

    # Headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    # Step 1: Scrape club links from the Premier League page
    response = requests.get(base_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve the Premier League page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    club_rows = soup.find_all('td', {'class': 'hauptlink no-border-links'})

    # Extract club names and links
    clubs = []
    for row in club_rows:
        club_name = row.get_text(strip=True)
        club_link = row.find('a')['href']
        full_link = f"https://www.transfermarkt.us{club_link}"  # Form the full URL for the club page
        clubs.append({'Club': club_name, 'Link': full_link})

    # Step 2: Scrape players from each club and update the player DataFrame
    for club in clubs:
        print(f"Scraping players for club: {club['Club']} from {club['Link']}")
        club_response = requests.get(club['Link'], headers=headers)
        if club_response.status_code != 200:
            print(f"Failed to retrieve the club page: {club['Link']}. Status code: {club_response.status_code}")
            continue

        club_soup = BeautifulSoup(club_response.content, 'html.parser')
        table = club_soup.find('table', {'class': 'items'})
        if not table:
            print(f"Table not found on the club page: {club['Link']}")
            continue

        # Find all table rows
        rows = table.find_all('tr')
        for row in rows:
            player_cell = row.find('td', {'class': 'hauptlink'})
            market_value_cell = row.find('td', {'class': 'rechts hauptlink'})

            # Extract player name and market value only if both cells are found
            if player_cell and market_value_cell:
                player_name = player_cell.get_text(strip=True)
                market_value = market_value_cell.get_text(strip=True)

                # Update the player's market value in the DataFrame if found
                if player_name in player_df['Player'].values:
                    player_df.loc[player_df['Player'] == player_name, 'Market Value'] = market_value

        # Sleep to mimic human behavior
        time.sleep(random.uniform(2, 5))

    # Display the updated DataFrame
    print(player_df)

    # Save the DataFrame as a CSV file
    player_df.to_csv('premier_league_players_with_market_values.csv', index=False)
    print("Data has been exported to 'premier_league_players_with_market_values.csv'")

# Call the scraping function to update player market values
scrape_transfermarkt()