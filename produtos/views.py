from django.http import JsonResponse
from django.shortcuts import render

from .models import Produtos, DataConsulta


def RenderTabela(request):
    return render(request, 'tabela.html')


def formata_data(produto, datas):
    dados = []
    for data in datas:
        try:
            total_vendas = DataConsulta.objects.get(produto=produto, consult_date=data[0]).c
        except:
           total_vendas = 0
        
        dados.append({
            'consult_date': data[0],
            'c': total_vendas
        })
        
    return dados
    

def ListaProdutos(request):
    queryset = Produtos.objects.order_by('product_url')
    datas = set(DataConsulta.objects.order_by('consult_date').values_list('consult_date'))
    json_data = []
    
    for produto in queryset:
        dados = {}
                
        consult_date = formata_data(produto, sorted(datas))
        dados = {
            'product_url': produto.product_url,
            'product_url_created_at': produto.product_url_created_at,
            'total': produto.total_vendas,
            'consult_date': consult_date
        }
        
        json_data.append(dados)
        
    return JsonResponse({'datas': sorted(datas), "recordsTotal": len(json_data), 'dados': json_data})