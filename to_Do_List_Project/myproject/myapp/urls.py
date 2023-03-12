from django.urls import path
from . import views

urlpatterns= [
    path('', views.readFile),
    path('write', views.writeFile),
    #path ('notes', views.notes),


]










