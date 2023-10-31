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
from . form import AtivoForm
from ast import literal_eval
# Create your views here.

# def save_form(request):
#     form = AtivoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form':form
#     }
#     return render(request,"Home.js",context)


class ReactView(APIView):
    serializer_class = ReactSerializer 

    
    def get(self, request):
        output = [{"symbol": output.symbol, "name": output.name, "actual_price": output.actual_price, "date": output.date}
                  for output in React.objects.all()]
        return Response(output)

    def post(self, request):
        var=False
        lista_data =[]
        form =React()
        form.symbol = literal_eval(request.body.decode('utf-8'))["symbol"]
        #get name, date and actual_price
        lista_data = get_stock_data(form.symbol, form)

        form.name = dict
        print(form.symbol)
        print(form.name)
        print(form.date)
        print(form.actual_price)
        if var==True:
            form.save()
        else :
            print("selva")
        context = {
            'form':form
        }

        # # return render(request,"Home.js",context)
        # serializer = ReactSerializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        # return Response(serializer.data)
        return Response("ok")
    
def get_stock_data(symbol, form):
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


        #get sql data
        stock_data = React.objects.values()
        lista_symbols = list(React.objects.values_list("symbol"))
        print(lista_symbols)
        for i in range(len(stock_data)):
            if symbol in lista_symbols :

                 pass
            else:
                #get name
                form.name = dict_ativos[symbol]
                ativo = Ticker(symbol) 
                df_ativo_history=pd.DataFrame(ativo.history(period="7d",  interval = "1m")).reset_index()

                try : 
                    form.actual_price = df_ativo_history.iloc[-1,df_ativo_history.columns.get_loc('close')]
                except:
                    form.actual_price = -1
                try : 
                    form.date = df_ativo_history.iloc[-1,df_ativo_history.columns.get_loc('date')].to_pydatetime().strftime("%Y-%m-%d %H:%M:%S")
                except:
                    form.date = datetime.datetime(2000, 10, 25, 00, 00, 00)
                
                React.objects.all()
                React.objects.create(symbol=form.symbol,name=form.name,actual_price=form.actual_price,date=form.date)
                break
