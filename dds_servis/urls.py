
from django.contrib import admin
from django.urls import path
from serv import views

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('create/', views.create_record, name='create_record')
]
