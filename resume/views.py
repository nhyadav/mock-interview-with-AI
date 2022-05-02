from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pickle
from .models import Resume
from .forms import ResumeSubmitForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# from pdfminer.high_level import extract_text

@login_required(login_url='/signin')
def scanresume(filepath):
    return extract_text(filepath)


@login_required(login_url='/signin')
def resume(request):
    user = get_object_or_404(User, id=request.user.id)
    form  = ResumeSubmitForm(request.POST, request.FILES)
    contxt = {'form': form}
    return render(request, "resume/index.html", context=contxt)

@login_required(login_url='/signin')
def resumescan(request):
    user = get_object_or_404(User, id=request.user.id)
    form  = ResumeSubmitForm(request.POST, request.FILES)
    contxt = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            messange.success(request, "Your details have been loaded successfully......")
        result=''
        context = {
            'result': result
        }
        return render(request, 'resume/scan_report.html', context=context)
    return render(request, 'resume/index.html', context=contxt)