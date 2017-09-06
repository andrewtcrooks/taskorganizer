from django.forms import ModelForm
from todolist.data.models import User


app_name = 'todolist.app'

class SignupForm(ModelForm):
    class Meta:
        model = User
        exclude = ()