from django.db import models

class ProjectArea(models.Model):
    name_area = models.CharField(verbose_name='name_area', max_length=64, unique=True)
    description = models.TextField(verbose_name='description', blank=True)

    def __str__(self):
        return self.name_area

class Project(models.Model):
    category = models.ForeignKey(ProjectArea, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='project_name', max_length=128)
    description = models.TextField(verbose_name='description', blank=True)
    links = models.TextField(verbose_name='links_to_project', blank=True)
    image = models.ImageField(upload_to='project_images', blank=True)

    def __str__(self):
        return f"{self.name} ({self.category.name_area})"
