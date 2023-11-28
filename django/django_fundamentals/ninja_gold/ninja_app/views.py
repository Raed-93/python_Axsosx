from django.shortcuts import render, HttpResponse,redirect
import random
# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, 'main.html')

def process(request):
    if request.POST['place'] == "quest":
        gold = random.randint(-50,50)
        request.session['gold'] += gold
        return redirect('/')
    else:
        gold = random.randint(10,20)
        request.session['gold'] += gold
        return redirect('/')