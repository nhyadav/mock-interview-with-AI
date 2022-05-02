from django import forms
from .models import Resume

class ResumeSubmitForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resume','types']

    def save(self, commit=True):
        resumesubmit = super(ResumeSubmitForm, self).save(commit=False)
        if commit:
            resumesubmit.save()
        return resumesubmit