from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from produtos.views import ListaProdutos, RenderTabela

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RenderTabela),
    path('dados/', ListaProdutos, name='order_list_json'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)