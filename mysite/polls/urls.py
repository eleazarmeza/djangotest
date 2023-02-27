from django.urls import path  #cuando llegues a polls, manda tal vista
from . import views  # el . se refiere al folder actual (parent folder) es decir importa views aqui
# asi tenemos la funcion index disponible aqui



#crea en un path una ruta, es decir, tnemos una ruta home del proyecto
    # cuando llegue a la ruta /polls, va a mandar aqui
    # y aqui indica que to-do lo que este en ese folder raiz ejecutara la funcion index de views
    # aqui debo crear subrutas de polls, es decir subcarpetas


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]