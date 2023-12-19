from django.urls import path
from recipes.views import home, contato, sobre


urlpatterns = [
    path('', home), #rota raiz
    path('sobre/', sobre), #rota sobre
    path('contato/', contato), #rota contato
]