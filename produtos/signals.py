from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

from .models import DataConsulta, Produtos

@receiver(post_save, sender=DataConsulta)
def atualiza_total_vendas(sender, instance, **kwargs):
    datas = DataConsulta.objects.filter(produto=instance.produto)
    
    total = 0
    for data in datas:
        total += data.c
        
    Produtos.objects.filter(product_url=instance.produto.product_url).update(total_vendas=total)
