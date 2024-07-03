import requests

class PremierLeagueFantasyAPI:
    FANTASY_BASE_URL: str = "https://fantasy.premierleague.com/api/"
    FIXTURES_URL = f"https://onefootball.com/en/competition/premier-league-9/fixtures"


    def fetch_json(self):
        request = requests.get(self.FANTASY_BASE_URL + "bootstrap-static/")

        if request.status_code != 200:
            raise Exception(
                f"Request to import static data failed with status code {request.status_code}"
            )
        return request.json()