from django.db import models

# Create your models here.
class Item(models.Model):

    name = models.CharField(max_length=30, blank=False) # will allow text based input
    done = models.BooleanField(blank=False, default=False) # definition of how our table will look

    def __str__(self):
        return self.name #shows name of item