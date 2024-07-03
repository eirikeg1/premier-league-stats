from Statistics import Statistics


if __name__ == "__main__":
    stats = Statistics()
    
    print("Static data imported")
    print(f"Standings:\n{stats.standings}\n\n")
    
    for team in stats.teams_by_name.values():
        print(f"{team.name} : {len(team.players)} players")
    