from django.urls import path
from . import views

urlpatterns = [
    path('',views.LaptopViewset.as_view(), name='movieView'),
]