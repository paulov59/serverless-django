from django.db import models

class Produtos(models.Model):
    product_url = models.URLField(
        primary_key=True,
        max_length=1000
    )
    
    product_url_created_at = models.DateField()
    
    product_url_image = models.URLField(
        max_length=1000
    )
    
    store_url = models.URLField(
        max_length=1000
    )
        
    total_vendas = models.IntegerField(
        default=0
    )
    
    class Meta:
        ordering = ['product_url']
        verbose_name_plural = "Produtos" 
        db_table = 'Produto'
        
    def __str__(self):
        return self.product_url


class DataConsulta(models.Model):
    produto = models.ForeignKey(
        Produtos,
        on_delete=models.CASCADE,
        db_constraint=False
    )
    
    consult_date = models.DateField()
    
    c = models.IntegerField()
    
    class Meta:
        ordering = ['consult_date']
        verbose_name_plural = "Data de Consulta" 
        db_table = 'DataConsulta'
        
    def __str__(self):
        return str(self.consult_date)