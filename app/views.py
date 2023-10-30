from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from yahooquery import Ticker
import numpy as np
import pandas as pd
import investpy as inv
import datetime
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
    lista_selecionados=['Banco BTG Pactual Pref','PETROBRAS PN']
    lista_symbol_selecionados =[]
    for i in range(len(lista_selecionados)):
        lista_symbol_selecionados.append(dict_ativos[lista_selecionados[i]])
 
    for i in range(len(lista_selecionados)):

            #Coleta de dados
            ativo = Ticker(lista_symbol_selecionados[i]) 
            df_ativo_history=pd.DataFrame(ativo.history(period="7d",  interval = "1m")).reset_index()
            # df_ativo_history.sort_values(by=['date'], ascending=False)
            print(df_ativo_history)

            # for column in df_ativo_history.columns :
            #     print(column)
            print(df_ativo_history.iloc[-1,df_ativo_history.columns.get_loc('close')])
            try : 
                lista_valores.append(df_ativo_history.iloc[-1,df_ativo_history.columns.get_loc('close')])
            except:
                lista_valores.append(datetime(2000, 10, 25, 00, 00, 00))
            try : 
                lista_data.append(df_ativo_history.iloc[-1,df_ativo_history.columns.get_loc('date')].to_pydatetime().strftime("%Y-%m-%d %H:%M:%S"))
            except:
                lista_data.append(datetime(2000, 10, 25, 00, 00, 00))


    
    print(lista_valores)
    print(lista_data)
        #print(pd.DataFrame(ativo.history(period="7d",  interval = "1m")))

    React.objects.all().delete()
    React.objects.all()
    for i in range(len(lista_selecionados)):
        React.objects.create(symbol=lista_symbol_selecionados[i],name=lista_selecionados[i],actual_price=lista_valores[i],date=lista_data[i])

    

    
    def get(self, request):
        output = [{"employee": output.employee, "department": output.department}
                  for output in React.objects.all()]
        return Response(output)

    def post(self, request):

        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)