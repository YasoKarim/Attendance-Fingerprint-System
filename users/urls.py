from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('about', views.about , name='about')
    ,path('employee' ,views.employee , name='employee')
    ,path('employees', views.employees, name='employees'),
    
    ]   
