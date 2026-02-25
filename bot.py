import os
from dotenv import load_dotenv

load_dotenv()

# Updated function with team1_id and team2_id

def get_match_info(match_id, team1_id, team2_id):
    # fetch match info based on match_id, team1_id and team2_id
    pass


def add_goal(match_id, team_id):
    match_info = get_match_info(match_id, team_id)
    # handle adding of goal using match_info
    pass

# Ensure to use: os.getenv('BOT_TOKEN') where needed in your code.
