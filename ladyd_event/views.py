from django.forms import DateTimeField
from django.shortcuts import render
from .models import Pictures,Services,Contact
import datetime

# Create your views here.
def index(request):
    service=Services.objects.all()
    if request.method=="POST":
        contact=Contact() 
        name=request.POST.get('fname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        date=datetime.datetime.now()
        

        contact.name=name
        contact.subject=subject
        contact.email=email
        contact.message=message
        contact.date=date
        contact.save()
        

    
    return render(request,'index.html' ,{'service':service})

def about(request):
    return render(request,'about.html')
  
