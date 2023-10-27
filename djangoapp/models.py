from django.db import models

# Create your models here.
class Candidate(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    # def __str__(self):
    #     return self.name

class Education(models.Model):
    course=models.CharField(max_length=30)
    university=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    reg_id=models.ForeignKey(Candidate,on_delete=models.CASCADE)

class todo(models.Model):
    player=models.CharField(max_length=30)
    club=models.CharField(max_length=30)
    value=models.CharField(max_length=30)
    # def __str__(self):
    #     return self.name
   