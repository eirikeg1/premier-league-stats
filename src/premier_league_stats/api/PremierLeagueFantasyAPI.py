import requests

class PremierLeagueFantasyAPI:
    """Class which fetches statistics/data from the Premier League Fantasy API

    Raises:
        Exception: If statuscode is not 200
    """
    
    FANTASY_BASE_URL: str = "https://fantasy.premierleague.com/api/"
    FIXTURES_URL = f"https://onefootball.com/en/competition/premier-league-9/fixtures"
    
    cached_requests = {}


    def fetch_static_json(self, cache=True):
        
        if cache and (cached := self.cached_requests.get('static')):
            request = cached
        else:
            request = requests.get(self.FANTASY_BASE_URL + "bootstrap-static/")

        if request.status_code != 200:
            raise Exception(
                f"Request to import static data failed with status code {request.status_code}"
            )
            
        if cache:
            self.cached_requests['static'] = request
        
        return request.json()
    
    
    def fetch_fixtures_json(self, cache=True):
        
        if cache and (cached := self.cached_requests.get('fixtures')):
            request = cached
        else:
            request = requests.get(self.FANTASY_BASE_URL + 'fixtures/')

        if request.status_code != 200:
            raise Exception(
                f"Request to import static data failed with status code {request.status_code}"
            )
            
        if cache:
            self.cached_requests['fixtures'] = request
        
        return request.json()
    
    
    def fetch_fixtures_by_game_week(self, game_week: int, cache=True):
            
            if cache and (cached := self.cached_requests.get('fixtures')):
                request = cached
            else:
                request = requests.get(f"{self.FIXTURES_URL}/fixtures?event={game_week}")
    
            if request.status_code != 200:
                raise Exception(
                    f"Request to import static data failed with status code {request.status_code}"
                )
                
            if cache:
                self.cached_requests['fixtures'] = request
            
            return request.json()
    
