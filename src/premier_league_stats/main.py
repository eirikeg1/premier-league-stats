import os
# Ensure all necessary imports are here
from data_classes.Fixtures import Fixtures
from StatisticsDataManager import StatisticsDataManager

class Main:
    def __init__(self):
        self.stats = StatisticsDataManager()

    def import_data(self):
        ### Import initial team and player data from before game-week 1
        self.stats.import_static_data()
        self.stats.create_standings()
        
        self.stats.import_fixtures_data()
        
        self.stats.download_raw_data()
        
        # TODO Import player data
        
    def preprocess_data(self):
        # Implement data preprocessing logic
        pass
        
    def predict(self):
        # Implement prediction logic
        pass
    
    def development_code(self):
        """changed thoughout development for testing various things"""
        # Implement debug logic
        for i, game_week in enumerate(self.stats.game_week_iterator()):
            print(f"Game week {i + 1}:")
            for game in game_week:
                print(f" * {game.id}")
                print(f"stats: {game.stats}")
            print("\n")
        
        # Ensure the Statistics class has standings and teams_by_name attributes
        print(f"Standings:\n{self.stats.standings}\n\n")
        
        print("Teams best performers:")
        for team in self.stats.teams_by_name.values():
            print(f"\n{team.name} : {len(team.players)} players")
            for player in sorted(team.players, key=lambda p: p.stats['total_points'], reverse=True)[:5]:  # Assuming team.players is a list
                print(f" * {player.name} : {player.stats['total_points']} total points")
   
if __name__ == "__main__":
    main = Main()
    main.import_data()
    main.preprocess_data()
    main.predict()
    main.development_code()
    