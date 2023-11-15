import requests
import time

class CryptoAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://pro-api.coinmarketcap.com/v1/'
        self.rate_limit_reset = None
        self.rate_limit_remaining = None

    def _check_rate_limit(self):
        # Check rate limit and wait if necessary
        if self.rate_limit_reset and self.rate_limit_remaining == 0:
            wait_time = max(self.rate_limit_reset - time.time(), 0) + 1
            print(f'Rate limit exceeded. Waiting for {wait_time:.2f} seconds...')
            time.sleep(wait_time)

    def _update_rate_limit(self, headers):
        # Update rate limit information
        if 'X-RateLimit-Reset' in headers:
            self.rate_limit_reset = float(headers['X-RateLimit-Reset'])
        if 'X-RateLimit-Remaining' in headers:
            self.rate_limit_remaining = int(headers['X-RateLimit-Remaining'])

    def get_token_price(self, symbol):
        endpoint = 'cryptocurrency/quotes/latest'
        url = f'{self.base_url}{endpoint}'
        headers = {
            'X-CMC_PRO_API_KEY': self.api_key,
        }
        params = {
            'symbol': symbol,
        }

        self._check_rate_limit()
        response = requests.get(url, headers=headers, params=params)
        self._update_rate_limit(response.headers)

        data = response.json()

        if response.status_code == 200:
            # Assuming the symbol is valid
            token_data = data['data'][symbol]
            return token_data['quote']['USD']['price']
        else:
            print(f"Error: {data['status']['error_message']}")
            return None

    def get_top_n_cryptocurrencies(self, limit=10):
        endpoint = 'cryptocurrency/listings/latest'
        url = f'{self.base_url}{endpoint}'
        headers = {
            'X-CMC_PRO_API_KEY': self.api_key,
        }
        params = {
            'limit': limit,
        }

        self._check_rate_limit()
        response = requests.get(url, headers=headers, params=params)
        self._update_rate_limit(response.headers)

        data = response.json()

        if response.status_code == 200:
            top_currencies = data['data']
            return [(entry['symbol'], entry['quote']['USD']['price']) for entry in top_currencies]
        else:
            print(f"Error: {data['status']['error_message']}")
            return None

    def get_historical_data(self, symbol, start_date, end_date, interval='daily'):
        endpoint = 'cryptocurrency/ohlcv/historical'
        url = f'{self.base_url}{endpoint}'
        headers = {
            'X-CMC_PRO_API_KEY': self.api_key,
        }
        params = {
            'symbol': symbol,
            'time_start': start_date,
            'time_end': end_date,
            'interval': interval,
        }

        self._check_rate_limit()
        response = requests.get(url, headers=headers, params=params)
        self._update_rate_limit(response.headers)

        data = response.json()

        if response.status_code == 200:
            historical_data = data['data']
            return historical_data
        else:
            print(f"Error: {data['status']['error_message']}")
            return None

    def get_global_market_data(self):
        endpoint = 'global-metrics/quotes/latest'
        url = f'{self.base_url}{endpoint}'
        headers = {
            'X-CMC_PRO_API_KEY': self.api_key,
        }

        self._check_rate_limit()
        response = requests.get(url, headers=headers)
        self._update_rate_limit(response.headers)

        data = response.json()

        if response.status_code == 200:
            global_data = data['data']
            return global_data
        else:
            print(f"Error: {data['status']['error_message']}")
            return None

    def convert_price(self, amount, from_currency='USD', to_currency='EUR'):
        endpoint = 'tools/price-conversion'
        url = f'{self.base_url}{endpoint}'
        headers = {
            'X-CMC_PRO_API_KEY': self.api_key,
        }
        params = {
            'amount': amount,
            'symbol': from_currency,
            'convert': to_currency,
        }

        self._check_rate_limit()
        response = requests.get(url, headers=headers, params=params)
        self._update_rate_limit(response.headers)

        data = response.json()

        if response.status_code == 200:
            converted_price = data['data']['quote'][to_currency]['price']
            return converted_price
        else:
            print(f"Error: {data['status']['error_message']}")
            return None

    def get_supported_fiat_currencies(self):
        endpoint = 'fiat/map'
        url = f'{self.base_url}{endpoint}'
        headers = {
            'X-CMC_PRO_API_KEY': self.api_key,
        }

        self._check_rate_limit()
        response = requests.get(url, headers=headers)
        self._update_rate_limit(response.headers)

        data = response.json()

        if response.status_code == 200:
            fiat_currencies = [entry['symbol'] for entry in data['data']]
            return fiat_currencies
        else:
            print(f"Error: {data['status']['error_message']}")
            return None