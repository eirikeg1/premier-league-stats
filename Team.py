from typing import Generator
import pandas as pd


class Team:
    """Class for storing and manipulating team data"""

    matches = pd.DataFrame()
    players = pd.DataFrame()

    def __init__(
        self,
        pandas_data: pd.Series = None,
        id: int = None,
        name: str = None,
        played: int = None,
        position: int = None,
        points: int = None,
        strength: int = None,
        players: pd.DataFrame = None,
    ):
        """Team can be initialized with either a Pandas Series or the individual parameters"""
        
        if pandas_data is not None:
            self.id = pandas_data["id"]
            self.name = pandas_data["name"]
            self.played = pandas_data["played"]
            self.position = pandas_data["position"]
            self.points = pandas_data["points"]
            self.strength = pandas_data["strength"]
        else:
            print("data_frame is None")
            assert all([id, name, played, position, points, strength]), "Missing parameters when trying to create team"
            self.id = id
            self.name = name
            self.played = played
            self.position = position
            self.points = points
            self.strength = strength

        if players:
            self.players = players

    def __str__(self):
        return f"{self.name} (matches simulated: {len(self.matches)})"

    def __lt__(self, other):
        if self.points == other.points:
            return self.name < other.name
        return self.points < other.points

    def __gt__(self, other):
        if self.points == other.points:
            return self.name > other.name
        return self.points > other.points

    def __getitem__(self, item: str) -> str | int | pd.DataFrame:
        """Get item from team. Valid items are: id, name, played, position, points, strength, matches"""
        match item:
            case "id":
                return self.id
            case "name":
                return self.name
            case "played":
                return self.played
            case "position":
                return self.position
            case "points":
                return self.points
            case "strength":
                return self.strength
            case "matches":
                return self.matches
            case _:
                raise KeyError(f"No such key: {item}")

    def __setitem__(self, key: str, value):
        """Set item in team. Valid items are: id, name, played, position, points, strength, matches"""
        match key:
            case "id":
                self.id = value
            case "name":
                self.name = value
            case "played":
                self.played = value
            case "position":
                self.position = value
            case "points":
                self.points = value
            case "strength":
                self.strength = value
            case "matches":
                self.matches = value
            case _:
                raise KeyError(f"No such key: {key}")

    def iter_match(self) -> Generator[pd.Series, None, None]:
        """Create a generator over matches"""
        return (match for match in self.matches.iterrows())

    def get_matches(self) -> pd.DataFrame:
        return self.matches

    def add_player(self, player: pd.Series):
        """Add player to team"""
        return NotImplementedError

    def add_players(self, players: pd.DataFrame):
        """Add players to team"""
        return NotImplementedError
