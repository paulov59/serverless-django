from django.contrib import admin

from .models import Produtos

class ProdutosForm(admin.ModelAdmin):
    search_fields = ['product_url']
    search_help_text = 'Busca por url do produto.'
    list_filter = ['consult_date', 'total_vendas']
    list_display = ['product', 'url_created_at', 'vendas']
    
    def product(self, instance):
        return instance.product_url
    
    def url_created_at(self, instance):
        return instance.product_url_created_at
    
    def vendas(self, instance):
        return instance.total_vendas
    
    product.short_description = "Produto"
    url_created_at.short_description = "Data de inserção na loja"
    vendas.short_description = "Total de vendas"
    

admin.site.register(Produtos, ProdutosForm)