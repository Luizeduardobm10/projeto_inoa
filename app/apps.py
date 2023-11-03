from django.apps import AppConfig
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .monitoring import *    

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self) -> None:
        from .models import React
        from .receiver import teste
        scheduler = BackgroundScheduler()

        for monitor in [1, 5 ,10] :
            start_scheduler(scheduler,monitor)
        scheduler.start()


        return super().ready()

def monitoring(monitor):
    from .models import React
    ativos = React.objects.filter(monitor__in = [monitor])
    for ativo in ativos :
        if ativo.high > ativo.max:
            print(ativo.symbol + " sell")
        if ativo.low < ativo.min:
            print(ativo.symbol + " buy")



def start_scheduler(scheduler, monitor):
    scheduler.add_job(monitoring,'interval',seconds=monitor, args=[monitor])

