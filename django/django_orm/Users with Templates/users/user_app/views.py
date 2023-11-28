from django.shortcuts import render,HttpResponse,redirect
from .models import Users
def app(request):
    context = {
        "users" : Users.objects.all()

    }
    print(Users.objects.all())
    return render(request,"index.html",context)

def index(request):
    name = request.POST['first name']
    last_name = request.POST['last name']
    email = request.POST['email']
    age = request.POST['age']
    newly_created_user = Users.objects.create(first_name=name,last_name=last_name,email=email,age=age)
    newly_created_user.save()
   
    return redirect("/")

# Create your views here.
