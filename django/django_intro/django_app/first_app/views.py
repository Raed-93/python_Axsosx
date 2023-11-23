from django.shortcuts import render,HttpResponse
def index(request):
    context = {
        "name":"Raed",
        "favorite_color":"red",
        "hopy": ["programin","foot_ball"]
    }
    return render(request,"index.html",context)
# Create your views here.
