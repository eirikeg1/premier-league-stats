import numpy as np
import pandas as pd
from pprint import pprint
import requests


class Statistics:
    """Class for storing and manipulating statistics for the premier league"""

    # Team data
    _team_data: pd.DataFrame = pd.DataFrame()

    # Fantasy PL specific data
    _events_data: pd.DataFrame = pd.DataFrame()
    _game_settings_data: pd.DataFrame = pd.DataFrame()
    _phases: pd.DataFrame = pd.DataFrame()

    # Player data
    _elements: pd.DataFrame = pd.DataFrame()
    _element_stats: pd.DataFrame = pd.DataFrame()
    _element_types: pd.DataFrame = pd.DataFrame()

    _match_data: pd.DataFrame = pd.DataFrame()
    _player_data: pd.DataFrame = pd.DataFrame()

    FANTASY_BASE_URL: str = "https://fantasy.premierleague.com/api/"

    ### Imports:

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
            raise Exception(f"Request failed with status code {request.status_code}")

        data = request.json()
        print(f"All static data collections: {data.keys()}")
        self._team_data = pd.json_normalize(data["teams"])

    ### Team functions:

    def get_teams(self) -> pd.DataFrame:
        """Return all team data. If no data is present, it will be imported from the API"""

        if self._team_data.empty:
            self.import_static_data()

        return self._team_data

    def get_standings(self) -> pd.DataFrame:
        """Return the current standings with columns: id, name, played, position, points"""

        if self._team_data.empty:
            raise Exception("No team data present. Please import data first")

        standings = self._team_data[["id", "name", "played", "position", "points"]]
        standings = standings.sort_values(by=["points", "played"], ascending=False)
        return standings


if __name__ == "__main__":
    stats = Statistics()
    stats.import_static_data()
    print(stats.get_standings())
