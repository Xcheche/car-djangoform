from django.db import models


# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review = models.CharField(max_length=500)

    def __str__(self):
        return self.name
