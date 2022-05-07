from django.db import models

class Produtos(models.Model):
    product_url = models.URLField(
        max_length=1000
    )
    
    product_url_created_at = models.DateField(
        auto_now_add=True
    )
    
    product_url_image = models.URLField(
        max_length=1000
    )
    
    store_url = models.URLField(
        max_length=1000
    )
    
    consult_date = models.DateField()
    
    total_vendas = models.IntegerField()
    
    class Meta:
        ordering = ['consult_date', 'total_vendas']
        verbose_name_plural = "Produtos" 
        db_table = 'Produto'
        
    def __str__(self):
        return self.product_url
