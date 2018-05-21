from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField(primary_key=True,max_length=30)
    password=models.CharField(max_length=10)
    mobile=models.IntegerField()
    qstn=models.CharField(max_length=45)
    ans=models.CharField(max_length=45)