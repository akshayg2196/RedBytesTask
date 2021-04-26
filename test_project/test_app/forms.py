from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django import forms
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation

class SignUp(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1= forms.CharField(label=_("Password"),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label=_("Confirm Password"),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
        # labels = {'password1':'Password','password2':'Confirm Password'}



class LoginForm(AuthenticationForm):
    username =UsernameField(widget =forms.TextInput(attrs={'autofocus':True,'class': 'form-control'}))
    password =forms.CharField(label=_("Password"),strip=False, widget =forms.PasswordInput(attrs={'autocomplete':'current-password','class': 'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
    email =forms.EmailField(max_length=254,widget=forms.EmailInput(attrs={'autocomplete' :'email','class':'form-control'})),


class MySetPasswordForm(SetPasswordForm):
    new_password1 =forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 =forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))




