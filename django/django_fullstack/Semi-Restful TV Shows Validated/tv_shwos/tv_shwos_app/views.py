from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import New
def shwo_new(request):
    context = {"new":New.objects.all()

    }
    return render(request,"new_shwo.html",context)

def shwo_creat(request):
#  if request.method == "POST":
    title = request.POST['title']
    net_work = request.POST['net work']
    release_date = request.POST['release date']
    description = request.POST['description']
    new_shwo = New.objects.create(title=title,net_work=net_work,release_date=release_date,desc=description)
    new_shwo.save()
    request.session['id'] = new_shwo.id
    return redirect(f'/shwo/{new_shwo.id}')
 
def shwo(request,id):
#  if request.method == "POST":
    context = {'new_creat':New.objects.get(id=id)}
    return render(request,"shwo_id.html",context)

def shwos(request):
#  if request.method == "POST":
   context = { "new_show":New.objects.all()}
   return render(request,"shwos.html",context)
 
def eidt_show(request,id):
   context = {'edit':New.objects.get(id=id)}
   return render(request,'show_edit.html',context)

def update(request,id):
    new_update = get_object_or_404(New, id=id)
    # new_update = New.object.get(id=id)
    new_update.title = request.POST['title']
    new_update.net_work = request.POST['network']
    new_update.release_date = request.POST['release']
    new_update.description = request.POST['desc']
    new_update.save()
    
    return render(request,'show_eidt.html')



# Create your views here.
