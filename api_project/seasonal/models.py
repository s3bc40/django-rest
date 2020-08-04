from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100, null=True)
    stock = models.IntegerField(null = True, blank=True)

    def __str__(self):
        return self.name
    