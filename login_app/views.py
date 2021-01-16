from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        pw_hash = bcrypt.hashpw(request.POST["pw"].encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name = request.POST["fname"],
            last_name = request.POST["lname"],
            email = request.POST["email"],
            birthday = request.POST["date"],
            password = pw_hash,
        )
        messages.success(request, 'You have successfully registered!')
        return redirect("/")


def logout(request):
    if "user_id" in request.session:
        del request.session["user_id"]
    if "user_first_name" in request.session:
        del request.session["user_first_name"]
    if "user_last_name" in request.session:
        del request.session["user_last_name"]
    if "user_email" in request.session:
        del request.session["user_email"]
    return redirect('/')

def authenticate_user(request):
    if request.method == "GET":
        return redirect('/')
    try:
        user = User.objects.get(email = request.POST["l_email"])
    except:
        messages.error(request, "Incorrect email address or password.")
        return redirect('/')
    
    if bcrypt.checkpw(request.POST['l_pw'].encode(), user.password.encode()):
        request.session['user_id'] = user.id
        request.session['user_first_name'] = user.first_name
        request.session['user_last_name'] = user.last_name
        request.session['user_email'] = user.email
        return redirect('/snacks')
    else:
        messages.error(request, "Incorrect email address or password.")
        return redirect('/')

def display_profile(request, user_id):
    context = {
        'user': User.objects.get(id = user_id)
    }
    return render(request, 'user.html', context)

def update_profile(request, user_id):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f'/users/{user_id}')
    else:
        pw_hash = bcrypt.hashpw(request.POST["pw"].encode(), bcrypt.gensalt()).decode()
        this_user = User.objects.get(id = user_id)
        this_user.first_name = request.POST['fname']
        this_user.last_name = request.POST['lname']
        this_user.email = request.POST['email']
        this_user.password = pw_hash
        this_user.save()
        request.session['user_email'] = request.POST['email']
        messages.success(request,'Profile successfully updated!')
        return redirect(f'/users/{user_id}')
