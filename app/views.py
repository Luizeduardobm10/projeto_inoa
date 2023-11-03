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
from ast import literal_eval
from datetime import datetime


class ReactView(APIView):
    serializer_class = ReactSerializer 

    def get(self, request):
        output = [{"symbol": output.symbol, "name": output.name, "actual_price": output.actual_price, "date": output.date,"monitor": output.monitor,"low":output.low,"high":output.high,"min":output.min,"max":output.max}
                  for output in React.objects.all()]                
        return Response(output)

    def post(self, request):
        form =React()
        #Armazenamento dos valores vindos do backend
        form.symbol = literal_eval(request.body.decode('utf-8'))["symbol"]
        form.monitor = literal_eval(request.body.decode('utf-8'))["monitor"]
        form.min = literal_eval(request.body.decode('utf-8'))["min"]
        form.max = literal_eval(request.body.decode('utf-8'))["max"]
        #Chama função para post dos dados vindos do frontend no database
        post_stock_data(form.symbol, form)
    


def post_stock_data(symbol, form):
        
        #GET dos dados do banco
        stock_data = React.objects.values()
        lista_symbols = list(React.objects.values_list("symbol"))
        #Loop de verificação se o ativo já está sendo monitorado
        if len(stock_data) !=0:
            for i in range(len(stock_data)):
                if symbol in lista_symbols :
                    pass
                else:
                #Criação do form para o form no database
                    create_form(form)
                    #POST
                    React.objects.create(symbol=form.symbol,name=form.name,actual_price=form.actual_price,date=form.date,monitor=form.monitor,low=form.low,high=form.high,min=form.min,max=form.max)
                    break
        else:
            #Criação do form para o form no database
            create_form(form)
            #POST
            React.objects.create(symbol=form.symbol,name=form.name,actual_price=form.actual_price,date=form.date,monitor=form.monitor,low=form.low,high=form.high,min=form.min,max=form.max)



def create_form (form) :

    #get stocks
    df = inv.get_stocks(country = 'brazil' ) 
    #Puxando o nome dos símbolos  
    symbols=df['symbol'].tolist()    
    for i in range(len(symbols)) : 
        symbols[i] = symbols[i] + ".SA"
    #Nome dos ativos
    nome_dos_ativos = df['name'].tolist()
    dict_ativos={}
    #Preenchendo o dict
    for i in range(len(nome_dos_ativos)) :
        dict_ativos[symbols[i]]= nome_dos_ativos[i]
    #filling the form with the data to send to database
    form.name = dict_ativos[form.symbol]
    ativo = Ticker(form.symbol) 
    df_ativo_history=pd.DataFrame(ativo.history(period="7d",  interval = "1m")).reset_index()
    try : 
        form.actual_price = df_ativo_history.iloc[-1,df_ativo_history.columns.get_loc('close')]
    except:
        form.actual_price = -1
    try : 
        form.low = df_ativo_history.iloc[-1,df_ativo_history.columns.get_loc('low')]
    except:
        form.low = -1
    try : 
        form.high = df_ativo_history.iloc[-1,df_ativo_history.columns.get_loc('high')]
    except:
        form.high = -1
    try : 
        form.date = df_ativo_history.iloc[-1,df_ativo_history.columns.get_loc('date')].to_pydatetime().strftime("%Y-%m-%d %H:%M:%S")
    except:
        form.date = datetime.datetime(2000, 10, 25, 00, 00, 00)

