from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta: 
        model = Survey
        fields = ['question', 'ans1', 'ans2',  'ans3', 'ans4']