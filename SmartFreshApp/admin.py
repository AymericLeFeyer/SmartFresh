from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Container

# Register your models here.

# admin.site.register(Container)

@admin.register(Container)
class ContainerAdmin(ImportExportModelAdmin):
    pass
