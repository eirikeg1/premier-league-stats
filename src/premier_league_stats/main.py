from Statistics import Statistics


if __name__ == "__main__":
    stats = Statistics()
    
    print("Static data imported")
    
    print(stats.fixtures.game_weeks[1][0])
    # print(f"Standings:\n{stats.standings}\n\n")
    
    # for team in stats.teams_by_name.values():
    #     print(f"{team.name} : {len(team.players)} players")
    #     for i in range(5):
    #         print(f" * {team.players[i].name}")
    