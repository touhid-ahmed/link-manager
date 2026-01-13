from django.urls import path, include
from . import views


app_name = 'linktracker'
urlpatterns = [
    
    path('links/', views.list_links, name='list_links'),
    path('links/<int:pk>/', views.detail_links, name='detail_links'),
    path('links/new/', views.create_link, name='create_link'),
]