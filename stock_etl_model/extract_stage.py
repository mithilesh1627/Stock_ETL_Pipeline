import requests

class Extract:
    def Extract_stage(self,Symbol,Password):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={Symbol}&outputsize=full&apikey={Password}'
        r = requests.get(url)
        return r.json()
