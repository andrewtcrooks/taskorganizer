from django import forms
from .models import User


app_name = 'tasklist.app'

class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields = '__all__'
