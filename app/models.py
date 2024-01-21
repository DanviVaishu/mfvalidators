from django.db import models
from django.core import validators
class Student(models.Model):
    SName=models.CharField(max_length=100,primary_key=True)
    SAge=models.IntegerField()
    SMbno=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    def __str__(self):
        return self.SName

