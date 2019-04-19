# coding: utf-8

from django.core.management.base import BaseCommand
from mainapp.models import ProjectArea, Project
from django.contrib.auth.models import User

import json, os

JSON_PATH = 'mainapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        areas = load_from_json('areas')

        ProjectArea.objects.all().delete()
        for area in areas:
            new_area = ProjectArea(**area)
            new_area.save()

        projects = load_from_json('projects')

        Project.objects.all().delete()
        for project in projects:
            area_name = project["area_name"]
            # Получаем категорию по имени
            _area = ProjectArea.objects.get(name=area_name)
            # Заменяем название категории объектом
            project['area'] = _area
            new_project = Project(**project)
            new_project.save()

        # Создаем суперпользователя при помощи менеджера модели
        # super_user = User.objects.create_superuser('wookie', 'wookie@email.net', 'wookie_pass')
