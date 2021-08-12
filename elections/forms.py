# from django import forms
# from .models import Candidate, Poll, Choice

# class ElectionForm(forms.ModelForm):
#     class Meta: 
#         model = Candidate
#         fields = ['name', 'introduction','party_number','area']


# class PollForm(forms.ModelForm):
#     class Meta: 
#         model = Poll
#         fields = ['area']

        
# class ChoiceForm(forms.ModelForm):
#     class Meta: 
#         model = Choice
#         fields = ['poll','candidate']
    
#     poll = forms.ModelChoiceField(queryset=Poll.objects.all())
#     candidate = forms.ModelChoiceField(queryset=Candidate.objects.all())
