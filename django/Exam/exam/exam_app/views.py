from django.shortcuts import render, HttpResponse, redirect
from .models import Sasquatch
from django.contrib import messages
from .models import *
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'forms.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value) 
        return redirect('/')
    fName = request.POST['first_name']
    lName = request.POST['last_name']
    email =  request.POST['email']
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    conPassword = request.POST['confrim_password']
    new_user = User.objects.create(firstName = fName, lastName = lName, email = email, password = pw_hash)
    request.session['id']  = new_user.id
    return redirect('/success')

def success(request):
    if "id" in request.session:
        user = User.objects.get(id = request.session['id'])
        context = {
            "user" : user
        }
        return render(request, "welcome.html", context)
    return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value) 
        return redirect('/')
    email = request.POST["email"]
    password = request.POST['password']
    user = User.objects.filter(email=email)
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['id'] = logged_user.id
            return redirect('/success')
    else:
        messages.error(request,"User is not Exist")
    return redirect('/')

def logout(request):
    del request.session['id']
    return redirect("/")



def sightings(request):
    context = {"Sasquatch":Sasquatch.objects.all()
    }
    return render(request,"sasquatch.html",context)


def new_creat(request):
    location = request.POST['location']
    date = request.POST['date']
    number = request.POST['number']
    WhatHappend = request.POST['WhatHappend']
    sightings_creat = Sasquatch.objects.create(location=location,date=date,number=number,whatHappend=WhatHappend)
    sightings_creat.save()
    return redirect('/page')

def page(request):
    context = {'new_page':Sasquatch.objects.all()}
    return render(request,'welcome.html',context)
    


    

def view(request):
    return render(request,'view.html')


