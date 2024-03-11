from abc import ABC, abstractmethod
import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# abstract data service class that we will use for the mock data and api calling classes
class AbstractDataService(ABC):
    @abstractmethod
    def getWeatherForecast(self):
        pass

    #have a fake data service for testing data should resemble the predicted data from the api
    #have the api calling service make
    #data source calls api service, verifies that the data is what we expect and return data to wherever we want it


# mock data service returning the only two 
class MockedDataService(AbstractDataService):
    def getWeatherForecast(self):
        return {
            "temperature_2m_max": 67,
            "temperature_2m_min": 45
        }
    

# api calling service
class APICallingService(AbstractDataService):
    def __init__(self):
        self.cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        self.retry_session = retry(self.cache_session, retries = 5, backoff_factor = 0.2)
        self.openmeteo = openmeteo_requests.Client(session = self.retry_session)
    def getWeatherForecast(self):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
	        "latitude": 37.3022,
	        "longitude": -120.483,
	        "daily": ["temperature_2m_max", "temperature_2m_min"],
	        "temperature_unit": "fahrenheit",
	        "timezone": "America/Los_Angeles",
	        "forecast_days": 1
        }
        responses = self.openmeteo.weather_api(url, params=params)
        response = responses[0]
        daily = response.Daily()
        daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()

        daily_data = {"date": pd.date_range(
	    start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	    end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	    freq = pd.Timedelta(seconds = daily.Interval()),
	    inclusive = "left"
        )}
        daily_data["temperature_2m_max"] = daily_temperature_2m_max
        daily_data["temperature_2m_min"] = daily_temperature_2m_min

        daily_dataframe = pd.DataFrame(data = daily_data)
        
        max_temp = daily_dataframe['temperature_2m_max'].iloc[0]

        min_temp = daily_dataframe['temperature_2m_min'].iloc[0]


        temperature_dict = {
            "temperature_2m_max": max_temp,
            "temperature_2m_min": min_temp
        }
        return temperature_dict
    
class DataSourceHandler:
    def __init__(self, service: AbstractDataService):
        self.service = service

    def get_data(self):
        
        data = self.service.getWeatherForecast()

        if not self._validate_data(data):
            raise ValueError("Data is not in the expected format.")
        
        return data

    def _validate_data(self, data):
        required_keys = ['temperature_2m_max', 'temperature_2m_min']
        if not isinstance(data, dict):
            return False
        return all(key in data for key in required_keys)





        

        












