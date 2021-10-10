from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    #zwraca string gdy wywołamy obiekt produktu
    #wyswietla nazwe na stronie
    def __str__(self):
        return self.name
