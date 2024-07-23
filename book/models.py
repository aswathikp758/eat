from django.db import models

# Create your models here.
class booking(models.Model):
    name = models.CharField(max_length=100)
    number=models.CharField(max_length=11)
    persons=models.CharField(max_length=2)
    date=models.CharField(max_length=10)
    time = models.CharField(max_length=10)

    def __str__(self):
        return self.name