from .models import React
from django.db.models.signals import post_save
from django.dispatch import receiver
from .monitoring import monitoring


def teste(scheduler):
    @receiver(post_save, sender=React)
    def novo_ativo(sender, **kwargs):

        ativo=kwargs['instance']
        #  scheduler.shutdown(wait=False)

        scheduler.add_job(monitoring,'interval',seconds=ativo.monitor, args=[ativo])




