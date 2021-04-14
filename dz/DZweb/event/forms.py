from .models import Part
from django.forms import ModelForm, TextInput, Textarea

class PartForm(ModelForm):
    class Meta:
        model = Part
        fields = ['title', 'abstract', 'full_text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название фильма'
            }),
            "abstract": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Аннотация'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
        }