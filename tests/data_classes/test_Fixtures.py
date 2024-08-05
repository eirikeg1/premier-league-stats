import pytest
import sys
from premier_league_stats.data_classes.Fixtures import Fixtures
from premier_league_stats.data_classes.Match import Match

@pytest.fixture
def fixtures():
    return Fixtures(None)

def test_import_fantasy_json(fixtures: Fixtures):
    data = [
        {
            'code': '123',
            'event': '1',
            'finished': True,
            'kickoff_time': '2022-01-01T12:00:00Z',
            'minutes': '90',
            'id': '123',
            'team_a': '1',
            'team_a_score': '2',
            'team_h': '2',
            'team_h_score': '1',
            'team_h_difficulty': '2',
            'team_a_difficulty': '3',
            'stats': {
                'goals_scored': {
                    'away': [
                        {'a_element': 2342, 'a_value': 1},
                        {'a_element': 432, 'a_value': 1}
                    ],
                    'home': [
                        {'h_element': 3234, 'h_value': 2}
                    ]
                },
                # Add more stats if needed
            }
        },
        # Add more games if needed
    ]

    fixtures.import_fantasy_json(data)
    # Assert the game week and match objects are created correctly
    assert len(fixtures.game_weeks) == 1
    assert fixtures.game_weeks[1]

    match: Match = fixtures.game_weeks[1][0]
    assert match.id == 123, "Error in match id"
    assert match.event == 1
    assert match.finished == True
    assert match.kickoff_time == '2022-01-01T12:00:00Z'
    assert match.minutes == 90
    assert match.team_a == 1
    assert match.team_a_score == 2
    assert match.team_h == 2
    assert match.team_h_score == 1

    # TODO: Assert the stats are imported correctly
    # assert 'goals_scored' in match.stats
    # assert match.get_away_sum('goals_scored') == 2
    # assert match.get_home_sum('goals_scored') == 2