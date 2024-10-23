from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


# Importação das views

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('home.urls')),
    path('', include('cadastro_pet.urls')),
    path('admin/', admin.site.urls),
    #As urls abaixo precisa ser descomentadas inclui-la nos seus app, meninas!
    path('', include('detalhes_pet.urls')),
    #  path('gestao_adocao/', include('gestao_adocao.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)