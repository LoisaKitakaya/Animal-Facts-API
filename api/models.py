from django.db import models

# Create your models here.
class AnimalFact(models.Model):

    animal = models.CharField(max_length=100)
    image_url = models.URLField(max_length=250)
    setup = models.CharField(max_length=250)
    delivery = models.TextField()

    def __str__(self):
        return self.animal