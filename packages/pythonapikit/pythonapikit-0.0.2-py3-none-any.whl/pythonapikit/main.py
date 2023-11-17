import requests

class WeatherAPI:
    def __init__(self, weatherapi_key, location, unit = "c"):
        self.key = weatherapi_key
        self.location = location
        self.unit = unit

    def get_current_temperature(self):
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        if self.response.status_code == 200:
            self.data = self.response.json()
            return self.data['current'][f'temp_{self.unit}']
        else:
            return self.response.status_code()
        
    def get_max_temperature(self):
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        if self.response.status_code == 200:
            self.data = self.response.json()
            return self.data['forecast']['forecastday'][0]['day'][f'maxtemp_{self.unit}']
        else:
            return self.response.status_code()
        
    def get_min_temperature(self):
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        if self.response.status_code == 200:
            self.data = self.response.json()
            return self.data['forecast']['forecastday'][0]['day'][f'mintemp_{self.unit}']
        else:
            return self.response.status_code()
        
    def get_avg_temperature(self):
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        if self.response.status_code == 200:
            self.data = self.response.json()
            return self.data['forecast']['forecastday'][0]['day'][f'avgtemp_{self.unit}']
        else:
            return self.response.status_code()
        
if __name__ == "__main__":
    pass