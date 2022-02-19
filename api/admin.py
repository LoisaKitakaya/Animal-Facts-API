from django.contrib import admin
from .models import AnimalFact

# Register your models here.
class AnimalFactAdmin(admin.ModelAdmin):

    list_display = ('animal', 'setup')

admin.site.register(AnimalFact, AnimalFactAdmin)