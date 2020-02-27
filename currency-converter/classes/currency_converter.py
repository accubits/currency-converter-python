import requests
import config


class ABCurrencyConv:
    baseURL = config.convertions_url

    def acquireData(self):

        try:
            response = requests.get(self.baseURL)
            data = response.json()

            if "success" in data:
                if data["success"] == True and 'rates' in data:
                    return data['rates']
        except Exception as e:
            print(e)
            return False

    def convert(self, fromCurrency, toCurrency, value):
        print(fromCurrency, toCurrency, value)
        if fromCurrency == toCurrency:
            return value

        data = self.acquireData()

        if data is not False:
            if fromCurrency in data and toCurrency in data:
                return (data[toCurrency] / data[fromCurrency]) * value

            else:
                # doesnt support this currency
                return False

        else:
            return False
