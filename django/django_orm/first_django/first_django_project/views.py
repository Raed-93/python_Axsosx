from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
def root(request):
    return HttpResponse("placeholder to later display a list of all blogs" )
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect('/')
def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")
def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")
def destroy(request):
    return redirect('/blog')

def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})




# Create your views here.
