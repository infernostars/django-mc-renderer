from django.urls import path

from . import views

urlpatterns = [
    path('generator', views.generator, name='generator'),
    path('place', views.place, name='place'),
]