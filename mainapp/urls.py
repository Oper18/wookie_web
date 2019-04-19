from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.projects, name='index'),
    path('<int:pk>/', mainapp.projects, name='projects'),
]
