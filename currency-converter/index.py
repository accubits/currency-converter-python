from classes import currency_converter

converter = currency_converter.ABCurrencyConv()


def get_currencies():
    try:
        data = converter.acquireData()
        currencies = list(data)
        return currencies

    except Exception as e:
        print(e)
        return False


def convert(from_currency, to_currency, value):
    try:
        data = converter.convert(from_currency, to_currency, value)
        return data
    except Exception as e:
        print(e)
        return False

