from dataclasses import dataclass
from src.premier_league_stats.data_classes.Match import Match
from src.premier_league_stats.data_processing.DataProcessingManager import DataProcessingManager
from src.premier_league_stats.data_classes.Team import Team

@dataclass
class MatchPlayersData:
    
    match_data: Match
    all_teams: list[Team]
        
    
    def get_players(self):
        team_ids = [self.match_data.team_h, self.match_data.team_a]
        teams = [team for team in self.all_teams if team.id in team_ids]
        
        players = [player for team in teams for player in team.players]
        print(f"Teams: {teams} ({team_ids})")
        return players
        
    
    def __str__(self):
        player_strings = [str(player) for player in self.get_players()]
        return f"MatchPlayersData(match_data: {self.match_data}, all_teams: {player_strings})"
        

class MatchPlayersProcessingManager(DataProcessingManager):
    """
    Can be used to fetch a match and all players in that match.
    """
    
    def __init__(self, data: MatchPlayersData, base_tokenizer=None):
        super().__init__(data, base_tokenizer=base_tokenizer)
        self.match_data = data.match_data
        self.players = data.get_players()
        
    def create_data_loader()
        ...
        
    