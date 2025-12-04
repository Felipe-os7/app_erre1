from django.urls import path
from . import views

app_name = 'mural'

urlpatterns = [
    path('', views.mural_list, name='mural_list'),
    path('enviar/', views.submit_mural, name='submit_mural'),
    path('enviar/exito/', views.submit_mural_success, name='submit_mural_success'),
    path('cotizacion-estandar/', views.send_standard_mural_quote, name='send_standard_quote'),
    path('cotizacion/', views.mural_quote, name='mural_quote'),
    path('cotizacion/exito/', views.mural_quote_success, name='mural_quote_success'),
    path('eliminar/<int:pk>/', views.delete_mural, name='delete_mural'),
]
