import requests


class Weather:
    def __init__(self, apikey, city=None, lat=None, lon=None):
        self.apikey = apikey
        self.city = city
        self.lat = lat
        self.lon = lon

        if self.city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={self.apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        elif self.lat and self.lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}" \
                  f"&appid={self.apikey}&units=metric "
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("provide either a city or lat lon arguments")

    def next_12h(self):
        return self.data['list'][:4]

    def next_12h_simplified(self):
        pass


weather = Weather(apikey="26631f0f41b95fb9f5ac0df9a8f43c92", city="Addis Ababa")
print(weather.next_12h())
weather = Weather(apikey="26631f0f41b95fb9f5ac0df9a8f43c92", lat="40.1", lon="3.4")
print(weather.next_12h())
# weather = Weather(apikey="26631f0f41b95fb9f5ac0df9a8f43c92")
# print(weather.next_12h())
