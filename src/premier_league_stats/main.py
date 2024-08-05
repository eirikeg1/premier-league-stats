from Statistics import Statistics
import sys
import os

from data_classes.Fixtures import Fixtures

   
if __name__ == "__main__":
    stats = Statistics()
    
    print("Static data imported")
    
    for i, game_week in enumerate(stats.game_week_iterator()):
        print(f"Game week {i + 1}:")
        for game in game_week:
            print(f" * {game.id}")
        print("\n")
    
    
    # print(f"Standings:\n{stats.standings}\n\n")
    
    # for team in stats.teams_by_name.values():
    #     print(f"{team.name} : {len(team.players)} players")
    #     for i in range(5):
    #         print(f" * {team.players[i].name}")
    