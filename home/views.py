from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    color='#133FC2'
    if request.method == "POST":
        color = request.POST['colorchoose']
    context = {
        'color': color
    }
    return render(request, "home/index.html", context=context)

