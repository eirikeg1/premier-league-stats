from Team import Team

from pprint import pprint
from typing import List

import numpy as np
import pandas as pd
import requests


class Statistics:
    """Class for storing and manipulating statistics for the premier league"""

    # Team data (Team.name: str -> Team)
    _teams: dict[Team] = {}
    _standings: pd.DataFrame = pd.DataFrame()

    # Fantasy PL specific data
    _events_data: pd.DataFrame = None
    _game_settings_data: pd.DataFrame = None
    _phases: pd.DataFrame = None
    
    # Match data
    simulated_game_weeks: int = 0

    # Player data
    _elements: pd.DataFrame = None
    _element_stats: pd.DataFrame = None
    _element_types: pd.DataFrame = None

    _match_data: pd.DataFrame = None
    _player_data: pd.DataFrame = None

    FANTASY_BASE_URL: str = "https://fantasy.premierleague.com/api/"
    
    def __init__(self):
        
        ### Import initial team and player data from before game-week 1
        self.import_static_data()
        self._create_standings()
        
        # TODO Import player data
        

    ### Importing data:

    def import_from_api(self, user_name: str = None, password: str = None):
        """Import data from premier leaguer fantasy API. If no log in details are provided, it will be retrieved
        from the environment variables <fantasy_username> and <fantasy_password>"""
        raise NotImplementedError

    def import_from_file(self, file: str):
        """Import data from a file. The file should be a json file with the same structure as the API response"""
        return NotImplementedError

    def import_static_data(self):
        """Import static data from premier league fantasy API. Static data is freezed from before game-week 1"""

        request = requests.get(self.FANTASY_BASE_URL + "bootstrap-static/")

        if request.status_code != 200:
            raise Exception(
                f"Request to import static data failed with status code {request.status_code}"
            )

        data = request.json()
        self._create_teams(pd.json_normalize(data["teams"]))

    ### Creating datastructures from data:
    def _create_teams(self, data: pd.DataFrame):
        """Create teams from data"""

        for index, row in data.iterrows():
            team = Team(pandas_data=row)
            self._teams[team.name] = team

    def _create_standings(self):
        if not self._teams:
            raise Exception("No team data present. Please import data first")

        self._standings = pd.DataFrame.from_dict(
            {"name": [team.name for team in self._teams.values()],
             "played": [team.played for team in self._teams.values()],
             "position": [team.position for team in self._teams.values()],
             "points": [team.points for team in self._teams.values()],
             "strength": [team.strength for team in self._teams.values()]
             },
        )
       
        self._standings.sort_values("points", ascending=False, inplace=True)
        self._standings.reset_index(drop=True, inplace=True)



    ### Get data:

    def get_teams(self) -> dict[Team]:
        """Return all team data. If no data is present, it will be imported from the API"""

        if self._standings.empty:
            print(f"No team data present. Importing from API")
            self.import_static_data()

        return self._teams

    def get_standings(self) -> pd.DataFrame:
        """Return the current standings with columns: id, name, played, position, points"""

        if self._standings.empty:
            self.import_static_data()
            
        return self._standings


if __name__ == "__main__":
    stats = Statistics()

    stats.import_static_data()
    print(stats.get_standings())
