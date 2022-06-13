from django import forms

from django_countries.fields import CountryField
from phonenumber_field.formfields import PhoneNumberField

from .models import User

class ContactForm(forms.Form):
    username = forms.CharField(max_length = 20, widget = forms.TextInput())
    email = forms.EmailField(max_length = 10,widget = forms.EmailInput())
    message = forms.Textarea()

class LoginForm(forms.Form):
    email = forms.EmailField(max_length = 20, widget = forms.EmailInput())
    password = forms.CharField(max_length = 32,widget = forms.TextInput())

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 10, widget = forms.TextInput())
    firstname = forms.CharField(max_length = 10, widget = forms.TextInput())
    lastname = forms.CharField(max_length = 10, widget = forms.TextInput())
    email = forms.EmailField(max_length = 20, widget = forms.EmailInput())
    password = forms.CharField(max_length = 32, widget  = forms.PasswordInput())
    telephone = PhoneNumberField()
    gender = forms.CharField(max_length = 15, widget = forms.Select(choices = User.GenderChoice.choices))
    country = CountryField().formfield(null = False)
    state = forms.CharField(max_length = 10, widget = forms.TextInput())
    