from django.urls import path

from . import views

app_name = 'furnitureapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('scrap_furniture/', views.scrap_furniture, name='scrap_furniture'),
]
