from dataclasses import dataclass, field
from typing import Dict, Optional

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
    stats: Optional[Dict[str, Dict[int, int]]] = field(default_factory=dict)  # Event name (goals): Dict[player: count]

