from django.db import models

# Create your models here.
class reg(models.Model):
    name=models.CharField(max_length=50,default='not available')
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=12)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name


