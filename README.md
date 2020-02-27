  
   ![alt text <>](https://accubits-image-assets.s3-ap-southeast-1.amazonaws.com/currency-converter/currency.png "")


# Currency Converter
[](https://accubits-image-assets.s3-ap-southeast-1.amazonaws.com/currency-converter/currency.png)


A currency convertion utility , which can be used to calculate the forex value of te currency.


## Installation

Install the package with:

`pip install currency-converter`

 ## USAGE

````python
from currency-converter import get_currencies,convert
````

 #### Get Available currencies

````python
from currency-converter import get_currencies

print(get_currencies)


````

#### Conversions

Example : Convert 200 USD to INR

````python
from currency-converter import convert

print(convert('USD','INR',200))


````