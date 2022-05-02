from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    color = '#133FC2'
    if request.method == "POST":
        color = request.POST['colorchoose']
    context = {
        'color': color
    }
    return render(request, "home/index.html", context=context)


def signin(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashbord')
    except Exception as ex:
        pass
    return render(request, "home/signin.html")


def signup(request):
    try:
        if request.method == "POST":
            firstname = request.POST['fname']
            middle_name = request.POST['mname']
            lastname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['repsw']

            if User.objects.filter(username=email):
                error = "Username and email id is already existing.!!"
                messages.error(request, error)
                # logging.error(error)
                return redirect('signup')
            else:
                if password == password2:
                    emp = User.objects.create_user(username=email, email=email, password=password)
                    emp.first_name = firstname + middle_name
                    emp.last_name = lastname
                    emp.save()
                    messages.success(request,"Your Account is created.")
                    return redirect('signin')
                else:
                    error = "Your password are not maching..."
                    messages.error(request, error)
                    return redirect('signup')
    except Exception as ex:
        pass
    return render(request, "home/signup.html")

@login_required(login_url='/signin')
def signout(request):
    logout(request)
    messages.success(request,'logout successfully!!')
    # logging.info("successfully logout..")
    return redirect('home')

@login_required(login_url='/signin')
def dashboard(request):
    return render(request, 'home/dashboard.html')
