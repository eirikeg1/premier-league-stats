from api.PremierLeagueFantasyAPI import PremierLeagueFantasyAPI
from data_classes.Team import Team
from data_classes.Fixtures import Fixtures
from utils.LoadingAnimator import LoadingAnimator

from pprint import pprint
from typing import List

import numpy as np
import pandas as pd


class Statistics:
    """Class for storing and manipulating statistics for the premier league"""

    # Team data (Team.name: str -> Team)
    teams_by_name: dict[Team] = None
    standings: pd.DataFrame = pd.DataFrame()

    # Fantasy PL specific data
    events_data: pd.DataFrame = None
    game_settings_data: pd.DataFrame = None
    phases: pd.DataFrame = None
    
    # Match data
    simulated_game_weeks: int = 0
    fixtures: Fixtures = None

    # Player data
    elements: pd.DataFrame = None
    element_stats: pd.DataFrame = None
    element_types: pd.DataFrame = None

    match_data: pd.DataFrame = None
    player_data: pd.DataFrame = None

    # API interfaces
    fantasy_api = PremierLeagueFantasyAPI()

    
    def __init__(self):
        
        self.teams_by_name = {}
        self.teams_by_id = {}
        self.simulated_game_weeks = 0 # reset to make unique for each object

        ### Import initial team and player data from before game-week 1
        self.import_static_data()
        self.create_standings()
        
        self.import_fixtures_data()
        
        # TODO Import player data
        

    ### Importing data:

    def import_static_data(self):
        """
        Import static data from premier league fantasy API. Static data is freezed from before
        game-week 1
        """

        # data = pd.json_normalize(request.json())
        self.static_data = self.fantasy_api.fetch_static_json()

        self.create_teams(self.static_data["teams"])
        self.create_standings()

        self.create_players(self.static_data["elements"])
        
    def import_fixtures_data(self, user_name: str = None, password: str = None):
        """
        Import data from premier leaguer fantasy API. If no log in details are provided, it will 
        be retrieved from the environment variables <fantasy_username> and <fantasy_password>
        """
        
        self.fixtures_data = self.fantasy_api.fetch_fixtures_json()
        self.fixtures = Fixtures(self.fixtures_data)

    def import_from_file(self, file: str):
        """
        Import data from a file. The file should be a json file with the same structure as the API
        response
        """
        return NotImplementedError


    ### Creating datastructures from data:

    def create_teams(self, data: pd.Series):
        """Create teams from data"""

        for team in data:
            team = Team(pandas_data=team)
            self.teams_by_name[team.name] = team
            self.teams_by_id[team.id] = team


    def create_standings(self):
        if not self.teams_by_name:
            raise Exception("No team data present. Please import data first")

        self.standings = pd.DataFrame.from_dict(
            {
                "name": [team.name for team in self.teams_by_name.values()],
                "played": [team.played for team in self.teams_by_name.values()],
                "position": [team.position for team in self.teams_by_name.values()],
                "points": [team.points for team in self.teams_by_name.values()],
                "strength": [team.strength for team in self.teams_by_name.values()],
             },
        )
       
        self.standings.sort_values(by=["points", "name"], ascending=[False, True], inplace=True)
        self.standings.index = np.arange(1, len(self.standings) + 1)

    def create_players(self, data):
        for i, element in enumerate(data):
            self.teams_by_id[element["team"]].add_player(element)


    ### Get data:

    def get_teams(self) -> dict[Team]:
        """Return all team data. If no data is present, it will be imported from the API"""

        if self.standings.empty:
            print(f"No team data present. Importing from API")
            self.import_static_data()

        return self.teams_by_name
    

    def get_standings(self) -> pd.DataFrame:
        """Return the current standings with columns: id, name, played, position, points"""

        if self.standings.empty:
            self.import_static_data()
            
        return self.standings
    
    
    def game_week_iterator(self):
        return iter(self.fixtures.game_week_iterator())


if __name__ == "__main__":
    stats = Statistics()
    
    print("Static data imported")
    # print(f"Standings:\n{stats.standings}\n\n")
    # animator = LoadingAnimator(animation_speed=40)
    
    # for _ in range(1000000):
    #     animator.print_animation_every_x()
    #     #time.sleep(0.001)
        
