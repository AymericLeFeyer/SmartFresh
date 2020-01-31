from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import admin
from .models import Container, Score
from django import forms

# Register your models here.

# admin.site.register(Container)

@admin.register(Container, Score)
class ContainerAdmin(ImportExportModelAdmin):   
    pass

