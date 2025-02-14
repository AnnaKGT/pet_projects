from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://stats.nba.com"
ALL_JSON = "/stats/scoreboard"

printer = PrettyPrinter()

data = get(BASE_URL + ALL_JSON).json()
printer.pprint(data)
