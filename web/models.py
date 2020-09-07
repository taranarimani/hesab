from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    text= models.CharField(max_length=110)
    date= models.DateField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Income(models.Model):
    text= models.CharField(max_length=110)
    date= models.DateField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
