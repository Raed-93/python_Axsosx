from django.shortcuts import render,HttpResponse,redirect
from .models import Shows
def root(request):
    content = {
        'shows' : Shows.objects.all()
    }
    return render(request,'index.html',content)
def tv_form(request):
    return render(request,'tv_form.html')

def tv_add(request):
    Shows.objects.create(title = request.POST['title'], network = request.POST['network'] , desc= request.POST['discription'] )
    request.session['id'] = Shows.objects.last().id
    return redirect(f'/shows/{Shows.objects.last().id}')
# Create your views here.

def show_detail(request, id):
    content = {
        'added_show': Shows.objects.get(id = id)
    }
    return render(request, 'show_detail.html', content)

def delete(request, id):
    Shows.objects.get(id = id).delete()
    return redirect('/shows')