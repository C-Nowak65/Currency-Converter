'''Imports'''
import requests
import os

API_KEY = os.getenv('EXCHANGE_RATES_API_KEY')
if not API_KEY:
    print("Error: API Key not found. Please set the the EXCHANGE_RATES_API_KEY environment varibale. ")
BASE_URL = 'http://api.exchangeratesapi.io/v1/'

def get_supported_currencies():
    '''Fetches the list of supported currencies from exchangeratesapi.io.'''
    url = f'{BASE_URL}symbols?access_key={API_KEY}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['symbols']
        else:
            print(f'Error: Unable to fetch symbols, status code: {response.status_code}')
            return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

def get_exchange_rates(source_currency, target_currency):
    url = f'{BASE_URL}latest?access_key={API_KEY}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            rates = data['rates']

            # Direct conversion if either source or target currency is EUR
            if source_currency == 'EUR':
                return rates.get(target_currency, None)
            if target_currency == 'EUR':
                return 1 / rates.get(source_currency, None)

            # Indirect conversion for other currencies
            if source_currency in rates and target_currency in rates:
                rate_from_source_to_EUR = 1 / rates[source_currency]
                rate_from_EUR_to_target = rates[target_currency]
                calculated_rate = rate_from_source_to_EUR * rate_from_EUR_to_target
                return calculated_rate
            else:
                print("One or both currency codes not found.")
                return None
        else:
            print(f'Error: Unable to fetch data, status code: {response.status_code}')
            return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None





