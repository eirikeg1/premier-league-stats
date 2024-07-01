import time
from LoadingAnimator import LoadingAnimator
from Team import Team

from pprint import pprint
from typing import List

import numpy as np
import pandas as pd
import requests


class Statistics:
    """Class for storing and manipulating statistics for the premier league"""

    # Team data (Team.name: str -> Team)
    teams: dict[Team] = None
    standings: pd.DataFrame = None

    # Fantasy PL specific data
    events_data: pd.DataFrame = None
    game_settings_data: pd.DataFrame = None
    phases: pd.DataFrame = None
    
    # Match data
    simulated_game_weeks: int = 0

    # Player data
    elements: pd.DataFrame = None
    element_stats: pd.DataFrame = None
    element_types: pd.DataFrame = None

    match_data: pd.DataFrame = None
    player_data: pd.DataFrame = None

    FANTASY_BASE_URL: str = "https://fantasy.premierleague.com/api/"
    FIXTURES_URL = f"https://onefootball.com/en/competition/premier-league-9/fixtures"
    
    def __init__(self):
        
        self.teams = {}
        self.simulated_game_weeks = 0 # reset to make unique for each object

        ### Import initial team and player data from before game-week 1
        self.import_static_data()
        self._create_standings()
        
        # TODO Import player data
        

    ### Importing data:

    def import_from_api(self, user_name: str = None, password: str = None):
        """
        Import data from premier leaguer fantasy API. If no log in details are provided, it will 
        be retrieved from the environment variables <fantasy_username> and <fantasy_password>
        """
        raise NotImplementedError

    def import_from_file(self, file: str):
        """
        Import data from a file. The file should be a json file with the same structure as the API
        response
        """
        return NotImplementedError

    def import_static_data(self):
        """
        Import static data from premier league fantasy API. Static data is freezed from before
        game-week 1
        """

        request = requests.get(self.FANTASY_BASE_URL + "bootstrap-static/")

        if request.status_code != 200:
            raise Exception(
                f"Request to import static data failed with status code {request.status_code}"
            )

        # data = pd.json_normalize(request.json())
        self.static_data = request.json()

        self._create_teams(self.static_data["teams"])
        self._create_standings()


    ### Creating datastructures from data:

    def _create_teams(self, data: pd.Series):
        """Create teams from data"""

        for team in data:
            team = Team(pandas_data=team)
            self.teams[team.name] = team

    def _create_standings(self):
        if not self.teams:
            raise Exception("No team data present. Please import data first")

        self.standings = pd.DataFrame.from_dict(
            {"name": [team.name for team in self.teams.values()],
             "played": [team.played for team in self.teams.values()],
             "position": [team.position for team in self.teams.values()],
             "points": [team.points for team in self.teams.values()],
             "strength": [team.strength for team in self.teams.values()],
             },
        )
       
        self.standings.sort_values(by=["points", "name"], ascending=[False, True], inplace=True)
        self.standings.index = np.arange(1, len(self.standings) + 1)



    ### Get data:

    def get_teams(self) -> dict[Team]:
        """Return all team data. If no data is present, it will be imported from the API"""

        if self.standings.empty:
            print(f"No team data present. Importing from API")
            self.import_static_data()

        return self.teams

    def get_standings(self) -> pd.DataFrame:
        """Return the current standings with columns: id, name, played, position, points"""

        if self.standings.empty:
            self.import_static_data()
            
        return self.standings


if __name__ == "__main__":
    stats = Statistics()

    stats.import_static_data()
    
    animator = LoadingAnimator(animation_speed=40)
    
    for _ in range(1000000):
        animator.print_animation_every_x()
        #time.sleep(0.001)
        
