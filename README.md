# Premier League Player Data Scraper

## Overview

This project gathers data on Premier League football players by combining data from an API and web scraping. The data includes player names, team associations, and market values. The primary sources of this data are:

1. **API Data (SportMonks API):** Fetches player names, teams, and other player-related details from the official SportMonks API, which is widely recognized for providing reliable football statistics and team data.
2. **Web Scraping (Transfermarkt):** Scrapes market values of players from Transfermarkt, a highly reputable source for football player valuations. This website was chosen due to its detailed and frequently updated data on player market values, which is often not freely available in other public datasets.

## Purpose

The purpose of this project is to create a comprehensive dataset combining player information and market values for Premier League players, which can be used by analysts, sports enthusiasts, or fantasy football participants to gain deeper insights into player performance and market trends.

### Why This Dataset?

- **Unique Value Combination:** This dataset uniquely combines team and player data from an API with accurate and up-to-date market values from Transfermarkt, offering a detailed picture of Premier League player statistics and financial evaluations.
- **Increased Accessibility:** Currently, there is no easily accessible free source that combines both comprehensive team/player statistics and up-to-date market values in one place. Many datasets are either behind paywalls or not integrated, making it cumbersome for users who require such combined data.
- **Enhanced Analysis:** This dataset allows users to perform advanced analysis such as identifying undervalued players, team market value assessments, or scouting for fantasy league picks based on both performance and market valuation.

### Why Is This Dataset Not Publicly Available?

- **Data Licensing and Restrictions:** While some elements of the data, like player names and team associations, are publicly available, market values from sources like Transfermarkt are usually restricted due to their proprietary algorithms and data licensing.
- **Cost of Comprehensive Data:** Integrating multiple sources into a cohesive dataset often involves costs and technical barriers that many users cannot overcome on their own, which is why such a combined dataset is valuable.

## Setup and Installation

### Prerequisites

Ensure you have Python installed on your machine. This project uses the following Python packages:
- `requests`
- `beautifulsoup4`
- `pandas`
- `python-dotenv`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/premier-league-player-scraper.git
2. Navigate into the project directory:
    ```bash
    cd data_cleaning
3. Install the required packages:
    ```bash
    pip install -r requirements.txt

### Setting Up the Environment Variables

1. Create a .env file in the root directory of the project
2. Add your API key to the .env file as follows:
    ```plaintext
    API_TOKEN = your_api_key

### Runing the Program

1. Run the script to fetch data
    ```bash
    python main.py
This will geenrate a CSV file with player data, including their teams and market values
