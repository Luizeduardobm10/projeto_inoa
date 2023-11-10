from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from backend.settings import EMAIL_HOST_USER

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self) -> None:
        #Criação do scheduler
        scheduler = BackgroundScheduler()
        #Criação dos schedulers por tempo de monitoramento
        for monitor in [1, 5 ,10,30,60] :
            start_scheduler(scheduler,monitor)
        scheduler.start()

        return super().ready()

#Função de monitoramento dos ativos
def monitoring(monitor):
    from .models import React
    #Get dos ativos do banco
    ativos = React.objects.filter(monitor__in = [monitor])
    #Lista de destinatários
    recipient_list=['luizeduardobm00@gmail.com']
    #Assunto do email
    subject="Monitoramento de ativos"
    for ativo in ativos :
        if ativo.high > ativo.max:
            "Mensagem de Compra de Ativo"
            message = ativo.symbol + "SELL"
            "Envio do email"
            send_mail(subject,message,EMAIL_HOST_USER,recipient_list,fail_silently=True)
        if ativo.low < ativo.min:
            "Mensagem de email de Venda de Ativo"
            message = ativo.symbol + "BUY"
            "Envio do email"
            send_mail(subject,message,EMAIL_HOST_USER,recipient_list,fail_silently=True)


#Start Schedulers
def start_scheduler(scheduler, monitor):
    scheduler.add_job(monitoring,'interval',minutes=monitor, args=[monitor])

