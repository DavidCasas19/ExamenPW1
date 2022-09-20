from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.menu,name='menu'),
    path('registerP/',views.Jugador_Form,name='Jugador_insert'),
    path('<int:id>/',views.Jugador_Form,name='Jugador_update'),
    path('deleteP/<int:id>/',views.Jugador_delete,name='Jugador_delete'),
    path('listP/',views.Jugador_List,name='Jugador_list'),
    path('listT/',views.Equipo_list,name='Equipo_list'),
    path('registerT/',views.Equipo_form,name='Equipo_insert'),
    path('updateT/<int:id>/',views.Equipo_form,name='Equipo_update'),
    path('deleteT/<int:id>/',views.Equipo_delete,name='Equipo_delete'),
    path('registerE/',views.Estadio_form,name='Estadio_insert'),
    path('listE/',views.Estadio_list,name='Estadio_list'),
    path('updateE/<int:id>/',views.Estadio_form,name='Estadio_update'),
    path('deleteE/<int:id>/',views.Estadio_delete,name='Estadio_delete'),
]