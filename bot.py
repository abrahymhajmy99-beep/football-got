import os
from dotenv import load_dotenv


def get_match_info(match):
    return {
        'match_id': match['id'],
        'team1_id': match['team1_id'],
        'team2_id': match['team2_id'],
        'score': match['score']
    }


def add_goal(match_id, team_id):
    # Assume match is retrieved from somewhere
    match = get_match_by_id(match_id)
    if match:
        # Retrieve team IDs properly
        match['score'][team_id] += 1
        # additional logic


# Load environment variable for BOT_TOKEN
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')