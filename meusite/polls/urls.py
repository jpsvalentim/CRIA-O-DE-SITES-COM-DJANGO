from django.urls import paths

from . import views
from ..meusite.urls import urlpatterns

urlpatterns = [

    path('',views.index, name ='index')
]