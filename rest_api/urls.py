from django.urls import path
from rest_api.views import hello_world
from . import views
from rest_framework.routers import SimpleRouter
from rest_api.views import PetModelViewSet

app_name = 'rest_api'
router = SimpleRouter(trailing_slash=False)
router.register('pet', PetModelViewSet)  

urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world_api'),
]


urlpatterns += router.urls  


