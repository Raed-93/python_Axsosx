from django.shortcuts import render, HttpResponse,redirect
def index(request):
    return render(request,"index.html")

def create_result(request):
    Name_from_form = request.POST['yourname']
    Dojo_Location_from_form = request.POST['name']
    Favorite_Language_from_form = request.POST['lang']
    Comment_from_form = request.POST['comment']

    context = {
        "Name_on_template" : Name_from_form,
        "Dojo_Location_on_template" : Dojo_Location_from_form,
        "Favorite_Language_on_template" : Favorite_Language_from_form,
        "Comment_on_template" : Comment_from_form,
    }

    return render(request,"show.html",context)

def succes(request):
    return render(request,"show.html")




# Create your views here.
