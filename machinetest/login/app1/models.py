from django.db import models

# Create your models here.
class Register(models.Model):

    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username