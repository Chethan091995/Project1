from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=20)
    def __str__(self):
        return self.title
    
class Employ(models.Model):
    Fullname = models.CharField(max_length=200)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=20)
    post = models.ForeignKey(Position,on_delete=models.CASCADE)