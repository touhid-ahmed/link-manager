from django.urls import path, include
from . import views


app_name = 'linktracker'
urlpatterns = [
    
    path('', views.home, name='home'),
    path('links/', views.list_links, name='list_links'),
    path('links/<int:pk>/', views.detail_links, name='detail_links'),
    path('links/new/', views.create_link, name='create_link'),
    path('links/update/<int:pk>/', views.update_link, name='update_link'),
    path('links/delete/<int:pk>/', views.delete_link, name='delete_link'),

]