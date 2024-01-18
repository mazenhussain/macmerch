import sys

def parseArguments():
    arguments = {
        "price": sys.argv[1],
        "quantity": 1,
        "province": "ON"
    }
    return arguments

def taxRate(province):
    tax = {
        "ON":0.13
    }

    return tax[province]

def mcmerchCalculator():
    arguments = parseArguments()
    tax = taxRate("ON")
    print(arguments['price'] * arguments['quantity'] * (1 + tax))

mcmerchCalculator()
 

