from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class Match:
    code: int
    event: int = 0
    finished: bool = False
    finished_provisional: bool = False
    id: int = 0
    kickoff_time: Optional[str] = None
    minutes: int = 0
    provisional_start_time: Optional[str] = None
    started: bool = False
    team_a: int = 0
    team_a_score: int = 0
    team_h: int = 0
    team_h_score: int = 0
    # stats: Optional[Dict[str, Dict[int, int]]] = field(default_factory=dict)  # Event name (goals): Dict[player: count]
    stats: Optional[Dict[str, Dict[str, List[Dict[str, int]]]]] = field(default_factory=dict)

    
    def get_team_sum(self, identifier: str, team: str):
        if team not in ['home', 'away']:
            raise Exception("'team' must be either 'home' or 'away'")
        
        if team == 'home':
            return self.get_home_sum(identifier)
        else:
            return self.get_away_sum(identifier)
    

    def get_away_sum(self, identifier):
        return sum(item['value'] for item in self.stats[identifier]['a'])

    def get_home_sum(self, identifier):
        return sum(item['value'] for item in self.stats[identifier]['h'])
    
    def get_score(self) -> str:
        return f"{self.team_h_score} - {self.team_a_score}"
