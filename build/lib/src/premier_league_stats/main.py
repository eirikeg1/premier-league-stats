from Statistics import Statistics
from premier_league_stats.data_classes.Fixtures import Fixtures

def foo(fixtures):
    data = [
        {
            'code': '123',
            'event': '1',
            'finished': True,
            'kickoff_time': '2022-01-01T12:00:00Z',
            'minutes': '90',
            'team_a': '1',
            'team_a_score': '2',
            'team_h': '2',
            'team_h_score': '1',
            'team_h_difficulty': '2',
            'team_a_difficulty': '3',
            'stats': [
                {
                    'identifier': 'goals_scored',
                    'a': [
                        {'value': '1', 'element': '2342'},
                        {'value': '1', 'element': '432'}
                    ],
                    'h': [
                        {'value': '2', 'element': '3234'}
                    ]
                },
                # Add more stats if needed
            ]
        },
        # Add more games if needed
    ]

    fixtures.import_fantasy_json(data)

    print(fixtures.game_weeks)
    # Assert the game week and match objects are created correctly
    assert len(fixtures.game_weeks) == 1
    assert len(fixtures.game_weeks['1']) == 1

    match = fixtures.game_weeks['1'][0]
    assert match.id == 123
    assert match.event == 1
    assert match.finished == True
    assert match.kickoff_time == '2022-01-01T12:00:00Z'
    assert match.minutes == 90
    assert match.team_a == 1
    assert match.team_a_score == 2
    assert match.team_h == 2
    assert match.team_h_score == 1

    # Assert the stats are imported correctly
    assert 'goals_scored' in match.stats
    assert len(match.stats['goals_scored']['away']) == 2
    assert len(match.stats['goals_scored']['home']) == 1

   
if __name__ == "__main__":
    stats = Statistics()
    
    fixtures = Fixtures()
    foo(fixtures)
    
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
    