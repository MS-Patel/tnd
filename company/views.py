from django.core import mail
from django.shortcuts import render
from django.core.mail import send_mail
from random import randint
from django.conf import settings
from.models import *


# Create your views here.
def index(request):
    return render(request,"company/index.html")

def contactus(request):
   
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name)

        send_mail("WEbsite ENQUIRY",message, email ,['Kinjal17baisa@gmail.com'])
        return render(request,"company/index.html")
    else:
        return render(request,"company/contactus.html")

def aboutus(request):
    return render(request,"company/aboutus.html")

def products(request):
    return render(request,"company/products.html")

def certificates(request):
    return render(request,"company/certificates.html")