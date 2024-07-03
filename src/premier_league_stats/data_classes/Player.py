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
    
    def add_news(self, news, news_added):
        self.news.append(News(news, news_added))
