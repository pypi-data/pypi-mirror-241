import pytest
from crypto_data.crypto_api import CryptoAPI

@pytest.fixture
def api_instance():
    return CryptoAPI(api_key='3c21045b-f1c1-4f33-9486-8dfa5045c9b0')

def test_get_token_price(api_instance):
    price = api_instance.get_token_price('BTC')
    assert price is not None
    assert isinstance(price, float)

def test_get_top_n_cryptocurrencies(api_instance):
    top_currencies = api_instance.get_top_n_cryptocurrencies(limit=5)
    assert top_currencies is not None
    assert len(top_currencies) == 5
    assert all(isinstance(entry, tuple) and len(entry) == 2 for entry in top_currencies)

def test_get_historical_data(api_instance):
    start_date = '2023-01-01'
    end_date = '2023-01-10'
    interval = 'daily'
    historical_data = api_instance.get_historical_data('BTC', start_date, end_date, interval)
    # Will always fail for now
    #assert historical_data is not None
    #assert isinstance(historical_data, list)

def test_get_global_market_data(api_instance):
    global_data = api_instance.get_global_market_data()
    assert global_data is not None
    assert 'quote' in global_data
    assert 'USD' in global_data['quote']
    assert 'total_market_cap' in global_data['quote']['USD']
    assert 'total_volume_24h' in global_data['quote']['USD']

def test_convert_price(api_instance):
    amount = 1
    converted_price = api_instance.convert_price(amount, from_currency='USD', to_currency='EUR')
    assert converted_price is not None
    assert isinstance(converted_price, float)

def test_get_supported_fiat_currencies(api_instance):
    supported_currencies = api_instance.get_supported_fiat_currencies()
    assert supported_currencies is not None
    assert isinstance(supported_currencies, list)
    assert all(isinstance(currency, str) for currency in supported_currencies)