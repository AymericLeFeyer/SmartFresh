from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Container, Score, LotBloque, Francite


# Register your models here.

# admin.site.register(Container)

@admin.register(Container, Score, LotBloque, Francite)
class ContainerAdmin(ImportExportModelAdmin):
    pass
