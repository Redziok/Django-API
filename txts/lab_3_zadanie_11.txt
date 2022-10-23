from base.models import Persons, Druzyna

Persons.objects.all()

Persons.objects.get(id=3)

Persons.objects.filter(imie__startswith='Z')

Persons.objects.values_list('Drużyna').distinct()

Druzyna.objects.all().order_by('-nazwa')

Persons.objects.create(imie = 'Marek', nazwisko = 'Stachurski', miesiac_urodzenia = '1', Drużyna = Druzyna.objects.get(id=1))