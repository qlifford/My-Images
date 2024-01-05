from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name = 'index'),
    path('delete/<str:pk>', delete_image, name = 'delete'),
    path('details/<str:pk>', detail, name = 'details'),
]
