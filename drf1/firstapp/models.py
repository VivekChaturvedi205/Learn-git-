from django.db import models

class student(models.Model):
    Name=models.CharField(max_length=15)
    Roll_no=models.IntegerField()
    City=models.CharField(max_length=20)
