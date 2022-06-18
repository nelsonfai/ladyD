from email import message

from django.db import models
from django.forms import FileField
import datetime


# Create your models here.
class Pictures (models.Model):
    name=models.CharField( default="Null-value",max_length=100)
    image=models.FileField(default='default.png',blank=True)
    date=datetime.datetime.now()




class Services(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    service_image=models.FileField(default='default.png',blank=True)
    date=datetime.datetime.now()
    




    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email= models.EmailField()
    subject=models.TextField()
    message=models.TextField()
    
   
    
    def __str__(self):
        date=datetime.datetime.now()
        return   self.subject +  '  from: '+ '[ '+ self.name +']'  #+ date.strftime("%a, %d %b %Y  %H:%M ")




