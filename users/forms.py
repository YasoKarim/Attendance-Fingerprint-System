from django import forms
from .models import Login 

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login 
        fields = '__all__'
    #username = forms.CharField( max_length=255)
    #password = forms.CharField( max_length=255, widget=forms.PasswordInput)