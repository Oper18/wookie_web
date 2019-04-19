from django.shortcuts import render
from .models import ProjectArea, Project

def main(request):
    return render(request, 'mainapp/index.html')

def projects(request, pk=None):
    title = 'Home'
    
    area = ProjectArea.objects.all()
    
    content = {'title': title, 'area': area}
    
    return render(request, 'mainapp/projects.html', content)

def contacts(request):
    return render(request, 'mainapp/contacts.html')
