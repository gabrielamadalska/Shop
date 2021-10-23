from django.db import models

# Create your models here.

class Producer(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Producer"
        verbose_name_plural = "Producers"

class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=25)


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Products(models.Model):

    # zwraca string gdy wywołamy obiekt produktu
    # wyswietla nazwe na stronie
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"



