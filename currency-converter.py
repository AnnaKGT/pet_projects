'''
https://www.currencyconverterapi.com/docs
https://free.currconv.com/api/v8/currencies?apiKey=a923a45de7346b8b9504
https://free.currconv.com/api/v8/currencies?apiKey=a923a45de7346b8b9504
'''

from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com"
API_KEY = "a923a45de7346b8b9504"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"/api/v8/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    print.pprint(data)


get_currencies()
