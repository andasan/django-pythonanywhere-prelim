from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #go ahead and create a form and pass it to the template
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

# def signupuser(request):
#     if request.method == 'GET':
#         return render(request, 'todo/signupuser.html', { 'form': UserCreationForm()})
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             #User.objects.create_user(request.POST['username'], password = request.POST['password1']) #dictionary to represent the values from the form

#             user = User.objects.create_user(request.POST['username'], password = request.POST['password1']) 
#             user.save()

#             #will show an error after submission because we didnt send back a response to the browser
#         else:
#             #Tell the user that the passwords do not match
#             #print('Didn\'t match')

#             return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})


### after testing passwords dont match, do the code below to check for same name

# def signupuser(request):
#     if request.method == 'GET':
#         return render(request, 'todo/signupuser.html', { 'form': UserCreationForm()})
#     else:
#         if request.POST['password1'] == request.POST['password2']:

#             try:
#                 user = User.objects.create_user(request.POST['username'], password = request.POST['password1']) 
#                 user.save()
#             except IntegrityError:
#                 return render(
#                     request, 
#                     'todo/signupuser.html', 
#                     {
#                         'form':UserCreationForm(), 
#                         'error':'That username has already been taken. Please choose a new username'
#                     }
#                 )
#         else:
#             return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', { 'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1']) 
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(
                    request, 
                    'todo/signupuser.html', 
                    {
                        'form':UserCreationForm(), 
                        'error':'That username has already been taken. Please choose a new username'
                    }
                )
        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', { 'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password are incorrect'})
        else:
            login(request, user)
            return redirect('currenttodos')
    
def logoutuser(request):
    if request.method == 'POST':
        # pass
        logout(request)
        return redirect('home')

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')

