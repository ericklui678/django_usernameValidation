from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager

def index(request):
    # User.objects.create(username='xrvk')
    # User.objects.filter(id=1).delete()
    return render(request, 'usernameValid/index.html')

def process(request):
    username = request.POST['username']

    # if username already exists in db
    if User.objects.filter(username=username):
        messages.info(request,'Username already exists')
    # else if username is > 8 or < 16
    elif not UserManager().login(username):
        messages.info(request, 'username must be greater than 8 characters and fewer than 16 characters')
    # else add username to db
    else:
        User.objects.create(username=username)
        return redirect('/success')

    return redirect('/')

def success(request):
    users = User.objects.all().order_by('-created_at')
    context = {'users': users}
    return render(request, 'usernameValid/success.html', context)
