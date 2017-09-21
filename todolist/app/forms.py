from django import forms
from todolist.data.models import User, Todo


app_name = 'todolist.app'

class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields = '__all__'
