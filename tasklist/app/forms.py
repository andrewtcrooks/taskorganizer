"""forms.py ."""
from django import forms
from .models import User


app_name = 'tasklist.app'


class SignupForm(forms.ModelForm):
    """Signup form."""

    class Meta:
        """Meta data."""

        model = User
        fields = '__all__'
