from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import HomePageContent

@admin.register(HomePageContent)
class HomePageContentAdmin(ImportExportModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)
    ordering = ('title',)

    class Meta:
        model = HomePageContent
