from django.forms import ModelForm
from .models import NewContent

class NewContentForm(ModelForm):
    class Meta:
        model = NewContent
        fields = ['name', 'date']