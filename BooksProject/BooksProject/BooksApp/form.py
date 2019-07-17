from .models  import contact,Book,profile
from django import forms
from django.contrib.auth.models import User

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'


class BookForm(forms.ModelForm):
    picture = forms.ImageField(required = False)
    class Meta:
        model = Book
        fields = ['name','isbn','author','publish_on','picture','about']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['mobile','gender']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget = forms.PasswordInput)