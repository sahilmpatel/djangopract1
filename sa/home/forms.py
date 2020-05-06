from django import forms
from .models import profile

class profieform(forms.ModelForm):
    class Meta: # for using the model fields
        model = profile
        fields = "__all__"


class loginform(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['email','password']