from typing import List

import pandas as pd

from data_classes.News import News


class Player:
    
    def __init__(
            self,
            id: int,
            name: str,
            team: int,
            position: str = None, # singlular_name in api
            photo: str = None,
            squad_number: int = None,
            stats: pd.Series = None
    ):
        """
        Initialize player
        """
        self.id = id
        self.position = position
        if squad_number:
            self.squad_number = squad_number

        self.news: List[News] = []
        self.name = name
        self.team = team
        self.photo = photo
        self.stats = pd.Series()
    
    def set_stats(self, stats):
        self.stats = stats
    
    # def set_stats(
    #     self,
    #     minutes_played: int|None = None,
    #     goals_scored: int|None = None,
    #     assists: int|None = None,
    #     clean_sheets: int|None = None,
    #     goals_conceded: int|None = None,
    #     own_goals: int|None = None,
    #     penalties_saved: int|None = None,
    #     yellow_cards: int|None = None,
    #     red_cards: int|None = None,
    #     saves: int|None = None,
    #     bonus: int|None = None,
    #     bonus_points_system: int|None = None,
    #     influence: float|None = None,
    #     creativity: float|None = None,
    #     threat: float|None = None,
    #     ict_index: float|None = None,
    #     games_started: int|None = None,
    #     expected_goals: float|None = None,
    #     expected_assists: float|None = None,
    #     expected_goal_involvements: float|None = None,
    #     expected_goals_conceded: float|None = None,
    #     cost_change_event: int|None = None,
    #     cost_change_event_fall: int|None = None,
    #     cost_change_start: int|None = None,
    #     cost_change_start_fall: int|None = None,
    #     dreamteam_count: int|None = None,
    #     element_type: int|None = None,
    #     ep_next: float|None = None,
    #     ep_this: float|None = None,
    #     event_points: int|None = None,
    #     form: float|None = None,
    #     id: int|None = None,
    #     points_per_game: float|None = None,
    #     selected_by_percent: float|None = None,
    #     team: int|None = None,
    #     total_points: int|None = None,
    #     transfers_in: int|None = None,
    #     transfers_in_event: int|None = None,
    #     transfers_out: int|None = None,
    #     transfers_out_event: int|None = None,
    #     value_form: float|None = None,
    #     value_season: float|None = None,
    #     minutes: int|None = None,
    #     penalties_missed: int|None = None,
    #     bps: int|None = None,
    #     starts: int|None = None,
    #     influence_rank: int|None = None,
    #     influence_rank_type: int|None = None,
    #     creativity_rank: int|None = None,
    #     creativity_rank_type: int|None = None,
    #     threat_rank: int|None = None,
    #     threat_rank_type: int|None = None,
    #     ict_index_rank: int|None = None,
    #     ict_index_rank_type: int|None = None,
    #     corners_and_indirect_freekicks_order: int|None = None,
    #     corners_and_indirect_freekicks_text: str|None = None,
    #     direct_freekicks_order: int|None = None,
    #     direct_freekicks_text: str|None = None,
    #     penalties_order: int|None = None,
    #     penalties_text: str|None = None,
    #     expected_goals_per_90: float|None = None,
    #     saves_per_90: float|None = None,
    #     expected_assists_per_90: float|None = None,
    #     expected_goal_involvements_per_90: float|None = None,
    #     expected_goals_conceded_per_90: float|None = None,
    #     goals_conceded_per_90: float|None = None,
    #     now_cost_rank: int|None = None,
    #     now_cost_rank_type: int|None = None,
    #     form_rank: int|None = None,
    #     form_rank_type: int|None = None,
    #     points_per_game_rank: int|None = None,
    #     points_per_game_rank_type: int|None = None,
    #     selected_rank: int|None = None,
    #     selected_rank_type: int|None = None,
    #     starts_per_90: float|None = None,
    #     clean_sheets_per_90: float|None = None
    # ):
    #     """
    #     Set the players stats. All arguments are optional
    #     """
    #     if minutes_played is not None:
    #         self.minutes_played = minutes_played
    #     if goals_scored is not None:
    #         self.goals_scored = goals_scored
    #     if assists is not None:
    #         self.assists = assists
    #     if clean_sheets is not None:
    #         self.clean_sheets = clean_sheets
    #     if goals_conceded is not None:
    #         self.goals_conceded = goals_conceded
    #     if own_goals is not None:
    #         self.own_goals = own_goals
    #     if penalties_saved is not None:
    #         self.penalties_saved = penalties_saved
    #     if yellow_cards is not None:
    #         self.yellow_cards = yellow_cards
    #     if red_cards is not None:
    #         self.red_cards = red_cards
    #     if saves is not None:
    #         self.saves = saves
    #     if bonus is not None:
    #         self.bonus = bonus
    #     if bonus_points_system is not None:
    #         self.bonus_points_system = bonus_points_system
    #     if influence is not None:
    #         self.influence = influence
    #     if creativity is not None:
    #         self.creativity = creativity
    #     if threat is not None:
    #         self.threat = threat
    #     if ict_index is not None:
    #         self.ict_index = ict_index
    #     if games_started is not None:
    #         self.games_started = games_started
    #     if expected_goals is not None:
    #         self.expected_goals = expected_goals
    #     if expected_assists is not None:
    #         self.expected_assists = expected_assists
    #     if expected_goal_involvements is not None:
    #         self.expected_goal_involvements = expected_goal_involvements
    #     if expected_goals_conceded is not None:
    #         self.expected_goals_conceded = expected_goals_conceded
    #     if cost_change_event is not None:
    #         self.cost_change_event = cost_change_event
    #     if cost_change_event_fall is not None:
    #         self.cost_change_event_fall = cost_change_event_fall
    #     if cost_change_start is not None:
    #         self.cost_change_start = cost_change_start
    #     if cost_change_start_fall is not None:
    #         self.cost_change_start_fall = cost_change_start_fall
    #     if dreamteam_count is not None:
    #         self.dreamteam_count = dreamteam_count
    #     if element_type is not None:
    #         self.element_type = element_type
    #     if ep_next is not None:
    #         self.ep_next = ep_next
    #     if ep_this is not None:
    #         self.ep_this = ep_this
    #     if event_points is not None:
    #         self.event_points = event_points
    #     if form is not None:
    #         self.form = form
    #     if id is not None:
    #         self.id = id
    #     if points_per_game is not None:
    #         self.points_per_game = points_per_game
    #     if selected_by_percent is not None:
    #         self.selected_by_percent = selected_by_percent
    #     if team is not None:
    #         self.team = team
    #     if total_points is not None:
    #         self.total_points = total_points
    #     if transfers_in is not None:
    #         self.transfers_in = transfers_in
    #     if transfers_in_event is not None:
    #         self.transfers_in_event = transfers_in_event
    #     if transfers_out is not None:
    #         self.transfers_out = transfers_out
    #     if transfers_out_event is not None:
    #         self.transfers_out_event = transfers_out_event
    #     if value_form is not None:
    #         self.value_form = value_form
    #     if value_season is not None:
    #         self.value_season = value_season
    #     if minutes is not None:
    #         self.minutes = minutes
    #     if penalties_missed is not None:
    #         self.penalties_missed = penalties_missed
    #     if bps is not None:
    #         self.bps = bps
    #     if starts is not None:
    #         self.starts = starts
    #     if influence_rank is not None:
    #         self.influence_rank = influence_rank
    #     if influence_rank_type is not None:
    #         self.influence_rank_type = influence_rank_type
    #     if creativity_rank is not None:
    #         self.creativity_rank = creativity_rank
    #     if creativity_rank_type is not None:
    #         self.creativity_rank_type = creativity_rank_type
    #     if threat_rank is not None:
    #         self.threat_rank = threat_rank
    #     if threat_rank_type is not None:
    #         self.threat_rank_type = threat_rank_type
    #     if ict_index_rank is not None:
    #         self.ict_index_rank = ict_index_rank
    #     if ict_index_rank_type is not None:
    #         self.ict_index_rank_type = ict_index_rank_type
    #     if corners_and_indirect_freekicks_order is not None:
    #         self.corners_and_indirect_freekicks_order = corners_and_indirect_freekicks_order
    #     if corners_and_indirect_freekicks_text is not None:
    #         self.corners_and_indirect_freekicks_text = corners_and_indirect_freekicks_text
    #     if direct_freekicks_order is not None:
    #         self.direct_freekicks_order = direct_freekicks_order
    #     if direct_freekicks_text is not None:
    #         self.direct_freekicks_text = direct_freekicks_text
    #     if penalties_order is not None:
    #         self.penalties_order = penalties_order
    #     if penalties_text is not None:
    #         self.penalties_text = penalties_text
    #     if expected_goals_per_90 is not None:
    #         self.expected_goals_per_90 = expected_goals_per_90
    #     if saves_per_90 is not None:
    #         self.saves_per_90 = saves_per_90
    #     if expected_assists_per_90 is not None:
    #         self.expected_assists_per_90 = expected_assists_per_90
    #     if expected_goal_involvements_per_90 is not None:
    #         self.expected_goal_involvements_per_90 = expected_goal_involvements_per_90
    #     if expected_goals_conceded_per_90 is not None:
    #         self.expected_goals_conceded_per_90 = expected_goals_conceded_per_90
    #     if goals_conceded_per_90 is not None:
    #         self.goals_conceded_per_90 = goals_conceded_per_90
    #     if now_cost_rank is not None:
    #         self.now_cost_rank = now_cost_rank
    #     if now_cost_rank_type is not None:
    #         self.now_cost_rank_type = now_cost_rank_type
    #     if form_rank is not None:
    #         self.form_rank = form_rank
    #     if form_rank_type is not None:
    #         self.form_rank_type = form_rank_type
    #     if points_per_game_rank is not None:
    #         self.points_per_game_rank = points_per_game_rank
    #     if points_per_game_rank_type is not None:
    #         self.points_per_game_rank_type = points_per_game_rank_type
    #     if selected_rank is not None:
    #         self.selected_rank = selected_rank
    #     if selected_rank_type is not None:
    #         self.selected_rank_type = selected_rank_type
    #     if starts_per_90 is not None:
    #         self.starts_per_90 = starts_per_90
    #     if clean_sheets_per_90 is not None:
    #         self.clean_sheets_per_90 = clean_sheets_per_90

    def add_news(self, news, news_added):
        self.news.append(News(news, news_added))
