from django.db import models

# Create your models here.
class School(models.Model):
    sName=models.CharField(max_length=100,primary_key=True)
    sLocation=models.CharField(max_length=100)
    Principal=models.CharField(max_length=100)
    def __str__(self):
        return self.sName
class University(models.Model):
    uName=models.CharField(max_length=100,primary_key=True)
    uLocation=models.CharField(max_length=100)
    Principal=models.ForeignKey(School,on_delete=models.CASCADE) 
    def __str__(self):
        return self.uName   
    
   

    

 
