from django import forms
from django.forms import ModelForm, widgets
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author']

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control'}),
            'branch' : forms.Select(attrs={'class' : 'form-control'}),
            'year' : forms.Select(attrs={'class' : 'form-control'}), 
        }