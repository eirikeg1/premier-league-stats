from src.premier_league_stats.Statistics import Statistics


if __name__ == "__main__":
    stats = Statistics()
    
    print("Static data imported")
    print(f"Standings:\n{stats.standings}\n\n")
    