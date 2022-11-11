from django.forms import ModelForm
from .models import Query

class QueryForm(ModelForm):
    class Meta:
        model = Query
        fields = '__all__'
        exclude = ['author', 'upvotes']
