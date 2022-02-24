from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.homeIndex, name='homeIndex'),
    path('success/', views.success_payment, name='success_payment'),
]