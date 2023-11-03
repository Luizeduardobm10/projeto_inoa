from django.conf import settings
import json

def monitoring(ativo):
    print(ativo.symbol)
    if ativo.high > ativo.max:
        print(ativo.symbol + " sell")
    if ativo.low < ativo.min:
        print(ativo.symbol + " buy")






