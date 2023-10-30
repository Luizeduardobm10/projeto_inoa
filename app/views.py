from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from yahooquery import Ticker
import numpy as np
import pandas as pd
import investpy as inv
# Create your views here.


class ReactView(APIView):
    serializer_class = ReactSerializer 

    df = inv.get_stocks(country = 'brazil' ) 
    #Puxando o nome dos símbolos  
    symbols=df['symbol'].tolist()    
    for i in range(len(symbols)) : 
        symbols[i] = symbols[i] + ".SA"
    #Nome dos ativos
    nome_dos_ativos = df['name'].tolist()
    dict_ativos={}
    #Preenchendo o dataframe
    for i in range(len(nome_dos_ativos)) :
        dict_ativos[nome_dos_ativos[i]]= symbols[i]
    lista_valores=[]
    lista_data=[]
    lista_selecionados=['PETR4.SA','CPF11.SA']

    for i in range(len(lista_selecionados)):

            #Coleta de dados
            ativo = Ticker(lista_selecionados[i]) 
            df_ativo_history=pd.DataFrame(ativo.history(period="7d",  interval = "1m")).reset_index()
            # for column in df_ativo_history.columns :
            #     print(column)
            try : 
                lista_valores.append(df_ativo_history.iloc[-1,df_ativo_history.columns.get_loc('close')])
            except:
                lista_valores.append(-1)
            try : 
                lista_data.append(df_ativo_history.iloc[-1,df_ativo_history.columns.get_loc('date')])
            except:
                lista_data.append(-1)


    
    print(lista_valores)
    print(lista_data)
        #print(pd.DataFrame(ativo.history(period="7d",  interval = "1m")))
    
    def get(self, request):
        output = [{"employee": output.employee, "department": output.department}
                  for output in React.objects.all()]
        return Response(output)

    def post(self, request):

        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
def transform_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
    df = df.round(2)
    df.rename({
        
       'symbol': 'Ticker',
        'date': 'Datetime',
        'open': 'Open',
        'high': 'High',
        'low': 'Low',
        'close'	: 'Close',
        'volume': 'Volume',
    }, axis = 1, inplace = True)