from django.core.management.base import BaseCommand

from .database import data
from produtos.models import Produtos, DataConsulta


class Command(BaseCommand):
    help = 'add instance in db'
    def handle(self, *args, **options):
        queryset = Produtos.objects.all()
        
        #populando banco
        if not queryset:
            for prod in data:
                try:
                    produto = Produtos.objects.get(product_url=prod['product_url'])
                    
                except:
                    produto = Produtos.objects.create(
                        product_url=prod['product_url'],
                        product_url_created_at = prod['product_url_created_at'],
                        product_url_image = prod['product_url_image'],
                        store_url = prod['store_url']
                    )
                    
                DataConsulta.objects.create(
                    produto=produto,
                    consult_date=prod['consult_date'],
                    c=prod['c']
                )