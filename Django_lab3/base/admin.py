from django.contrib import admin
from base.models import Persons, Druzyna

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['imie', 'miesiac_urodzenia', 'Drużyna']
    list_filter = ['data_dodania','Drużyna']

admin.site.register(Persons, PersonAdmin)

class DruzynaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kraj']
    list_filter = ['kraj']

admin.site.register(Druzyna, DruzynaAdmin)