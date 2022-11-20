from django import forms
from django.forms import ModelForm, widgets
from .models import Query

class QueryForm(ModelForm):
    class Meta:
        model = Query
        fields = '__all__'
        exclude = ['author', 'upvotes']

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control'}),
        }