from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import TextInput,PasswordInput



# Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Senha')
    # def init(self, args, **kwargs):
    #     super(LoginForm, self).init(args, **kwargs)
    #     self.fields['username'].widget.attrs['placeholder'] = 'username'
    #     self.fields['password '].widget.attrs['placeholder'] = 'password'