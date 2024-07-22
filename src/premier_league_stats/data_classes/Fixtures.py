from collections import defaultdict
from typing import Dict, List
from data_classes.Match import Match


class Fixtures:
    
    def __init__(self, data_json):
        self.game_weeks = defaultdict(list)
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
            # stats = {
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
            # }

            
            stats = defaultdict(list)
            
            for stat in game['stats']:
                identifier = stat['identifier']
                a_stats = stat['a']
                h_stats = stat['h']
                
                cur_id_stats = {
                    'away': defaultdict(list),
                    'home': defaultdict(list),
                }
                
                cur_id_stats = stats[identifier]
                
                for a_stat in a_stats:
                    a_value = int(a_stat['value'])
                    a_element = int(a_stat['element'])
                    
                    cur_id_stats.append({'a_element': a_element, 'a_value': a_value})

                
                for h_stat in h_stats:
                    h_value = int(h_stat['value'])
                    h_element = int(h_stat['element'])
                    cur_id_stats.append({'h_element': h_element, 'h_value': h_value})                    

            # Create an object and add it to fixture game week
            self.game_weeks[event].append(Match(
                id,
                event,
                finished,
                id,
                kickoff_time,
                minutes,
                team_a,
                team_a_score,
                team_h,
                team_h_score,
                stats
            ))
            
    def game_week_iterator(self):
        return iter(self.game_weeks.values())
    
    def game_iterator(self):
        return iter([game for game_week in self.game_weeks.values() for game in game_week])
