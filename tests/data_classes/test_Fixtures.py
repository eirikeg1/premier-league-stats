import pytest
import sys
from premier_league_stats.data_classes.Fixtures import Fixtures

@pytest.fixture
def fixtures():
    return Fixtures(None)

def test_import_fantasy_json(fixtures):
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

    # Add more assertions for other stats if neededdef test_import_fantasy_json(fixtures):
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
    # Add more assertions for other stats if neededdef test_import_fantasy_json(fixtures):
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
    # Assert the game week and match objects are created correctly
    assert len(fixtures.game_weeks) == 1
    assert len(fixtures.game_weeks[1]) == 1
    match = fixtures.game_weeks[1][0]
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
    # Add more assertions for other stats if neededdef test_import_fantasy_json(fixtures):
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
    # Add more assertions for other stats if needed