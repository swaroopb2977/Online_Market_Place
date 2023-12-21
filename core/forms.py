from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
        
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Your Password',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
    

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Your Email',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Your Password',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Repeat Password',
            'class': 'w-full py-4 px-6 rounded-xl'
        })
