from collections import defaultdict
from typing import DefaultDict, Dict, List

import pandas as pd
from .Match import Match


class Fixtures:
    
    def __init__(self, data_json, team_names: Dict[int, str] = None):
        self.game_weeks = defaultdict(list)
        self.standings_dict = defaultdict(lambda: {'played': 0, 'points': 0, 'strength': 0, 'position': 0})
        self.team_names = team_names or {}
        if data_json:
            self.import_fantasy_json(data_json)


    def import_fantasy_json(self, data: List[dict]):
        
        for game in data:
            
            # Values
            id = int(game['code'])
            event = int(game['event'])
            finished = bool(game['finished'])
            kickoff_time = game['kickoff_time']  # this will be a string in ISO 8601 format
            minutes = int(game['minutes'])
            team_a = int(game['team_a'])
            team_a_score = int(game['team_a_score']) if game['team_a_score'] is not None else None
            team_h = int(game['team_h'])
            team_h_score = int(game['team_h_score']) if game['team_h_score'] is not None else None
            team_h_difficulty = int(game['team_h_difficulty'])
            team_a_difficulty = int(game['team_a_difficulty'])
            
            
            
            # TODO: Look into cleaning up structure?
            # Create stats dictionary to store player statistics per match
            # Structure mirrors Fantasy API stats format, where:
            # - 'identifier' is the type of statistic (e.g., 'goals_scored', 'assists')
            # - 'a' and 'h' are lists of statistics for away and home teams respectively
            # Example:
            # stats = [{
            #     'goals_scored': {
            #         'away': [
            #             {'a_element': 2342, 'a_value': 1},
            #             {'a_element': 432, 'a_value': 1}
            #         ],
            #         'home': [
            #             {'h_element': 3234, 'h_value': 2}
            #         ]
            #     },
            #     'assists': ...
            # }, ...]

            
            stats = defaultdict(list)
            
            # TODO: Implement stats import once the structure is clear
            # print(game['stats'])
            # for stat, value in game['stats'].items():
            #     identifier = stat['identifier']
            #     a_stats = stat['a']
            #     h_stats = stat['h']
                
            #     cur_id_stats = {
            #         'away': defaultdict(list),
            #         'home': defaultdict(list),
            #     }
                
            #     cur_id_stats = stats[identifier]
                
            #     for a_stat in a_stats:
            #         a_value = int(a_stat['value'])
            #         a_element = int(a_stat['element'])
                    
            #         cur_id_stats.append({'a_element': a_element, 'a_value': a_value})

                
            #     for h_stat in h_stats:
            #         h_value = int(h_stat['value'])
            #         h_element = int(h_stat['element'])
            #         cur_id_stats.append({'h_element': h_element, 'h_value': h_value})                    

            # Create an object and add it to fixture game week
            self.game_weeks[event].append(Match(
                code=id,  # Assuming 'code' should be the same as 'id'
                event=event,
                finished=finished,
                id=id,
                kickoff_time=kickoff_time,
                minutes=minutes,
                team_a=team_a,
                team_a_score=team_a_score,
                team_h=team_h,
                team_h_score=team_h_score,
                stats=stats
            ))
            
            # Update standings
            if team_h_score is not None and team_a_score is not None:
                # Increment matches played
                self.standings_dict[team_h]['played'] += 1
                self.standings_dict[team_a]['played'] += 1
                
                # Update points based on match result
                if team_h_score > team_a_score:
                    self.standings_dict[team_h]['points'] += 3
                elif team_h_score < team_a_score:
                    self.standings_dict[team_a]['points'] += 3
                else:
                    self.standings_dict[team_h]['points'] += 1
                    self.standings_dict[team_a]['points'] += 1

            # Update team strength
            self.standings_dict[team_h]['strength'] += team_h_difficulty
            self.standings_dict[team_a]['strength'] += team_a_difficulty
        
        # TODO: Implement position calculation
                    

        # Convert standings to DataFrame
        self.update_standings_df()
        
    
    def update_standings_df(self):
        # Convert defaultdict to DataFrame
        data = []
        for team_id, stats in self.standings_dict.items():
            
            team = self.team_names.get(team_id)
            
            data.append({
                'name': team.name if team else f"Team {team_id}",
                'played': stats['played'],
                'points': stats['points'],
                'strength': stats['strength'],
                'id': team_id,
                'position': stats['position']
            })
        
        # Create DataFrame
        self.standings = pd.DataFrame(data)
        
        # Calculate positions
        self.standings.sort_values(by='points', ascending=False, inplace=True)
        self.standings.reset_index(drop=True, inplace=True)
        self.standings['position'] = self.standings.index + 1
    
    def get_standings_dataframe(self):
        return self.standings


    def game_week_iterator(self):
        return iter(self.game_weeks.values())
    
    def game_iterator(self):
        return iter([game for game_week in self.game_weeks.values() for game in game_week])
