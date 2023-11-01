from django.apps import AppConfig
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .monitoring import *


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self) -> None:
        from .models import React
        ativos = React.objects.all()
        for ativo in ativos :
            start(ativo)
        




        return super().ready()

def start(ativo):
    scheduler = BackgroundScheduler()
    scheduler.add_job(monitoring,'interval',seconds=ativo.monitor, args=[ativo])
    scheduler.start()
