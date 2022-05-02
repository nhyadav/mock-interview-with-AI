from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import pickle
from django.contrib import messages
from .models import Resume
from .forms import ResumeSubmitForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from pdfminer.high_level import extract_text
from src.EDA import get_parameter, \
    remove_punction, remove_stopwords
import numpy as np

path = "params.yaml"
params = get_parameter(path)
tfidf_path = params['feature_engineering']['tfidf']
model_path = params['model_building']['model_path']
target_id = params['base']['target_id']

def resume_predict(text):
    with open(tfidf_path, 'rb') as res:
        tfidf = pickle.load(res)
    with open(model_path, 'rb') as res:
        model = pickle.load(res)
    text_vector = tfidf.transform(text)
    # result = model.predict(text_vector)
    preb_conf = model.predict_proba(text_vector)
    pred_list = list(preb_conf[0])
    max_prob = max(pred_list)
    max_ind = pred_list.index(max_prob)
    res = target_id[max_ind]
    return [res, max_prob]

def scanresume(filepath):
    text = extract_text(filepath)
    text = remove_punction(text)
    text = remove_stopwords(text)
    return text


@login_required(login_url='/signin')
def resume(request):
    user = get_object_or_404(User, id=request.user.id)
    form = ResumeSubmitForm(request.POST, request.FILES)
    contxt = {'form': form}
    return render(request, "resumes/index.html", context=contxt)

@login_required(login_url='/signin')
def resumescan(request):
    user = get_object_or_404(User, id=request.user.id)
    form = ResumeSubmitForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            form_data = form.cleaned_data['resume']
            print(form_data)
            messages.success(request, "Your details have been loaded successfully......")
            resume_text=scanresume('media/resume/'+str(form_data))
            result, prabability = resume_predict([resume_text])
            context = {
                'result': result,
                'probability': round(prabability*100, 2)
            }
            return render(request, 'resumes/scan_report.html', context=context)
    return redirect('resume')