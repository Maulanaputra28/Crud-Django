from django.db import models

# Create your models here.
class users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50)

