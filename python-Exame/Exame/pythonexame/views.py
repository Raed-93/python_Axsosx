from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users

def root(request):
    return render(request, 'index.html')

def processing(request):
    if request.method == 'POST':
        if 'which_form' in request.POST and request.POST['which_form'] == 'Register':
            errors = Users.objects.basic_validator(request.POST)
            if errors:
                for error in errors.values():
                    messages.error(request, error)
                return redirect('/')
            else:
                Users.objects.create(
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email_address=request.POST['email_address'],
                    password=request.POST['password']
                )
                messages.success(request, "User created successfully")
                return redirect('/success')
        
        elif 'which_form' in request.POST and request.POST['which_form'] == 'login':
            try:
                user = Users.objects.get(email_address=request.POST['email_address'])
                if user.password == request.POST['password']:
                    request.session['id'] = user.id
                    request.session['action'] = 'Logged in'
                    return redirect('/success')
                else:
                    messages.error(request, "Invalid email or password")
                    return redirect('/')
            except Users.DoesNotExist:
                messages.error(request, "Invalid email or password")
                return redirect('/')
    return redirect('/')

def success(request):
    if 'id' in request.session:
        user = Users.objects.get(id=request.session['id'])
        context = {'user': user, 'action': request.session['action']}
        return render(request, 'welcome.html', context)
    else:
        return redirect('/')

def logout(request):
    if 'id' in request.session:
        request.session.pop('id')
        request.session['action'] = 'Logged out'
    return redirect('/')
