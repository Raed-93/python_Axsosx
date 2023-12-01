from django.shortcuts import render,redirect,HttpResponse
from .models import Book,Author
def app(request):
    context = { "Book": Book.objects.all(),
               "Author":Author.objects.all()
    }
    return render(request,'index.html',context)

def index(request):
    title = request.POST['title']
    description = request.POST['description']
    new_book = Book.objects.create(title=title,description=description)
    new_book.save()
    return redirect('/')


def authors(request):
    context = {"Author":Author.objects.all()}
    return render(request, "author.html",context)

def add_author(request):
    if request.method == "POST":
        fname = request.POST['first']
        lname = request.POST['last']
        notes = request.POST['notes']
        new_author = Author.objects.create(first_name=fname,last_name=lname,notes=notes)
        new_author.save()
    return redirect('/authors')
    

def php(request, book_id):
    new_book=Book.objects.get(id=book_id)
    all_auther = Author.objects.all()
    author_book = new_book.Author.all()
    # new_book.Author.add(*all_auther)
    context = {"new_book" : new_book, "all_auther":all_auther,"author_book":author_book}
    return render(request,'php.html', context)

def hello(request,author_id):
 if request.method == "POST":
    new_author = Author.objects.get(id=author_id)
    title_book = new_author.Author.all()
    all_book = Book.objects.all()
    context = {"new_author":new_author,"name_book":title_book,"all_book":all_book}
    # return render(request,"Lau.html",context)
    return HttpResponse("hello")
# Create your views here.
