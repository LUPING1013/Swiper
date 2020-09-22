from django.db import models

# Create your models here.
class User(models.Model):
    phonenum = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32)
    gender=models.BooleanField(default=True)
    birthday=models.DateField(auto_now=True)
    avatar=models.ImageField()
    location=models.CharField(max_length=32,default='北京')

    class Meta:
        db_table='user'

