import requests


class Weather:
    def __init__(self, apikey, city, lat=None, lon=None):
        self.apikey = apikey
        self.city = city
        self.lat = lat
        self.lon = lon

        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.apikey}&units=metric"
        r = requests.get(url)
        self.data = r.json()

    def next_12h(self):
        return self.data

    def next_12h_simplified(self):
        pass


weather = Weather(apikey="26631f0f41b95fb9f5ac0df9a8f43c92", city="Addis Ababa")
print(weather.data)
