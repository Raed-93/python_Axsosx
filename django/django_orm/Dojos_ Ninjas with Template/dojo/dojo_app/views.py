from django.shortcuts import render,redirect
from .models import dojos,ninjas
def app(request):
    context = {"dojos": dojos.objects.all(),
               "ninjas": ninjas.objects.all()}
    print(dojos.objects.all())
    return render(request,"index.html",context)

def index(request):
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    new_dojos = dojos.objects.create(name=name,city=city,state=state)
    new_dojos.save()
    return redirect('/')

def show(request):
    first_name = request.POST['first name']
    last_name = request.POST['last name']
    dojo = request.POST['dojo']
    dojo_from_form = dojos.objects.get(id=dojo)
    print(dojo)
    new_ninjas = ninjas.objects.create(first_name=first_name,last_name=last_name,dojo=dojo_from_form)
    new_ninjas.save()
    return redirect('/')
# Create your views here.
