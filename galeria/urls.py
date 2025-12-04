from django.urls import path
from . import views

app_name = 'galeria'

urlpatterns = [
    path('', views.gallery_list, name='gallery_list'),
    path('submit/', views.submit_art, name='submit_art'),
    path('coleccion/<int:pk>/', views.collection_detail, name='collection_detail'),
    path('eliminar/<int:pk>/', views.delete_painting, name='delete_painting'),
]
