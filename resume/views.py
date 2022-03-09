from django.shortcuts import render
import pickle
from .models import Resume
# from pdfminer.high_level import extract_text

def scanresume(filepath):
    return extract_text(filepath)



def resume(request):
    return render(request, "resume/index.html")


def resumescan(request):
    if request.method == "POST":
        file = request.POST['myfile']
        # result = scanresume(file)
        # print(result)
    return render(request, 'resume/scan_report.html')