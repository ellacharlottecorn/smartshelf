from django import forms

from .models import Paint

class PostForm(forms.ModelForm):

    class Meta:
        model = Paint
        fields = ('color', 'type', 'size')
