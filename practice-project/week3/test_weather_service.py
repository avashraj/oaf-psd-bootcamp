import pytest
from thirdtask import MockedDataService, APICallingService, DataSourceHandler

# Test the MockedDataService
def test_mocked_data_service():
    service = MockedDataService()
    data = service.getWeatherForecast()
    assert 'temperature_2m_max' in data
    assert 'temperature_2m_min' in data
    assert data['temperature_2m_max'] == 67
    assert data['temperature_2m_min'] == 45

# Test the APICallingService

def test_api_calling_service():
    service = APICallingService()
    data = service.getWeatherForecast()
    assert 'temperature_2m_max' in data
    assert 'temperature_2m_min' in data
   


def test_data_source_handler_with_mocked_service():
    mocked_service = MockedDataService()
    handler = DataSourceHandler(mocked_service)
    data = handler.get_data()
    assert 'temperature_2m_max' in data
    assert 'temperature_2m_min' in data
    assert data['temperature_2m_max'] == 67
    assert data['temperature_2m_min'] == 45


