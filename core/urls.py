from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('news/submit/', views.news_submit, name='news_submit'),
    path('news/submit/success/', views.news_submit_success, name='news_submit_success'),
    path('news/eliminar/<int:pk>/', views.delete_news, name='delete_news'),
]
