from django.contrib import admin
from base.models import Persons, Druzyna

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['imie', 'miesiac_urodzenia', 'druzyna']
    list_filter = ('data_dodania','druzyna')

# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Persons, PersonAdmin)

class DruzynaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kraj']
    list_filter = ('kraj')

admin.site.register(Druzyna, DruzynaAdmin)