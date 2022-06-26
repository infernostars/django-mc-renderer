from django.urls import path

from . import views

urlpatterns = [
    path('generator', views.generator, name='generator'),
]