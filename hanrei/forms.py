from django import forms

from .models import HanreiPost

from django.contrib.auth.forms import (
    AuthenticationForm
)


class HanreiPostForm(forms.ModelForm):

    class Meta:
        model = HanreiPost
        fields = '__all__'


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
